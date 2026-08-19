import asyncio
import json
import uuid
from datetime import datetime, timezone
from sqlalchemy import select
from .db import SessionLocal
from .models import Job, JobAttempt, AssetDraft, ProjectAsset, CastingMapping, GlobalAsset, GlobalAssetVersion, ProductionDesign, AssetImagePrompt
from .events import event_bus
from .lmstudio import LMStudioProvider
from .diagnostics import exception_diagnostics, compact_error
from .mcp_manager import mcp_manager
from .logging_setup import logger


class JobQueue:
    def __init__(self):
        self.queue: asyncio.PriorityQueue = asyncio.PriorityQueue()
        self.worker_task: asyncio.Task | None = None
        self.provider = LMStudioProvider()
        self.cancelled: set[str] = set()

    async def start(self):
        if self.worker_task is None or self.worker_task.done():
            self.worker_task = asyncio.create_task(self._worker())

        # Recovery: re-queue interrupted / queued jobs.
        with SessionLocal() as db:
            jobs = db.scalars(select(Job).where(Job.state.in_(["QUEUED", "DISPATCHING", "RUNNING", "STREAMING", "INTERRUPTED"]))).all()
            for job in jobs:
                job.state = "QUEUED"
                job.progress_message = "Recovered after restart"
                db.add(job)
                await self.queue.put((job.priority, job.created_at.timestamp(), job.id))
            db.commit()

    async def stop(self):
        if self.worker_task:
            self.worker_task.cancel()
            try:
                await self.worker_task
            except asyncio.CancelledError:
                pass

    def create_job(self, script: str, priority: int = 20, project_id: str | None = None, node_type: str = "asset_requirement_extractor") -> str:
        job_id = "JOB_" + uuid.uuid4().hex[:12].upper()
        with SessionLocal() as db:
            job = Job(id=job_id, project_id=project_id, node_type=node_type, state="QUEUED", priority=priority, input_text=script, progress_message="Waiting in queue")
            db.add(job); db.commit()
        return job_id

    async def enqueue(self, job_id: str):
        logger.info("queue.enqueue job_id=%s", job_id)
        with SessionLocal() as db:
            job = db.get(Job, job_id)
            if not job:
                return
            await self.queue.put((job.priority, job.created_at.timestamp(), job.id))
        await self._publish(job_id)

    async def cancel(self, job_id: str):
        self.cancelled.add(job_id)
        with SessionLocal() as db:
            job = db.get(Job, job_id)
            if job and job.state not in ("COMPLETED", "FAILED", "CANCELLED"):
                job.state = "CANCELLED"
                job.progress_message = "Cancelled by user"
                db.commit()
        await self._publish(job_id)

    async def retry(self, job_id: str):
        with SessionLocal() as db:
            job = db.get(Job, job_id)
            if not job:
                return
            job.state = "QUEUED"
            job.error = None
            job.progress_message = "Queued for retry"
            db.commit()
        self.cancelled.discard(job_id)
        await self.enqueue(job_id)

    async def _worker(self):
        while True:
            _, _, job_id = await self.queue.get()
            try:
                if job_id in self.cancelled:
                    continue
                await self._run_job(job_id)
            finally:
                self.queue.task_done()

    async def _run_job(self, job_id: str):
        logger.info("job.start job_id=%s", job_id)
        with SessionLocal() as db:
            job = db.get(Job, job_id)
            if not job or job.state in ("CANCELLED", "COMPLETED"):
                logger.info("job.skip job_id=%s state=%s", job_id, job.state if job else "NONE")
                return
            job.state = "DISPATCHING"

            is_mcp = job.node_type == "mcp_tool"
            job.progress_message = "Starting MCP server" if is_mcp else "Connecting to LM Studio"
            attempt_no = len(job.attempts) + 1
            mcp_meta = {}
            if is_mcp:
                try:
                    mcp_meta = json.loads(job.input_text)
                except Exception:
                    mcp_meta = {}
            attempt = JobAttempt(
                job_id=job.id,
                attempt_no=attempt_no,
                state="RUNNING",
                provider=(mcp_meta.get("server_id") or "MCP") if is_mcp else self.provider.provider_id,
                model=(mcp_meta.get("tool_name") or "") if is_mcp else self.provider.model,
            )
            db.add(attempt)
            db.commit()
            attempt_id = attempt.id

        await self._publish(job_id)

        try:
            # Stage 1: GENERATING
            with SessionLocal() as db:
                job = db.get(Job, job_id)
                if not job or job.state == "CANCELLED":
                    return
                job.state = "RUNNING"
                job.progress_message = {
                    "asset_requirement_extractor": "LM Studio: generating structured asset requirements",
                    "production_designer": "LM Studio: designing project assets",
                    "asset_image_prompt_compiler": "LM Studio: compiling asset reference-image prompts",
                    "mcp_tool": "MCP: tool is running",
                }.get(job.node_type, "Generating")
                db.commit()
            await self._publish(job_id)

            with SessionLocal() as db:
                current = db.get(Job, job_id)
                input_text = current.input_text
                node_type = current.node_type
                project_id = current.project_id

            if node_type == "asset_requirement_extractor":
                result, raw = await self.provider.extract_assets(input_text)
            elif node_type == "production_designer":
                result, raw = await self.provider.production_design(json.loads(input_text))
            elif node_type == "asset_image_prompt_compiler":
                result, raw = await self.provider.compile_asset_image_prompts(json.loads(input_text))
            elif node_type == "mcp_tool":
                meta = json.loads(input_text)
                server_id = meta.get("server_id")
                tool_name = meta.get("tool_name")
                arguments = meta.get("arguments") or {}
                if not server_id or not tool_name:
                    raise RuntimeError("mcp_tool requires server_id and tool_name")
                result = await mcp_manager.call_tool(server_id, tool_name, arguments)
                raw = json.dumps(result, ensure_ascii=False, default=str)
                if result.get("isError"):
                    raise RuntimeError(f"MCP tool returned isError=true: {raw}")
            else:
                raise RuntimeError(f"Unsupported node_type: {node_type}")

            # Stage 2: VALIDATING
            with SessionLocal() as db:
                job = db.get(Job, job_id)
                attempt = db.get(JobAttempt, attempt_id)
                if job.state == "CANCELLED":
                    attempt.state = "CANCELLED"
                    attempt.finished_at = datetime.now(timezone.utc)
                    db.commit()
                    return

                job.state = "VALIDATING"
                job.progress_message = "Validating schema"
                attempt.raw_response = raw
                db.commit()
            await self._publish(job_id)

            # Stage 3: SAVING ASSETS
            with SessionLocal() as db:
                job = db.get(Job, job_id)
                if job.state == "CANCELLED":
                    return
                job.state = "SAVING_ASSETS"
                job.progress_message = "Saving assets to database"
                db.commit()
            await self._publish(job_id)

            # Stage 4: DB Persistence & Finalize
            with SessionLocal() as db:
                job = db.get(Job, job_id)
                attempt = db.get(JobAttempt, attempt_id)
                if job.state == "CANCELLED":
                    attempt.state = "CANCELLED"
                    attempt.finished_at = datetime.now(timezone.utc)
                    db.commit()
                    return

                artifact_path = f"data/jobs/{job.id}_result.json"

                if job.node_type == "asset_requirement_extractor":
                    if not job.project_id:
                        raise RuntimeError("Job has no project_id assigned; cannot save asset drafts to project.")

                    assets = result.get("assets", [])
                    extractor_asset_count = len(assets)
                    created_count = 0
                    updated_count = 0

                    for a in assets:
                        asset_id = a.get("asset_id")
                        if not asset_id:
                            continue
                        asset_type = a.get("type", "other")
                        name = a.get("name", asset_id)
                        persistence = a.get("persistence", "scene")
                        importance = a.get("importance", "medium")
                        reference_required = bool(a.get("reference_required", False))
                        known_attrs = a.get("known_attributes", {})
                        missing_attrs = a.get("missing_attributes", [])

                        existing = db.scalar(
                            select(AssetDraft).where(
                                AssetDraft.project_id == job.project_id,
                                AssetDraft.asset_id == asset_id
                            )
                        )
                        if existing:
                            existing.asset_type = asset_type
                            existing.name = name
                            existing.persistence = persistence
                            existing.importance = importance
                            existing.reference_required = reference_required
                            existing.known_attributes_json = json.dumps(known_attrs, ensure_ascii=False)
                            existing.missing_attributes_json = json.dumps(missing_attrs, ensure_ascii=False)
                            existing.source_job_id = job.id
                            existing.status = "DRAFT"
                            updated_count += 1
                        else:
                            draft = AssetDraft(
                                project_id=job.project_id,
                                source_job_id=job.id,
                                asset_id=asset_id,
                                asset_type=asset_type,
                                name=name,
                                persistence=persistence,
                                importance=importance,
                                reference_required=reference_required,
                                known_attributes_json=json.dumps(known_attrs, ensure_ascii=False),
                                missing_attributes_json=json.dumps(missing_attrs, ensure_ascii=False),
                                status="DRAFT",
                                version=1
                            )
                            db.add(draft)
                            created_count += 1

                    total_saved = created_count + updated_count

                    diagnostics_info = {
                        "extractor_asset_count": extractor_asset_count,
                        "asset_drafts_created": created_count,
                        "asset_drafts_updated": updated_count,
                        "draft_rows_saved": total_saved,
                        "project_id": job.project_id,
                        "artifact_path": artifact_path,
                        "persistence_status": "OK",
                        "persistence_error": None
                    }
                    result["diagnostics"] = diagnostics_info
                    job.result_json = json.dumps(result, ensure_ascii=False)
                    job.progress_message = f"Completed: {extractor_asset_count} assets · Drafts saved: {total_saved}"

                elif job.node_type == "production_designer":
                    designs = result.get("designs", [])
                    for item in designs:
                        latest = db.scalar(
                            select(ProductionDesign).where(
                                ProductionDesign.project_id == job.project_id,
                                ProductionDesign.asset_id == item["asset_id"]
                            ).order_by(ProductionDesign.version.desc())
                        )
                        version = (latest.version + 1) if latest else 1
                        db.add(ProductionDesign(
                            project_id=job.project_id,
                            asset_id=item["asset_id"],
                            asset_type=item["asset_type"],
                            asset_name=item["asset_name"],
                            source_asset_version=1,
                            version=version,
                            status="DRAFT",
                            design_json=json.dumps(item.get("design", {}), ensure_ascii=False),
                            locked_attributes_json=json.dumps(item.get("locked_attributes", []), ensure_ascii=False),
                            variable_attributes_json=json.dumps(item.get("variable_attributes", []), ensure_ascii=False),
                            required_views_json=json.dumps(item.get("required_views", []), ensure_ascii=False),
                            missing_attributes_json=json.dumps(item.get("missing_attributes", []), ensure_ascii=False),
                            source_job_id=job.id
                        ))
                    diagnostics_info = {
                        "items_count": len(designs),
                        "project_id": job.project_id,
                        "artifact_path": artifact_path,
                        "persistence_status": "OK",
                        "persistence_error": None
                    }
                    result["diagnostics"] = diagnostics_info
                    job.result_json = json.dumps(result, ensure_ascii=False)
                    job.progress_message = f"Completed: {len(designs)} designs"

                elif job.node_type == "asset_image_prompt_compiler":
                    prompts = result.get("prompts", [])
                    design_map = {
                        d.asset_id: d
                        for d in db.scalars(
                            select(ProductionDesign).where(
                                ProductionDesign.project_id == job.project_id
                            ).order_by(ProductionDesign.version.desc())
                        ).all()
                    }
                    for item in prompts:
                        latest = db.scalar(
                            select(AssetImagePrompt).where(
                                AssetImagePrompt.project_id == job.project_id,
                                AssetImagePrompt.asset_id == item["asset_id"],
                                AssetImagePrompt.view_id == item["view_id"]
                            ).order_by(AssetImagePrompt.version.desc())
                        )
                        version = (latest.version + 1) if latest else 1
                        d = design_map.get(item["asset_id"])
                        db.add(AssetImagePrompt(
                            project_id=job.project_id,
                            asset_id=item["asset_id"],
                            asset_type=item["asset_type"],
                            design_id=d.id if d else None,
                            view_id=item["view_id"],
                            version=version,
                            status="DRAFT",
                            prompt_text=item["prompt"],
                            negative_prompt=item.get("negative_prompt", ""),
                            invariant_lock_json=json.dumps(item.get("invariant_lock", []), ensure_ascii=False),
                            source_job_id=job.id
                        ))
                    diagnostics_info = {
                        "items_count": len(prompts),
                        "project_id": job.project_id,
                        "artifact_path": artifact_path,
                        "persistence_status": "OK",
                        "persistence_error": None
                    }
                    result["diagnostics"] = diagnostics_info
                    job.result_json = json.dumps(result, ensure_ascii=False)
                    job.progress_message = f"Completed: {len(prompts)} prompts"

                else:
                    job.result_json = json.dumps(result, ensure_ascii=False)
                    job.progress_message = "Completed successfully"

                # Mark as COMPLETED and commit
                job.state = "COMPLETED"
                attempt.state = "COMPLETED"
                attempt.finished_at = datetime.now(timezone.utc)
                db.commit()
                logger.info("job.completed job_id=%s node_type=%s", job_id, job.node_type)

        except Exception as exc:
            with SessionLocal() as db:
                job = db.get(Job, job_id)
                attempt = db.get(JobAttempt, attempt_id)

                extracted_count = 0
                if 'result' in locals() and isinstance(result, dict):
                    extracted_count = len(result.get("assets", []))

                persistence_info = {
                    "extractor_asset_count": extracted_count,
                    "asset_drafts_created": created_count if 'created_count' in locals() else 0,
                    "asset_drafts_updated": updated_count if 'updated_count' in locals() else 0,
                    "draft_rows_saved": 0,
                    "project_id": job.project_id if job else None,
                    "artifact_path": f"data/jobs/{job_id}_result.json",
                    "persistence_status": "FAILED",
                    "persistence_error": str(exc),
                }

                context = {
                    "job_id": job_id,
                    "node_type": job.node_type if job else None,
                    "project_id": job.project_id if job else None,
                    "attempt_no": attempt.attempt_no if attempt else None,
                    "provider": attempt.provider if attempt else None,
                    "model_or_tool": attempt.model if attempt else None,
                    "lmstudio_base_url": self.provider.base_url if (job and job.node_type != "mcp_tool") else None,
                    "input_excerpt": (job.input_text[:1500] if job and job.input_text else ""),
                    "persistence": persistence_info
                }
                diag = exception_diagnostics(exc, stage=(job.progress_message if job else "worker"), context=context)
                diag_text = json.dumps(diag, ensure_ascii=False, indent=2)
                if job:
                    job.state = "FAILED"
                    job.error = diag_text
                    job.progress_message = compact_error(diag)
                if attempt:
                    attempt.state = "FAILED"
                    attempt.error = diag_text
                    attempt.finished_at = datetime.now(timezone.utc)
                db.commit()
                logger.exception("job.failed job_id=%s", job_id, exc_info=exc)

        await self._publish(job_id)

    async def _publish(self, job_id: str):
        with SessionLocal() as db:
            job = db.get(Job, job_id)
            if not job:
                return
            event = {
                "type": "job.state_changed",
                "job": {
                    "id": job.id,
                    "state": job.state,
                    "progress_message": job.progress_message,
                    "error": job.error,
                }
            }
        await event_bus.publish(event)


job_queue = JobQueue()
