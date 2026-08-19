# AI 드라마 스튜디오 작업 규칙

## 프로젝트 범위

- 이 작업공간은 Codex에서 텍스트 드라마와 제작 문서를 만드는 전용 프로젝트다.
- 저장소 스킬은 `.agents/skills/`의 `drama-*` 워크플로우만 사용한다.
- 결과물은 텍스트와 Markdown으로 만든다. 이미지·영상은 생성하지 않지만 제작팀 전달용 AI 이미지 프롬프트 패키지까지 작성한다.

## 스킬 라우팅

- 새 작품 기획, 현재 상태 확인, 다음 공정 판단은 `$drama-showrunner`를 사용한다.
- 대본·인물·구조·검수·대사·훅·자산 요구사항·디자인·캐스팅·자산 이미지 프롬프트·자산 이미지 승인 검수·종합 자산 검수·비주얼 프롬프트·프롬프트 검수·물리 모션 설계·모션 검수·Motion Start/End 이미지 프롬프트·최종본 요청은 가장 구체적으로 일치하는 `drama-*` 스킬을 사용한다.
- 작품 공정을 시작하기 전에 선택한 스킬의 `SKILL.md`와 그 스킬이 연결하는 공통 `pipeline.md`를 읽는다.

## 작품 상태와 파일

- 작품별 결과는 `<프로젝트 루트>/works/{slug}/`에 저장한다.
- 작품 작업 전에 `manifest.json`과 필요한 선행 산출물을 읽고, 완료 후에 manifest를 병합 갱신한다.
- 기존 작업본은 전체를 맹목적으로 교체하지 말고 필요한 부분만 수정한다.
- `08_final/`의 이전 납품 버전은 삭제하거나 덮어쓰지 않는다. 레거시 `06_final/` 또는 `07_final/`은 내용 손실 없이 새 경로로 이동한다.

## 검증

- 대본 표기와 씬 번호는 `.agents/skills/drama-showrunner/references/pipeline.md`의 규약을 따른다.
- `manifest.runtime_min`은 필수 납품 조건이다. 대본 집필 완료·후속 공정 진입·최종 릴리즈 전에 `.agents/skills/drama-screenwriter/scripts/estimate_runtime.py`를 실행하고 전 회차 `PLAUSIBLE`을 확인한다. 회차 헤더나 훅 큐시트에 적힌 시간만으로 통과 처리하지 않는다.
- 최종 패키징 전에 `.agents/skills/drama-script-finalizer/scripts/analyze_scripts.py`로 씬 번호·대사 블록·로케이션 표를 검증한다.
- 제작팀 전달 전에 `.agents/skills/drama-visual-prompt-auditor/scripts/validate_prompt_package.py`로 프롬프트 파일·ID·전 씬 커버리지를 검증한다.
- `drama-asset-image-prompt-compiler`, `drama-asset-image-validator`, `drama-visual-prompt-designer`, `drama-visual-prompt-auditor`는 이미지 생성 도구를 호출하지 않는다. 실제 생성은 제작팀/외부 생성 단계다.
- 텍스트 프롬프트를 승인된 이미지 자산으로 취급하지 않는다. 실제 Reference Image가 검수되어 `04_assets/approved/registry.json`에 APPROVED로 등록되어야 자산 이미지 승인으로 본다.

- `09_motion/`에서는 Start/End State, Contact Topology, Motion Budget, Life Motion, Cut Timing을 설계하고, 검증 통과 후 `drama-motion-keyframe-prompt-compiler`가 `09_motion/keyframes/`에 Start/End 정지 이미지 프롬프트를 작성한다. MiniMax H3 전용 최종 Prompt Compiler와 `[reference generation]` 등 최종 영상 프롬프트 문장 생성은 아직 범위 밖이다. Narrative 이미지 키프레임 프롬프트에 영상 동작 지시를 섞지 않는다.
- Motion Plan 검수 시 `.agents/skills/drama-motion-validator/scripts/validate_motion_plan.py`를 사용한다.
