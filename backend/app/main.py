import json, uuid
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, WebSocket, WebSocketDisconnect, Body
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from .config import settings
from .db import Base, engine, get_db
from .models import Job, Project, AssetDraft, ProjectAsset, GlobalAsset, GlobalAssetVersion, CastingMapping, ProductionDesign, AssetImagePrompt
from .providers import provider_manager
from .schemas import CreateJobRequest, CreateProjectRequest, UpdateAssetDraftRequest, CreateGlobalAssetRequest, CreateGlobalAssetVersionRequest, UpsertCastingRequest, UpdateCastingRequest, CreatePipelineJobRequest, UpdateProductionDesignRequest, UpdateAssetImagePromptRequest, UpdateProviderConfigRequest, TestProviderRequest, RefreshModelsRequest
from .queue import job_queue
from .events import event_bus
from .lmstudio import LMStudioProvider
from .mcp_manager import mcp_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    await job_queue.start()
    yield
    await job_queue.stop()


app = FastAPI(title="DramaStudio API", version="0.4.1-debug-mcp", lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=settings.cors_list, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
provider = LMStudioProvider()

@app.get("/api/health")
def health(): return {"status":"ok","version":"0.4.1-debug-mcp"}

@app.get("/api/providers/lmstudio/probe")
async def probe_provider(): return await provider_manager.get_health("LMSTUDIO_01")

@app.get("/api/providers")
async def list_providers():
    providers = provider_manager.list_providers()
    res = []
    for p in providers:
        item = dict(p)
        if p.get("enabled"):
            health = await provider_manager.get_health(p["id"])
            item["status"] = health.get("state", "OFFLINE")
            if health.get("models"):
                item["available_models"] = health.get("models")
        else:
            item["status"] = "DISABLED"
        res.append(item)
    return res

@app.get("/api/providers/{provider_id}")
async def get_provider(provider_id: str):
    pid = "LMSTUDIO_01" if provider_id.lower() == "lmstudio" else provider_id
    p = provider_manager.get_provider(pid)
    if not p:
        raise HTTPException(404, "Provider not found")
    item = dict(p)
    if p.get("enabled"):
        health = await provider_manager.get_health(p["id"])
        item["status"] = health.get("state", "OFFLINE")
        item["available_models"] = health.get("models", [])
    else:
        item["status"] = "DISABLED"
    return item

@app.put("/api/providers/{provider_id}")
def update_provider(provider_id: str, req: UpdateProviderConfigRequest):
    pid = "LMSTUDIO_01" if provider_id.lower() == "lmstudio" else provider_id
    try:
        updated = provider_manager.update_provider(pid, req.model_dump(exclude_none=True))
        return {"ok": True, "provider": updated}
    except KeyError as e:
        raise HTTPException(404, str(e))

@app.post("/api/providers/{provider_id}/test")
async def test_provider(provider_id: str, req: TestProviderRequest | None = None):
    pid = "LMSTUDIO_01" if provider_id.lower() == "lmstudio" else provider_id
    override = req.model_dump(exclude_none=True) if req else None
    return await provider_manager.test_connection(pid, override)

@app.post("/api/providers/{provider_id}/models/refresh")
async def refresh_provider_models(provider_id: str, req: RefreshModelsRequest | None = None):
    pid = "LMSTUDIO_01" if provider_id.lower() == "lmstudio" else provider_id
    base_url = req.base_url if req else None
    return await provider_manager.refresh_models(pid, base_url)


@app.get("/api/mcp/servers")
def list_mcp_servers():
    return mcp_manager.list_servers()

@app.get("/api/mcp/servers/{server_id}")
def get_mcp_server(server_id:str):
    cfg=mcp_manager.get(server_id)
    if not cfg: raise HTTPException(404,"MCP server not found")
    return mcp_manager._public(cfg)

@app.put("/api/mcp/servers/{server_id}")
def update_mcp_server(server_id:str, payload:dict=Body(...)):
    try:
        return {"ok":True,"server":mcp_manager.update(server_id,payload)}
    except Exception as exc:
        raise HTTPException(400,str(exc))

@app.post("/api/mcp/servers/{server_id}/test")
async def test_mcp_server(server_id:str):
    try:
        tools=await mcp_manager.list_tools(server_id)
        return {"ok":True,"server_id":server_id,"tools":tools,"count":len(tools)}
    except Exception as exc:
        return {"ok":False,"server_id":server_id,"error":f"{type(exc).__name__}: {exc}"}

@app.get("/api/mcp/servers/{server_id}/tools")
async def list_mcp_tools(server_id:str):
    try:
        return {"ok":True,"tools":await mcp_manager.list_tools(server_id)}
    except Exception as exc:
        raise HTTPException(502,f"{type(exc).__name__}: {exc}")

@app.post("/api/mcp/jobs")
async def create_mcp_job(payload:dict=Body(...)):
    server_id=payload.get("server_id")
    tool_name=payload.get("tool_name")
    if not server_id or not tool_name:
        raise HTTPException(400,"server_id and tool_name are required")
    if not mcp_manager.get(server_id):
        raise HTTPException(404,"MCP server not found")
    meta={"server_id":server_id,"tool_name":tool_name,"arguments":payload.get("arguments") or {}}
    job_id=job_queue.create_job(json.dumps(meta,ensure_ascii=False), int(payload.get("priority",30)), payload.get("project_id"), node_type="mcp_tool")
    await job_queue.enqueue(job_id)
    return {"job_id":job_id}

@app.post("/api/mcp/servers/{server_id}/check-backends")
async def mcp_check_backends(server_id:str):
    # Fast diagnostic call; Mir Studio documents this as the mandatory preflight.
    try:
        result=await mcp_manager.call_tool(server_id,"check_backends",{})
        return {"ok":not result.get("isError",False),"result":result}
    except Exception as exc:
        return {"ok":False,"error":f"{type(exc).__name__}: {exc}"}


@app.get("/api/projects")
def list_projects(db: Session = Depends(get_db)):
    return [{"id":p.id,"name":p.name,"created_at":p.created_at} for p in db.scalars(select(Project).order_by(Project.created_at.desc())).all()]

@app.post("/api/projects")
def create_project(req: CreateProjectRequest, db: Session = Depends(get_db)):
    if not req.name.strip(): raise HTTPException(400,"project name is empty")
    p=Project(id="PRJ_"+uuid.uuid4().hex[:10].upper(),name=req.name.strip()); db.add(p); db.commit(); db.refresh(p)
    return {"id":p.id,"name":p.name}

@app.post("/api/jobs")
async def create_job(req: CreateJobRequest):
    if not req.script.strip(): raise HTTPException(400,"script is empty")
    job_id = job_queue.create_job(req.script, req.priority, req.project_id)
    await job_queue.enqueue(job_id)
    return {"job_id":job_id}

@app.get("/api/jobs")
def list_jobs(db: Session = Depends(get_db)):
    jobs=db.scalars(select(Job).order_by(Job.created_at.desc()).limit(100)).all()
    return [{"id":j.id,"project_id":j.project_id,"node_type":j.node_type,"state":j.state,"priority":j.priority,"progress_message":j.progress_message,"error":j.error,"created_at":j.created_at} for j in jobs]

@app.get("/api/jobs/{job_id}")
def get_job(job_id:str, db:Session=Depends(get_db)):
    j=db.get(Job,job_id)
    if not j: raise HTTPException(404,"job not found")
    diagnostics = None
    if j.error:
        try:
            diagnostics = json.loads(j.error)
        except Exception:
            diagnostics = {"message": j.error}
    elif j.result_json:
        try:
            res_dict = json.loads(j.result_json)
            if "diagnostics" in res_dict:
                diagnostics = {"context": res_dict["diagnostics"]}
        except Exception:
            pass

    attempts=[]
    for a in j.attempts:
        ad=None
        if a.error:
            try: ad=json.loads(a.error)
            except Exception: ad={"message":a.error}
        attempts.append({"attempt_no":a.attempt_no,"state":a.state,"provider":a.provider,"model":a.model,"error":a.error,"diagnostics":ad,"started_at":a.started_at,"finished_at":a.finished_at})
    return {"id":j.id,"project_id":j.project_id,"node_type":j.node_type,"state":j.state,"priority":j.priority,"progress_message":j.progress_message,"result":json.loads(j.result_json) if j.result_json else None,"error":j.error,"diagnostics":diagnostics,"attempts":attempts}

@app.get("/api/jobs/{job_id}/diagnostics")
def get_job_diagnostics(job_id:str, db:Session=Depends(get_db)):
    j=db.get(Job,job_id)
    if not j: raise HTTPException(404,"job not found")
    diag = None
    if j.error:
        try: diag = json.loads(j.error)
        except Exception: diag = {"message": j.error}
    elif j.result_json:
        try:
            res_dict = json.loads(j.result_json)
            if "diagnostics" in res_dict:
                diag = {"context": res_dict["diagnostics"]}
        except Exception:
            pass
    return {
        "job_id":j.id, "node_type":j.node_type, "state":j.state,
        "progress_message":j.progress_message, "diagnostics":diag,
        "attempts":[{"attempt_no":a.attempt_no,"state":a.state,"provider":a.provider,"model":a.model,"error":a.error,"started_at":a.started_at,"finished_at":a.finished_at} for a in j.attempts]
    }


@app.post("/api/jobs/{job_id}/retry")
async def retry_job(job_id:str, db:Session=Depends(get_db)):
    if not db.get(Job,job_id): raise HTTPException(404,"job not found")
    await job_queue.retry(job_id); return {"ok":True}

@app.post("/api/jobs/{job_id}/cancel")
async def cancel_job(job_id:str, db:Session=Depends(get_db)):
    if not db.get(Job,job_id): raise HTTPException(404,"job not found")
    await job_queue.cancel(job_id); return {"ok":True}

@app.post("/api/jobs/{job_id}/workspace")
def materialize_workspace(job_id:str, db:Session=Depends(get_db)):
    job=db.get(Job,job_id)
    if not job or not job.result_json: raise HTTPException(400,"completed extraction result required")
    if not job.project_id: raise HTTPException(400,"job has no project_id")
    result=json.loads(job.result_json)
    existing=db.scalars(select(AssetDraft).where(AssetDraft.source_job_id==job_id)).all()
    if existing:
        return {"created":0,"existing":len(existing)}
    for a in result.get("assets",[]):
        db.add(AssetDraft(project_id=job.project_id,source_job_id=job_id,asset_id=a["asset_id"],asset_type=a["type"],name=a["name"],persistence=a.get("persistence","scene"),importance=a.get("importance","medium"),reference_required=a.get("reference_required",False),known_attributes_json=json.dumps(a.get("known_attributes",{}),ensure_ascii=False),missing_attributes_json=json.dumps(a.get("missing_attributes",[]),ensure_ascii=False)))
    db.commit(); return {"created":len(result.get("assets",[]))}

@app.get("/api/projects/{project_id}/asset-drafts")
def list_asset_drafts(project_id:str, db:Session=Depends(get_db)):
    rows=db.scalars(select(AssetDraft).where(AssetDraft.project_id==project_id).order_by(AssetDraft.asset_type,AssetDraft.asset_id)).all()
    return [{"id":r.id,"asset_id":r.asset_id,"type":r.asset_type,"name":r.name,"persistence":r.persistence,"importance":r.importance,"reference_required":r.reference_required,"known_attributes":json.loads(r.known_attributes_json),"missing_attributes":json.loads(r.missing_attributes_json),"status":r.status,"version":r.version,"source_job_id":r.source_job_id} for r in rows]

@app.patch("/api/asset-drafts/{draft_id}")
def update_asset_draft(draft_id:int, req:UpdateAssetDraftRequest, db:Session=Depends(get_db)):
    r=db.get(AssetDraft,draft_id)
    if not r: raise HTTPException(404,"asset draft not found")
    data=req.model_dump(exclude_none=True)
    for k,v in data.items():
        if k=="known_attributes": r.known_attributes_json=json.dumps(v,ensure_ascii=False)
        elif k=="missing_attributes": r.missing_attributes_json=json.dumps(v,ensure_ascii=False)
        else: setattr(r,k,v)
    r.status="DRAFT"; db.commit(); return {"ok":True}

@app.post("/api/asset-drafts/{draft_id}/approve")
def approve_asset_draft(draft_id:int, db:Session=Depends(get_db)):
    r=db.get(AssetDraft,draft_id)
    if not r: raise HTTPException(404,"asset draft not found")
    payload={"persistence":r.persistence,"importance":r.importance,"reference_required":r.reference_required,"known_attributes":json.loads(r.known_attributes_json),"missing_attributes":json.loads(r.missing_attributes_json)}
    existing=db.scalar(select(ProjectAsset).where(ProjectAsset.project_id==r.project_id,ProjectAsset.asset_id==r.asset_id).order_by(ProjectAsset.version.desc()))
    version=(existing.version+1) if existing else 1
    db.add(ProjectAsset(project_id=r.project_id,asset_id=r.asset_id,asset_type=r.asset_type,name=r.name,version=version,status="APPROVED",payload_json=json.dumps(payload,ensure_ascii=False)))
    r.status="APPROVED"; r.version=version; db.commit(); return {"ok":True,"version":version}

@app.post("/api/projects/{project_id}/asset-drafts/approve-all")
def approve_all(project_id:str, db:Session=Depends(get_db)):
    rows=db.scalars(select(AssetDraft).where(AssetDraft.project_id==project_id,AssetDraft.status!="APPROVED")).all(); count=0
    for r in rows:
        payload={"persistence":r.persistence,"importance":r.importance,"reference_required":r.reference_required,"known_attributes":json.loads(r.known_attributes_json),"missing_attributes":json.loads(r.missing_attributes_json)}
        existing=db.scalar(select(ProjectAsset).where(ProjectAsset.project_id==r.project_id,ProjectAsset.asset_id==r.asset_id).order_by(ProjectAsset.version.desc()))
        version=(existing.version+1) if existing else 1
        db.add(ProjectAsset(project_id=r.project_id,asset_id=r.asset_id,asset_type=r.asset_type,name=r.name,version=version,status="APPROVED",payload_json=json.dumps(payload,ensure_ascii=False))); r.status="APPROVED"; r.version=version; count+=1
    db.commit(); return {"approved":count}

@app.get("/api/projects/{project_id}/assets")
def list_project_assets(project_id:str, db:Session=Depends(get_db)):
    rows=db.scalars(select(ProjectAsset).where(ProjectAsset.project_id==project_id).order_by(ProjectAsset.asset_type,ProjectAsset.asset_id,ProjectAsset.version.desc())).all()
    return [{"id":r.id,"asset_id":r.asset_id,"type":r.asset_type,"name":r.name,"version":r.version,"status":r.status,"payload":json.loads(r.payload_json),"approved_at":r.approved_at} for r in rows]


@app.get("/api/global-assets")
def list_global_assets(asset_type: str | None = None, db: Session = Depends(get_db)):
    q = select(GlobalAsset).order_by(GlobalAsset.asset_type, GlobalAsset.display_name)
    if asset_type:
        q = q.where(GlobalAsset.asset_type == asset_type)
    assets = db.scalars(q).all()
    out=[]
    for a in assets:
        versions=db.scalars(select(GlobalAssetVersion).where(GlobalAssetVersion.global_asset_id==a.id).order_by(GlobalAssetVersion.version.desc())).all()
        out.append({"asset_id":a.asset_id,"type":a.asset_type,"display_name":a.display_name,"versions":[{"version":v.version,"status":v.status,"metadata":json.loads(v.metadata_json),"reference_uri":v.reference_uri,"approved_at":v.approved_at} for v in versions]})
    return out

@app.post("/api/global-assets")
def create_global_asset(req: CreateGlobalAssetRequest, db: Session = Depends(get_db)):
    prefix="ACTOR" if req.asset_type=="actor" else "VOICE"
    existing=db.scalars(select(GlobalAsset).where(GlobalAsset.asset_type==req.asset_type)).all()
    nums=[]
    for x in existing:
        try: nums.append(int(x.asset_id.split("_")[-1]))
        except: pass
    asset_id=f"{prefix}_{(max(nums) if nums else 0)+1:03d}"
    a=GlobalAsset(asset_id=asset_id,asset_type=req.asset_type,display_name=req.display_name.strip() or asset_id)
    db.add(a); db.flush()
    v=GlobalAssetVersion(global_asset_id=a.id,version=1,status="DRAFT",metadata_json=json.dumps(req.metadata,ensure_ascii=False),reference_uri=req.reference_uri)
    db.add(v); db.commit()
    return {"asset_id":asset_id,"version":1,"status":"DRAFT"}

@app.post("/api/global-assets/{asset_id}/versions")
def create_global_asset_version(asset_id:str, req:CreateGlobalAssetVersionRequest, db:Session=Depends(get_db)):
    a=db.scalar(select(GlobalAsset).where(GlobalAsset.asset_id==asset_id))
    if not a: raise HTTPException(404,"global asset not found")
    latest=db.scalar(select(GlobalAssetVersion).where(GlobalAssetVersion.global_asset_id==a.id).order_by(GlobalAssetVersion.version.desc()))
    version=(latest.version+1) if latest else 1
    v=GlobalAssetVersion(global_asset_id=a.id,version=version,status="DRAFT",metadata_json=json.dumps(req.metadata,ensure_ascii=False),reference_uri=req.reference_uri)
    db.add(v); db.commit(); return {"asset_id":asset_id,"version":version,"status":"DRAFT"}

@app.post("/api/global-assets/{asset_id}/versions/{version}/approve")
def approve_global_asset_version(asset_id:str,version:int,db:Session=Depends(get_db)):
    a=db.scalar(select(GlobalAsset).where(GlobalAsset.asset_id==asset_id))
    if not a: raise HTTPException(404,"global asset not found")
    v=db.scalar(select(GlobalAssetVersion).where(GlobalAssetVersion.global_asset_id==a.id,GlobalAssetVersion.version==version))
    if not v: raise HTTPException(404,"version not found")
    v.status="APPROVED"; v.approved_at=__import__('datetime').datetime.now(__import__('datetime').timezone.utc); db.commit()
    return {"ok":True,"asset_id":asset_id,"version":version,"status":"APPROVED"}

@app.get("/api/projects/{project_id}/characters")
def list_project_characters(project_id:str,db:Session=Depends(get_db)):
    rows=db.scalars(select(ProjectAsset).where(ProjectAsset.project_id==project_id,ProjectAsset.asset_type=="character",ProjectAsset.status=="APPROVED").order_by(ProjectAsset.asset_id,ProjectAsset.version.desc())).all()
    latest={}
    for r in rows:
        latest.setdefault(r.asset_id,r)
    return [{"asset_id":r.asset_id,"name":r.name,"version":r.version,"payload":json.loads(r.payload_json)} for r in latest.values()]

@app.get("/api/projects/{project_id}/castings")
def list_castings(project_id:str,db:Session=Depends(get_db)):
    rows=db.scalars(select(CastingMapping).where(CastingMapping.project_id==project_id).order_by(CastingMapping.character_asset_id)).all()
    return [{"id":r.id,"character_asset_id":r.character_asset_id,"character_name":r.character_name,"actor_asset_id":r.actor_asset_id,"actor_version":r.actor_version,"voice_asset_id":r.voice_asset_id,"voice_version":r.voice_version,"status":r.status,"notes":r.notes} for r in rows]

@app.post("/api/projects/{project_id}/castings")
def upsert_casting(project_id:str,req:UpsertCastingRequest,db:Session=Depends(get_db)):
    row=db.scalar(select(CastingMapping).where(CastingMapping.project_id==project_id,CastingMapping.character_asset_id==req.character_asset_id))
    if not row:
        row=CastingMapping(project_id=project_id,character_asset_id=req.character_asset_id,character_name=req.character_name)
        db.add(row)
    row.character_name=req.character_name; row.actor_asset_id=req.actor_asset_id; row.actor_version=req.actor_version; row.voice_asset_id=req.voice_asset_id; row.voice_version=req.voice_version; row.notes=req.notes; row.status="DRAFT"
    db.commit(); db.refresh(row); return {"id":row.id,"status":row.status}

@app.patch("/api/castings/{casting_id}")
def update_casting(casting_id:int,req:UpdateCastingRequest,db:Session=Depends(get_db)):
    row=db.get(CastingMapping,casting_id)
    if not row: raise HTTPException(404,"casting not found")
    for k,v in req.model_dump(exclude_none=True).items(): setattr(row,k,v)
    db.commit(); return {"ok":True}

@app.post("/api/castings/{casting_id}/approve")
def approve_casting(casting_id:int,db:Session=Depends(get_db)):
    row=db.get(CastingMapping,casting_id)
    if not row: raise HTTPException(404,"casting not found")
    if not row.actor_asset_id or not row.actor_version: raise HTTPException(400,"approved actor mapping required")
    if not row.voice_asset_id or not row.voice_version: raise HTTPException(400,"approved voice mapping required")
    for aid,ver,typ in [(row.actor_asset_id,row.actor_version,"actor"),(row.voice_asset_id,row.voice_version,"voice")]:
        a=db.scalar(select(GlobalAsset).where(GlobalAsset.asset_id==aid,GlobalAsset.asset_type==typ))
        if not a: raise HTTPException(400,f"{typ} asset not found: {aid}")
        v=db.scalar(select(GlobalAssetVersion).where(GlobalAssetVersion.global_asset_id==a.id,GlobalAssetVersion.version==ver,GlobalAssetVersion.status=="APPROVED"))
        if not v: raise HTTPException(400,f"{aid}@v{ver} is not APPROVED")
    row.status="APPROVED"; db.commit(); return {"ok":True,"status":"APPROVED"}


@app.post("/api/projects/{project_id}/production-design/jobs")
async def create_production_design_job(project_id:str, req:CreatePipelineJobRequest, db:Session=Depends(get_db)):
    assets=db.scalars(select(ProjectAsset).where(ProjectAsset.project_id==project_id,ProjectAsset.status=="APPROVED").order_by(ProjectAsset.asset_type,ProjectAsset.asset_id,ProjectAsset.version.desc())).all()
    latest_assets={}
    for a in assets: latest_assets.setdefault(a.asset_id,a)
    if not latest_assets: raise HTTPException(400,"approved project assets required")
    castings=db.scalars(select(CastingMapping).where(CastingMapping.project_id==project_id,CastingMapping.status=="APPROVED")).all()
    context={"project_id":project_id,"approved_assets":[{"asset_id":a.asset_id,"asset_type":a.asset_type,"name":a.name,"version":a.version,"payload":json.loads(a.payload_json)} for a in latest_assets.values()],"approved_castings":[{"character_asset_id":c.character_asset_id,"character_name":c.character_name,"actor_ref":f"{c.actor_asset_id}@v{c.actor_version}","voice_ref":f"{c.voice_asset_id}@v{c.voice_version}","notes":c.notes} for c in castings]}
    job_id=job_queue.create_job(json.dumps(context,ensure_ascii=False),req.priority,project_id,"production_designer"); await job_queue.enqueue(job_id); return {"job_id":job_id}

@app.get("/api/projects/{project_id}/production-designs")
def list_production_designs(project_id:str,db:Session=Depends(get_db)):
    rows=db.scalars(select(ProductionDesign).where(ProductionDesign.project_id==project_id).order_by(ProductionDesign.asset_type,ProductionDesign.asset_id,ProductionDesign.version.desc())).all(); latest={}
    for r in rows: latest.setdefault(r.asset_id,r)
    return [{"id":r.id,"asset_id":r.asset_id,"asset_type":r.asset_type,"asset_name":r.asset_name,"version":r.version,"status":r.status,"design":json.loads(r.design_json),"locked_attributes":json.loads(r.locked_attributes_json),"variable_attributes":json.loads(r.variable_attributes_json),"required_views":json.loads(r.required_views_json),"missing_attributes":json.loads(r.missing_attributes_json)} for r in latest.values()]

@app.patch("/api/production-designs/{design_id}")
def update_production_design(design_id:int,req:UpdateProductionDesignRequest,db:Session=Depends(get_db)):
    r=db.get(ProductionDesign,design_id)
    if not r: raise HTTPException(404,"production design not found")
    d=req.model_dump(exclude_none=True)
    for k,v in d.items(): setattr(r,{"design":"design_json","locked_attributes":"locked_attributes_json","variable_attributes":"variable_attributes_json","required_views":"required_views_json","missing_attributes":"missing_attributes_json"}[k],json.dumps(v,ensure_ascii=False))
    r.status="DRAFT"; db.commit(); return {"ok":True}

@app.post("/api/production-designs/{design_id}/approve")
def approve_production_design(design_id:int,db:Session=Depends(get_db)):
    r=db.get(ProductionDesign,design_id)
    if not r: raise HTTPException(404,"production design not found")
    r.status="APPROVED"; r.approved_at=__import__('datetime').datetime.now(__import__('datetime').timezone.utc); db.commit(); return {"ok":True,"status":"APPROVED"}

@app.post("/api/projects/{project_id}/asset-image-prompts/jobs")
async def create_asset_prompt_job(project_id:str,req:CreatePipelineJobRequest,db:Session=Depends(get_db)):
    rows=db.scalars(select(ProductionDesign).where(ProductionDesign.project_id==project_id,ProductionDesign.status=="APPROVED").order_by(ProductionDesign.asset_id,ProductionDesign.version.desc())).all(); latest={}
    for r in rows: latest.setdefault(r.asset_id,r)
    if not latest: raise HTTPException(400,"approved production designs required")
    castings=db.scalars(select(CastingMapping).where(CastingMapping.project_id==project_id,CastingMapping.status=="APPROVED")).all()
    context={"project_id":project_id,"approved_designs":[{"id":r.id,"asset_id":r.asset_id,"asset_type":r.asset_type,"asset_name":r.asset_name,"version":r.version,"design":json.loads(r.design_json),"locked_attributes":json.loads(r.locked_attributes_json),"variable_attributes":json.loads(r.variable_attributes_json),"required_views":json.loads(r.required_views_json)} for r in latest.values()],"approved_castings":[{"character_asset_id":c.character_asset_id,"actor_ref":f"{c.actor_asset_id}@v{c.actor_version}","voice_ref":f"{c.voice_asset_id}@v{c.voice_version}"} for c in castings]}
    job_id=job_queue.create_job(json.dumps(context,ensure_ascii=False),req.priority,project_id,"asset_image_prompt_compiler"); await job_queue.enqueue(job_id); return {"job_id":job_id}

@app.get("/api/projects/{project_id}/asset-image-prompts")
def list_asset_image_prompts(project_id:str,db:Session=Depends(get_db)):
    rows=db.scalars(select(AssetImagePrompt).where(AssetImagePrompt.project_id==project_id).order_by(AssetImagePrompt.asset_id,AssetImagePrompt.view_id,AssetImagePrompt.version.desc())).all(); latest={}
    for r in rows: latest.setdefault((r.asset_id,r.view_id),r)
    return [{"id":r.id,"asset_id":r.asset_id,"asset_type":r.asset_type,"design_id":r.design_id,"view_id":r.view_id,"version":r.version,"status":r.status,"prompt":r.prompt_text,"negative_prompt":r.negative_prompt,"invariant_lock":json.loads(r.invariant_lock_json)} for r in latest.values()]

@app.patch("/api/asset-image-prompts/{prompt_id}")
def update_asset_image_prompt(prompt_id:int,req:UpdateAssetImagePromptRequest,db:Session=Depends(get_db)):
    r=db.get(AssetImagePrompt,prompt_id)
    if not r: raise HTTPException(404,"asset image prompt not found")
    d=req.model_dump(exclude_none=True)
    if "prompt" in d:r.prompt_text=d["prompt"]
    if "negative_prompt" in d:r.negative_prompt=d["negative_prompt"]
    if "invariant_lock" in d:r.invariant_lock_json=json.dumps(d["invariant_lock"],ensure_ascii=False)
    r.status="DRAFT";db.commit();return {"ok":True}

@app.post("/api/asset-image-prompts/{prompt_id}/approve")
def approve_asset_image_prompt(prompt_id:int,db:Session=Depends(get_db)):
    r=db.get(AssetImagePrompt,prompt_id)
    if not r: raise HTTPException(404,"asset image prompt not found")
    r.status="APPROVED";r.approved_at=__import__('datetime').datetime.now(__import__('datetime').timezone.utc);db.commit();return {"ok":True,"status":"APPROVED"}

@app.get("/api/workflow")
def workflow():
    return {"nodes":[{"id":i,"label":l,"order":n+1} for n,(i,l) in enumerate([("script","Script Input"),("extract","Asset Requirement Extractor"),("asset_workspace","Asset Requirement Workspace"),("cast","Casting Resolver"),("design","Production Designer"),("asset_prompt","Asset Image Prompt Compiler"),("asset_validate","Asset Image Validator"),("approved","Approved Asset Library"),("narrative","Narrative Keyframe"),("motion","Motion Scene Compiler"),("motion_validate","Motion Validator"),("motion_keyframe","Motion Keyframe Prompt Compiler"),("frames","Start / End Frames"),("h3","H3 Prompt Compiler"),("video","Video Output (Future)")])]}

@app.websocket("/ws/events")
async def websocket_endpoint(ws:WebSocket):
    await event_bus.connect(ws)
    try:
        await ws.send_json({"type":"system.connected"})
        while True: await ws.receive_text()
    except WebSocketDisconnect: await event_bus.disconnect(ws)
    except Exception: await event_bus.disconnect(ws)
