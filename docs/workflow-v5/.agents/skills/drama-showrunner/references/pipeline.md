# 드라마 제작 파이프라인 공통 규약

모든 `drama-*` 스킬이 공유하는 작업 공간·산출물·인수인계 규칙이다.
페르소나가 서로 다른 세션에서 일해도 이 규약만 지키면 결과가 이어붙는다.

---

## 1. 작업 공간 찾기와 구조

절대 경로를 사용하지 마라. 먼저 현재 경로에서 위로 올라가며
`.agents/skills/drama-showrunner/` 폴더를 가진 가장 가까운 폴더를 **프로젝트 루트**로 정한다.
작품은 항상 `<프로젝트 루트>/works/{작품-slug}/`에 저장한다.
프로젝트 루트를 찾지 못하면 파일을 쓰지 말고 사용자에게 작업 경로를 확인한다.

작품 하나는 폴더 하나다. 슬러그는 영문 kebab-case로 짓는다 (예: `midnight-ferry`).

```
<프로젝트 루트>/
├── assets/global/                ← 작품 독립 공용 자산
│   ├── actors/ACTOR-*/           ← 얼굴·체형·기본 헤어·참조 이미지 메타데이터
│   ├── voices/VOICE-*/           ← 음색·참조 음성·TTS/클론 메타데이터
│   └── shared/                   ← 범용 재사용 자산
└── works/{작품-slug}/
    ├── manifest.json
    ├── 00_bible/
    ├── 01_script/
    ├── 02_audit/
    ├── 03_hooks/
    ├── 04_assets/
    │   ├── requirements.json
    │   ├── relationships.json
    │   ├── state-ledger.json
    │   ├── construction-queue.md
    │   ├── extraction-report.md
    │   ├── validation-report.md
    │   ├── image_prompts/
    │   │   ├── 00_asset-image-style.md
    │   │   ├── 01_actor-prompts.md
    │   │   ├── 02_wardrobe-prompts.md
    │   │   ├── 03_location-prompts.md
    │   │   ├── 04_vehicle-prompts.md
    │   │   ├── 05_prop-prompts.md
    │   │   ├── 06_generation-queue.md
    │   │   └── 07_handoff-guide.md
    │   └── approved/
    │       ├── registry.json
    │       ├── validation-report.md
    │       └── retry-queue.md
    ├── 05_design/
    │   ├── locations.md
    │   ├── costumes.md
    │   ├── vehicles.md
    │   └── props.md
    ├── 06_cast/
    │   ├── cast-identity.md
    │   └── cast-map.json
    ├── 07_visual_prompts/
    │   ├── 00_style-bible.md
    │   ├── 01_asset-locks.md
    │   ├── 02_episode-keyframes.md
    │   ├── 03_negative-prompts.md
    │   ├── 04_handoff-guide.md
    │   ├── 07_prompt-audit.md
    │   └── 08_prompt-fix-log.md
    ├── 08_final/
    │   └── {작품-slug}_최종대본_v{n}.md
    └── 09_motion/
        ├── epXX-motion.json
        ├── shot-state-ledger.json
        ├── complexity-report.md
        ├── validation-report.md
        ├── fix-log.md
        └── keyframes/
            ├── 00_motion-keyframe-rules.md
            ├── epXX-motion-keyframes.md
            ├── generation-queue.md
            └── handoff-guide.md
```

작품 폴더가 없으면 만들고, 있으면 기존 파일을 먼저 읽은 뒤 이어서 작업한다.
쇼러너가 아닌 개별 스킬이 호출됐는데 작품 폴더나 `manifest.json`이 없으면 임의로 상태 파일을 만들지 말고 `drama-showrunner`로 초기화를 넘긴다.
단, 사용자가 특정 파일만 대상으로 일회성 검수·수정을 명시했다면 작품 폴더를 만들지 않고 그 파일만 처리하며, manifest 상태가 추적되지 않음을 보고한다.

### 기존 파일 수정 규칙

- **맹목적 전체 교체 금지**: 기존 내용을 읽지 않은 채 같은 파일을 새로 쓰지 마라.
- **작업본은 제자리 수정**: 사용자가 수정을 요청했거나 승인한 경우 `concept.md`, `structure.md`, `characters.md`, `ep*.md`는 필요한 부분만 수정한다.
- **변경 추적**: 대본 교정은 `02_audit/fix-log.md`, 프롬프트 교정은 `07_visual_prompts/08_prompt-fix-log.md`에 기록하고, 납품본은 `08_final/`에서 `v1`, `v2`처럼 새 버전을 만든다.
- **기존 납품본 보존**: `08_final/`의 이전 버전은 삭제하거나 덮어쓰지 않는다. 레거시 작품에 `06_final/` 또는 `07_final/`이 있으면 내용 손실 없이 `08_final/`로 이동한 뒤 새 공정을 추가한다.

---

## 2. manifest.json

작품의 단일 진실 원천(single source of truth). 페르소나는 작업 시작 시 읽고, 끝나면 갱신한다.

```json
{
  "slug": "midnight-ferry",
  "title": "자정의 연락선",
  "format": "미니시리즈",
  "episodes": 8,
  "runtime_min": 60,
  "genre": ["미스터리", "가족"],
  "tone": "차갑고 습한 항구 도시, 절제된 감정",
  "stage": "script",
  "phases": {
    "concept": "done",
    "structure": "done",
    "characters": "done",
    "script": "in_progress",
    "audit": "todo",
    "dialogue": "todo",
    "hooks": "todo",
    "asset_requirements": "todo",
    "design": "todo",
    "cast": "todo",
    "asset_image_prompts": "todo",
    "asset_image_validation": "todo",
    "asset_validation": "todo",
    "visual_prompts": "todo",
    "prompt_audit": "todo",
    "final": "todo",
    "motion_plan": "todo",
    "motion_validation": "todo",
    "motion_keyframe_prompts": "todo"
  },
  "canon": {
    "note": "확정된 설정. 아래 항목과 충돌하는 서술은 결함으로 간주한다.",
    "items": [
      "주인공 서지운은 1993년생, 항해사 면허 2급",
      "연락선은 하루 4회 운항, 마지막 배는 23:40"
    ]
  },
  "open_questions": ["3화 이후 형사 시점을 유지할지 미정"],
  "updated_at": "2026-08-05T00:00:00+09:00"
}
```

`canon`은 특히 중요하다. 확정 사실이 여기 쌓이면 뒤 공정이 앞 공정과 어긋나는 사고를 막을 수 있다.

### manifest 갱신 권한

개별 스킬을 직접 호출해도 상태가 누락되지 않게 다음처럼 나눈다.

- 모든 스킬은 작업 시작 전 `manifest.json`을 읽는다.
- 각 스킬은 자기 `phases.{phase}`, 자기 작업에서 새로 확정된 `canon.items`, `open_questions`, `updated_at`만 갱신할 수 있다.
- phase 값은 `todo`, `in_progress`, `done` 중 하나만 쓴다. 산출물은 완성됐지만 후속 수정이 필요하면 phase는 `done`으로 두고 미해결 사항을 `open_questions`에 남긴다.
- `stage`와 다른 공정의 phase는 쇼러너만 갱신한다. 단, 파이널라이저는 납품 완료 시 `stage: released`를 설정할 수 있다.
- 쓰기 직전 manifest를 다시 읽고 기존 값에 병합한다. `canon.items`와 `open_questions`는 기존 순서를 유지하며 동일한 문자열을 중복 추가하지 않는다. JSON 객체 전체를 예전 스냅샷으로 교체하지 마라.
- `updated_at`은 현재 타임존 오프셋을 포함한 ISO 8601 형식(예: `2026-08-05T14:30:00+09:00`)으로 쓴다.
- design과 cast를 병렬로 만들어도 manifest 갱신은 한 번에 하나씩 병합한다.

---

## 3. 인수인계 계약

각 페르소나는 **읽을 것**과 **쓸 것**이 정해져 있다. 자기 담당이 아닌 파일은 고치지 않는다.
남의 파일에 문제가 있으면 직접 고치지 말고 `02_audit/continuity-report.md`에 결함으로 올린다.
단, 비주얼 프롬프트의 문제는 `07_visual_prompts/07_prompt-audit.md`에 올린다.
소유권이 흐려지면 두 페르소나가 같은 파일을 서로 다른 방향으로 되돌리는 일이 생긴다.

| 페르소나 | 읽기 | 쓰기 |
|---|---|---|
| drama-showrunner | 전체 | `manifest.json` 전체, `00_bible/concept.md` |
| drama-story-architect | concept | `00_bible/world.md`, `structure.md` |
| drama-character-bible | concept, structure | `00_bible/characters.md` |
| drama-screenwriter | bible 전체 | `01_script/ep*.md` |
| drama-continuity-auditor | 전체 | `02_audit/*` |
| drama-dialogue-director | characters, script | `01_script/ep*.md` (대사 라인만) |
| drama-hook-psychologist | structure, script | `03_hooks/hook-map.md` |
| drama-asset-requirement-extractor | bible, script, global asset metadata | `04_assets/requirements.json`, `relationships.json`, `state-ledger.json`, `construction-queue.md`, `extraction-report.md` |
| drama-production-designer | bible, script, asset requirements | `05_design/*` |
| drama-casting-director | characters, script, asset requirements, global actors/voices | `06_cast/cast-identity.md`, `cast-map.json` |
| drama-asset-image-prompt-compiler | asset requirements, design, cast, global asset metadata | `04_assets/image_prompts/*` |
| drama-asset-image-validator | asset image prompts, actual reference images, design/cast/global metadata | `04_assets/approved/*` |
| drama-asset-validator | assets, design, cast, approved asset registry, global asset metadata | `04_assets/validation-report.md` |
| drama-visual-prompt-designer | bible, script, hooks, design, cast | `07_visual_prompts/00_*`–`06_handoff-guide.md` |
| drama-visual-prompt-auditor | 전체, visual prompts | `07_visual_prompts/07_prompt-audit.md`, `08_prompt-fix-log.md` |
| drama-script-finalizer | 전체 | `08_final/*` |
| drama-motion-scene-compiler | script, assets, design, cast, audited keyframes | `09_motion/epXX-motion.json`, `shot-state-ledger.json`, `complexity-report.md`, `README.md` |
| drama-motion-validator | 전체, motion plan | `09_motion/validation-report.md`, `fix-log.md` |
| drama-motion-keyframe-prompt-compiler | validated motion plan, approved assets, style/asset locks | `09_motion/keyframes/*` |

위 표의 쓰기 범위와 별개로, 모든 스킬은 바로 위 `manifest 갱신 권한`에서 허용한 필드만 제한적으로 수정할 수 있다.

---

## 4. 공정 순서

```
concept → structure → characters → script → audit → dialogue → hooks → asset-requirements → design + cast
                                     ↑                            │
                                     └────── 결함 반영 재집필 ─────┘
design + cast → asset-image-prompts → [외부 이미지 생성] → asset-image-validation → asset-validation → visual-prompts → prompt-audit → final
              ↑              │                         │
              └── 프롬프트 교정 ─┘                    └→ motion-plan → motion-validation → motion-keyframe-prompts → [외부 Start/End 이미지 생성] → (향후 H3 Prompt Compiler)
```

- **script가 가장 크다.** 앞 세 공정(concept/structure/characters)은 대본을 쓰기 위한 최소 준비이므로 짧고 빠르게 끝낸다.
- **회당 분량은 완료 게이트다.** `manifest.runtime_min`을 기준으로 러닝타임 검사기가 전 회차 `PLAUSIBLE`을 내기 전에는 script를 `done`으로, 최종본을 `released`로 바꾸지 않는다. 회차 헤더·씬 수·훅 큐시트의 목표 시간은 검증 자료가 아니다.
- audit → dialogue → hooks는 대본이 존재해야 의미가 있다. 대본 없이 호출되면 먼저 대본부터 쓰자고 제안한다.
- asset-requirements는 대본 확정 후 필요한 공용/전용/상태 자산을 정규화한다.
- design/cast는 asset-requirements 완료 후 병렬로 진행할 수 있다.
- asset-image-prompts는 design/cast 결과를 재사용 가능한 Actor/Wardrobe/Location/Vehicle/Prop 기준 이미지 생성 프롬프트로 컴파일한다.
- 실제 이미지 생성은 이 저장소 바깥 제작 단계다. 생성 결과는 승인 전까지 `PENDING`이다.
- asset-image-validation은 실제 Reference Image의 identity/geometry/cross-view consistency를 검수해 `04_assets/approved/registry.json`에 버전별 승인 상태를 기록한다.
- asset-validation은 승인 레지스트리, Actor/Voice 매핑, 프로젝트 자산 상태를 종합해 제작 준비도를 판단한다.
- visual-prompts는 design, cast, asset-validation이 모두 끝난 뒤 **승인된 자산을 참조하는 Narrative Keyframe 중심**의 제작용 프롬프트를 만든다. 승인 자산이 있는데 얼굴·공간 구조를 다시 발명하지 않는다.
- prompt-audit는 이미지를 만들지 않고 프롬프트의 캐논·시각 연속성·씬 커버리지만 검증한다.
- 제작팀 전달용 `released` 상태는 미해결 치명·중대 프롬프트 결함이 없을 때만 허용한다.
- motion-plan은 기존 대본/이미지 프롬프트 납품과 분리된 **영상화 준비 브랜치**다. released 작품도 영상 제작을 시작할 때 motion-plan을 새로 진행할 수 있다.
- motion-plan은 고정 컷 간격보다 상태 변화, Motion Budget, Contact Topology를 기준으로 Shot을 나눈다. 2초 Shot도 정상 단위이며 짧다는 이유로 gaze/expression/camera/environment 정보를 줄이지 않는다.
- motion-validation 통과 전에는 Motion Keyframe Prompt Compiler로 넘기지 않는다.
- motion-keyframe-prompts는 검증된 Start/End State를 승인 자산 Reference와 결합해 **정지 이미지 상태 쌍**으로 컴파일한다. Start/End에서 identity, wardrobe, location geometry, camera, lighting을 기본 잠금하고 pose/hand/gaze/expression/prop state 등 필요한 Delta만 변경한다.
- 실제 Start/End 이미지 생성은 저장소 바깥 제작 단계다. H3 최종 프롬프트 포맷은 이 버전에서 정의하지 않는다.

---

## 5. 대본 표기 규약

모든 대본은 마크다운 텍스트로 쓴다. 아래 형식을 고정한다 — 검증관과 파이널라이저가 이 형식을 파싱한다.

```
## S#12. 항구 창고 / 내부 / 밤

지운이 젖은 외투를 벗어 못에 건다. 형광등이 두 번 깜빡인다.

**지운**
(낮게)
배는 이미 떠났어요.

**형사 박**
그럼 넌 왜 여기 있냐.

    [지운, 대답하지 않는다. 창밖으로 불빛 하나가 멀어진다.]
```

- 씬 헤딩: `## S#{번호}. {장소} / {내부·외부} / {시간}`
- 인물명: `**이름**` 굵게, 다음 줄부터 대사
- 지문(연기 지시): 대사 바로 위 `(괄호)`
- 액션/상황: 일반 문단
- 편집·연출 노트: `    [대괄호 들여쓰기]`

씬 번호는 회차 안에서 1부터 연속으로 매기고, 중간 삽입 시 재번호를 매긴 뒤 `02_audit/fix-log.md`에 기록한다.

---

## 6. 텍스트 산출물 원칙

이 서비스의 저장소 산출물은 전부 텍스트다. 이미지·영상 생성은 하지 않지만, 제작팀이 생성에 사용할 **자산 기준 이미지 프롬프트**, **Narrative Keyframe 프롬프트**, **Motion Start/End Keyframe 프롬프트**까지 텍스트로 작성한다. 외부에서 생성된 실제 이미지가 제공되면 자산 승인 검수 결과와 파일 매핑 메타데이터를 기록할 수 있다.
따라서 시각 정보(배경, 의상, 배우 외형)도 **읽어서 머릿속에 그려지는 산문**으로 쓴다.
"파란 셔츠"가 아니라 "세 번 빨아 목깃이 늘어난, 형광등 아래서 회색으로 보이는 파란 셔츠"처럼
질감·상태·조명 아래에서의 변화를 함께 적어야 텍스트가 자원 명세로 기능한다.

프롬프트는 실제 이미지를 대신하지 않는다. 생성기·모델·시드·참조 이미지가 확정되지 않은 값은 추측하지 말고 제작팀 확정 슬롯으로 남긴다.
