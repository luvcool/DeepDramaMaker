# Asset Requirement Schema

`requirements.json` 최상위 구조:

```json
{
  "schema_version": "1.0",
  "project": "slug",
  "assets": [
    {
      "asset_id": "CHAR-SEOHA",
      "type": "character",
      "name": "한서하",
      "scope": "project_dedicated",
      "persistence": "persistent",
      "importance": "critical",
      "priority": "P0",
      "source_refs": ["00_bible/characters.md", "ep01 S#1"],
      "actor_ref": "UNASSIGNED",
      "voice_ref": "UNASSIGNED",
      "visual_identity_required": true,
      "voice_identity_required": true,
      "performance_profile_required": true,
      "known_attributes": {},
      "missing_attributes": []
    }
  ]
}
```

`state-ledger.json`은 `asset_id`, `from`, `to`, `state`, `source_ref`를 사용한다. 상태가 끝나지 않으면 후속 씬에 계속 적용되는 것으로 본다.

`relationships.json`의 관계 동사는 최소 `portrayed_by`, `voiced_by`, `owns`, `uses`, `wears`, `lives_at`, `works_at`, `located_in`, `connected_to`, `carries`를 사용한다.
