from datetime import datetime, timezone
from sqlalchemy import String, Text, DateTime, Integer, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .db import Base


def utcnow():
    return datetime.now(timezone.utc)


class Project(Base):
    __tablename__ = "projects"
    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class Job(Base):
    __tablename__ = "jobs"
    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    project_id: Mapped[str | None] = mapped_column(ForeignKey("projects.id"), nullable=True, index=True)
    node_type: Mapped[str] = mapped_column(String(100), default="asset_requirement_extractor")
    state: Mapped[str] = mapped_column(String(40), default="CREATED", index=True)
    priority: Mapped[int] = mapped_column(Integer, default=20)
    input_text: Mapped[str] = mapped_column(Text, default="")
    result_json: Mapped[str | None] = mapped_column(Text, nullable=True)
    error: Mapped[str | None] = mapped_column(Text, nullable=True)
    progress_message: Mapped[str] = mapped_column(String(255), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, onupdate=utcnow)

    attempts: Mapped[list["JobAttempt"]] = relationship(back_populates="job", cascade="all, delete-orphan")


class JobAttempt(Base):
    __tablename__ = "job_attempts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    job_id: Mapped[str] = mapped_column(ForeignKey("jobs.id"), index=True)
    attempt_no: Mapped[int] = mapped_column(Integer)
    state: Mapped[str] = mapped_column(String(40), default="CREATED")
    provider: Mapped[str] = mapped_column(String(100), default="LMSTUDIO_01")
    model: Mapped[str] = mapped_column(String(255), default="")
    raw_response: Mapped[str | None] = mapped_column(Text, nullable=True)
    error: Mapped[str | None] = mapped_column(Text, nullable=True)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    job: Mapped[Job] = relationship(back_populates="attempts")


class AssetDraft(Base):
    __tablename__ = "asset_drafts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    project_id: Mapped[str] = mapped_column(ForeignKey("projects.id"), index=True)
    source_job_id: Mapped[str] = mapped_column(ForeignKey("jobs.id"), index=True)
    asset_id: Mapped[str] = mapped_column(String(64), index=True)
    asset_type: Mapped[str] = mapped_column(String(50), index=True)
    name: Mapped[str] = mapped_column(String(200))
    persistence: Mapped[str] = mapped_column(String(30), default="scene")
    importance: Mapped[str] = mapped_column(String(30), default="medium")
    reference_required: Mapped[bool] = mapped_column(Boolean, default=False)
    known_attributes_json: Mapped[str] = mapped_column(Text, default="{}")
    missing_attributes_json: Mapped[str] = mapped_column(Text, default="[]")
    status: Mapped[str] = mapped_column(String(30), default="DRAFT", index=True)
    version: Mapped[int] = mapped_column(Integer, default=1)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, onupdate=utcnow)


class ProjectAsset(Base):
    __tablename__ = "project_assets"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    project_id: Mapped[str] = mapped_column(ForeignKey("projects.id"), index=True)
    asset_id: Mapped[str] = mapped_column(String(64), index=True)
    asset_type: Mapped[str] = mapped_column(String(50), index=True)
    name: Mapped[str] = mapped_column(String(200))
    version: Mapped[int] = mapped_column(Integer, default=1)
    status: Mapped[str] = mapped_column(String(30), default="APPROVED")
    payload_json: Mapped[str] = mapped_column(Text, default="{}")
    approved_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class GlobalAsset(Base):
    __tablename__ = "global_assets"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    asset_id: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    asset_type: Mapped[str] = mapped_column(String(30), index=True)  # actor / voice
    display_name: Mapped[str] = mapped_column(String(200))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class GlobalAssetVersion(Base):
    __tablename__ = "global_asset_versions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    global_asset_id: Mapped[int] = mapped_column(ForeignKey("global_assets.id"), index=True)
    version: Mapped[int] = mapped_column(Integer, default=1)
    status: Mapped[str] = mapped_column(String(30), default="DRAFT", index=True)
    metadata_json: Mapped[str] = mapped_column(Text, default="{}")
    reference_uri: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    approved_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)


class CastingMapping(Base):
    __tablename__ = "casting_mappings"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    project_id: Mapped[str] = mapped_column(ForeignKey("projects.id"), index=True)
    character_asset_id: Mapped[str] = mapped_column(String(64), index=True)
    character_name: Mapped[str] = mapped_column(String(200))
    actor_asset_id: Mapped[str | None] = mapped_column(String(64), nullable=True)
    actor_version: Mapped[int | None] = mapped_column(Integer, nullable=True)
    voice_asset_id: Mapped[str | None] = mapped_column(String(64), nullable=True)
    voice_version: Mapped[int | None] = mapped_column(Integer, nullable=True)
    status: Mapped[str] = mapped_column(String(30), default="DRAFT")
    notes: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, onupdate=utcnow)


class ProductionDesign(Base):
    __tablename__ = "production_designs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    project_id: Mapped[str] = mapped_column(ForeignKey("projects.id"), index=True)
    asset_id: Mapped[str] = mapped_column(String(64), index=True)
    asset_type: Mapped[str] = mapped_column(String(50), index=True)
    asset_name: Mapped[str] = mapped_column(String(200))
    source_asset_version: Mapped[int] = mapped_column(Integer, default=1)
    version: Mapped[int] = mapped_column(Integer, default=1)
    status: Mapped[str] = mapped_column(String(30), default="DRAFT", index=True)
    design_json: Mapped[str] = mapped_column(Text, default="{}")
    locked_attributes_json: Mapped[str] = mapped_column(Text, default="[]")
    variable_attributes_json: Mapped[str] = mapped_column(Text, default="[]")
    required_views_json: Mapped[str] = mapped_column(Text, default="[]")
    missing_attributes_json: Mapped[str] = mapped_column(Text, default="[]")
    source_job_id: Mapped[str | None] = mapped_column(ForeignKey("jobs.id"), nullable=True, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    approved_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)


class AssetImagePrompt(Base):
    __tablename__ = "asset_image_prompts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    project_id: Mapped[str] = mapped_column(ForeignKey("projects.id"), index=True)
    asset_id: Mapped[str] = mapped_column(String(64), index=True)
    asset_type: Mapped[str] = mapped_column(String(50), index=True)
    design_id: Mapped[int | None] = mapped_column(ForeignKey("production_designs.id"), nullable=True, index=True)
    view_id: Mapped[str] = mapped_column(String(80), index=True)
    version: Mapped[int] = mapped_column(Integer, default=1)
    status: Mapped[str] = mapped_column(String(30), default="DRAFT", index=True)
    prompt_text: Mapped[str] = mapped_column(Text)
    negative_prompt: Mapped[str] = mapped_column(Text, default="")
    invariant_lock_json: Mapped[str] = mapped_column(Text, default="[]")
    source_job_id: Mapped[str | None] = mapped_column(ForeignKey("jobs.id"), nullable=True, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    approved_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
