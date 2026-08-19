---
name: drama-motion-validator
description: `09_motion/epXX-motion.json`의 물리 상태·Motion Density·Cut·Contact Topology·소품 연속성을 검증하는 영상화 준비 QA 스킬. 짧은 Shot의 생동감 부족, 과도한 Story Motion, 정적인 시선/표정/카메라/배경, 손/소품/접촉 불명확, Shot 경계 상태 불연속을 찾을 때 사용한다. H3 최종 프롬프트는 생성하지 않는다.
---

# Motion Validator

`drama-motion-scene-compiler`의 결과를 검증한다. 먼저 공통 `pipeline.md`와 compiler의 `references/motion-density-rules.md`, `references/motion-plan-schema.md`를 읽어라.

## 읽기

- `09_motion/epXX-motion.json`
- `01_script/ep*.md`
- `04_assets/state-ledger.json`, `relationships.json`
- `05_design/*`
- `06_cast/*`
- `07_visual_prompts/02_episode-keyframes.md` (v4) 또는 레거시 `04_episode-keyframes.md`, `07_prompt-audit.md`

## 쓰기

- `09_motion/validation-report.md`
- `09_motion/fix-log.md`

## 검사 항목

### 구조
- 모든 대상 Scene이 최소 1 Shot으로 커버되는가
- Shot ID가 유일한가
- target duration이 0보다 큰가
- start/end state가 있는가

### Motion Density
- Primary Story Motion이 명확한가
- Life Motion이 일반 Shot 기준 최소 2개 있는가
- gaze와 expression transition이 비어 있지 않은가
- 카메라가 static이면 의도적 이유가 있는가
- 환경이 반드시 움직여야 하는 장면에서 완전히 죽어 있지 않은가

### Complexity / Budget
- score 4 이상인데 split_recommended=false이면 이유가 있는가
- 짧은 Shot에 독립 Story Motion이 여러 개 들어가 있지 않은가
- Primary Motion이 사실상 2개 이상이지 않은가

### 물리·인체
- 두 인물 상호작용에 Reaction이 있는가
- 접촉이 있는데 Contact Topology가 비어 있지 않은가
- 손/발/몸/소품 접촉 관계가 가능한가
- 중요 손·얼굴·소품 Visibility Constraint가 있는가

### Continuity
- 이전 Shot end_state와 다음 Shot start_state가 충돌하지 않는가
- 소품 owner/hand/position이 순간이동하지 않는가
- 진행 방향, 자세, 손 위치, 젖음·파손 상태가 이유 없이 초기화되지 않는가

## 자동 검사

먼저:

```bash
python .agents/skills/drama-motion-validator/scripts/validate_motion_plan.py works/{slug}
```

를 실행한다. 기계 검사는 구조적 결함만 잡는다. 이후 의미 검수를 직접 수행한다.

## 판정

- `READY`: 중대 결함 0
- `CONDITIONAL`: 자동 생성은 가능하지만 고위험 Shot 수정 권고가 남음
- `BLOCKED`: 물리 상태/연속성/필수 필드 결함으로 다음 H3 단계 금지

H3 프롬프트 문장을 직접 수정하거나 만들지 않는다. 오류는 Motion Plan으로 되돌린다.

완료 후 `manifest.phases.motion_validation`을 갱신한다.


## 다음 공정

검증 PASS 후 `drama-motion-keyframe-prompt-compiler`로 넘겨 Start/End 정지 이미지 프롬프트를 만든다.
