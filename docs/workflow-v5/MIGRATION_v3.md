# Migration v3 — Motion Planning Branch

## 변경 목적

v2는 공용 Actor/Voice와 프로젝트 전용 자산, 이미지 키프레임까지 정리했다. 실제 reference-to-video 테스트에서는 짧은 2초 영상도 잘 생성되지만, 단순 행동 문장만 주면 인물 시선·표정·카메라·배경이 정지하고, 10초 이상 긴 장면은 행동 밀도가 낮아지거나 물리 오류 위험이 커지는 문제가 확인됐다.

따라서 v3는 **H3 최종 프롬프트를 쓰기 전 단계**를 추가한다.

## 새 스킬

- `drama-motion-scene-compiler`
  - Scene을 물리적으로 단순한 Shot으로 분해
  - 2초 Shot 허용
  - Start/End State
  - Story Motion vs Life Motion
  - Motion Priority
  - Motion Complexity Score / Motion Budget
  - Contact Topology
  - Visibility/Occlusion
  - Camera Complexity
  - Cut on State Change
  - Momentum Continuity

- `drama-motion-validator`
  - 필수 필드/ID/구조 자동 검사
  - 짧은 Shot의 Life Motion 부족 탐지
  - 복잡도 대비 split 누락 탐지
  - 접촉/소품/Shot 경계 상태 의미 검수

## 새 작품 폴더

`works/{slug}/09_motion/`

기존 `08_final/`은 이동하지 않는다. v3 Motion Planning은 **기존 릴리즈와 독립된 영상화 준비 브랜치**라 기존 납품본을 깨지 않는다.

## 핵심 공식

`Video Shot = Simple Story Motion + Rich Life Motion + Explicit Start/End State + Controlled Camera + Clear Physical Result`

`High Motion Density, Low Action Complexity`

## H3와의 경계

이 버전은 H3 최종 프롬프트를 생성하지 않는다. 다음은 후속 설계 범위다.

- `[reference generation]`
- `integrated_multimodal_description:`
- `overall_soundscape:`
- H3용 영어 최종 Prompt Compiler
- Start/End Frame 실제 선택/생성 로직
- Video QA

현재 `09_motion` 결과가 향후 H3 Prompt Compiler의 직접 입력이 된다.

## 샘플 작품 《없던 사이》

기존 24화/168씬 릴리즈는 그대로 보존했다. 새 Motion Plan을 저품질로 소급 자동 생성하지 않고, 실제 영상화 대상 회차부터 작성하도록 `motion_plan`, `motion_validation` phase를 `todo`로 추가했다.
