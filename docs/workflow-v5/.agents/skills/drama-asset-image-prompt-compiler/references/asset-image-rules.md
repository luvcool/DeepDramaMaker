# Asset Image Rules v0.1

## 공통 원칙
- 재사용 가능한 기준 자료가 목적이다.
- Identity, Geometry, Scale, Material, Visibility, Cross-view Consistency가 미장센보다 우선한다.
- 과도한 wide-angle, extreme angle, 강한 blur, 구조를 가리는 그림자/머리카락/소품을 피한다.
- 기준 View는 자연 시점과 명확한 구조 판독을 우선한다.

## Invariant Lock
- ACTOR: face identity, facial proportions, base hair, body proportions
- WARDROBE: construction, color, material, length, fit
- LOCATION: geometry, doors, windows, major furniture positions, zone connections
- VEHICLE: body geometry, wheel/door layout, steering side, interior architecture
- PROP: shape, scale, material, color, functional structure

## Allowed Variation
- ACTOR: expression, pose (Master 이후)
- WARDROBE: wearer pose; garment structure는 불변
- LOCATION: 시간대/조명/상태 변형; geometry는 불변
- VEHICLE: door open/closed, light state; body/interior architecture는 불변
- PROP: 명세된 state variation만 허용

## Prompt Density
Asset Prompt는 짧을 필요가 없다. 구조 정보는 충분히 적되 장면 사건·감정·카메라 쇼맨십은 최소화한다.

## Scale Anchor
정확한 수치가 없는 경우 임의 확정하지 않는다. `UNSPECIFIED` 또는 인간 대비 크기 표현을 사용한다.
