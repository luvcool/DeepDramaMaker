import json
import traceback
from datetime import datetime, timezone
from typing import Any


def _safe(value: Any, limit: int = 4000) -> Any:
    if value is None:
        return None
    if isinstance(value, (dict, list)):
        try:
            text = json.dumps(value, ensure_ascii=False, default=str)
        except Exception:
            text = str(value)
    else:
        text = str(value)
    if len(text) > limit:
        return text[:limit] + f"... <truncated {len(text)-limit} chars>"
    return text


def exception_diagnostics(exc: BaseException, *, stage: str, context: dict | None = None) -> dict:
    cause = exc.__cause__ or exc.__context__
    data = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "stage": stage,
        "exception_type": type(exc).__name__,
        "message": str(exc),
        "traceback": traceback.format_exc(),
        "context": {},
    }
    if cause and cause is not exc:
        data["cause"] = {"type": type(cause).__name__, "message": str(cause)}
    for k, v in (context or {}).items():
        if "token" in k.lower() or "key" in k.lower() or "secret" in k.lower():
            data["context"][k] = "***"
        else:
            data["context"][k] = _safe(v)
    return data


def compact_error(diag: dict) -> str:
    stage = diag.get("stage", "unknown")
    typ = diag.get("exception_type", "Error")
    msg = diag.get("message", "")
    return f"[{stage}] {typ}: {msg}"
