# 《없던 사이》 Motion Planning

이 폴더는 v3에서 추가된 **영상화 전 물리 모션 설계** 공정이다.

현재 기존 v3 릴리즈에는 168씬 이미지 키프레임까지 존재하지만, 새 Motion Plan은 아직 생성하지 않았다. 기존 납품본을 소급해 저품질 자동 변환하지 않고, 실제 영상 제작 대상 씬부터 `drama-motion-scene-compiler`로 `epXX-motion.json`을 만든다.

## 다음 작업

1. 승인 Actor/Voice 자산 연결
2. 영상화 대상 회차/씬 선택
3. `epXX-motion.json` 생성
4. `drama-motion-validator` 검수
5. `drama-motion-keyframe-prompt-compiler`로 Start/End 이미지 프롬프트 생성
6. 외부에서 Start/End 이미지 생성 및 검수
7. 향후 별도 H3 Prompt Compiler로 전달

H3 최종 프롬프트 문장은 이 폴더에서 작성하지 않는다. `keyframes/`에는 H3 동영상 프롬프트가 아니라 Start/End 정지 이미지 생성 프롬프트만 작성한다.
