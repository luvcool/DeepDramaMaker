# Global Actors

`ACTOR-001`처럼 작품에 독립적인 배우 ID를 사용한다. 사용자가 얼굴 참조 이미지를 제공하면 원본을 보존하고, 승인된 정면/3-4/측면/전신 참조의 파일 경로를 `actor.json`에 기록한다. 참조가 없으면 `status: needs_identity_build`로 남기며 임의의 실존 배우를 대입하지 않는다.
