# Motion Density & Cut Timing Rules v1.0

이 규칙은 특정 H3 문장 포맷이 아니라 **영상화 전 Shot 설계 규칙**이다.

## 1. Duration ≠ Description Density

짧은 영상이라고 연출 정보를 줄이지 않는다. 2초 Shot도 하나의 완성된 Shot이다.

- 2~4초: 하나의 단순 Story Motion + 높은 Motion Density
- 5~8초: 하나의 명확한 행동 흐름 또는 2~3 Micro Beat
- 9~12초: 의미 있는 상태 변화가 둘 이상이면 Shot 분할 우선 검토
- 12초 초과: 한 Shot 유지보다 상태 변화 기반 분할을 기본 검토

## 2. Motion Channels

각 Shot은 아래 채널을 검토한다.

1. Primary Action
2. Gaze
3. Facial Expression Transition
4. Secondary Body Motion
5. Camera Motion
6. Environment Motion
7. Action Result

일반 Shot은 최소 4개 채널이 실제로 변하도록 설계한다. 인물 상호작용/감정 Shot은 가능하면 5개 이상을 쓴다.

## 3. Story Motion vs Life Motion

### Story Motion
서사를 전진시키는 큰 변화: 걷기, 문 열기, 꽃 전달, 앉기, 포옹, 물건 집기, 위치 이동.

### Life Motion
같은 행동을 살아 있게 만드는 미세 변화: 시선 이동, 눈 깜박임, 호흡, 입술/턱 변화, 작은 체중 이동, 손가락 이완, 머리카락/옷자락 반응, 미세 카메라 이동, 환경의 자연스러운 움직임.

**목표는 Story Motion을 늘리는 것이 아니라 Life Motion을 충분히 넣는 것**이다. 일반 Shot에는 최소 2개의 의미 있는 Life Motion을 권장한다.

## 4. Primary Motion Priority

Motion Priority는 3단계로 둔다.

- PRIMARY: 모델이 반드시 성공해야 하는 핵심 Story Motion 1개
- SECONDARY: 시선, 표정, 반응 등 핵심을 읽히게 하는 움직임
- SUPPORT: 머리카락, 옷자락, 환경, 미세 카메라 등 생동감 지원

PRIMARY가 둘 이상이면 분할 가능성을 먼저 검토한다.

## 5. Start / End State

모든 Shot은 최소 다음 상태를 가진다.

- 인물 위치/방향
- 자세
- 손 상태
- 핵심 소품 소유/위치
- 주요 접촉 관계
- 시선 대상

종료 상태는 다음 Shot의 시작 상태와 연결되어야 한다.

## 6. Contact Topology

접촉 장면은 `누가 / 어떤 신체 부위로 / 무엇을 / 어떤 상태로` 접촉하는지 명시한다.

예:
- `S1.right_hand -> FLOWER.stem : holding`
- `S2.left_hand -> FLOWER.stem : receiving`
- `S1.left_palm -> WALL : bracing`

접촉이 바뀌면 그 순간은 강한 Cut 후보이거나 별도 Micro Beat다.

## 7. Visibility / Occlusion

중요한 인체·소품이 가려졌다가 다시 나타나면 구조가 흔들릴 수 있다. 중요한 동작은 가능한 한:

- 양손이 보임
- 얼굴이 가려지지 않음
- 전달되는 소품이 두 사람 사이에서 계속 보임
- 손이 몸 뒤로 장시간 사라지지 않음

을 선호한다. 가림이 서사상 필수면 시작/종료 상태를 더 명확하게 적는다.

## 8. Camera Complexity

한 Shot에는 기본적으로 **하나의 주 Camera Motion**만 둔다.

좋음: gentle push-in / side follow / short pan / controlled pull-back / slight handheld drift

위험: orbit + push-in + tilt + whip pan을 동시에 요구

카메라는 주행동을 강조해야 하며 경쟁하면 안 된다.

## 9. Environment Must Breathe

상황에 맞는 환경 움직임을 선택한다: 바람, 머리카락, 의상, 커튼, 증기, 빗물, 반사광, 멀리 흐릿한 차량 등.

환경 움직임은 장면 물리와 맞아야 한다. 실내 무풍 장면에 이유 없는 강풍을 넣지 않는다.

## 10. Micro Beat Packing

2~4초 Shot도 내부 순서를 갖는다.

예: 꽃 전달 2초
1. S1이 꽃을 내밀며 S2를 본다.
2. S2 시선이 얼굴→꽃으로 이동하고 표정이 풀린다.
3. S2가 꽃을 잡고 S1이 놓으며 시선이 다시 만난다.

시간 표기를 강제하지 않아도 순서는 명확해야 한다.

## 11. Motion Complexity Score

아래는 경험적 절대값이 아니라 **분할 판단용 휴리스틱**이다.

각 항목이 있으면 +1:
- 큰 신체 동작
- 위치 이동
- 자세 전환(앉기↔서기, 눕기↔일어나기)
- 소품 전달/소유권 변경
- 인물 간 접촉 topology 변경
- 큰 감정 상태 전환
- 새로운 정보 공개에 따른 반응 전환
- 큰 카메라 재배치

점수 4 이상이면 `SPLIT_RECOMMENDED`를 기본값으로 검토한다. 4 미만도 동작이 서로 종속되지 않거나 손/접촉 난도가 높으면 분할할 수 있다.

## 12. Motion Budget

Motion Budget은 **Story Motion 난이도**를 제한하고 Life Motion은 별도로 풍부하게 유지한다.

권장 휴리스틱:
- ~2초: PRIMARY Story Motion 1개, 큰 상태 전환은 최대 1개
- 3~4초: PRIMARY 1개 + 종속 Micro Beat 1~2개
- 5~6초: 연속된 하나의 행동 흐름. 독립 Story Motion이 3개 이상이면 분할 검토
- 7초 이상: 상태 변화 지점마다 Cut 후보를 반드시 찾는다

## 13. Cut on State Change

고정 1.5~2.5초 간격을 절대 규칙으로 쓰지 않는다. Cut은 다음 변화에서 우선 찾는다.

- 시선 대상 변화
- 접촉 시작/종료
- 물체 소유권 변경
- 자세 완료
- 이동 목표 도착
- 감정 전환
- 정보 공개
- Reaction으로 관점 전환
- 장소 변경

## 14. Momentum Continuity

Cut 전후 다음을 보존한다.

- 진행 방향
- 속도/운동량
- 몸 방향
- 손에 든 소품
- 손 위치
- 젖음/손상 등 상태
- 시선 목적

의도적 반전 컷이면 예외 이유를 적는다.

## 15. Emotional Motion

`looks sad`처럼 감정을 형용사 하나로 끝내지 않는다. 중요 감정은 gaze / expression / breathing / posture / hand response 중 최소 2개로 보이게 한다.

## 16. Interaction Rule

상호작용은 `Action → Reaction → Completion` 구조를 기본으로 한다. 한 인물만 움직이고 상대가 마네킹처럼 고정되지 않도록 한다.

## 17. Core Formula

**Video Shot = Simple Story Motion + Rich Life Motion + Explicit Start/End State + Controlled Camera + Clear Physical Result**

핵심: **High Motion Density, Low Action Complexity.**
