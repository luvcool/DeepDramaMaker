---
name: drama-asset-requirement-extractor
description: 확정 대본을 영상 제작 자산 요구사항으로 구조화하는 드라마 자산 요구사항 추출기. 등장인물·배우/목소리 필요 여부·로케이션/존·의상·차량·극적 소품·배경 요소를 추출하고 중복 엔티티를 통합하며 공용/프로젝트/회차 상태 자산, 중요도, 지속성, 누락 속성, 관계, 제작 우선순위를 결정한다. 사용자가 "자산 추출", "대본에서 필요한 에셋", "Asset Requirement", "배우 얼굴/목소리 뭐가 필요해", "영상화 전에 자산 정리"라고 하거나 script 이후 디자인/캐스팅 전에 제작 자산을 정리해야 할 때 사용한다.
---

# Asset Requirement Extractor

대본을 읽고 **무엇을 만들어야 하는지**만 결정한다. 어떻게 생길지는 프로덕션 디자이너, 누가 연기할지는 캐스팅 디렉터의 책임이다.

먼저 `../drama-showrunner/references/pipeline.md`와 `references/asset-schema.md`를 읽는다.

## 읽기
- `manifest.json`
- `00_bible/` 전체
- `01_script/` 전체
- 있으면 `assets/global/` 레지스트리

## 쓰기
`04_assets/` 아래만 쓴다.
- `requirements.json` — 정규화된 자산 요구사항
- `relationships.json` — 인물-장소-차량-소품 소유/사용/거주 관계
- `construction-queue.md` — P0/P1/P2 제작 큐와 이유
- `state-ledger.json` — 회차·씬별 상태 변화
- `extraction-report.md` — 중복 통합, 미지정 속성, 충돌·질문

## 핵심 규칙
1. 대본에 없는 세부를 사실로 발명하지 않는다. 불명확하면 `UNSPECIFIED`와 `missing_attributes`를 사용한다.
2. `서하의 폰`, `폰`, `스마트폰`처럼 같은 실체는 하나의 ID로 통합한다.
3. 자산 scope는 세 가지다.
   - `global_shared`: 여러 작품에서 재사용 가능한 배우/목소리/범용 자산 후보
   - `project_dedicated`: 작품의 정체성과 연속성에 묶이는 집·전용 의상·상징 소품·주요 차량
   - `episode_state`: 파손·젖음·부상·헤어 변화처럼 특정 시점 이후 이어지는 상태
4. 배우와 배역을 분리한다. 배역에는 `actor_ref`와 `voice_ref` 슬롯을 만들고, 실제 매핑 전에는 `UNASSIGNED`로 둔다.
5. 주요 인물은 반드시 `visual_identity_required`, `voice_identity_required`, `performance_profile_required`를 판정한다.
6. 로케이션은 가능한 경우 부모 `LOC-*`와 내부 `ZONE-*` 계층으로 추출하고 이동 가능한 연결관계를 남긴다.
7. 배경 엑스트라·일회성 컵처럼 일관성 가치가 낮은 것은 `background` 등급으로 두고 독립 마스터 제작을 강제하지 않는다.
8. 제작 우선순위는 `P0`(없으면 주요 장면 제작 불가), `P1`(반복/연속성 중요), `P2`(장면 한정/배경)다.

## 분류
`character`, `actor_identity`, `voice_identity`, `location`, `zone`, `wardrobe`, `vehicle`, `prop`, `environment`, `background_entity`를 기본 타입으로 쓴다.

## 완료 게이트
- 이름 있는 주요 인물이 모두 requirements에 존재
- 주요 인물마다 visual/voice identity 필요 여부 판정
- 대본 씬 헤딩의 장소가 모두 LOC/ZONE에 매핑
- 극적 소품의 상태 변화가 state-ledger에 기록
- 동일 실체 중복 ID 없음
- `missing_attributes`가 대본 사실과 생성 추측을 명확히 구분

완료 후 `phases.asset_requirements`와 `updated_at`만 병합한다. 다음은 `drama-casting-director`와 `drama-production-designer`이며, 둘은 requirements를 읽고 병렬 진행할 수 있다.
