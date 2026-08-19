---
name: drama-asset-image-prompt-compiler
description: 확정된 자산 요구사항·프로덕션 디자인·캐스팅 정보를 재사용 가능한 기준 이미지 생성 프롬프트로 변환한다. 배우/의상/로케이션/차량/소품별 Reference Pack, 잠금 속성, 허용 변형, 필수 View, 카메라·조명·가시성·스케일·네거티브 규칙을 작성한다. 자산 이미지는 생성하지 않는다.
---

# Asset Image Prompt Compiler

목표는 '멋진 한 장'이 아니라 이후 수십 개 장면에서 반복 참조할 수 있는 **기준 자산 이미지 패키지**를 만드는 것이다.

먼저 `../drama-showrunner/references/pipeline.md`와 `references/asset-image-rules.md`를 읽는다.

## 읽기
- `manifest.json`
- `04_assets/requirements.json`, `relationships.json`, `state-ledger.json`
- `05_design/` 전체
- `06_cast/cast-identity.md`, `06_cast/cast-map.json`
- 참조되는 `assets/global/actors/`, `assets/global/voices/`, `assets/global/shared/`

## 쓰기
`04_assets/image_prompts/` 아래만 쓴다.
- `00_asset-image-style.md`
- `01_actor-prompts.md`
- `02_wardrobe-prompts.md`
- `03_location-prompts.md`
- `04_vehicle-prompts.md`
- `05_prop-prompts.md`
- `06_generation-queue.md`
- `07_handoff-guide.md`

## 핵심 철학

> Asset Image = Reference Data, not Hero Shot.

- 높은 구조 정보 밀도(High Structural Density), 낮은 서사 밀도(Low Narrative Density)를 사용한다.
- 극단적 앵글, 과도한 심도, 모션 블러, 얼굴/손/구조 가림을 피한다.
- 모든 자산은 `locked_attributes`와 `variable_attributes`를 명시한다.
- 대본/명세에 없는 값을 사실로 고정하지 않는다. `UNSPECIFIED`를 유지한다.
- 승인된 사용자 얼굴 참조가 있으면 새 얼굴을 발명하지 않는다.

## 자산별 최소 Reference Pack

### ACTOR
P0 배우 권장:
- FACE_FRONT
- FACE_LEFT45
- FACE_RIGHT45
- FACE_LEFT_PROFILE
- FACE_RIGHT_PROFILE
- UPPERBODY_FRONT
- FULLBODY_FRONT
- FULLBODY_SIDE
- FULLBODY_BACK

Master는 중립 표정, 중립 자세, 단순 의상, 자연 시점, 최소 왜곡을 우선한다.
Performance Reference는 Master 승인 이후 별도 파생 자산으로 만든다.

### WARDROBE
- FRONT
- LEFT45
- RIGHT45
- SIDE
- BACK
- DETAIL

형태·재질·색·길이·핏·버튼·포켓·패턴·액세서리를 잠근다.

### LOCATION
- MASTER_FRONT
- REVERSE_VIEW
- LEFT_CORNER
- RIGHT_CORNER
- ENTRANCE_TO_ROOM
- ROOM_TO_ENTRANCE
- IMPORTANT_ZONE_VIEW

문/창/가구/존 연결과 실제 이동 경로가 서로 모순되지 않아야 한다.

### VEHICLE
- EXTERIOR_FRONT
- EXTERIOR_FRONT45
- EXTERIOR_SIDE
- EXTERIOR_REAR45
- EXTERIOR_REAR
- INTERIOR_DRIVER
- INTERIOR_PASSENGER
- INTERIOR_REAR
- DASHBOARD

차문 수, 휠, 조향 위치, 좌석 구조, 창문 형상을 잠근다.

### PROP
중요도와 상호작용에 따라 FRONT/BACK/SIDE/GRIP/STATE 뷰를 만든다.
손으로 다루는 소품은 사람 손 대비 스케일과 권장 Grip 영역을 명시한다.

## 프롬프트 블록
각 실제 생성 프롬프트는 다음 정보를 순서대로 포함한다.
1. Asset Identity
2. Locked Physical Attributes
3. Required View
4. Pose / State
5. Camera
6. Lighting
7. Visibility
8. Scale / Geometry
9. Background
10. Consistency Constraints
11. Negative Constraints

`PROMPT_KO`와 `PROMPT_EN`을 모두 제공한다. 특정 생성 모델이 지정되지 않았다면 모델 고유 문법·파라미터를 추측하지 않는다.

## 완료 게이트
- P0 자산에 필수 View 프롬프트가 모두 존재
- 모든 Prompt에 Locked/Variable 속성이 연결
- 사용자 제공 Actor 참조를 다른 얼굴로 재해석하지 않음
- Location 다중 View가 동일 Geometry를 설명
- Vehicle 외부/내부가 동일 구조를 설명
- 손 사용 Prop에 Scale/Grip 정보가 있음
- `06_generation-queue.md`에 생성 순서와 의존성 있음

완료 후 `phases.asset_image_prompts`를 `done`으로 갱신한다. 실제 이미지 생성은 이 스킬 범위 밖이며, 생성된 결과는 `drama-asset-image-validator`가 검수한다.
