# DramaStudio v0.4.1-debug-mcp

## What changed

### Detailed debugging
- Job failures now save structured diagnostics instead of only `Execution failed`.
- Diagnostics include stage, exception type, message, Python traceback and execution context.
- LM Studio HTTP failures include endpoint, model, HTTP status and response excerpt where available.
- Job Detail shows Diagnostics, Attempts and a Copy button.
- Recent Activity shows the first useful error summary.
- Rotating backend log: `backend/data/logs/dramastudio.log`.
- New endpoint: `GET /api/jobs/{job_id}/diagnostics`.

### MCP support
- Generic stdio MCP server registry added.
- Default server profile: `MIR_STUDIO`.
- Settings Center → MCP Servers → Mir Studio MCP.
- Test/List Tools and `check_backends` buttons.
- MCP tool calls can be submitted as persistent DramaStudio Jobs.
- MCP jobs use the same Job / Attempt / Retry / diagnostics system.
- Per-server serialization lock is enabled by default.

## MCP API

```text
GET  /api/mcp/servers
GET  /api/mcp/servers/{server_id}
PUT  /api/mcp/servers/{server_id}
POST /api/mcp/servers/{server_id}/test
GET  /api/mcp/servers/{server_id}/tools
POST /api/mcp/servers/{server_id}/check-backends
POST /api/mcp/jobs
```

Example MCP queue job:

```json
{
  "server_id": "MIR_STUDIO",
  "tool_name": "generate_image",
  "project_id": "PRJ_...",
  "priority": 30,
  "arguments": {
    "prompt": "a persimmon on a wooden table, soft window light",
    "width": 768,
    "height": 768,
    "out": "test.png"
  }
}
```

## Mir Studio notes

- Install backend dependency: `pip install -r requirements.txt` (`mcp` was added).
- Enable Mir Studio MCP in Settings and set the path to `server.py`.
- Run `check_backends` before long generation batches.
- stdio means file paths are resolved on the PC where `server.py` is spawned.
- image/video calls can take minutes and have no progress callback.
- Keep `Serialize Calls` enabled for the provided Mir Studio MCP because ComfyUI contention makes concurrent generation slower.

## Validation performed
- Python modules compile successfully.
- FastAPI health and MCP registry endpoints smoke-tested.
- Frontend TypeScript (`tsc -b`) passes.
- Full Vite build could not be executed in the Linux sandbox because the uploaded `node_modules` contains Windows-native Rollup dependencies. Run `npm install` and `npm run build` on the target Windows PC.
