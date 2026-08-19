---
name: drama-motion-keyframe-prompt-compiler
description: 검증된 Shot Motion Plan을 H3 reference-to-video용 Start/End 정지 이미지 프롬프트 쌍으로 컴파일하는 스킬. 승인된 Actor/Wardrobe/Location/Vehicle/Prop Reference를 잠그고, Start/End 사이에서 변하면 안 되는 Invariant와 변해야 하는 Delta를 분리하며 손·시선·표정·접촉·소품 상태를 정확한 정지 상태로 작성한다. H3 동영상 프롬프트 자체는 생성하지 않는다.
---

# Motion Keyframe Prompt Compiler — Start / End Frame 프롬프트

당신은 영상 프롬프트 작가가 아니다. **검증된 Motion Plan의 시작 상태와 종료 상태를 각각 재현 가능한 정지 이미지 프롬프트로 컴파일**한다.

먼저 다음을 읽어라.

- `../drama-showrunner/references/pipeline.md`
- `references/motion-keyframe-rules.md`
- `references/motion-keyframe-schema.md`

## 목적

- Motion Plan의 `start_state`와 `end_state`를 시각적으로 정확한 두 장의 기준 이미지로 만든다.
- Start/End 사이에서 바뀌면 안 되는 값을 `INVARIANT LOCK`으로 고정한다.
- 실제로 바뀌어야 하는 값만 `DELTA`로 제한한다.
- 손, 시선, 표정, 자세, 소품 소유권, 접촉 관계를 정지 상태로 명확하게 보이게 한다.
- H3가 두 이미지 사이의 동작을 추론할 수 있도록 **중간 동작을 이미지 프롬프트에 서술하지 않는다.**

## 입력

필수:

- `manifest.json`
- `04_assets/approved/registry.json`
- `05_design/*`
- `06_cast/cast-map.json`, `cast-identity.md`
- `07_visual_prompts/00_style-bible.md`, `01_asset-locks.md`
- `09_motion/epXX-motion.json`
- `09_motion/validation-report.md`

조건:

- 대상 Motion Plan이 `drama-motion-validator` 검수를 통과해야 한다.
- 필요한 P0/P1 자산이 실제 `APPROVED@vN` Reference로 매핑되어야 한다. 미승인 자산이 있으면 최종 프롬프트를 APPROVED로 만들지 않고 DRAFT/BLOCKED로 표시한다.

## 출력

`09_motion/keyframes/`에 작성한다.

- `00_motion-keyframe-rules.md` — 작품별 적용 규칙/예외
- `epXX-motion-keyframes.md` — Shot별 START/END 프롬프트 쌍
- `generation-queue.md` — 생성 순서, 참조 이미지, 상태
- `handoff-guide.md` — 외부 이미지 생성 및 다음 단계 인수인계

실제 이미지를 생성하지 않는다.

## 핵심 구조

각 Shot마다 다음을 작성한다.

1. `SHOT_ID`
2. `DURATION`
3. `SOURCE_MOTION_PLAN`
4. `APPROVED_REFERENCES`
5. `INVARIANT_LOCK`
6. `DELTA_ALLOWED`
7. `START_STATE`
8. `START_PROMPT_KO`
9. `START_PROMPT_EN`
10. `END_STATE`
11. `END_PROMPT_KO`
12. `END_PROMPT_EN`
13. `NEGATIVE / DO-NOT-CHANGE`
14. `QA_CHECKS`

## 컴파일 순서

1. Motion Plan의 `start_state`, `end_state`, `contact_topology`, `visibility_constraints`, `gaze`, `expression_transition`, `primary_motion`, `result`를 읽는다.
2. 승인 자산 레지스트리에서 정확한 Actor/Wardrobe/Location/Vehicle/Prop 버전과 Reference View를 선택한다.
3. Start와 End에 공통인 값을 `INVARIANT_LOCK`으로 만든다.
4. 실제 상태 전이에 필요한 항목만 `DELTA_ALLOWED`에 넣는다.
5. Start Prompt는 **동작 직전의 안정된 정지 상태**를 쓴다.
6. End Prompt는 **동작 완료 후의 안정된 정지 상태**를 쓴다.
7. 동작 과정은 쓰지 않는다. `reaches`, `turns`, `walks`, `gives`처럼 시간 진행을 암시하는 동사보다 `arm extended`, `head facing`, `flower held by B` 같은 상태 문장을 우선한다.
8. Start/End에서 카메라 위치·렌즈·프레이밍·조명·배경 geometry는 기본적으로 동일하게 잠근다.
9. Contact Topology가 바뀌면 시작과 끝의 접촉 관계를 각각 명확히 쓴다.
10. 중요한 손, 얼굴, 소품은 둘 다 가려지지 않도록 한다.
11. Start/End의 차이는 **필요한 물리 상태 변화만** 남기고 최소화한다.
12. 이미지 생성기가 읽을 수 있는 자연어 프롬프트로 만들되, 프롬프트가 자산을 새로 발명하지 않도록 승인 Reference ID를 명시한다.

## Invariant Lock 기본값

특별한 서사적 이유가 없으면 다음은 Start/End 사이에서 동일해야 한다.

- Actor identity / face / body proportions
- 기본 hair geometry
- Wardrobe 구조·색·재질
- Location geometry / door / window / major furniture
- Vehicle 구조
- Prop 자체의 shape / scale / material
- Camera position / height / focal-length class / framing
- Lighting direction / time-of-day / major exposure
- Background object placement
- Image aspect ratio

## Delta Allowed 예

- pose
- hand position
- gaze target
- expression
- body weight distribution
- prop ownership
- door state
- small subject position shift
- plot-mandated hair/wardrobe/physical state change

변화가 없는 항목을 DELTA에 넣지 않는다.

## 정지 상태 문법

BAD:

`S1 reaches toward the flower and gives it to B.`

GOOD START:

`S1 stands frame-left, torso angled toward B, right elbow bent, holding the flower by the lower stem; B stands frame-right with both hands empty and visible, looking at S1.`

GOOD END:

`B stands frame-right holding the same flower securely by the middle-lower stem in her left hand; S1's right hand is empty and withdrawn near her torso; both faces remain clearly visible.`

## Camera Rule

- 한 Shot의 Start/End는 기본적으로 **동일 카메라**다.
- H3가 만들어야 할 움직임에 카메라 이동이 포함되더라도 Start/End 프레임의 시점 변화는 필요한 최소치만 허용한다.
- 큰 camera orbit, lens jump, axis reversal을 Start/End 이미지 자체에 동시에 넣지 않는다.
- 컷이 필요한 변화라면 같은 Shot의 End로 강제하지 말고 Motion Plan에서 Shot을 분리한다.

## Contact / Hand Rule

- 각 손의 소유자와 역할을 구분한다.
- `right hand`, `left hand`를 가능하면 명시한다.
- 소품 전달은 Start와 End의 소유권이 명확해야 한다.
- 두 사람의 손이 겹쳐 보이지 않도록 transfer area를 가시화한다.
- 포옹·부축·악수·앉기·일어나기 등 접촉 장면은 접촉점과 비접촉점을 필요한 만큼 명시한다.

## Gaze / Expression Rule

- Start와 End의 gaze target을 별도로 쓴다.
- 감정 전환이 있다면 결과 표정이 End에서 명확히 보이게 한다.
- "sad", "happy" 하나로 끝내지 말고 눈, 입, 턱, 어깨 등 관찰 가능한 결과 상태로 쓴다.

## Narrative Keyframe과의 구분

- Narrative Keyframe은 장면의 대표 이미지다.
- Motion Keyframe은 **물리 상태 계약**이다.
- Narrative Keyframe의 극적인 구도나 가장 예쁜 순간을 Start/End에 억지로 복제하지 않는다.
- 필요하면 Narrative Keyframe을 참고하되 Motion Plan과 승인 자산이 우선한다.

## 절대 금지

- Start/End에서 인물 얼굴을 다시 설계하기
- 승인 자산과 다른 의상/차량/공간 구조 발명
- 한 이미지 안에 전후 상태를 동시에 표현
- 모션 블러로 상태를 숨기기
- 손/소품/얼굴 핵심 부분을 프레임 밖으로 자르기
- Start와 End의 카메라가 이유 없이 크게 달라지기
- 시간 진행형 서술로 이미지 생성기에게 중간 동작을 만들게 하기
- H3의 `[reference generation]`, `integrated_multimodal_description`, `overall_soundscape` 작성

## 완료 조건

- 대상 Shot마다 START/END 프롬프트 쌍이 존재한다.
- 모든 쌍에 Invariant와 Delta가 있다.
- 승인 Reference ID/version이 명시된다.
- Start와 End는 각각 단일 시점의 정지 상태다.
- 손/시선/표정/접촉/소품 상태가 Motion Plan과 일치한다.
- 불필요한 geometry/camera/identity drift를 유발할 표현이 없다.
- 생성 전 QA 체크가 PASS 또는 명확한 BLOCKED 사유를 가진다.

완료 후 `manifest.phases.motion_keyframe_prompts`만 `done`으로 갱신한다. 실제 Motion Keyframe 이미지 생성·검수와 H3 최종 프롬프트는 후속 단계다.
