---
name: drama-asset-image-validator
description: 외부에서 생성되거나 사용자가 제공한 자산 Reference Image가 지속적 제작 기준으로 안전한지 검수한다. Actor identity, anatomy, cross-view consistency, Location geometry, Vehicle architecture, Wardrobe/Prop 구조와 가시성을 판정하고 PASS/RETRY/REJECT 및 타깃 재생성 지시를 만든다. 이미지를 생성하거나 수정하지 않는다.
---

# Asset Image Validator

목표는 '예쁜가'가 아니라 **이 이미지가 지속적 제작의 기준 자산으로 안전한가**를 판단하는 것이다.

먼저 `../drama-showrunner/references/pipeline.md`와 `references/validation-rules.md`를 읽는다.

## 읽기
- `04_assets/requirements.json`
- `04_assets/image_prompts/` 전체
- `05_design/`, `06_cast/`
- 참조되는 global asset metadata
- 제작팀/사용자가 제공한 실제 Reference Image 및 그 파일 매핑 정보

## 쓰기
- `04_assets/approved/registry.json`
- `04_assets/approved/validation-report.md`
- `04_assets/approved/retry-queue.md`

이미지가 제공되지 않았다면 임의로 PASS하지 않고 `PENDING`으로 기록한다.

## 판정
개별 View: `PASS`, `RETRY`, `REJECT`, `PENDING`
Asset Pack: `APPROVED`, `INCOMPLETE`, `REJECTED`

## 공통 검사
- Identity / Geometry
- Cross-view Consistency
- Visibility / Occlusion
- Anatomy (해당 시)
- Camera distortion
- Scale
- Material / Color
- Required View correctness
- Locked attribute drift

## Critical Violations
### ACTOR
- 다른 사람으로 보이는 identity drift
- 심각한 얼굴/신체 변형
- 잠금된 나이·성별 인상·헤어의 큰 변화

### LOCATION
- 불가능한 geometry
- 주요 문/창/가구의 위치 모순
- reverse view가 같은 공간으로 성립하지 않음

### VEHICLE
- 차문/휠/조향 위치/외형 구조의 큰 변화
- 외관과 실내 architecture 불일치

### WARDROBE / PROP
- 핵심 형태·스케일·기능 구조가 달라짐

Critical Violation이 있으면 점수와 무관하게 PASS 불가.

## 점수(선택)
- Identity 0–25
- Geometry 0–20
- Consistency 0–20
- Visibility 0–15
- Anatomy 0–10
- Image Quality 0–10

90–100 PASS, 75–89 RETRY 권장, 0–74 REJECT를 기본으로 하되 Critical 규칙이 우선한다.

## Retry Instruction
FAIL만 적지 않는다. 잠금값을 유지한 채 무엇만 다시 생성해야 하는지 타깃 지시를 작성한다.
예: `ACTOR_001 FACE_LEFT45만 재생성. 승인된 정면 얼굴 identity를 유지하고 왼쪽 눈썹을 가리는 머리만 제거. 얼굴형/코/눈 모양 변경 금지.`

## Asset Pack 완료 조건
P0 Asset은 필수 View 전체 PASS 후에만 APPROVED다. 한 장이 PASS여도 전체 Pack은 INCOMPLETE일 수 있다.

## Versioning
승인된 자산은 `{ASSET_ID}@vN`으로 기록한다. 이미 사용 중인 작품은 명시적 승인 없이 새 버전으로 자동 교체하지 않는다.

완료 후 `phases.asset_image_validation`을 갱신한다. P0 자산이 모두 APPROVED면 기존 `drama-asset-validator`의 종합 readiness 검수로 넘긴다.
