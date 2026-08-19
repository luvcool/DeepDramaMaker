import json
import os
import time
import httpx
from .config import settings

CONFIG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "providers_config.json")

DEFAULT_PROVIDERS = {
    "LMSTUDIO_01": {
        "id": "LMSTUDIO_01",
        "type": "lmstudio",
        "displayName": "LM Studio",
        "enabled": True,
        "base_url": settings.lmstudio_base_url,
        "model": settings.lmstudio_model,
        "timeout_seconds": settings.lmstudio_timeout_seconds,
        "max_retries": 3,
        "temperature": 0.1,
        "auto_select_model": True,
        "structured_output": True,
        "api_token": ""
    },
    "OPENAI_01": {
        "id": "OPENAI_01",
        "type": "openai",
        "displayName": "OpenAI",
        "enabled": False,
        "base_url": "https://api.openai.com/v1",
        "model": "gpt-4o",
        "timeout_seconds": 60,
        "max_retries": 3,
        "temperature": 0.7,
        "auto_select_model": False,
        "structured_output": True,
        "api_token": ""
    },
    "CUSTOM_01": {
        "id": "CUSTOM_01",
        "type": "custom-openai",
        "displayName": "Custom API",
        "enabled": False,
        "base_url": "http://localhost:8080/v1",
        "model": "",
        "timeout_seconds": 120,
        "max_retries": 3,
        "temperature": 0.1,
        "auto_select_model": True,
        "structured_output": True,
        "api_token": ""
    }
}


class ProviderManager:
    def __init__(self):
        self._providers = {}
        self.load_config()

    def load_config(self):
        try:
            if os.path.exists(CONFIG_FILE):
                with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self._providers = {**DEFAULT_PROVIDERS, **data}
            else:
                self._providers = json.loads(json.dumps(DEFAULT_PROVIDERS))
                self.save_config()
        except Exception:
            self._providers = json.loads(json.dumps(DEFAULT_PROVIDERS))

    def save_config(self):
        try:
            os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
            with open(CONFIG_FILE, "w", encoding="utf-8") as f:
                json.dump(self._providers, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error saving provider config: {e}")

    def list_providers(self) -> list[dict]:
        return list(self._providers.values())

    def get_provider(self, provider_id: str) -> dict | None:
        return self._providers.get(provider_id)

    def update_provider(self, provider_id: str, updates: dict) -> dict:
        if provider_id not in self._providers:
            # allow updating LMSTUDIO_01 if requested as 'lmstudio'
            if provider_id.lower() == "lmstudio":
                provider_id = "LMSTUDIO_01"
            else:
                raise KeyError(f"Provider {provider_id} not found")

        current = self._providers[provider_id]
        for k, v in updates.items():
            if v is not None:
                current[k] = v

        if "base_url" in current and current["base_url"]:
            current["base_url"] = current["base_url"].rstrip("/")

        self._providers[provider_id] = current
        self.save_config()
        return current

    async def get_health(self, provider_id: str = "LMSTUDIO_01") -> dict:
        p = self.get_provider(provider_id) or self.get_provider("LMSTUDIO_01")
        if not p or not p.get("enabled", True):
            return {
                "state": "DISABLED",
                "base_url": p.get("base_url", "") if p else "",
                "configured_model": p.get("model", "") if p else "",
                "models": [],
            }

        base_url = p.get("base_url", settings.lmstudio_base_url).rstrip("/")
        model = p.get("model", "")
        headers = {}
        if p.get("api_token"):
            headers["Authorization"] = f"Bearer {p['api_token']}"

        try:
            async with httpx.AsyncClient(timeout=8) as client:
                resp = await client.get(f"{base_url}/models", headers=headers)
                resp.raise_for_status()
                data = resp.json()
                model_ids = [m.get("id") for m in data.get("data", []) if m.get("id")]
                
                # Rule 8: If auto_select_model is ON and model is empty or not in model_ids
                if p.get("auto_select_model", True):
                    if not model or model not in model_ids:
                        if model_ids:
                            model = model_ids[0]
                            p["model"] = model
                            self.save_config()

                return {
                    "state": "ONLINE",
                    "base_url": base_url,
                    "configured_model": model,
                    "models": model_ids,
                }
        except Exception as exc:
            return {
                "state": "OFFLINE",
                "base_url": base_url,
                "configured_model": model,
                "error": str(exc),
            }

    async def test_connection(self, provider_id: str, payload_override: dict | None = None) -> dict:
        p = self.get_provider(provider_id) or self.get_provider("LMSTUDIO_01")
        if not p:
            return {"status": "OFFLINE", "error": "Provider not found"}

        base_url = (payload_override.get("base_url") if payload_override and payload_override.get("base_url") else p.get("base_url", "")).rstrip("/")
        model = payload_override.get("model") if payload_override and payload_override.get("model") is not None else p.get("model", "")
        api_token = payload_override.get("api_token") if payload_override and payload_override.get("api_token") is not None else p.get("api_token", "")

        headers = {}
        if api_token:
            headers["Authorization"] = f"Bearer {api_token}"

        start_time = time.time()
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(f"{base_url}/models", headers=headers)
                elapsed_ms = int((time.time() - start_time) * 1000)
                resp.raise_for_status()
                data = resp.json()
                models = [m.get("id") for m in data.get("data", []) if m.get("id")]
                
                # Format endpoint display (e.g. 192.168.0.30:1234)
                endpoint_display = base_url.replace("http://", "").replace("https://", "").replace("/v1", "")

                return {
                    "status": "ONLINE",
                    "endpoint": endpoint_display,
                    "base_url": base_url,
                    "model": model or (models[0] if models else ""),
                    "models_count": len(models),
                    "models": models,
                    "response_time_ms": elapsed_ms,
                    "error": None
                }
        except Exception as exc:
            elapsed_ms = int((time.time() - start_time) * 1000)
            endpoint_display = base_url.replace("http://", "").replace("https://", "").replace("/v1", "")
            err_msg = str(exc)
            if "ConnectError" in err_msg or "Connection refused" in err_msg:
                err_code = "CONNECTION_REFUSED"
            elif "Timeout" in err_msg:
                err_code = "TIMEOUT"
            else:
                err_code = err_msg

            return {
                "status": "OFFLINE",
                "endpoint": endpoint_display,
                "base_url": base_url,
                "model": model,
                "models_count": 0,
                "models": [],
                "response_time_ms": elapsed_ms,
                "error": f"{err_code}: {err_msg}"
            }

    async def refresh_models(self, provider_id: str, base_url_override: str | None = None) -> dict:
        p = self.get_provider(provider_id) or self.get_provider("LMSTUDIO_01")
        if not p:
            return {"success": False, "models": [], "error": "Provider not found"}

        base_url = (base_url_override or p.get("base_url", "")).rstrip("/")
        headers = {}
        if p.get("api_token"):
            headers["Authorization"] = f"Bearer {p['api_token']}"

        try:
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(f"{base_url}/models", headers=headers)
                resp.raise_for_status()
                data = resp.json()
                model_ids = [m.get("id") for m in data.get("data", []) if m.get("id")]
                
                # Rule 8: If auto_select_model is ON and model is empty or not in model_ids
                selected_model = p.get("model", "")
                if p.get("auto_select_model", True):
                    if not selected_model or selected_model not in model_ids:
                        if model_ids:
                            selected_model = model_ids[0]
                            p["model"] = selected_model
                            self.save_config()

                return {
                    "success": True,
                    "models": model_ids,
                    "selected_model": selected_model,
                    "message": f"{len(model_ids)} models found"
                }
        except Exception as exc:
            return {
                "success": False,
                "models": [],
                "selected_model": p.get("model", ""),
                "error": f"Failed to refresh models: {str(exc)}"
            }


provider_manager = ProviderManager()
