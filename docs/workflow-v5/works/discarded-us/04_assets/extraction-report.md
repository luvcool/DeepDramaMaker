# Asset Extraction Migration Report — 《없던 사이》

기존 결과물을 새 자산 계층으로 **비파괴 마이그레이션**했다. 기존 디자인/캐스팅/프롬프트의 ID는 `legacy_id`로 보존한다.

## 발견
- 주요 배역 4명은 얼굴/연기/목소리 **요구조건**은 충분하지만 실제 공용 `ACTOR-*` / `VOICE-*` 승인 자산이 없다.
- 로케이션·의상·극적 소품 명세는 이미 충분히 존재하므로 Project Dedicated Asset으로 승격 가능하다.
- 기존 프롬프트는 `CHAR-LOCK`가 얼굴을 텍스트로 정의하므로, 실제 Actor 참조가 등록되면 해당 Actor를 우선하도록 새 규칙을 적용해야 한다.
- 상태 변화는 기존 문서에 산문으로 존재하나 `state-ledger.json`의 씬 단위 구조화는 아직 재추출이 필요하다.

## 다음 액션
1. 사용자 제공 또는 생성 승인 얼굴을 `assets/global/actors/ACTOR-*`에 등록.
2. 승인 목소리를 `assets/global/voices/VOICE-*`에 등록.
3. `06_cast/cast-map.json`에서 각 CHAR에 매핑.
4. Asset Validator 실행 후 Visual Prompt 재생성/교정.
