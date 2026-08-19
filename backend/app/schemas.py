from typing import Literal
from pydantic import BaseModel, Field


class AssetRequirement(BaseModel):
    asset_id: str
    type: Literal["character", "voice", "location", "wardrobe", "vehicle", "prop", "environment", "other"]
    name: str
    persistence: Literal["persistent", "scene", "background"] = "scene"
    importance: Literal["critical", "high", "medium", "low"] = "medium"
    reference_required: bool = False
    known_attributes: dict = Field(default_factory=dict)
    missing_attributes: list[str] = Field(default_factory=list)


class AssetExtractionResult(BaseModel):
    assets: list[AssetRequirement]
    relationships: list[dict] = Field(default_factory=list)
    missing_definition_report: list[str] = Field(default_factory=list)
    construction_queue: list[dict] = Field(default_factory=list)


class CreateJobRequest(BaseModel):
    script: str
    priority: int = 20
    project_id: str | None = None


class CreateProjectRequest(BaseModel):
    name: str


class UpdateAssetDraftRequest(BaseModel):
    name: str | None = None
    persistence: Literal["persistent", "scene", "background"] | None = None
    importance: Literal["critical", "high", "medium", "low"] | None = None
    reference_required: bool | None = None
    known_attributes: dict | None = None
    missing_attributes: list[str] | None = None


class CreateGlobalAssetRequest(BaseModel):
    asset_type: Literal["actor", "voice"]
    display_name: str
    metadata: dict = Field(default_factory=dict)
    reference_uri: str | None = None


class CreateGlobalAssetVersionRequest(BaseModel):
    metadata: dict = Field(default_factory=dict)
    reference_uri: str | None = None


class UpsertCastingRequest(BaseModel):
    character_asset_id: str
    character_name: str
    actor_asset_id: str | None = None
    actor_version: int | None = None
    voice_asset_id: str | None = None
    voice_version: int | None = None
    notes: str = ""


class UpdateCastingRequest(BaseModel):
    actor_asset_id: str | None = None
    actor_version: int | None = None
    voice_asset_id: str | None = None
    voice_version: int | None = None
    notes: str | None = None
    status: Literal["DRAFT", "APPROVED"] | None = None


class ProductionDesignItem(BaseModel):
    asset_id: str
    asset_type: str
    asset_name: str
    design: dict = Field(default_factory=dict)
    locked_attributes: list[str] = Field(default_factory=list)
    variable_attributes: list[str] = Field(default_factory=list)
    required_views: list[str] = Field(default_factory=list)
    missing_attributes: list[str] = Field(default_factory=list)

class ProductionDesignResult(BaseModel):
    designs: list[ProductionDesignItem]
    warnings: list[str] = Field(default_factory=list)

class AssetImagePromptItem(BaseModel):
    asset_id: str
    asset_type: str
    view_id: str
    prompt: str
    negative_prompt: str = ""
    invariant_lock: list[str] = Field(default_factory=list)

class AssetImagePromptResult(BaseModel):
    prompts: list[AssetImagePromptItem]
    warnings: list[str] = Field(default_factory=list)

class CreatePipelineJobRequest(BaseModel):
    priority: int = 20

class UpdateProductionDesignRequest(BaseModel):
    design: dict | None = None
    locked_attributes: list[str] | None = None
    variable_attributes: list[str] | None = None
    required_views: list[str] | None = None
    missing_attributes: list[str] | None = None

class UpdateAssetImagePromptRequest(BaseModel):
    prompt: str | None = None
    negative_prompt: str | None = None
    invariant_lock: list[str] | None = None

class UpdateProviderConfigRequest(BaseModel):
    enabled: bool | None = None
    base_url: str | None = None
    model: str | None = None
    timeout_seconds: float | None = None
    max_retries: int | None = None
    temperature: float | None = None
    auto_select_model: bool | None = None
    structured_output: bool | None = None
    api_token: str | None = None

class TestProviderRequest(BaseModel):
    base_url: str | None = None
    model: str | None = None
    api_token: str | None = None

class RefreshModelsRequest(BaseModel):
    base_url: str | None = None
