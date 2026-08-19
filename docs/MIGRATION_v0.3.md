# DramaStudio v0.3 Migration

## Added

- Global Actor Library: `ACTOR_###@vN`
- Global Voice Library: `VOICE_###@vN`
- Global asset version states: `DRAFT`, `APPROVED`
- Project Character -> Actor/Voice mapping
- Casting approval gate: both actor and voice versions must be APPROVED
- Casting Workspace UI
- Global Library UI

## Separation rule

Project `CHAR_###` assets are roles inside one drama. Global `ACTOR_###` and `VOICE_###` assets are reusable performer identities shared across projects.

## Test flow

1. Create/select a project.
2. Run Asset Requirement Extractor.
3. Open Requirements and approve Character assets.
4. Open Casting -> Global Library.
5. Create an Actor and Voice; approve their versions.
6. Map each project Character to an approved Actor and Voice.
7. Save and Approve casting.

## Database

For the starter build, begin with a fresh SQLite DB. Alembic migration support is not yet included and should be added before preserving production databases across schema versions.
