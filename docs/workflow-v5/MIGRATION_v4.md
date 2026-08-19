# Migration v4 — Asset Reference Image Pipeline

## 목적
v3의 자산 요구사항 + Motion Planning 구조에 **자산 기준 이미지 생성/승인 공정**을 추가한다.

## 새 공정

```text
asset-requirements
→ design + cast
→ asset-image-prompts
→ [외부 이미지 생성]
→ asset-image-validation
→ asset-validation
→ Narrative visual-prompts
→ prompt-audit
→ final
                  ↘ motion-plan → motion-validation
```

## 핵심 변경

1. `drama-asset-image-prompt-compiler` 추가
   - ACTOR / WARDROBE / LOCATION / VEHICLE / PROP의 재사용 기준 이미지 프롬프트 작성
   - High Structural Density / Low Narrative Density
   - Locked / Variable attribute, View Pack, Scale, Visibility, Camera 규칙 포함

2. `drama-asset-image-validator` 추가
   - 실제 생성/제공된 Reference Image를 PASS / RETRY / REJECT / PENDING으로 검수
   - Cross-view consistency, identity, geometry, anatomy, occlusion 검수
   - 승인 자산을 `{ASSET_ID}@vN`으로 버전 관리

3. `04_assets/` 확장
   - `image_prompts/`: 자산 기준 이미지 프롬프트
   - `approved/`: 실제 승인 Reference Image 레지스트리/검수/재생성 큐

4. `drama-visual-prompt-designer` 역할 축소
   - 더 이상 Actor Master, Location Master, Prop Master를 새로 발명하지 않음
   - 승인 자산 Reference를 잠그고 **Narrative Keyframe**을 만드는 역할에 집중
   - Motion Start/End Frame 프롬프트는 여전히 별도 후속 Compiler 범위

5. Single Source of Truth
   - 텍스트 프롬프트 ≠ 승인 이미지 자산
   - `04_assets/approved/registry.json`의 APPROVED 버전이 시각 자산 SSOT
   - 이미 사용 중인 작품의 자산 버전은 자동 교체 금지

## 레거시 호환
《없던 사이》의 기존 `07_visual_prompts/01_character-prompts.md` ~ `06_handoff-guide.md`는 삭제하지 않는다. v4 검증/패키징 스크립트는 새 구조와 레거시 구조를 모두 읽는다. 새 작품부터 v4 구조를 기본으로 사용한다.

## 이번 버전에서 아직 하지 않는 것
- 실제 이미지 생성
- Motion Start/End Frame Prompt Compiler
- MiniMax H3 최종 Prompt Compiler
- 실제 동영상 생성/QA
