# DramaStudio Starter v0.3 — Asset Requirement Workspace + Global Casting

v0.2 upgrades the original vertical slice into the first real production workspace.

## New in v0.2

- Project creation / selection
- Extractor Job is bound to a Project
- Completed extraction can be materialized into editable Asset Drafts
- Asset Requirement Workspace + Global Casting
  - type-grouped asset table
  - name / persistence / importance editing
  - reference-required flag
  - known_attributes JSON editor
  - missing_attributes editor
- Per-asset Approve
- Approve All
- Approved Project Asset Registry with immutable version increments
- Job panel with Retry / Cancel / Open Workspace
- Pipeline graph now includes an explicit **Asset Requirement Workspace + Global Casting** node
- Existing LM Studio / Queue / JobAttempt architecture preserved

## Quick start

### Backend
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload --port 8000
```

### Frontend
```powershell
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`.

## First use

1. Click **+ New** in the top Project selector.
2. Configure `backend/.env` for the remote LM Studio PC.
3. Confirm `LM Studio ONLINE`.
4. Run the extractor from the lower Script panel.
5. Open the new Job in the Job panel after it reaches `COMPLETED`.
6. Click **Open Workspace**.
7. Edit extracted assets as needed.
8. Approve assets individually or use **Approve All**.
9. Open the **Registry** tab to verify project assets and versions.

## v0.2 workflow

```text
Script Input
  ↓
Asset Requirement Extractor
  ↓
Asset Requirement Workspace + Global Casting
  ├─ Edit
  ├─ Missing Definition Review
  ├─ Approve / Reject later
  ↓
Project Asset Registry
  ↓
Casting Resolver (next)
  ↓
Production Designer (next)
```

## Database note

If you previously ran v0.1, use a fresh SQLite database for this starter because v0.2 adds tables/columns and no migration framework is included yet.
Delete `backend/data/dramastudio.db` before the first v0.2 run if necessary.

The next logical version is v0.3: **Casting Resolver + Global Actor/Voice Library mapping**.


## v0.3 additions

- Global Actor Library (`ACTOR_###@vN`)
- Global Voice Library (`VOICE_###@vN`)
- DRAFT / APPROVED global asset versions
- Project Character → Actor/Voice casting mapping
- Casting approval requires APPROVED actor + voice versions
- Existing project character assets remain separate from reusable performer identity assets

### Recommended test flow

1. Create project.
2. Run Asset Requirement Extractor.
3. Open Requirements and approve Character assets.
4. Open Casting → Global Library.
5. Create Actor and Voice, approve v1.
6. Return to Casting and map each Character.
7. Save mapping, then Approve.

## v0.4.1 Debug + MCP additions

- Detailed Job Diagnostics and traceback UI
- `backend/data/logs/dramastudio.log`
- Generic stdio MCP registry
- Mir Studio MCP settings / tool discovery / `check_backends`
- MCP tool calls through persistent DramaStudio Job Queue

See `docs/MIGRATION_v0.4.1_debug_mcp.md` and `docs/mcp/MIR_STUDIO_USAGE.md`.
