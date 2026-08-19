# DramaStudio Workflow Integration

The `docs/workflow-v5/` directory is not merely reference documentation.

It is the canonical source material for the DramaStudio production workflow that
the application will progressively turn into executable Node Definitions.

## Current relationship

```text
docs/workflow-v5/
        ↓
Workflow / Skill specifications
        ↓
Node Definition Loader        (next implementation step)
        ↓
WorkflowVersion
        ↓
Node Graph UI
        ↓
Job / Queue / Worker
```

## Source-of-truth layers

### 1. Global / project production workflow
`docs/workflow-v5/`

Contains the workflow rules created for:

- Asset Requirement Extraction
- Global actor / voice asset separation
- Project-specific assets
- Asset image prompt compilation
- Asset image validation
- Narrative keyframes
- Motion scene compilation
- Motion validation
- Motion start/end keyframe prompt compilation
- Asset / prompt / state continuity rules

### 2. System architecture
`docs/architecture/`

Contains the implementation architecture for:

- React / TypeScript UI
- FastAPI backend
- LM Studio provider
- Job / JobAttempt
- Queue / Retry / Timeout
- Workflow DAG
- Asset versioning
- Artifact persistence
- WebSocket monitoring
- First vertical slice

### 3. Executable application
`frontend/` + `backend/`

The application should never duplicate workflow rules by hand if the same rule
already exists in the workflow specification. Over time, hard-coded starter nodes
should be replaced by definitions loaded from the workflow package.

## Version rule

A Workflow Run must eventually pin:

```text
workflow_version
skill_version
prompt_version
schema_version
asset_versions
provider_profile
model_id
```

so that a production result can be reproduced or audited later.

## Next implementation target

Implement a `WorkflowDefinitionLoader` that indexes the workflow package and exposes:

```text
GET /api/definitions/skills
GET /api/definitions/nodes
GET /api/definitions/workflows
```

The React graph can then render nodes from those definitions instead of the current
hard-coded demo graph.
