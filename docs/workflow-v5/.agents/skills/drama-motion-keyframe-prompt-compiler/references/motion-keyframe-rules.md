# Motion Keyframe Rules v0.1

## 핵심 공식

**Motion Keyframe Pair = Approved Assets + Shared Invariants + Minimal State Delta**

Start/End는 같은 세계와 같은 Shot 안의 두 상태다. 차이를 크게 만들수록 reference-to-video 모델이 중간을 안정적으로 연결하기 어려워진다.

## 1. State, not action

이미지 프롬프트는 시간축을 쓰지 않는다.

- `reaches for` → `right arm extended toward`
- `turns to look` → `head and eyes facing`
- `gives the phone` → START/END의 소유 상태로 분리
- `sits down` → START standing / END seated

## 2. Invariant Lock

기본 고정:

- identity
- body proportions
- hair unless plot change
- wardrobe
- location geometry
- vehicle geometry
- prop geometry
- camera class and framing
- main light direction
- background layout

## 3. Delta Whitelist

변화는 Motion Plan이 요구하는 것만 허용한다.

- pose
- hand state
- gaze
- expression
- small position shift
- contact state
- prop ownership/state
- door/object functional state

## 4. Minimal Visual Distance

Start/End 간 차이는 목표 동작을 표현하는 데 필요한 최소한이어야 한다.

BAD: 꽃 전달 2초 Shot에서 카메라 위치, 인물 위치, 조명, 배경, 표정, 의상 주름까지 모두 크게 변경.

GOOD: 같은 카메라/배경/조명에서 손·시선·표정·꽃 소유권만 변경.

## 5. Physical Legibility

- 모든 중요한 접촉점이 보여야 한다.
- 손은 가능한 한 명확한 좌/우를 쓴다.
- 작은 소품은 손과 분리되어 형태가 읽혀야 한다.
- 팔이 얼굴 앞을 가리지 않게 한다.
- 다리/발이 자세 변화에 중요하면 프레임 안에 포함한다.

## 6. Contact Topology

START와 END 각각 접촉 그래프를 생각한다.

예:

START
- S1.right_hand -> flower.stem
- S2.left_hand -> none
- S2.right_hand -> none

END
- S1.right_hand -> none
- S2.left_hand -> flower.stem

중간 접촉은 H3의 동작 영역이며 정지 이미지에 동시에 표현하지 않는다.

## 7. Gaze State

- 누구를/무엇을 보는지 명시한다.
- Start/End의 gaze 변화가 감정/행동 결과와 연결되어야 한다.
- 카메라 응시는 대본/연출상 필요한 경우만.

## 8. Expression State

감정 형용사보다 관찰 가능한 표정 결과를 우선한다.

- eyes slightly widened
- lips pressed together
- brows relaxed
- jaw unclenched
- restrained small smile

## 9. Camera Stability

기본값은 동일한 camera pose다.

Start/End 사이의 카메라 이동 자체가 중요한 Motion이면 작은 위치 차이를 허용할 수 있지만, 큰 축 변화는 Shot Split을 우선한다.

## 10. Background Stability

H3가 인물 동작에 집중하도록 주요 배경 geometry는 유지한다.
환경의 움직임은 H3 Prompt에서 지시할 수 있으므로 Start/End 이미지가 서로 다른 바람/군중/조명 상태로 과도하게 변하지 않게 한다.

## 11. Plot-mandated transformation

헤어컷, 변신, 의상 변경, 파손처럼 이야기 자체가 외형 변화라면 해당 항목을 DELTA로 명시하고 나머지는 더 강하게 잠근다.

## 12. 2-second Shot

2초라도 Start/End 이미지는 충분히 구체적이어야 한다.
짧다고 해서 손·시선·표정·소품 상태를 생략하지 않는다.
다만 상태 차이는 단순하게 유지한다.

## 13. Negative Constraints

각 쌍은 최소 다음 drift를 막는다.

- different face / identity
- different hairstyle unless allowed
- wardrobe redesign
- extra/missing fingers
- merged hands
- duplicate prop
- changed location geometry
- changed camera angle without reason
- object teleportation state inconsistency

## 14. Pair QA

- 두 프롬프트가 같은 Shot처럼 보이는가?
- Motion Plan 없이 봐도 무엇이 바뀌는지 한 문장으로 설명 가능한가?
- 바뀌는 항목이 DELTA와 일치하는가?
- 바뀌면 안 되는 항목이 프롬프트에서 흔들릴 여지가 없는가?
- End가 primary motion의 완료 상태인가?
