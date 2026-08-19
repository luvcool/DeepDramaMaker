# DramaStudio v0.4 — Production Designer + Asset Image Prompt Compiler

## Added

- ProductionDesign persistent model and approval workflow
- AssetImagePrompt persistent model and approval workflow
- LM Studio structured-output Production Designer job
- LM Studio structured-output Asset Image Prompt Compiler job
- Production Workspace UI
- Manual edit + approve gates for designs and prompts
- Prompt versions by asset/view

## Flow

```text
Approved Project Assets + Approved Casting
→ Production Designer
→ Human Edit / Approve
→ Asset Image Prompt Compiler
→ Human Edit / Approve
→ Next: image generation + Asset Image Validator
```

## Database

v0.4 introduces new tables. During prototype development, use a fresh SQLite database unless migrations are added.
