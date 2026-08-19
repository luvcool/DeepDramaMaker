# Migration v5 — Motion Keyframe Prompt Pipeline

## 목적

v4의 Approved Asset Library와 v3의 Motion Plan 사이를 연결해, 검증된 Shot 상태를 **H3 reference-to-video용 Start/End 정지 이미지 프롬프트**로 변환한다.

## 신규 스킬

`drama-motion-keyframe-prompt-compiler`

입력:
- 승인 자산 레지스트리
- 디자인/캐스팅
- Narrative Style/Asset Lock
- 검증된 `09_motion/epXX-motion.json`

출력:
- `09_motion/keyframes/00_motion-keyframe-rules.md`
- `09_motion/keyframes/epXX-motion-keyframes.md`
- `09_motion/keyframes/generation-queue.md`
- `09_motion/keyframes/handoff-guide.md`

## 핵심 변경

### 1. Motion Keyframe은 Narrative Keyframe과 분리

Narrative Keyframe은 장면 대표 이미지다.
Motion Keyframe은 Shot의 **물리 Start/End State 계약**이다.

### 2. State, not action

Motion Keyframe Prompt에는 중간 동작을 쓰지 않는다.

- `reaches` → `arm extended`
- `gives` → Start/End 소유 상태
- `turns` → `head facing ...`

### 3. Invariant Lock + Delta Allowed

기본 Invariant:
- Actor identity
- body proportions
- hair
- wardrobe
- location/vehicle/prop geometry
- camera/framing
- lighting
- background layout

기본 Delta:
- pose
- hands
- gaze
- expression
- contact
- prop ownership/state
- 작은 위치 변화

### 4. Minimal Visual Distance

Start/End의 차이는 목표 행동을 설명하는 데 필요한 최소한으로 유지한다. 카메라·조명·배경·정체성을 불필요하게 바꾸지 않는다.

### 5. Contact Topology를 이미지 상태로 반영

손/소품/신체 접촉은 Start와 End에서 각각 명시한다. 중간 접촉 상태는 H3가 생성할 Motion 영역으로 남긴다.

## 새 공정

```text
Narrative Keyframe / Approved Assets
             ↓
       Motion Plan
             ↓
      Motion Validation
             ↓
Motion Keyframe Prompt Compiler
             ↓
 External Start/End Image Generation
             ↓
      [future image QA]
             ↓
     Future H3 Prompt Compiler
```

## 범위 밖

v5에서도 다음은 아직 구현하지 않는다.

- MiniMax H3 최종 3-part prompt compiler
- `[reference generation]`
- `integrated_multimodal_description:`
- `overall_soundscape:`
- 실제 동영상 생성

## 레거시 작품

《없던 사이》는 기존 168개 Narrative Keyframe을 보존한다. `09_motion`이 아직 생성되지 않았으므로 Motion Keyframe Prompt를 소급 자동 생성하지 않는다. 실제 영상화할 씬부터 Motion Plan → Validation → Motion Keyframe Prompt 순으로 생성한다.
