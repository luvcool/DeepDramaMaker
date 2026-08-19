# 《없던 사이》 Motion Keyframe Prompts

이 폴더는 v5에서 추가된 **H3용 Start/End Frame 이미지 프롬프트** 공정이다.

현재 《없던 사이》는 아직 `09_motion/epXX-motion.json`이 생성되지 않았으므로 Motion Keyframe Prompt도 생성하지 않는다.

## 실행 순서

1. `drama-motion-scene-compiler`로 대상 씬의 Motion Plan 생성
2. `drama-motion-validator` 통과
3. `drama-motion-keyframe-prompt-compiler` 실행
4. `epXX-motion-keyframes.md`의 START/END 프롬프트로 외부 이미지 생성
5. 생성된 이미지의 실제 일관성/물리 상태를 검수
6. 향후 H3 Prompt Compiler가 승인된 Start/End 이미지와 Motion Plan을 함께 사용

## 핵심 원칙

- Start/End는 같은 Shot의 두 정지 상태다.
- 얼굴·의상·공간·카메라·조명은 기본적으로 동일하다.
- pose, hand, gaze, expression, prop state 등 Motion Plan이 요구하는 Delta만 바꾼다.
- 프롬프트에 중간 동작을 서술하지 않는다.
- H3 최종 영상 프롬프트는 이 폴더의 책임이 아니다.
