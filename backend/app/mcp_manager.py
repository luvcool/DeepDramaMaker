import asyncio
import json
import os
from pathlib import Path
from typing import Any

CONFIG_FILE = Path(__file__).resolve().parent.parent / "data" / "mcp_servers.json"

DEFAULT_CONFIG = {
    "MIR_STUDIO": {
        "id": "MIR_STUDIO",
        "display_name": "Mir Studio MCP",
        "enabled": False,
        "transport": "stdio",
        "command": "python",
        "args": [r"D:/Windy/mcp/mir-studio-mcp/server.py"],
        "env": {},
        "working_directory": "",
        "timeout_seconds": 3600,
        "serialize_calls": True,
        "notes": "generate_video/image should run sequentially; paths are relative to the MCP server machine."
    }
}

class MCPManager:
    def __init__(self):
        self._servers: dict[str, dict] = {}
        self._locks: dict[str, asyncio.Lock] = {}
        self.load()

    def load(self):
        try:
            if CONFIG_FILE.exists():
                saved = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
                self._servers = {**DEFAULT_CONFIG, **saved}
            else:
                self._servers = json.loads(json.dumps(DEFAULT_CONFIG))
                self.save()
        except Exception:
            self._servers = json.loads(json.dumps(DEFAULT_CONFIG))

    def save(self):
        CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
        CONFIG_FILE.write_text(json.dumps(self._servers, ensure_ascii=False, indent=2), encoding="utf-8")

    def list_servers(self) -> list[dict]:
        return [self._public(x) for x in self._servers.values()]

    def get(self, server_id: str) -> dict | None:
        return self._servers.get(server_id)

    def update(self, server_id: str, updates: dict) -> dict:
        current = self._servers.get(server_id) or {
            "id": server_id, "display_name": server_id, "enabled": False,
            "transport": "stdio", "command": "python", "args": [], "env": {},
            "working_directory": "", "timeout_seconds": 3600, "serialize_calls": True,
        }
        for k, v in updates.items():
            if v is not None:
                current[k] = v
        self._servers[server_id] = current
        self.save()
        return self._public(current)

    def _public(self, cfg: dict) -> dict:
        x = dict(cfg)
        env = dict(x.get("env") or {})
        for k in list(env):
            if "TOKEN" in k.upper() or "KEY" in k.upper() or "SECRET" in k.upper():
                env[k] = "***" if env[k] else ""
        x["env"] = env
        return x

    def _stdio_params(self, cfg: dict):
        try:
            from mcp import StdioServerParameters
        except ImportError as e:
            raise RuntimeError("Python package 'mcp' is not installed. Run: pip install mcp") from e
        env = os.environ.copy()
        env.update({str(k): str(v) for k, v in (cfg.get("env") or {}).items()})
        return StdioServerParameters(
            command=cfg.get("command") or "python",
            args=list(cfg.get("args") or []),
            env=env,
            cwd=cfg.get("working_directory") or None,
        )

    async def list_tools(self, server_id: str) -> list[dict]:
        cfg = self.get(server_id)
        if not cfg:
            raise KeyError(f"MCP server not found: {server_id}")
        if not cfg.get("enabled", False):
            raise RuntimeError(f"MCP server is disabled: {server_id}")
        try:
            from mcp import ClientSession
            from mcp.client.stdio import stdio_client
        except ImportError as e:
            raise RuntimeError("Python package 'mcp' is not installed. Run: pip install mcp") from e
        params = self._stdio_params(cfg)
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.list_tools()
                return [
                    {"name": t.name, "description": getattr(t, "description", None), "inputSchema": getattr(t, "inputSchema", None)}
                    for t in result.tools
                ]

    async def call_tool(self, server_id: str, tool_name: str, arguments: dict | None = None) -> dict:
        cfg = self.get(server_id)
        if not cfg:
            raise KeyError(f"MCP server not found: {server_id}")
        if not cfg.get("enabled", False):
            raise RuntimeError(f"MCP server is disabled: {server_id}")
        lock = self._locks.setdefault(server_id, asyncio.Lock())
        if cfg.get("serialize_calls", True):
            async with lock:
                return await self._call_tool_unlocked(cfg, tool_name, arguments or {})
        return await self._call_tool_unlocked(cfg, tool_name, arguments or {})

    async def _call_tool_unlocked(self, cfg: dict, tool_name: str, arguments: dict) -> dict:
        try:
            from mcp import ClientSession
            from mcp.client.stdio import stdio_client
        except ImportError as e:
            raise RuntimeError("Python package 'mcp' is not installed. Run: pip install mcp") from e
        params = self._stdio_params(cfg)
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool(tool_name, arguments)
                content = []
                for item in result.content:
                    text = getattr(item, "text", None)
                    if text is not None:
                        try:
                            content.append(json.loads(text))
                        except Exception:
                            content.append(text)
                    else:
                        content.append(str(item))
                return {"isError": bool(getattr(result, "isError", False)), "content": content}

mcp_manager = MCPManager()
