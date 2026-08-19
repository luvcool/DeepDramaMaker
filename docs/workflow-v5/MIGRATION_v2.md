# Workflow v2 Migration Notes

## 이번 변경
- `Asset Requirement Extractor` 신설: 대본에서 필요한 자산을 디자인/캐스팅 전에 정규화.
- 공용 `ACTOR-*` / `VOICE-*` 라이브러리와 작품 `CHAR-*` 배역을 분리.
- `04_assets/`에 요구사항·관계·상태 ledger·Construction Queue·검수 결과를 추가.
- `Asset Validator` 신설: 실제 승인 얼굴/음성 및 P0 프로젝트 자산이 준비되기 전 visual 단계 READY 금지.
- Production Designer는 추출 기능을 내려놓고 LOC/ZONE/WARD/VEH/PROP의 시각·물리 설계에 집중.
- Casting Director는 배역 요구조건 + 공용 Actor/Voice 매핑을 담당.
- Visual Prompt Designer는 승인 Actor 참조가 있으면 텍스트로 새 얼굴을 발명하지 않고 그 참조를 잠금으로 사용.
- 기존 샘플 《없던 사이》를 새 폴더 번호 체계로 비파괴 이동하고 자산 마이그레이션 초안을 추가.

## 새 폴더 번호
- `04_assets`
- `05_design`
- `06_cast`
- `07_visual_prompts`
- `08_final`

## 의도적으로 이번에 제외
- MiniMax H3 동영상 프롬프트
- Physical Scene Compiler
- Start/End Frame 모션 설계
- Video Prompt Compiler / Video QA

위 영상화 단계는 이미지/자산 시스템이 확정된 뒤 별도 버전에서 설계한다.

## 샘플 작품 현재 상태
기존 대본/프롬프트는 검증을 통과한다. 다만 실제 승인된 `ACTOR-*`와 `VOICE-*`가 없어서 새로운 Asset Validator 기준으로는 `CONDITIONAL`이다. 이는 기존 결과물의 실패가 아니라, 새 파이프라인이 실제 생성 자산과 텍스트 명세를 구분하도록 강화된 결과다.
