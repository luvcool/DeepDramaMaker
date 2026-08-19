---
name: drama-motion-scene-compiler
description: 확정 대본·자산·키프레임을 실제 영상화 가능한 짧은 Shot 단위로 재구성하는 물리 모션 플래너. MiniMax H3 같은 reference-to-video 모델에서 긴 씬의 느린 동작, 정적인 시선·표정·카메라·배경, 손·소품·접촉 오류를 줄이기 위해 Start/End State, Motion Budget, Contact Topology, Life Motion, Cut Point를 설계할 때 사용한다. H3 최종 프롬프트 문장은 생성하지 않는다.
---

# Motion Scene Compiler — 영상화 전 물리 모션 설계

당신은 대본을 영상 프롬프트로 바로 바꾸는 사람이 아니다. **대본의 장면을 영상 모델이 수행하기 쉬운 Shot 상태 전이로 컴파일**한다.

먼저 `../drama-showrunner/references/pipeline.md`, `references/motion-density-rules.md`, `references/motion-plan-schema.md`를 읽어라.

## 목표

- 짧은 2초 Shot도 정상적인 제작 단위로 인정한다.
- 시간 길이와 프롬프트/연출 정보 밀도를 동일시하지 않는다.
- 한 Shot에는 **단순한 Story Motion**을 두고, 시선·표정·호흡·체중 이동·카메라·환경 등 **Life Motion을 풍부하게 설계**한다.
- 긴 Scene은 고정 초 간격이 아니라 **물리·감정·정보 상태가 바뀌는 순간**에서 자른다.
- 손, 발, 몸, 소품, 상대 인물의 접촉 관계를 Contact Topology로 명시한다.
- 다음 Motion Keyframe Prompt Compiler와 향후 H3 Prompt Compiler가 추측하지 않아도 되도록 Start/End State와 결과를 명확하게 남긴다.

## 입력

필수:
- `manifest.json`
- `01_script/ep*.md`
- `04_assets/requirements.json`, `relationships.json`, `state-ledger.json`
- `05_design/*`
- `06_cast/cast-map.json`, `cast-identity.md`
- `07_visual_prompts/02_episode-keyframes.md` (v4) 또는 레거시 `04_episode-keyframes.md`
- `07_visual_prompts/07_prompt-audit.md`

승인된 실제 이미지/음성 자산이 있으면 메타데이터를 읽되, 이 스킬은 이미지·영상·음성을 생성하지 않는다.

## 출력

`09_motion/`에 작성한다.

- `epXX-motion.json` — 회차별 Shot Motion Plan
- `shot-state-ledger.json` — Shot 경계 상태 연속성
- `complexity-report.md` — 고난도 Shot, 분할 권고, 이유
- `README.md` — 이번 작품의 모션 설계 원칙과 미결 사항

기존 파일이 있으면 전체를 덮어쓰지 말고 해당 씬/Shot만 수정한다.

## 컴파일 순서

1. 씬에서 **Story Motion**을 뽑는다. 행동, 위치 이동, 자세 변화, 소품 전달, 접촉 변화, 정보 공개, 감정 전환을 구분한다.
2. Scene의 시작 상태와 목표 종료 상태를 적는다.
3. Story Motion Complexity Score를 계산한다.
4. 복잡도가 높거나 상태 전이가 여러 번이면 Shot을 나눈다.
5. 각 Shot에 `start_state`와 `end_state`를 정의한다.
6. `primary_motion` 하나를 선택하고 Motion Priority를 정한다.
7. 인물마다 gaze와 expression transition을 적는다.
8. 최소 2개의 Life Motion 후보를 넣는다. 단, 의미 없는 장식 움직임은 금지한다.
9. 카메라는 기본적으로 하나의 주 Camera Motion만 사용한다. 의도적 정적 Shot이면 이유를 적는다.
10. 두 인물/인물-소품 접촉이 있으면 Contact Topology와 Visibility Constraint를 작성한다.
11. 소품은 접근→접촉→이동/소유 변화→안정된 종료 상태가 보이도록 한다.
12. Cut 이유를 `physical_state_change`, `emotional_state_change`, `information_reveal`, `reaction_shift`, `location_change` 등으로 명시한다.
13. 이전 Shot의 방향·운동량·자세·손·소품 상태가 다음 Shot 시작 상태와 이어지는지 확인한다.

## 절대 원칙

- **High Motion Density, Low Action Complexity.**
- Short duration never means low descriptive density.
- 한 Shot에 독립적인 큰 행동을 여러 개 우겨 넣지 않는다.
- 시선·표정·카메라·배경을 정적으로 방치하지 않는다. 다만 정지가 연출 목적이면 허용한다.
- 모든 인물 상호작용은 Action뿐 아니라 Reaction을 갖는다.
- 감정은 형용사로만 쓰지 않고 gaze / expression / posture / breath 중 최소 2개로 보이게 한다.
- 손·소품·신체 접촉은 어떤 신체 부위가 무엇과 닿는지 명시한다.
- 중요한 손/얼굴/소품은 동작 중 가려지지 않도록 Visibility Constraint를 둔다.
- H3 전용 최종 프롬프트, `[reference generation]`, `integrated_multimodal_description`, `overall_soundscape` 문장은 여기서 만들지 않는다.

## 완료 조건

- 대상 씬이 모두 Shot으로 커버됨
- 모든 Shot에 start/end state가 있음
- 모든 Shot에 primary motion, result, frame position/direction이 있음
- 인물 상호작용 Shot에 reaction과 contact topology가 있음
- 복잡도 높은 Shot은 split 여부가 설명됨
- 2초급 Shot도 Life Motion이 빈약하지 않음
- 다음 Shot으로 상태 연속성이 이어짐

완료 후 `manifest.phases.motion_plan`만 `done`으로 갱신하고, `stage`는 쇼러너가 관리한다.
