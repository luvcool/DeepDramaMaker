# Motion Plan Schema v1.0

회차별 파일: `09_motion/epXX-motion.json`

```json
{
  "episode": 1,
  "source_script": "01_script/ep01.md",
  "shots": [
    {
      "scene_id": "EP01-S01",
      "shot_id": "EP01-S01-SH01",
      "target_duration_sec": 2.0,
      "source_keyframe": "KF-EP01-S01-01",
      "cut_reason": "physical_state_change",
      "primary_motion": "S1 extends the flower and transfers it to S2",
      "motion_priority": {
        "primary": ["flower_transfer"],
        "secondary": ["mutual_gaze_shift", "expression_softening"],
        "support": ["gentle_push_in", "light_hair_movement"]
      },
      "frame_staging": {
        "S1": "lower-left, facing frame-right",
        "S2": "lower-right, facing frame-left"
      },
      "start_state": {
        "S1": {"pose": "standing", "gaze": "S2 eyes", "right_hand": "holding FLOWER"},
        "S2": {"pose": "standing", "gaze": "S1 face", "left_hand": "relaxed"},
        "FLOWER": {"owner": "S1", "position": "S1 right hand"}
      },
      "micro_beats": [
        "S1 extends flower while keeping nervous eye contact",
        "S2 gaze shifts from S1 face to flower and expression softens",
        "S2 grips stem; S1 releases; both look back at each other"
      ],
      "gaze": {
        "S1": "S2 eyes -> flower briefly -> S2 eyes",
        "S2": "S1 face -> flower -> S1 eyes"
      },
      "expression_transition": {
        "S1": "nervous -> relieved",
        "S2": "guarded -> surprised -> small smile"
      },
      "secondary_body_motion": ["S1 small weight shift forward", "S2 shoulders soften"],
      "life_motion": ["subtle breathing", "light hair and sleeve movement"],
      "camera_motion": "gentle push-in",
      "environment_motion": ["light breeze moves loose hair"],
      "contact_topology": [
        "S1.right_hand -> FLOWER.stem : holding",
        "S2.left_hand -> FLOWER.stem : receiving",
        "S1.right_hand -> FLOWER.stem : release_at_end"
      ],
      "visibility_constraints": ["both hands visible", "FLOWER remains unobstructed", "both faces visible"],
      "result": "FLOWER ends fully in S2 left hand",
      "end_state": {
        "S1": {"right_hand": "empty", "gaze": "S2 eyes"},
        "S2": {"left_hand": "holding FLOWER", "gaze": "S1 eyes"},
        "FLOWER": {"owner": "S2", "position": "S2 left hand"}
      },
      "complexity": {
        "score": 2,
        "factors": ["object_transfer", "reaction_shift"],
        "split_recommended": false,
        "motion_budget": "safe"
      },
      "continuity_from_previous": "N/A"
    }
  ]
}
```

## 필수 키

Shot마다 반드시:
- `scene_id`, `shot_id`, `target_duration_sec`
- `cut_reason`
- `primary_motion`
- `motion_priority.primary`
- `frame_staging`
- `start_state`, `end_state`
- `micro_beats`
- `gaze`
- `expression_transition`
- `life_motion`
- `camera_motion`
- `contact_topology`
- `visibility_constraints`
- `result`
- `complexity.score`, `complexity.factors`, `complexity.split_recommended`, `complexity.motion_budget`
- `continuity_from_previous`

`camera_motion`이 `static`이면 왜 정적인지 `micro_beats` 또는 `result`에서 연출 이유가 드러나야 한다.

## `cut_reason` 권장 값

- `physical_state_change`
- `emotional_state_change`
- `information_reveal`
- `reaction_shift`
- `contact_change`
- `object_transfer_complete`
- `location_change`
- `intentional_hold`

## Motion Budget 권장 값

- `safe`
- `dense_but_controlled`
- `high_risk_split_recommended`
