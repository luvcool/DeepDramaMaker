# 《없던 사이》 비주얼 프롬프트 교정 이력

## v1 · 2026-08-06

| ID | 심각도 | 수정 파일 | 변경 | 결과 |
|---|---|---|---|---|
| VP-C01 | 중대 | `04_episode-keyframes.md` | 현실 관리센터의 잘못된 잔여 시간 LIGHT를 교체하고, 버려진 시간 연속 씬의 LIGHT를 시퀀스 단위로 통일 | 해결 |
| VP-C02 | 중대 | `04_episode-keyframes.md` | ep01 S#4 이후 현실 사진을 `PROP-PHOTO-DRY`로 전환, 잔여 시간 재현만 WET 유지 | 해결 |
| VP-C03 | 중대 | `03_prop-prompts.md`, `04_episode-keyframes.md` | `PROP-KEYCHAIN-WORN` 추가, ep13 전달과 ep14 반환 키프레임에 잠금 | 해결 |
| VP-C04 | 경미 | `04_episode-keyframes.md` | 4인 키프레임 두 개를 대표 행동 중심 3인 이하로 정리 | 해결 |
| VP-C05 | 경미 | `04_episode-keyframes.md` | ep08 S#1 장소 잠금을 `LOC-CENTER-SORT`에서 `LOC-FOOD-TENT`로 교정 | 해결 |

## 재검증

- 명령: `validate_prompt_package.py works/discarded-us --format markdown`
- 결과: 대본 93씬 / 커버 93씬 / 키프레임 93개 / 자산 ID 60개 / 오류 0
- 미해결 치명·중대: 0
- 판정: READY

## v2 · 2026-08-06

| ID | 심각도 | 수정 파일 | 변경 | 결과 |
|---|---|---|---|---|
| VP2-M01 | 중대 | `03_prop-prompts.md`, `04_episode-keyframes.md` | ep01 S01~S06의 사진은 얼굴 비가시 WET, S07부터 관계 정보가 드러나는 DRY로 상태 전환 | 해결 |
| VP2-M02 | 중대 | `01_character-prompts.md`, `05_design/costumes.md` | ep17 서하 의상의 대본 밖 실제 그을림을 삭제하고 붉은 경보광 반사만 유지 | 해결 |
| VP2-M03 | 중대 | `04_episode-keyframes.md`, `06_cast/cast-brief.md` | 전경 얼굴 잠금을 최대 3명으로 제한하고 주연 우선순위 및 이름 없는 반복 배경 인물 연속성 노트 확정 | 해결 |
| VP2-m01 | 경미 | `04_episode-keyframes.md` | ep03·15·20·24의 구버전 씬/장소 연결을 7씬 대본 기준으로 교정 | 해결 |
| VP2-m02 | 경미 | `00_style-bible.md`, `04_episode-keyframes.md` | 현실 낮·밤 조명 잠금을 추가하고 잔시/센터/현실 시퀀스를 분리 | 해결 |

## v2 재검증

- 명령: `validate_prompt_package.py works/discarded-us --format markdown`
- 결과: 대본 168씬 / 커버 168씬 / 키프레임 168개 / 자산 ID 71개 / 오류 0
- 추가 검사: 키프레임당 CHAR 잠금 3명 초과 0, 미정의 ID 0
- 미해결 치명·중대·경미: 0
- 판정: READY
