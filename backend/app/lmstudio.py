import json
import httpx
from .config import settings
from .schemas import AssetExtractionResult, ProductionDesignResult, AssetImagePromptResult


def _http_error_details(exc: Exception, *, url: str, model: str) -> RuntimeError:
    if isinstance(exc, httpx.HTTPStatusError):
        r = exc.response
        body = r.text[:5000] if r is not None else ""
        return RuntimeError(
            f"LM Studio HTTP error | status={r.status_code if r else 'unknown'} | "
            f"url={url} | model={model} | response={body}"
        )
    if isinstance(exc, httpx.ConnectError):
        return RuntimeError(f"LM Studio connection failed | url={url} | model={model} | detail={exc}")
    if isinstance(exc, httpx.TimeoutException):
        return RuntimeError(f"LM Studio timeout | url={url} | model={model} | detail={exc}")
    return RuntimeError(f"LM Studio request failed | url={url} | model={model} | {type(exc).__name__}: {exc}")


ASSET_SCHEMA = {
    "name": "asset_extraction_result",
    "strict": True,
    "schema": {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "assets": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "asset_id": {"type": "string"},
                        "type": {
                            "type": "string",
                            "enum": ["character", "voice", "location", "wardrobe", "vehicle", "prop", "environment", "other"]
                        },
                        "name": {"type": "string"},
                        "persistence": {"type": "string", "enum": ["persistent", "scene", "background"]},
                        "importance": {"type": "string", "enum": ["critical", "high", "medium", "low"]},
                        "reference_required": {"type": "boolean"},
                        "known_attributes": {"type": "object"},
                        "missing_attributes": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": [
                        "asset_id", "type", "name", "persistence", "importance",
                        "reference_required", "known_attributes", "missing_attributes"
                    ]
                }
            },
            "relationships": {"type": "array", "items": {"type": "object"}},
            "missing_definition_report": {"type": "array", "items": {"type": "string"}},
            "construction_queue": {"type": "array", "items": {"type": "object"}}
        },
        "required": ["assets", "relationships", "missing_definition_report", "construction_queue"]
    }
}


SYSTEM_PROMPT = """You are the Asset Requirement Extractor for a short-form drama production pipeline.

Analyze the supplied script ONLY for production assets required to visualize it.

Rules:
- Do not invent missing facts. Put unknowns into missing_attributes.
- Merge repeated references that clearly refer to the same entity.
- Characters are project characters; voice is separately represented if voice identity is needed.
- Classify persistence as persistent / scene / background.
- Mark recurring lead characters, recurring locations, signature vehicles and story-critical props as important.
- Locations may be hierarchical; use known_attributes for parent_location / zone when useful.
- Return only structured JSON matching the required schema.
- Use stable readable IDs such as CHAR_001, VOICE_001, LOC_001, WARD_001, VEH_001, PROP_001.
"""


class LMStudioProvider:
    def __init__(self, provider_id: str = "LMSTUDIO_01"):
        self.provider_id = provider_id

    @property
    def config(self) -> dict:
        from .providers import provider_manager
        p = provider_manager.get_provider(self.provider_id)
        if not p:
            p = provider_manager.get_provider("LMSTUDIO_01")
        return p or {}

    @property
    def base_url(self) -> str:
        return self.config.get("base_url", settings.lmstudio_base_url).rstrip("/")

    @property
    def model(self) -> str:
        return self.config.get("model", settings.lmstudio_model)

    @property
    def timeout(self) -> float:
        return float(self.config.get("timeout_seconds", settings.lmstudio_timeout_seconds))

    @property
    def temperature(self) -> float:
        return float(self.config.get("temperature", 0.1))

    async def health() -> dict:
        from .providers import provider_manager
        return await provider_manager.get_health(self.provider_id)

    async def extract_assets(self, script: str) -> tuple[dict, str]:
        model = self.model
        if not model:
            health = await self.health()
            models = health.get("models", [])
            if not models:
                raise RuntimeError("LM Studio has no discoverable loaded model and configured model is empty.")
            model = models[0]

        headers = {}
        if self.config.get("api_token"):
            headers["Authorization"] = f"Bearer {self.config['api_token']}"

        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": script},
            ],
            "temperature": self.temperature,
            "response_format": {
                "type": "json_schema",
                "json_schema": ASSET_SCHEMA,
            },
        }

        url = f"{self.base_url}/chat/completions"
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(url, json=payload, headers=headers)
                response.raise_for_status()
                raw = response.text
                data = response.json()
        except Exception as exc:
            raise _http_error_details(exc, url=url, model=model) from exc

        try:
            content = data["choices"][0]["message"]["content"]
            parsed = json.loads(content)
            validated = AssetExtractionResult.model_validate(parsed)
            return validated.model_dump(), raw
        except Exception as exc:
            excerpt = raw[:5000] if 'raw' in locals() else str(data)[:5000]
            raise RuntimeError(f"LM Studio structured-output parse/validation failed | model={model} | raw_response={excerpt} | {type(exc).__name__}: {exc}") from exc


PRODUCTION_DESIGN_SYSTEM = """You are the Production Designer for a short-form drama production pipeline.
Input is an approved project asset registry plus approved casting mappings.
Design ONLY project-specific visual assets: location, wardrobe, vehicle, prop, environment, and character styling overrides when needed.
Do not redesign the approved global actor identity or approved global voice identity.
Do not invent facts that should remain unknown; report them in missing_attributes.
For every asset, produce reusable reference specifications rather than cinematic scene prose.
Prioritize identity, geometry, material, scale, cross-view consistency, visibility and interaction usefulness.
Return JSON only matching the schema."""

ASSET_IMAGE_PROMPT_SYSTEM = """You are the Asset Image Prompt Compiler for DramaStudio.
Convert approved production design records into reusable reference-image generation prompts.
These are ASSET reference prompts, not narrative keyframes and not motion prompts.
Use high structural density and low narrative density. Prefer neutral camera, clear visibility, minimal occlusion and consistent geometry.
For actors referenced through casting, preserve the approved actor identity and do not invent a new face.
Generate one prompt per required view. Clearly lock invariant attributes. Avoid readable labels, logos and unnecessary cinematic effects.
Return JSON only matching the schema."""

PRODUCTION_DESIGN_SCHEMA = {
 "name":"production_design_result","strict":True,"schema":{
  "type":"object","additionalProperties":False,
  "properties":{
   "designs":{"type":"array","items":{"type":"object","additionalProperties":False,"properties":{
    "asset_id":{"type":"string"},"asset_type":{"type":"string"},"asset_name":{"type":"string"},
    "design":{"type":"object"},"locked_attributes":{"type":"array","items":{"type":"string"}},
    "variable_attributes":{"type":"array","items":{"type":"string"}},"required_views":{"type":"array","items":{"type":"string"}},
    "missing_attributes":{"type":"array","items":{"type":"string"}}},
    "required":["asset_id","asset_type","asset_name","design","locked_attributes","variable_attributes","required_views","missing_attributes"]}},
   "warnings":{"type":"array","items":{"type":"string"}}
  },"required":["designs","warnings"]}}

ASSET_IMAGE_PROMPT_SCHEMA = {
 "name":"asset_image_prompt_result","strict":True,"schema":{
  "type":"object","additionalProperties":False,
  "properties":{
   "prompts":{"type":"array","items":{"type":"object","additionalProperties":False,"properties":{
    "asset_id":{"type":"string"},"asset_type":{"type":"string"},"view_id":{"type":"string"},
    "prompt":{"type":"string"},"negative_prompt":{"type":"string"},"invariant_lock":{"type":"array","items":{"type":"string"}}},
    "required":["asset_id","asset_type","view_id","prompt","negative_prompt","invariant_lock"]}},
   "warnings":{"type":"array","items":{"type":"string"}}
  },"required":["prompts","warnings"]}}

async def _structured_generate(self, system_prompt: str, user_payload: dict, schema: dict, validator):
    model = self.model
    if not model:
        health = await self.health(); models = health.get("models", [])
        if not models: raise RuntimeError("LM Studio has no discoverable loaded model and configured model is empty.")
        model = models[0]

    headers = {}
    if self.config.get("api_token"):
        headers["Authorization"] = f"Bearer {self.config['api_token']}"

    payload={"model":model,"messages":[{"role":"system","content":system_prompt},{"role":"user","content":json.dumps(user_payload,ensure_ascii=False)}],"temperature":self.temperature,"response_format":{"type":"json_schema","json_schema":schema}}
    url=f"{self.base_url}/chat/completions"
    try:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response=await client.post(url,json=payload,headers=headers)
            response.raise_for_status()
            raw=response.text
            data=response.json()
    except Exception as exc:
        raise _http_error_details(exc, url=url, model=model) from exc
    try:
        parsed=json.loads(data["choices"][0]["message"]["content"])
        return validator.model_validate(parsed).model_dump(), raw
    except Exception as exc:
        raise RuntimeError(f"LM Studio structured-output parse/validation failed | model={model} | raw_response={raw[:5000]} | {type(exc).__name__}: {exc}") from exc

LMStudioProvider._structured_generate = _structured_generate

async def _production_design(self, context: dict):
    return await self._structured_generate(PRODUCTION_DESIGN_SYSTEM, context, PRODUCTION_DESIGN_SCHEMA, ProductionDesignResult)
LMStudioProvider.production_design = _production_design

async def _compile_asset_image_prompts(self, context: dict):
    return await self._structured_generate(ASSET_IMAGE_PROMPT_SYSTEM, context, ASSET_IMAGE_PROMPT_SCHEMA, AssetImagePromptResult)
LMStudioProvider.compile_asset_image_prompts = _compile_asset_image_prompts
