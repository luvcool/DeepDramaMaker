# AI 드라마 스튜디오 (drama-studio-service)

19개의 전문 작업 모드가 순서대로 이어서 **드라마 한 편을 전부 텍스트로** 만들어내는 서비스.
영상·이미지를 생성하지 않는다. 결과물은 대본과 제작 문서다.

## 구성

서버가 없는 **Codex 스킬 기반 서비스**다. 각 전문 모드는 Codex 저장소 스킬 하나로 구현되어 있고,
이 폴더에서 작업할 때 요청과 일치하는 스킬을 Codex가 불러온다.
각 스킬은 독립된 인간·에이전트가 아니라 같은 Codex 작업에 로드되는 전문 워크플로우다.

```
drama-studio-service/
├── README.md
├── AGENTS.md               ← Codex 프로젝트 공통 규칙
├── .agents/skills/           ← 전문 워크플로우 19개
│   ├── drama-showrunner/         (총괄 · 파이프라인 지휘)
│   │   └── references/pipeline.md   ← 공통 규약 (작업공간·manifest·인수인계)
│   ├── drama-story-architect/    (세계관 · 회차 구조)
│   ├── drama-character-bible/    (인물 심리 설계)
│   ├── drama-screenwriter/       (시나리오 집필 ★가장 큰 산출물)
│   ├── drama-continuity-auditor/ (검증 · 교정)
│   ├── drama-dialogue-director/  (대사 · 화술)
│   ├── drama-hook-psychologist/  (심리 테크니션 · 호기심 설계)
│   ├── drama-asset-requirement-extractor/ (대본→자산 요구사항)
│   ├── drama-production-designer/(배경 · 의상 · 차량 · 소품)
│   ├── drama-casting-director/   (공용 배우·목소리 매핑 + 배역 아이덴티티)
│   ├── drama-asset-image-prompt-compiler/ (자산 기준 이미지 프롬프트)
│   ├── drama-asset-image-validator/ (실제 Reference Image 승인 검수)
│   ├── drama-asset-validator/    (종합 자산 준비도·연속성 검수)
│   ├── drama-visual-prompt-designer/ (이미지 프롬프트 패키지)
│   ├── drama-visual-prompt-auditor/  (프롬프트 연속성 검수)
│   ├── drama-motion-scene-compiler/ (씬→물리적으로 단순한 Shot Motion Plan)
│   ├── drama-motion-validator/      (Motion Density·접촉·상태·Cut 검수)
│   ├── drama-motion-keyframe-prompt-compiler/ (검증된 Motion Plan→Start/End 이미지 프롬프트)
│   └── drama-script-finalizer/   (통합 · 납품, 씬·대사·로케이션 기계 분석)
└── works/                   ← 작품별 폴더 (작품 하나 = 폴더 하나)
    └── {작품-slug}/
```

## 공정 순서

```
concept → structure → characters → script → audit → dialogue → hooks → asset-requirements → design+cast
→ asset-image-prompts → [외부 이미지 생성] → asset-image-validation → asset-validation → visual-prompts → prompt-audit → final
                                                                                                  ↘ motion-plan → motion-validation → motion-keyframe-prompts → [외부 Start/End 이미지 생성] → (향후 H3 Compiler)
   쇼러너   아키텍트    바이블      작가    검증관   대사디렉터  심리   디자이너  캐스팅  파이널라이저
                                     ↑                          │
                                     └──── 결함 반영 재집필 ─────┘
```

- **script가 가장 크다.** 앞 세 공정은 대본을 쓰기 위한 최소 준비이므로 짧게 끝낸다.
- audit / dialogue / hooks는 대본이 있어야 의미가 있다.
- asset-requirements 완료 후 design / cast를 병렬로 돌릴 수 있다. 그 결과로 기준 자산 이미지 프롬프트를 만들고, 외부 생성 결과를 승인한 뒤 종합 asset-validation을 통과해야 최종 Narrative visual-prompts로 간다.

## 쓰는 법

```text
드라마 만들자
```

로 시작하면 쇼러너가 열리고, 컨셉 6항목을 잡은 뒤 다음 공정을 제안한다.
공정별로 직접 부를 수도 있다 — "3화 대본 써줘", "일관성 검수해줘", "훅 좀 만들어줘", "의상 설계해줘".

Codex에서 스킬을 명시적으로 고르려면 `$`로 멘션한다.

```text
$drama-showrunner 새 8부작 미스터리 기획을 시작해줘
$drama-screenwriter midnight-ferry 3화 대본을 써줘
$drama-continuity-auditor midnight-ferry 전체 대본을 검수해줘
```

스킬을 새로 추가했는데 목록에 보이지 않으면 Codex를 새로 시작하거나 새 작업을 연다.

작품 상태는 프로젝트 루트의 `works/{slug}/manifest.json` 하나로 관리된다. 개별 스킬을 직접 호출해도
해당 공정 phase와 새로 확정된 사실이 manifest에 병합된다. 특히 `canon.items` 배열이
확정 사실 저장소라, 여기가 채워질수록 뒤 공정이 앞 공정과 어긋나는 사고가 줄어든다.

## 산출물

| 폴더 | 내용 |
|---|---|
| `00_bible/` | 기획의도 · 세계관 · 구조 · 인물 |
| `01_script/` | 회차 대본 |
| `02_audit/` | 컨티뉴이티 리포트 · 수정 이력 |
| `03_hooks/` | 훅 지도 · 이탈 구간 진단 |
| `04_assets/` | 자산 요구사항 · 관계 · 상태 · 기준 이미지 프롬프트 · 승인 레지스트리 · 제작 큐/검수 |
| `05_design/` | 로케이션 · 의상 · 차량 · 소품 명세 |
| `06_cast/` | 공용 Actor/Voice 매핑 · 배역 아이덴티티 |
| `07_visual_prompts/` | 제작팀용 이미지 프롬프트 패키지 |
| `08_final/` | 납품용 통합본 |
| `09_motion/` | 영상화 전 Shot Motion Plan · 상태 연속성 · 복잡도/검수 · Motion Start/End 이미지 프롬프트 |

## 상태

스킬 19종 작성 완료. 샘플 작품 《없던 사이》를 새 자산 계층으로 마이그레이션했으며, 기존 대본·프롬프트 검증기는 정상 통과한다. Actor/Voice 실제 승인 자산은 아직 미매핑이다.


## 자산 계층

- `assets/global/`: 작품과 독립적인 배우 얼굴/체형, 목소리, 범용 공유 자산
- `works/{slug}/04_assets/`: 해당 작품이 요구하는 캐릭터·로케이션·차량·의상·소품과 관계/상태
- 회차 중 파손·젖음·부상·헤어 변화는 `state-ledger.json`에서 시점별 상태로 관리

> v4는 자산 기준 이미지 프롬프트/승인 단계를 장면 이미지 프롬프트와 분리한다. Approved Asset Library가 이후 Narrative Keyframe과 영상화 준비의 기준이 된다.
>
> v3에서 추가한 영상화 전 물리 모션 설계는 그대로 유지한다. 2초 Shot도 정상 단위로 인정하며 Start/End State, Motion Budget, Contact Topology, Life Motion, Cut Timing을 구조화한다. Motion Plan 검수 후 `09_motion/keyframes/`에서 Start/End Frame 이미지 프롬프트를 만든다. MiniMax H3 최종 Prompt Compiler와 실제 동영상 프롬프트 생성은 여전히 별도 후속 공정이다.
