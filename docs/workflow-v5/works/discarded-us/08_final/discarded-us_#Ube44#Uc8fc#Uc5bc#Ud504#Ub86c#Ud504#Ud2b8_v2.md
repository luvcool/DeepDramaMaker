# 《없던 사이》 비주얼 프롬프트 패키지 v2
> 세로형 9:16 · 24화 · 93씬 · 텍스트 프롬프트 전용 · 2026-08-06

## 납품 상태

| 항목 | 상태 |
|---|---|
| 이미지 생성 | 미실행 — 제작팀 수행 |
| 대본 씬 커버 | 93/93 |
| 키프레임 | 93개 |
| 등록 자산 ID | 60개 |
| 기계 검증 | 오류 0 |
| 의미·연속성 검수 | READY |

## 문서 구성

1. 스타일·카메라·조명·등급 잠금
2. 배우 아이덴티티와 회차별 의상
3. 로케이션 마스터
4. 소품·상태 마스터
5. 24화 93씬 키프레임
6. 공통 네거티브
7. 제작팀 인수인계
8. 프롬프트 검수와 교정 이력

---

<!-- SOURCE: 06_visual_prompts/00_style-bible.md -->

# 《없던 사이》 비주얼 프롬프트 스타일 바이블 v1
> 생성기 독립형 마스터 · 이미지 생성 미실행

## 전역 잠금

### STYLE-MASTER | 생활 밀착형 로맨스 미스터리
- **SOURCE**: `concept.md`, `locations.md`, `hook-map.md`
- **PURPOSE**: 전 자산 공통 스타일 잠금
- **LOCKS**: 자연스러운 한국 현대극, 절제된 초현실, 15세 등급
- **VARIABLES**: 막별 색감과 잔시 효과만 변경
- **ASPECT**: 기본 9:16
- **COMPOSITION**: 얼굴·손·핵심 소품이 세로축 안에서 전후로 겹치고 좌우 빈 공간은 최소화
- **PROMPT_KO**: `현대 서울을 배경으로 한 생활 밀착형 실사 드라마 스틸, 자연스러운 한국 성인의 얼굴과 피부 결, 과도한 뷰티 보정 없는 미세 표정, 일상적인 공공기관과 생활 공간의 사용감, 로맨스는 시선과 손의 멈춤으로 표현, 초현실 현상은 물건 가장자리의 약한 자주색 측광과 현실 프레임의 미세한 어긋남으로만 표현, 깊은 검정 속에도 재질 정보 유지, 절제된 대비, 촬영 가능한 현실적 미술`
- **PROMPT_EN**: `live-action contemporary Korean drama still set in present-day Seoul, natural adult Korean faces and real skin texture, micro-expressions without beauty-filter polish, worn public-service and everyday environments, romantic tension expressed through gaze and hands pausing before contact, supernatural time residue shown only as faint magenta edge light and subtle frame misalignment around objects, restrained contrast, readable material detail in shadows, physically producible art direction`
- **NEGATIVE**: `NEG-GLOBAL, NEG-RATING, NEG-TEXT`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: 전 파일에서 실사성·피부 질감·절제된 잔시 효과 고정

### CAM-VERTICAL-MASTER | 9:16 세로 촬영 문법
- **SOURCE**: `concept.md` 포맷, `hook-map.md`
- **PURPOSE**: 키프레임 카메라 잠금
- **LOCKS**: STYLE-MASTER
- **VARIABLES**: 샷 크기와 렌즈만 씬별 변경
- **ASPECT**: 9:16
- **COMPOSITION**: 상단 15%는 얼굴·시선 여유, 중앙은 인물 관계, 하단 35%는 손·소품, 화면 가장자리 8% 안전 영역
- **PROMPT_KO**: `9:16 세로 프레임, 한 명은 중앙축 정면이고 두 명일 때는 앞뒤 깊이로 겹침, 얼굴을 상단 중앙에 두고 손과 극적 소품을 하단 3분의 1에 배치, 모바일 화면에서도 눈동자 방향과 손가락 간격이 읽히는 피사계심도, 과도한 네덜란드 앵글 없이 사람 눈높이 중심`
- **PROMPT_EN**: `vertical 9:16 frame, one subject centered or two subjects layered in depth rather than spread wide, faces in the upper central area, hands and dramatic props in the lower third, depth of field that keeps eye direction and finger spacing readable on a phone screen, mostly human eye-level camera, no gratuitous dutch angle`
- **NEGATIVE**: `NEG-GLOBAL, cropped hands, clipped head, excessive empty side space`
- **POST TEXT**: 자막 안전영역은 하단 12% 비움
- **CONTINUITY CHECK**: 모든 KF의 ASPECT 9:16, 얼굴·손·소품 우선순위 유지

### CAM-VERTICAL-CLOSE | 관계 클로즈업
- **SOURCE**: `cast-identity.md`, `hook-map.md`
- **PURPOSE**: 썸·결심 장면의 카메라
- **LOCKS**: CAM-VERTICAL-MASTER
- **VARIABLES**: 50–85mm 상당, 한 명 또는 투샷
- **ASPECT**: 9:16
- **COMPOSITION**: 두 눈 사이와 손의 정지 지점을 같은 세로축에 배치
- **PROMPT_KO**: `50~85mm 상당의 절제된 세로 클로즈업, 얕지만 두 사람 눈과 닿기 직전 손끝이 함께 읽히는 초점, 얼굴 왜곡 없는 거리, 숨과 시선의 긴장을 포착하는 정적인 카메라`
- **PROMPT_EN**: `restrained vertical close-up with a 50–85mm equivalent lens, shallow focus while keeping both eye lines and the paused fingertips legible, distortion-free facial distance, static camera attentive to breath and consent before contact`
- **NEGATIVE**: `extreme glamour close-up, fisheye distortion, voyeuristic body crop`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: 접촉 전 정지와 상대의 반응이 같은 프레임에 존재

## 광원 잠금

### LIGHT-CENTER-NIGHT | 센터 야간
- **SOURCE**: `locations.md` 시각 문법
- **PURPOSE**: 잔시물 관리센터 공통 광원
- **LOCKS**: STYLE-MASTER
- **VARIABLES**: 경보 시 붉은 보조광 추가
- **ASPECT**: 9:16
- **COMPOSITION**: 위에서 누르는 형광등, 눈 아래 약한 그림자, 금속 반사선
- **PROMPT_KO**: `4300K의 오래된 천장 형광등, 한 박자 늦게 켜진 듯 일부 관이 어둡고, 눈 아래 얇은 그림자와 긁힌 금속 위 청록 반사, 피부는 창백하게 죽이지 않고 실제 혈색을 남김`
- **PROMPT_EN**: `aging 4300K overhead fluorescent tubes with one dim section, thin shadows beneath the eyes, oxidized teal reflections on scratched metal, natural blood tone preserved in skin rather than drained cyan faces`
- **NEGATIVE**: `neon cyberpunk, saturated blue wash, beauty ring light`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: 센터 현재 시점 전 장면에서 위쪽 형광등 방향 고정

### LIGHT-RESIDUAL-TIME | 버려진 시간
- **SOURCE**: `world.md`, `locations.md`
- **PURPOSE**: 잔시 구역 광원
- **LOCKS**: STYLE-MASTER
- **VARIABLES**: 물건 종류와 반복 구간
- **ASPECT**: 9:16
- **COMPOSITION**: 현실 광원은 유지하고 잔시물 가장자리에서만 자주색 측광
- **PROMPT_KO**: `현실 공간의 원래 광원을 그대로 유지하고 시간 폐기물의 모서리, 젖은 표면, 거울 반사에만 저채도 자주색 측광, 반복 인물은 유령처럼 투명하지 않고 미세한 프레임 중첩으로 표시, 공포영화 안개 없음`
- **PROMPT_EN**: `preserve the location's practical lighting; add low-saturation magenta edge light only to discarded-time objects, wet surfaces and reflections; repeated people remain solid and human, indicated by a subtle offset double frame rather than ghost transparency; no horror fog`
- **NEGATIVE**: `portal vortex, fantasy particles, hologram people, purple neon room`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: 잔시 효과는 인물 전체가 아니라 물건·반사·프레임 경계에 제한

### LIGHT-PRESENT-MORNING | 현재의 아침
- **SOURCE**: `locations.md` 변화 규칙, ep24
- **PURPOSE**: 결말 현실 광원
- **LOCKS**: STYLE-MASTER
- **VARIABLES**: 카페 내부·골목 외부
- **ASPECT**: 9:16
- **COMPOSITION**: 한 사람 폭의 자연광이 두 인물 얼굴에 동시에 닿음
- **PROMPT_KO**: `서울 아침의 흐린 자연광과 건물 사이로 들어오는 옅은 호박색 직사광, 처음으로 두 사람 얼굴에 같은 방향의 빛, 과거 증거를 강조하는 색광 없이 도자기와 피부의 따뜻한 실제 질감`
- **PROMPT_EN**: `soft Seoul morning daylight with a narrow band of pale amber sun between buildings, the same natural light reaching both faces for the first time, warm real texture on skin and ceramic, no colored supernatural accent`
- **NEGATIVE**: `golden fantasy glow, wedding-commercial lighting, blown highlights`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: ep24 이전에는 이 양방향 자연광을 사용하지 않음

## 색·등급 잠금

### GRADE-ARC-MASTER | 막별 색 이동
- **SOURCE**: `structure.md`, `locations.md`
- **PURPOSE**: 24화 색보정 연속성
- **LOCKS**: STYLE-MASTER
- **VARIABLES**: A1 ep01–06 / A2 ep07–12 / A3 ep13–18 / A4 ep19–24
- **ASPECT**: 모든 비율
- **COMPOSITION**: 해당 없음
- **PROMPT_KO**: `A1 청록 70%와 중성 피부, A2 청록 안에 흐린 호박과 자주색 반사 증가, A3 피부색과 생활 공간의 갈색을 회복하되 사고 장면은 붉은 경보, A4 ep19~23 청록 재우세 후 ep24 자연광의 옅은 호박색으로 해소`
- **PROMPT_EN**: `A1 uses oxidized teal at seventy percent with neutral skin; A2 introduces muted amber and magenta reflections; A3 restores skin and everyday brown tones while the accident uses red alarm light; A4 returns to teal in episodes 19–23, then resolves in pale amber natural daylight in episode 24`
- **NEGATIVE**: `random episode color palette, teal-orange blockbuster grade, monochrome flashback`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: 과거와 현재를 흑백으로 나누지 않음

### RATING-15-CONSENT | 15세 경계형 성인 썸
- **SOURCE**: `concept.md`, `characters.md`
- **PURPOSE**: 전 인물 관계 표현 잠금
- **LOCKS**: STYLE-MASTER
- **VARIABLES**: 씬별 허용 접촉
- **ASPECT**: 9:16
- **COMPOSITION**: 얼굴·눈·멈춘 손으로 긴장 표현, 신체 일부의 선정적 분절 금지
- **PROMPT_KO**: `성인 간의 세련된 긴장, 동의가 확인되기 전 손은 피부에 닿지 않고 벽·문·소품에서 멈춤, 입맞춤은 대본에 있는 ep15 과거와 ep24 현재에서만 짧고 비노골적으로, 가슴·엉덩이 중심 구도와 침실 노출 없음`
- **PROMPT_EN**: `sophisticated tension between adults; before consent, hands pause on walls, doors or props rather than skin; kisses appear only where scripted, briefly and without explicit sensuality; no chest- or hip-centered framing, no bedroom nudity`
- **NEGATIVE**: `NEG-RATING`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: 대본 밖 접촉을 프롬프트가 추가하지 않음

---

<!-- SOURCE: 06_visual_prompts/01_character-prompts.md -->

# 《없던 사이》 배우·캐릭터 생성 프롬프트 v1
> 실존 배우 참조 없음 · 승인 이미지 슬롯은 제작팀이 채움

## 한서하

### CHAR-SEOHA-LOCK | 한서하 정체성 잠금
- **SOURCE**: `characters.md`, `cast-identity.md`, `costumes.md`
- **PURPOSE**: 주연 배우 외형 고정
- **LOCKS**: STYLE-MASTER, RATING-15-CONSENT
- **VARIABLES**: 표정·의상·젖음·조명만 변경
- **ASPECT**: 4:5 캐릭터 시트 또는 9:16 키프레임
- **COMPOSITION**: 얼굴과 왼손 검지가 함께 보이는 상반신 기준
- **PROMPT_KO**: `화면 나이 32세의 한국 여성, 길고 단정한 타원형 얼굴에 턱선은 부드럽지만 긴장하면 각이 드러남, 좌우 눈썹 높이가 아주 미세하게 다르고 짙은 갈색의 얇은 쌍꺼풀 눈, 곧은 코와 감정을 참을 때 단단해지는 입술, 실제 피부결과 눈 밑의 희미한 피로, 쇄골에 닿는 검은 직모를 낮은 옆가르마로 정리, 장식 없는 귀, 물건을 정확히 다룬 손과 왼손 검지의 작은 굳은살, 물러서지 않고 턱을 약간 드는 자세, 냉정함보다 감정을 관리하는 긴장이 읽히는 얼굴`
- **PROMPT_EN**: `Korean woman, screen age 32, elongated neat oval face with a jaw that becomes angular under tension, subtly uneven eyebrow height, dark brown eyes with narrow natural double lids, straight nose, lips that press firm when containing emotion, real skin texture and faint under-eye fatigue, straight black hair touching the collarbone with a low side part, unadorned ears, precise working hands with a small callus on the left index finger, upright stance that lifts the chin slightly rather than stepping back, a face controlling emotion rather than lacking it`
- **NEGATIVE**: `NEG-GLOBAL, NEG-CHARACTER, doll face, glossy idol makeup, long wavy hair, bangs, large jewelry`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: 얼굴형·가르마·머리 길이·왼손 굳은살 고정

### CHAR-SEOHA-SHEET | 한서하 승인용 캐릭터 시트
- **SOURCE**: CHAR-SEOHA-LOCK
- **PURPOSE**: 정면·좌우 3/4·측면·전신·손·표정 승인
- **LOCKS**: CHAR-SEOHA-LOCK, WARD-SEOHA-A1, STYLE-MASTER
- **VARIABLES**: 정면 중립, 웃음 참기, 질문 전 들숨, 무너짐 직전, 현재형 미소
- **ASPECT**: 3:2 가로 시트
- **COMPOSITION**: 동일 인물 7패널, 동일 렌즈·광원·피부색, 얼굴 4패널·전신 1·손 1·표정 변화 1
- **PROMPT_KO**: `동일한 한서하 정체성을 유지한 배우 승인 시트, 정면·왼쪽 3/4·오른쪽 3/4·완전 측면, 잿빛 청록 작업 셔츠의 전신 직선 실루엣, 왼손 검지 굳은살과 사원증 클립 손 클로즈업, 웃음을 참아 턱에 힘이 드는 표정과 도윤의 손에서 눈으로 시선이 올라오는 표정, 중성 회색 배경, 85mm 얼굴 기준, 색과 비율 변화 없음`
- **PROMPT_EN**: `actor approval sheet preserving the exact same Han Seoha identity across seven panels: front, left three-quarter, right three-quarter, full profile, full-body straight silhouette in an ash-teal work shirt, close-up of the left index-finger callus and ID clip, expression study with tension appearing in the jaw while suppressing a smile and gaze rising from a man's hand to his eyes, neutral gray background, 85mm facial reference, identical color and proportions`
- **NEGATIVE**: `different person between panels, hairstyle change, mirrored beauty mark, fashion editorial pose, text labels`
- **POST TEXT**: 패널명은 후반 합성
- **CONTINUITY CHECK**: 모든 패널이 CHAR-SEOHA-LOCK과 동일 인물

### WARD-SEOHA-A1 | 서하 ep01–06
- **SOURCE**: `costumes.md`
- **PURPOSE**: 초반 의상 잠금
- **LOCKS**: CHAR-SEOHA-LOCK
- **VARIABLES**: 재킷 착탈·잔시 젖음
- **ASPECT**: 전신
- **COMPOSITION**: 어깨와 소매 접힘, 무광 안전화까지 표시
- **PROMPT_KO**: `잿빛 청록 셔츠의 소매를 정확히 두 번 접고 검정 스트레이트 팬츠, 얇은 먹색 방수 작업 재킷, 장식 없는 무광 검정 안전화, 검정 메탈 클립 사원증, 셔츠는 형광등에서 거의 회색으로 보이고 재킷 팔꿈치만 닳은 상태`
- **PROMPT_EN**: `ash-teal shirt with sleeves folded exactly twice, black straight work trousers, thin charcoal waterproof work jacket with worn elbows, plain matte black safety shoes, ID card on a black metal clip; the shirt reads almost gray under fluorescent light`
- **NEGATIVE**: `skirt, heels, tight blouse, luxury logo, jewelry`
- **POST TEXT**: 사원증 이름은 후반 합성
- **CONTINUITY CHECK**: ep01–06 동일, ep03 젖은 소매만 추가

### WARD-SEOHA-A2 | 서하 ep07–16
- **SOURCE**: `costumes.md`
- **PURPOSE**: 친밀감 상승 의상 잠금
- **LOCKS**: CHAR-SEOHA-LOCK
- **VARIABLES**: 크림 이너 노출량·젖음
- **ASPECT**: 전신
- **COMPOSITION**: 윗단추 한 개 열린 셔츠와 손목이 보임
- **PROMPT_KO**: `초반과 같은 직선 실루엣, 잿빛 청록 셔츠 윗단추 하나만 열어 크림색 면 이너가 얇게 보임, 검정 팬츠와 같은 안전화, 소매와 어깨에 완전히 마르지 않은 빗물 자국, 과장된 노출 없이 재질만 부드러워짐`
- **PROMPT_EN**: `same straight silhouette as the early arc, ash-teal shirt with only the top button open to reveal a narrow line of cream cotton inner layer, black trousers and the same safety shoes, incompletely dried rain marks on sleeve and shoulder, softer texture without revealing styling`
- **NEGATIVE**: `cleavage, silk blouse, costume redesign, romantic dress`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: ep07–16만 사용

### WARD-SEOHA-A3 | 서하 ep17–23
- **SOURCE**: `costumes.md`
- **PURPOSE**: 선택 비용 구간 의상 잠금
- **LOCKS**: CHAR-SEOHA-LOCK
- **VARIABLES**: ep17 잔시 그을림·ep21 명찰 위치
- **ASPECT**: 전신
- **COMPOSITION**: 끝까지 잠근 작업 재킷, 한쪽 소매 상태 표시
- **PROMPT_KO**: `먹색 작업 재킷을 목 아래까지 잠근 한서하, 한쪽 소매에 붉은 경보광 아래 보이는 약한 그을림, ep21 이후 사원증은 가리지 않고 가슴 중앙에 정면 배치, 검정 팬츠와 안전화 유지`
- **PROMPT_EN**: `Han Seoha with the charcoal work jacket zipped to the base of the neck, a faint scorch mark on one sleeve visible under red alarm light, ID card displayed face-forward at the center of her chest from episode 21 onward, same black trousers and safety shoes`
- **NEGATIVE**: `battle damage, torn clothing, tactical costume`
- **POST TEXT**: 사원증 이름은 후반 합성
- **CONTINUITY CHECK**: ep17 그을림 발생 후 ep23까지 유지

### WARD-SEOHA-A4 | 서하 ep24
- **SOURCE**: `costumes.md`
- **PURPOSE**: 현재형 결말 의상 잠금
- **LOCKS**: CHAR-SEOHA-LOCK
- **VARIABLES**: 재킷 벗음
- **ASPECT**: 전신
- **COMPOSITION**: 자연광에서 셔츠 본래 청록과 같은 안전화가 함께 보임
- **PROMPT_KO**: `작업 재킷을 벗고 옅은 청록 본색이 드러난 기존 셔츠, 검정 스트레이트 팬츠와 익숙한 안전화, 새 옷처럼 보이지 않는 세탁 주름, 자연광에서만 부드러워진 동일 인물`
- **PROMPT_EN**: `the same existing shirt without the work jacket, its true pale teal visible in daylight, black straight trousers and familiar safety shoes, lived-in wash creases rather than a new outfit, the same woman softened only by natural light`
- **NEGATIVE**: `date dress, makeover, high heels, new hairstyle`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: ep24에서만 사용

## 이도윤

### CHAR-DOYUN-LOCK | 이도윤 정체성 잠금
- **SOURCE**: `characters.md`, `cast-identity.md`, `costumes.md`
- **PURPOSE**: 주연 배우 외형 고정
- **LOCKS**: STYLE-MASTER, RATING-15-CONSENT
- **VARIABLES**: 웃음 강도·의상·부상·기억 손실 표정
- **ASPECT**: 4:5 또는 9:16
- **COMPOSITION**: 눈과 멈춘 손, 왼쪽 옆구리 흉터 위치 기준
- **PROMPT_KO**: `화면 나이 34세의 한국 남성, 긴 타원형 얼굴과 부드럽지만 선명한 턱선, 눈꼬리가 아주 조금 내려간 짙은 갈색 눈과 낮은 눈썹, 곧은 코, 농담할 때 한쪽 입꼬리만 먼저 올라가는 입, 실제 피부결과 옅은 면도 자국, 짧은 검은 머리를 7대3 옆가르마로 넘기되 관자놀이 한 가닥은 쉽게 내려옴, 손가락이 길고 손목에 시계가 없는 옅은 자국, 평소 한쪽 어깨가 느슨하고 위험 시 중심이 즉시 낮아지는 자세, 왼쪽 옆구리의 오래된 3cm 흉터`
- **PROMPT_EN**: `Korean man, screen age 34, long oval face with a soft but defined jaw, dark brown eyes with slightly lowered outer corners and low-set brows, straight nose, one corner of the mouth lifting first when joking, real skin texture and faint shaving shadow, short black hair in a seven-three side part with one strand easily falling at the temple, long fingers, pale empty watch mark on the wrist, one shoulder relaxed at rest but center dropping instantly in danger, old three-centimeter scar on the left flank`
- **NEGATIVE**: `NEG-GLOBAL, NEG-CHARACTER, idol styling, muscular action-hero body, pompadour, beard, wristwatch in present timeline`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: 7대3 가르마·한쪽 입꼬리·빈 손목 자국·왼쪽 흉터 고정

### CHAR-DOYUN-SHEET | 이도윤 승인용 캐릭터 시트
- **SOURCE**: CHAR-DOYUN-LOCK
- **PURPOSE**: 정면·측면·전신·손·표정 승인
- **LOCKS**: CHAR-DOYUN-LOCK, WARD-DOYUN-A1, STYLE-MASTER
- **VARIABLES**: 농담, 진심, 기억 손실, 허락 기다림
- **ASPECT**: 3:2 가로 시트
- **COMPOSITION**: 동일 인물 7패널, 얼굴 4·전신 1·손목 1·표정 1
- **PROMPT_KO**: `동일한 이도윤 정체성을 유지한 배우 승인 시트, 정면·좌우 3/4·측면, 먹색 셔츠와 느슨한 회색 넥타이 전신, 시계 없는 손목 자국과 긴 손가락 클로즈업, 입은 웃지만 눈은 반응을 확인하는 표정, 농담이 사라진 단정한 표정, 기억 손실 뒤 명찰을 읽는 낯선 시선, 중성 회색 배경과 동일 광원`
- **PROMPT_EN**: `actor approval sheet preserving the exact same Lee Doyun identity: front, both three-quarter angles and profile, full body in charcoal shirt with a loose gray tie, close-up of long fingers and the empty watch mark, expression with a smiling mouth while the eyes check the other person, a firm face after humor disappears, unfamiliar gaze reading an ID after memory loss, neutral gray background and identical lighting`
- **NEGATIVE**: `different person between panels, watch on present wrist, fashion editorial, exaggerated grin`
- **POST TEXT**: 패널명은 후반 합성
- **CONTINUITY CHECK**: 전 패널 CHAR-DOYUN-LOCK 동일

### WARD-DOYUN-A1 | 도윤 ep01–06
- **SOURCE**: `costumes.md`
- **PURPOSE**: 복귀자 의상 잠금
- **LOCKS**: CHAR-DOYUN-LOCK
- **VARIABLES**: 재킷·젖음
- **ASPECT**: 전신
- **COMPOSITION**: 넥타이 끝과 구두형 안전화까지 표시
- **PROMPT_KO**: `먹색 면 셔츠, 짙은 남색 작업 바지, 규정보다 2cm 길고 매듭이 느슨한 가는 회색 넥타이, 낡았지만 닦인 검정 구두형 안전화, 목깃은 여러 번 세탁해 부드럽고 손목에는 시계 없이 자국만 있음`
- **PROMPT_EN**: `charcoal cotton shirt, deep navy work trousers, narrow gray tie hanging two centimeters longer than regulation with a loose knot, worn but polished black shoe-style safety footwear, softened washed collar, no watch on the wrist, only the pale mark`
- **NEGATIVE**: `business suit, luxury shoes, watch, open shirt exposing chest`
- **POST TEXT**: 사원증 이름은 후반 합성
- **CONTINUITY CHECK**: ep01–06 동일

### WARD-DOYUN-A2 | 도윤 ep07–16
- **SOURCE**: `costumes.md`, `props.md`
- **PURPOSE**: 과거와 현재 충돌 의상 잠금
- **LOCKS**: CHAR-DOYUN-LOCK
- **VARIABLES**: ep09 과거 셔츠 착용·ep13 흉터 노출
- **ASPECT**: 전신
- **COMPOSITION**: 기본 셔츠 또는 PROP-SHIRT-FOUND 상태를 명시
- **PROMPT_KO**: `기본 먹색 셔츠와 남색 작업 바지 유지, ep09에서만 회청색 과거 셔츠로 교체하며 두 번째 단추가 비어 있고 안쪽 D 표식은 후반 합성, ep13에는 셔츠 밑단이 살짝 들려 왼쪽 옆구리 흉터 3cm만 보임, 선정적 노출 없음`
- **PROMPT_EN**: `maintain the basic charcoal shirt and navy work trousers; only in episode 9 switch to the faded blue-gray past shirt with the second button missing and a blank inner label for the D mark in post; in episode 13 the hem lifts just enough to reveal only the three-centimeter left-flank scar, no sensual exposure`
- **NEGATIVE**: `shirtless, large wound, watch, different tie style`
- **POST TEXT**: 셔츠 안쪽 `D`는 후반 합성
- **CONTINUITY CHECK**: ep09 셔츠 예외, ep13 흉터 위치 일치

### WARD-DOYUN-A3 | 도윤 ep17–23
- **SOURCE**: `costumes.md`
- **PURPOSE**: 자기희생 구간 의상 잠금
- **LOCKS**: CHAR-DOYUN-LOCK
- **VARIABLES**: 과거 ep17 피 묻음 / 현재는 깨끗함
- **ASPECT**: 전신
- **COMPOSITION**: 넥타이 없이 내린 소매, 과거와 현재 상태 분리
- **PROMPT_KO**: `현재 도윤은 넥타이 없이 먹색 셔츠 소매를 끝까지 내리고 지나치게 단정한 상태, 과거 사고 도윤만 왼쪽 옆구리에 제한된 짙은 피 얼룩, 현재 도윤에게 피나 새 상처 없음`
- **PROMPT_EN**: `present Doyun wears the charcoal shirt with no tie and sleeves fully down, unusually neat; only past-accident Doyun has a contained dark blood stain at the left flank; present Doyun has no blood or fresh injury`
- **NEGATIVE**: `heroic combat damage, torn shirt, blood on present Doyun`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: 과거·현재 피 상태 혼합 금지

### WARD-DOYUN-A4 | 도윤 ep24
- **SOURCE**: `costumes.md`
- **PURPOSE**: 머무는 사람 결말 의상 잠금
- **LOCKS**: CHAR-DOYUN-LOCK
- **VARIABLES**: 느슨한 넥타이를 서하가 잡음
- **ASPECT**: 전신
- **COMPOSITION**: 회색 넥타이와 빈 손목 자국이 함께 보임
- **PROMPT_KO**: `ep01과 같은 먹색 셔츠와 가는 회색 넥타이, 매듭은 여전히 느슨해 손가락 두 개가 들어갈 여백, 남색 바지와 구두형 안전화, 빈 손목 자국 유지, 새 옷이나 변신처럼 보이지 않음`
- **PROMPT_EN**: `same charcoal shirt and narrow gray tie as episode 1, knot still loose with room for two fingers, navy trousers and shoe-style safety footwear, empty watch mark preserved, not a makeover or new wardrobe`
- **NEGATIVE**: `formal date suit, bow tie, watch, makeover hairstyle`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: ep24 전 씬 동일

## 장현숙

### CHAR-HYUNSUK-LOCK | 장현숙 정체성 잠금
- **SOURCE**: `cast-identity.md`, `costumes.md`
- **PURPOSE**: 주요 조연 외형 고정
- **LOCKS**: STYLE-MASTER
- **VARIABLES**: 사원증 방향·경보광
- **ASPECT**: 4:5 또는 9:16
- **COMPOSITION**: 수직 자세와 사원증을 한 프레임에
- **PROMPT_KO**: `화면 나이 47세의 한국 여성, 넓지 않은 각진 얼굴과 단단한 턱, 눈가에 오래 참은 피로선, 짙은 갈색의 낮고 안정된 눈, 귀 아래로 정리한 짧은 검은 머리에 관자놀이의 자연스러운 은빛 몇 가닥, 화장기 적은 실제 피부, 팔을 몸 가까이 두고 앉아도 서 있는 듯한 수직 자세, 짙은 작업 셔츠와 주머니 많은 조끼, 뒤집을 수 있는 검정 사원증 케이스`
- **PROMPT_EN**: `Korean woman, screen age 47, compact angular face and firm jaw, fine fatigue lines around steady low-set dark brown eyes, short black hair tucked below the ears with a few natural silver strands at the temples, minimally made-up real skin, arms held close and an upright posture that reads standing even while seated, dark work shirt, multi-pocket vest, reversible black ID case`
- **NEGATIVE**: `villain glamour, severe military uniform, dyed fashion hair, heavy makeup`
- **POST TEXT**: 사원증 이름은 후반 합성
- **CONTINUITY CHECK**: ep01–23 사진 면 가림 가능, ep24 정면 전환

### WARD-HYUNSUK-MASTER | 현숙 전편
- **SOURCE**: `costumes.md`
- **PURPOSE**: 팀장 의상 잠금
- **LOCKS**: CHAR-HYUNSUK-LOCK
- **VARIABLES**: 사원증 앞뒤
- **ASPECT**: 전신
- **COMPOSITION**: 셔츠와 조끼 사이 여유가 거의 없는 직선
- **PROMPT_KO**: `짙은 회청색 작업 셔츠와 몸에 맞는 먹색 다주머니 조끼, 검정 작업 바지와 낮은 안전화, 개인 장식 없음, 사원증 케이스만 손으로 뒤집을 수 있음`
- **PROMPT_EN**: `dark blue-gray work shirt, fitted charcoal multi-pocket vest, black work trousers and low safety shoes, no personal ornament, only the ID case may be turned by hand`
- **NEGATIVE**: `police uniform, executive suit, jewelry`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: 전편 동일

## 오민주

### CHAR-MINJU-LOCK | 오민주 정체성 잠금
- **SOURCE**: `cast-identity.md`, `costumes.md`
- **PURPOSE**: 주요 조연 외형 고정
- **LOCKS**: STYLE-MASTER
- **VARIABLES**: 안경천 사용·눈물
- **ASPECT**: 4:5 또는 9:16
- **COMPOSITION**: 서류 모서리·손·안경이 함께 보임
- **PROMPT_KO**: `화면 나이 29세의 한국 여성, 짧고 둥근 타원형 얼굴, 선명하지만 긴장하면 빠르게 움직이는 짙은 눈, 코끝이 작고 입술은 말하기 전 살짝 벌어짐, 턱선 길이의 짙은 갈색 단발을 귀 뒤로 한쪽만 넘김, 얇은 은테 타원 안경, 실제 피부결, 약간 큰 베이지 카디건과 짙은 하의, 종이 모서리를 정확히 맞추는 가는 손과 회색 안경천`
- **PROMPT_EN**: `Korean woman, screen age 29, short rounded oval face, clear dark eyes that move quickly under stress, small nose tip, lips parting slightly before rapid speech, chin-length dark brown bob tucked behind one ear only, thin silver oval glasses, real skin texture, slightly oversized beige cardigan over dark bottoms, slender hands aligning paper corners, gray lens cloth`
- **NEGATIVE**: `comic nerd caricature, oversized black glasses, schoolgirl styling, messy hair`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: 한쪽 귀만 드러나는 단발·은테 안경 고정, ep23 안경천 미사용

### WARD-MINJU-MASTER | 민주 전편
- **SOURCE**: `costumes.md`
- **PURPOSE**: 기록 담당 의상 잠금
- **LOCKS**: CHAR-MINJU-LOCK
- **VARIABLES**: 종이 먼지·ep23 눈물
- **ASPECT**: 전신
- **COMPOSITION**: 큰 카디건 실루엣과 종이 파일
- **PROMPT_KO**: `세탁해 보풀이 약간 생긴 베이지 카디건, 크림 셔츠, 짙은 회색 직선 바지와 낮은 검정 신발, 은테 안경과 회색 천, 종이 먼지가 어깨에 보이는 생활 상태`
- **PROMPT_EN**: `washed beige cardigan with slight pilling, cream shirt, dark gray straight trousers and low black shoes, silver glasses and gray cloth, visible paper dust on the shoulder`
- **NEGATIVE**: `preppy uniform, bright colors, fashion accessories`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: ep23 눈물은 안경에 남고 천은 손에 없음

## 기능 인물

### CHAR-SUJIN-LOCK | 김수진
- **SOURCE**: `characters.md`, `cast-identity.md`, `costumes.md`
- **PURPOSE**: ep13–14 기능 인물 고정
- **LOCKS**: STYLE-MASTER
- **VARIABLES**: 다림질·열쇠고리
- **ASPECT**: 4:5 또는 9:16
- **COMPOSITION**: 생활 노동의 손과 얼굴 동시
- **PROMPT_KO**: `화면 나이 38세의 한국 여성, 둥글고 현실적인 얼굴, 눈가에 잠이 부족한 잔주름, 검은 머리를 낮게 묶고 잔머리 몇 가닥, 화장기 적은 피부, 증기 아래 갈색으로 보이는 남색 작업 앞치마, 다림질로 단단해진 손, 기억보다 현재 아이를 먼저 보는 안정된 시선`
- **PROMPT_EN**: `Korean woman, screen age 38, grounded rounded face with fine sleep-deprived lines around the eyes, black hair tied low with a few loose strands, minimal makeup and real skin, navy work apron reading warm brown through steam, hands firm from ironing, steady gaze prioritizing her present child over a missing memory`
- **NEGATIVE**: `melodramatic victim, glamorous salon owner, tears in every shot`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: ep13–14 동일 앞치마

### CHAR-TAESIK-LOCK | 박태식
- **SOURCE**: `characters.md`, `cast-identity.md`
- **PURPOSE**: ep10 기능 인물 고정
- **LOCKS**: STYLE-MASTER
- **VARIABLES**: 영수증 묶음
- **ASPECT**: 9:16
- **COMPOSITION**: 운반 노동자의 손과 종이 묶음
- **PROMPT_KO**: `화면 나이 41세의 한국 남성, 햇빛과 야간 노동에 거칠어진 얼굴과 손, 짧은 검은 머리, 형광 안전조끼 위 낡은 남색 작업복, 불평하는 입과 결국 도와주는 눈, 열전사 영수증 묶음을 한 손에 쥠`
- **PROMPT_EN**: `Korean man, screen age 41, face and hands weathered by daylight and night-shift labor, short black hair, worn navy workwear under a reflective safety vest, complaining mouth with helpful eyes, holding a bundle of faded thermal receipts`
- **NEGATIVE**: `comic buffoon, construction helmet indoors, brand logo`
- **POST TEXT**: 영수증 글자는 후반 합성
- **CONTINUITY CHECK**: ep10 단일 등장

### CHAR-MINSEOK-LOCK | 민석
- **SOURCE**: `script ep01–02`, `cast-identity.md`
- **PURPOSE**: 호텔 의뢰인 고정
- **LOCKS**: STYLE-MASTER
- **VARIABLES**: 턱시도·새벽 현실 복장
- **ASPECT**: 9:16
- **COMPOSITION**: 혼란스러운 신랑의 얼굴과 휴대폰
- **PROMPT_KO**: `30대 초반 한국 남성, 단정하지만 잠을 못 잔 얼굴, 버려진 시간에서는 약간 구겨진 검정 턱시도와 풀린 나비넥타이, 현실 새벽에는 셔츠 소매를 걷은 상태, 사람 얼굴을 잘 기억하지만 자기 사진 폴더의 오류에 당황한 시선`
- **PROMPT_EN**: `Korean man in his early thirties, neat but sleep-deprived face; in discarded time, slightly creased black tuxedo with loosened bow tie; in present dawn, shirt sleeves rolled up; observant eyes that remember faces but are confused by corrupted photo slots on his phone`
- **NEGATIVE**: `luxury wedding ad, perfect tuxedo, drunken caricature`
- **POST TEXT**: 휴대폰 UI는 후반 합성
- **CONTINUITY CHECK**: ep01 잔시 턱시도, ep02 현실 셔츠

### CHAR-CHILD-LOCK | 수진의 아이
- **SOURCE**: `script ep13`, `cast-identity.md`
- **PURPOSE**: ep13 기능 인물 고정
- **LOCKS**: STYLE-MASTER
- **VARIABLES**: 교복·열쇠고리
- **ASPECT**: 9:16
- **COMPOSITION**: 성인 허리 아래 높이의 자연스러운 시선
- **PROMPT_KO**: `초등학교 저학년 한국 아이, 생활 주름이 있는 깨끗한 교복과 이름표용 빈 영역, 과장된 아역 표정 없이 어른들이 당연히 아는 사실을 말하는 눈, 작은 손에 낡은 열쇠고리`
- **PROMPT_EN**: `young Korean elementary-school child in a clean but lived-in school uniform with a blank name-tag area, natural matter-of-fact gaze without exaggerated child-actor expression, small hand holding a worn key ring`
- **NEGATIVE**: `adult styling, glamour makeup, oversized emotional tears`
- **POST TEXT**: 이름표는 후반 합성
- **CONTINUITY CHECK**: ep13 동일 교복

---

<!-- SOURCE: 06_visual_prompts/02_location-prompts.md -->

# 《없던 사이》 배경·로케이션 생성 프롬프트 v1
> 빈 공간 마스터 우선 · 인물은 키프레임 단계에서 합성

### LOC-CENTER-SORT | 잔시물 관리센터 분류실
- **SOURCE**: `locations.md L-01`, ep01·02·06·08·09·18·20
- **PURPOSE**: 중심 세트 마스터
- **LOCKS**: STYLE-MASTER, LIGHT-CENTER-NIGHT, CAM-VERTICAL-MASTER
- **VARIABLES**: 세척대·사물함·봉인실·빨간 분리선·시간대
- **ASPECT**: 9:16
- **COMPOSITION**: 전경 젖은 세척대, 중경 작업 통로, 후경 금속 선반과 반투명 봉인실
- **PROMPT_KO**: `서울 외곽 폐기물 집하장 지하의 준공공기관 시간 폐기물 분류실, 낮은 콘크리트 천장과 오래된 4300K 형광등, 산화된 청록 금속 선반, 물 얼룩이 층층이 남은 스테인리스 세척대, 검은 태그와 봉인 테이프, 뒤편 반투명 비닐 봉인실, 한쪽 벽의 회색 사물함과 오래된 자판기, 젖은 콘크리트 바닥의 생활 오염, 세로 화면 중앙에 두 사람이 마주 설 한 사람 폭 통로, 사람 없는 빈 세트 기준`
- **PROMPT_EN**: `empty master set of a quasi-public discarded-time sorting room beneath a waste depot outside Seoul, low concrete ceiling, aging 4300K fluorescent tubes, oxidized teal metal shelves, stainless wash table layered with old water marks, black tags and sealing tape, translucent plastic quarantine booth in back, gray lockers and an old vending machine along one wall, lived-in wet concrete floor, a one-person-wide central aisle designed for two adults facing in depth, vertical 9:16`
- **NEGATIVE**: `NEG-GLOBAL, neon laboratory, futuristic spaceship, pristine hospital, large open warehouse`
- **POST TEXT**: 표지판·라벨·자판기 버튼은 후반 합성
- **CONTINUITY CHECK**: 선반·세척대·사물함·자판기 위치 전편 고정

### LOC-CENTER-ADMIN | 센터 행정·기록 구역
- **SOURCE**: ep02 기록실 앞, ep04 보안실, ep11–12 기록창고·팀장실, ep19 격리 복도, ep20–21 시스템실
- **PURPOSE**: 센터 행정 구역 부모 마스터
- **LOCKS**: STYLE-MASTER, LIGHT-CENTER-NIGHT
- **VARIABLES**: `SECURITY`, `RECORDS`, `TEAMOFFICE`, `ISOLATION`, `SYSTEM`
- **ASPECT**: 9:16
- **COMPOSITION**: 좁은 복도와 세로 문틀, 각 변형은 동일 회색 벽체·청록 문틀 공유
- **PROMPT_KO**: `같은 지하 관리센터의 행정 구역, 회색 방염벽과 산화된 청록 철제 문틀, 낮은 형광등, 사람 두 명이 비켜 지나기 어려운 복도. SECURITY 변형은 구형 CCTV 모니터와 스크래치 난 조작대, RECORDS는 붉은 면사로 묶인 종이 상자가 빽빽한 한 사람 폭 서가, TEAMOFFICE는 개인 물건 없는 금속 책상과 뒤집힌 사원증, ISOLATION은 손자국이 잘 남는 투명 유리벽, SYSTEM은 오래된 검정 모니터와 손글씨 메모가 붙은 랙. 모든 변형은 같은 기관 건축으로 연결`
- **PROMPT_EN**: `administrative zone of the same underground center, gray fireproof walls, oxidized teal steel door frames, low fluorescent ceiling and corridors too narrow for two people to pass comfortably. SECURITY variant: old CCTV monitors and scratched console. RECORDS: one-person-wide shelves packed with paper boxes tied in red thread. TEAMOFFICE: bare metal desk and reversible ID case. ISOLATION: transparent glass wall that catches handprints. SYSTEM: aging black monitors and handwritten notes on equipment racks. All variants share the same institutional architecture`
- **NEGATIVE**: `modern tech campus, glass corporate office, endless archive fantasy, police interrogation room`
- **POST TEXT**: 모니터 UI·문서 표지는 후반 합성
- **CONTINUITY CHECK**: 회색 벽·청록 문틀·형광등 사양 공통

### LOC-CENTER-INDUSTRIAL | 장비·하역·소각 구역
- **SOURCE**: ep06 장비실, ep10 하역장, ep23–24 소각실, ep24 출입구
- **PURPOSE**: 산업 구역 부모 마스터
- **LOCKS**: STYLE-MASTER, LIGHT-CENTER-NIGHT
- **VARIABLES**: `EQUIP`, `LOADING`, `INCINERATOR`, `EXIT`
- **ASPECT**: 9:16
- **COMPOSITION**: 굵은 배관과 안전선이 세로축을 만들고 중앙 작업대 확보
- **PROMPT_KO**: `관리센터의 산업 구역, 굵은 회색 배관과 노란 안전선, 긁힌 철제 캐비닛과 낮은 하역 도크. EQUIP에는 휴대 반출기와 방수 장갑 선반, LOADING에는 기둥과 수레와 종이 영수증이 놓일 작업대, INCINERATOR에는 불꽃 대신 고온 백색광이 새는 투명 소각 상자와 동시에 눌러야 하는 두 버튼, EXIT에는 낡은 철문 너머 처음 들어오는 아침빛. 먼지와 사용감은 있으나 폐허가 아님`
- **PROMPT_EN**: `industrial zone of the center with thick gray pipes, yellow safety lines, scratched steel cabinets and a low loading dock. EQUIP variant has portable extraction devices and waterproof-glove racks. LOADING has concrete columns, carts and a worktable for paper receipts. INCINERATOR has a transparent disposal chamber emitting high-temperature white light rather than flames, with two simultaneous buttons. EXIT opens through an old steel door to the first morning light. Used and dusty, never derelict`
- **NEGATIVE**: `furnace flames, sci-fi reactor, abandoned factory, luxury machinery`
- **POST TEXT**: 안전 표지·버튼 문구는 후반 합성
- **CONTINUITY CHECK**: 소각실 상자·두 버튼 위치 ep23–24 동일

### LOC-ACCIDENT-CORE | 고밀도 잔시 발생실
- **SOURCE**: `locations.md L-04`, ep17–18
- **PURPOSE**: 사고 회상 중심 세트
- **LOCKS**: STYLE-MASTER, GRADE-ARC-MASTER
- **VARIABLES**: 경보·코어 안정도·43개 모니터 상태
- **ASPECT**: 9:16
- **COMPOSITION**: 중앙 코어, 좌우 동의 단말기, 후경에 세로 모니터 43개를 밀도감 있게 배열
- **PROMPT_KO**: `준공공기관 지하의 고밀도 시간 폐기 사고실, 벽 전체를 채우는 좁은 세로 모니터 43개, 중앙의 산업용 냉각 코어는 기계적이고 무정하며 붉은 경보등이 회전, 바닥의 붉은 안전선과 두 개의 손바닥 동의 단말기, 관찰자를 가르는 투명 경계, 낡은 냉각 호스와 실제 작업 흔적, 판타지 제단이 아닌 위험한 공공 설비`
- **PROMPT_EN**: `high-density discarded-time accident chamber in a public-service underground facility, forty-three narrow vertical monitors densely covering the back wall, an industrial cooling core at center, mechanical and indifferent, rotating red alarm light, red safety lines on the floor, two palm-consent terminals and a transparent observation boundary, worn cooling hoses and real work traces, dangerous civic infrastructure rather than a fantasy altar`
- **NEGATIVE**: `magic temple, glowing fantasy crystal, spaceship bridge, gore`
- **POST TEXT**: 43명 얼굴·안정도·동의 UI는 후반 합성
- **CONTINUITY CHECK**: ep17 붉은 경보 → ep18 얼굴 회복, 구조는 동일

### LOC-HOTEL-807 | 호텔 807호·복도·로비
- **SOURCE**: `locations.md L-03`, ep01·02·21·22
- **PURPOSE**: 호텔 부모 마스터
- **LOCKS**: STYLE-MASTER
- **VARIABLES**: `ROOM`, `CORRIDOR`, `LOBBY`, `ELEVATOR`, `VENDING`, 잔시/현실
- **ASPECT**: 9:16
- **COMPOSITION**: ROOM은 침대–거울–옷장 세로축, CORRIDOR는 긴 소실점
- **PROMPT_KO**: `오래된 중급 비즈니스 호텔, ROOM 807은 습기를 먹어 들뜬 값싼 금색 벽지, 한쪽만 켜지는 침대등, 침대 아래가 거울에 먼저 보이고 옷장 문을 열면 두 사람이 겹쳐 설 수 있는 좁은 구조. CORRIDOR는 발소리를 삼키는 어두운 카펫과 얼룩진 금색 객실 번호, LOBBY는 낡은 대리석과 새벽의 빈 접수대, VENDING은 라벤더 음료 버튼이 있는 차가운 흰빛 자판기, ELEVATOR는 좁은 금속 벽. 잔시일 때만 젖은 표면과 약한 자주색 가장자리`
- **PROMPT_EN**: `aging mid-range business hotel. ROOM 807 has cheap gold wallpaper lifted by humidity, only one bedside lamp working, a mirror that reveals the space beneath the bed first, and a narrow wardrobe axis that forces two adults into depth. CORRIDOR has dark sound-absorbing carpet and stained gold room numbers. LOBBY uses worn stone and an empty dawn desk. VENDING has a cold white machine with a lavender-drink button. ELEVATOR has narrow metal walls. Only the discarded-time variant adds wet surfaces and faint magenta edges`
- **NEGATIVE**: `luxury honeymoon suite, red romantic lighting, spotless boutique hotel, erotic bedroom`
- **POST TEXT**: 객실 번호·자판기 라벨·휴대폰 UI는 후반 합성
- **CONTINUITY CHECK**: 금색 벽지·침대·거울·옷장 위치 ep01·21·22 고정

### LOC-OFFICE-ELEVATOR | 오피스 엘리베이터 잔시
- **SOURCE**: ep03, `locations.md`
- **PURPOSE**: 반복·거울 장면 배경
- **LOCKS**: LIGHT-RESIDUAL-TIME, CAM-VERTICAL-MASTER
- **VARIABLES**: 급정지·천장 점검구·거울 과거 투영
- **ASPECT**: 9:16
- **COMPOSITION**: 세 면 거울과 낮은 천장, 두 인물의 전후 반사가 반복
- **PROMPT_KO**: `비에 젖은 회사 엘리베이터 내부, 세 면의 오래된 거울 스테인리스, 낮은 천장 점검구, 바닥의 얇은 빗물과 손잡이의 흐린 립스틱 자국, 37초 반복은 유령이 아니라 반사 프레임이 몇 픽셀 어긋난 모습, 두 사람이 나란히 서기보다 한 명이 다른 사람 앞에 겹치는 좁은 깊이`
- **PROMPT_EN**: `rain-wet office elevator interior, aging mirrored stainless steel on three sides, low ceiling service hatch, a thin layer of rainwater on the floor and a faint lipstick mark on the rail, the thirty-seven-second loop shown as reflections offset by a few pixels rather than ghosts, narrow depth layering one adult in front of the other`
- **NEGATIVE**: `luxury elevator, horror ghost, infinite mirror fantasy, nightclub light`
- **POST TEXT**: 층수 UI는 후반 합성
- **CONTINUITY CHECK**: ep03 세 씬 거울·점검구·물 위치 동일

### LOC-CHAT-RESIDUAL | 채팅방 음성 파형 잔시
- **SOURCE**: ep05
- **PURPOSE**: 추상 잔시 배경
- **LOCKS**: STYLE-MASTER, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 파형 밀도·삭제 카운트
- **ASPECT**: 9:16
- **COMPOSITION**: 검은 공간이 아니라 실제 센터 채팅방 잔상이 세로 파형 사이로 보임
- **PROMPT_KO**: `현실의 사무실 구조가 희미하게 남아 있는 버려진 음성 메시지 공간, 거대한 자주색 음성 파형이 투명한 벽처럼 세로로 서고 28초마다 간격이 좁아짐, 파형은 빛 입자가 아니라 얇은 유리 리본 같은 물성, 두 사람이 겨우 통과할 폭, 삭제 버튼과 카운트다운 자리는 빈 그래픽 영역으로 확보`
- **PROMPT_EN**: `discarded voice-message space retaining a faint real office structure, giant muted-magenta audio waveforms standing vertically like translucent glass ribbons and narrowing every twenty-eight seconds, tangible rather than particle effects, barely enough width for two adults to pass, clean blank graphic areas reserved for the delete control and countdown`
- **NEGATIVE**: `cyberspace grid, matrix code, concert waveform, floating readable text`
- **POST TEXT**: 음성 메시지·카운트다운은 후반 합성
- **CONTINUITY CHECK**: ep05 파형은 동일 재질, 씬 진행에 따라 간격만 축소

### LOC-MOTEL-ROOM | 모텔방 잔시
- **SOURCE**: ep07, `locations.md`
- **PURPOSE**: 한 침대 안전지대
- **LOCKS**: LIGHT-RESIDUAL-TIME, RATING-15-CONSENT
- **VARIABLES**: 검은 비 침범 범위
- **ASPECT**: 9:16
- **COMPOSITION**: 하단 싱글 침대, 위쪽 벽을 타고 내려오는 검은 비
- **PROMPT_KO**: `퇴색한 벽지와 고장 난 비상등이 있는 값싼 모텔방, 선정적 장식 없이 싱글 침대 하나만 마른 안전지대, 천장과 벽에서 잉크처럼 검은 비가 흘러 바닥을 덮고 침대 가장자리를 서서히 잠식, 매트리스가 중앙으로 약간 꺼져 두 사람이 가까워지는 물리적 이유, 침대 아래 작은 공간`
- **PROMPT_EN**: `cheap motel room with faded wallpaper and a broken emergency lamp, no erotic decor, a single bed as the only dry safe zone, ink-black rain running down ceiling and walls to cover the floor and slowly reach the mattress edge, mattress dipping toward the center to create a physical reason for proximity, narrow space beneath the bed`
- **NEGATIVE**: `red satin, mirrors over bed, nudity, horror blood rain`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: 검은 비는 S1 바닥 → S3 침대 가장자리 순으로 전진

### LOC-FOOD-TENT | 100일 포장마차
- **SOURCE**: ep08
- **PURPOSE**: 과거 100일 데이트
- **LOCKS**: STYLE-MASTER, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 내부·뒤편 빗길
- **ASPECT**: 9:16
- **COMPOSITION**: 김 오른 비닐막이 과거·현재를 전후 층으로 분리
- **PROMPT_KO**: `서울 골목의 작은 포장마차, 주황색 텅스텐 전구와 김 오른 투명 비닐막, 긁힌 스테인리스 원형 테이블과 서로 다른 플라스틱 의자, 비닐막 앞 현재 인물과 뒤쪽 과거 인물을 깊이로 겹칠 수 있는 구조, 뒤편은 젖은 아스팔트와 약한 빗소리, 낭만적 장식보다 생활감`
- **PROMPT_EN**: `small Seoul street food tent with warm tungsten bulbs, steamed transparent plastic walls, scratched stainless round table and mismatched plastic stools, depth designed to layer present figures before the plastic and past figures behind it, wet asphalt in back, everyday wear rather than romantic decoration`
- **NEGATIVE**: `festival lanterns, luxury restaurant, nostalgic sepia filter`
- **POST TEXT**: 간판 글자는 후반 합성
- **CONTINUITY CHECK**: ep08 내외부 동일 주황 전구·비닐막

### LOC-LAUNDROMAT | 김수진의 세탁소
- **SOURCE**: `locations.md`, ep13–14
- **PURPOSE**: 현재 삶의 윤리적 기준 공간
- **LOCKS**: STYLE-MASTER, GRADE-ARC-MASTER
- **VARIABLES**: 작업실·뒷방·가게 앞
- **ASPECT**: 9:16
- **COMPOSITION**: 전경 다리미와 증기, 중경 수진, 후경 아이 교복
- **PROMPT_KO**: `동네 골목의 작은 수선 세탁소, 오래된 스팀다리미와 천장까지 걸린 비닐 포장 옷, 따뜻한 다림질 증기가 남색 앞치마를 갈색으로 보이게 함, 뒷방에는 낮은 탁자와 아이 교복, 가게 앞에는 생활 자전거와 바랜 차양, 과거보다 오늘의 노동이 무겁게 보이는 현실적 공간`
- **PROMPT_EN**: `small neighborhood alteration laundry, aging steam iron, plastic-wrapped clothes hanging to the ceiling, warm ironing steam turning a navy apron visually brown, back room with a low table and a child's school uniform, storefront with a practical bicycle and faded awning, grounded space where present labor feels heavier than missing history`
- **NEGATIVE**: `self-service laundromat rows, fashionable atelier, excessive cozy decor`
- **POST TEXT**: 상호·이름표는 후반 합성
- **CONTINUITY CHECK**: ep13–14 다리미·교복·차양 위치 고정

### LOC-ROOFTOP | 첫 키스 옥상 잔시
- **SOURCE**: ep15
- **PURPOSE**: 과거·현재 접촉선 비교
- **LOCKS**: LIGHT-RESIDUAL-TIME, RATING-15-CONSENT
- **VARIABLES**: 물탱크 뒤·출입문·열쇠 낙하
- **ASPECT**: 9:16
- **COMPOSITION**: 물탱크와 출입문 사이 한 걸음 공간, 과거는 후경·현재는 전경
- **PROMPT_KO**: `서울의 평범한 상업건물 옥상 밤, 낡은 원통형 물탱크와 회색 철제 출입문, 낮은 난간과 멀리 흐린 도시 불빛, 물탱크와 문 사이 정확히 한 걸음 폭의 그늘, 전경 현재 두 사람과 후경 과거 두 사람을 겹칠 수 있는 깊이, 바닥의 작은 집 열쇠가 측광을 받음`
- **PROMPT_EN**: `ordinary commercial-building rooftop in Seoul at night, aging cylindrical water tank, gray steel access door, low parapet and soft distant city lights, exactly one step of shadow between tank and door, depth for present couple in front and past couple behind, a small house key catching edge light on the floor`
- **NEGATIVE**: `skyscraper glamour, rooftop garden, fireworks, dangerous ledge pose`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: ep15 세 씬 동일 동선, 열쇠는 S3에서만 바닥

### LOC-SEOHA-HOME | 서하의 집 잔시
- **SOURCE**: ep16, `locations.md`
- **PURPOSE**: 사람 없는 친밀감 공간
- **LOCKS**: STYLE-MASTER, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 현관·부엌·침실 문·식탁
- **ASPECT**: 9:16
- **COMPOSITION**: 하단 신발·컵·셔츠, 문틀로 깊이 구성
- **PROMPT_KO**: `혼자 사는 직장인의 작고 정돈된 서울 원룸형 집, 현관의 남자 구두와 여자 안전화가 엇갈리고, 나무 식탁에 서로 다른 머그 두 개, 소파 팔걸이의 회청색 남자 셔츠, 욕실 거울의 손가락 자국용 빈 영역, 반쯤 열린 침실 문 너머 흐트러진 이불, 새 가구보다 오래 관리한 면·나무·도자기 질감, 사람 없이도 두 사람의 동선이 읽힘`
- **PROMPT_EN**: `small carefully maintained Seoul studio apartment of a person living alone, men's dress shoes crossed with women's safety shoes at the entry, two mismatched mugs on a wooden table, faded blue-gray men's shirt over the sofa arm, blank finger-written area on the bathroom mirror, half-open bedroom door revealing disturbed bedding, long-kept cotton, wood and ceramic rather than new furniture, two people's routines legible even when empty`
- **NEGATIVE**: `luxury apartment, erotic bedroom, messy hoarder room, readable generated handwriting`
- **POST TEXT**: 거울 `늦음`, 쪽지 문구와 `02:17`은 후반 합성
- **CONTINUITY CHECK**: 셔츠·컵·신발·단추 위치 ep16 내 유지

### LOC-BUS-STOP | 버스 정류장 잔시
- **SOURCE**: ep20
- **PURPOSE**: 분리와 기다림 배경
- **LOCKS**: STYLE-MASTER, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 간판 낙하·맨홀·벤치 빈자리
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 정류장 기둥, 중앙 빈 좌석 하나, 앞뒤로 분리된 두 인물
- **PROMPT_KO**: `비가 그친 서울 외곽 버스 정류장 밤, 젖은 아스팔트와 낡은 투명 아크릴 벽, 형광 노선표용 빈 영역, 세 칸 벤치 중앙 한 자리만 비어 있고 양끝에 성인이 앉을 구조, 위쪽 느슨한 광고 간판과 앞쪽 열린 맨홀, 반복 속 노인의 빈자리 습관이 배경에 남음`
- **PROMPT_EN**: `bus stop on the outskirts of Seoul after rain at night, wet asphalt, worn transparent acrylic walls, blank fluorescent route-map area, three-seat bench with exactly the center seat empty and room for adults at both ends, loose advertising sign above and an open manhole in front, an elderly man's repeated habit of preserving an empty seat in the background`
- **NEGATIVE**: `romantic bus-stop advertisement, heavy rain, crowded city center`
- **POST TEXT**: 노선표·광고 문구는 후반 합성
- **CONTINUITY CHECK**: ep20 S2–3 중앙 빈자리 유지

### LOC-CAFE-ALLEY | 현재형 카페와 골목
- **SOURCE**: `locations.md L-06`, ep24
- **PURPOSE**: 결말 현실 공간
- **LOCKS**: STYLE-MASTER, LIGHT-PRESENT-MORNING
- **VARIABLES**: 카페 내부·문밖·골목
- **ASPECT**: 9:16
- **COMPOSITION**: 작은 원형 테이블과 한 사람 폭 햇빛, 출근 인파는 후경 흐림
- **PROMPT_KO**: `서울 출근길의 작고 평범한 카페, 세로 통유리 한 칸 안에 둘만 앉으면 꽉 차는 나무 원형 테이블, 유약 흠집이 서로 다른 도자기 컵 두 개, 과거를 암시하는 소품 없음, 문밖 골목은 배송 상자와 실외기 사이로 한 사람 폭의 옅은 호박색 아침 햇빛, 후경 출근 인파는 현실적으로 흐르고 두 사람은 그 반대 방향으로 걸을 수 있음`
- **PROMPT_EN**: `small ordinary cafe on a Seoul commute route, a wooden round table filling one vertical window bay when two adults sit, two ceramic cups with different glaze flaws, no props from the past, outside alley with delivery boxes and air-conditioning units and a one-person-wide band of pale amber morning sun, commuting crowd moving softly in the background while the couple can walk the opposite direction`
- **NEGATIVE**: `luxury date cafe, flower wall, wedding mood, empty fantasy street`
- **POST TEXT**: 카페 메뉴·도로 문구는 후반 합성
- **CONTINUITY CHECK**: ep24 S3–5 같은 아침빛 방향

### LOC-SEOUL-MONTAGE | 43명 서울 몽타주
- **SOURCE**: ep13 S#1
- **PURPOSE**: 43명의 현재 삶 몽타주 배경
- **LOCKS**: STYLE-MASTER, GRADE-ARC-MASTER
- **VARIABLES**: 등굣길·버스·병원·시장·아파트
- **ASPECT**: 9:16 다중 컷
- **COMPOSITION**: 한 프레임에 군중 43명을 넣지 않고 4–6개 생활 조각으로 분할
- **PROMPT_KO**: `서울의 평범한 낮 생활을 4~6개의 세로 조각으로 구성, 등굣길에서 아이 손을 잡는 보호자, 버스 운전석, 병원 복도, 재래시장 작업대, 오래된 아파트 현관, 각 조각은 실제 노동과 가족 행동 하나만 담고 얼굴은 과장된 슬픔 없이 현재에 집중, 명단 숫자는 이미지 밖 후반 그래픽으로 분리`
- **PROMPT_EN**: `four to six vertical fragments of ordinary daytime life in Seoul: guardian holding a child's hand on the school route, city-bus driver's seat, hospital corridor, traditional market worktable, older apartment entry; each fragment contains one grounded act of work or family life, faces focused on the present without exaggerated sorrow; the list and numbers remain post-production graphics outside the generated image`
- **NEGATIVE**: `single crowd of 43 posed people, disaster montage, sentimental commercial`
- **POST TEXT**: 43개 이름·숫자는 후반 합성
- **CONTINUITY CHECK**: ep13 S1에서만 사용, 김수진 세탁소로 자연스럽게 연결

---

<!-- SOURCE: 06_visual_prompts/03_prop-prompts.md -->

# 《없던 사이》 소품 마스터 프롬프트

> 모든 문자·숫자·서명은 생성 단계에서 비워 두고 `POST TEXT` 지시에 따라 후반 합성한다. 소품의 흠집, 젖음, 밀봉, 혈흔 등 상태 변화는 연속성 정보다.

### PROP-PHOTO-WET | 젖은 커플 사진

- **SOURCE**: 01_script 전반, 04_design/props.md 1번
- **PURPOSE**: 두 사람이 실제로 연인이었다는 최초의 물증
- **LOCKS**: STYLE-MASTER, CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK
- **VARIABLES**: 젖음 정도, 손에 들린 방향, 봉투 수납 여부
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙의 작은 인화 사진, 사진을 쥔 손과 번진 표면을 함께 클로즈업
- **PROMPT_KO**: 9:16 실사 한국 미스터리 로맨스 소품 사진. 오래된 무광 4x6 인화지, 빗물과 오염수에 젖어 가장자리가 말리고 표면 유제가 부분적으로 번졌다. 사진 안에는 CHAR-SEOHA-LOCK과 CHAR-DOYUN-LOCK의 동일한 얼굴을 가진 두 사람이 과거의 자연스러운 연인 거리에서 어깨를 맞대고 있으나 선정적 포즈는 없다. 현재 장면에서는 작업 장갑 또는 맨손이 사진 모서리를 조심스럽게 쥔다. 얼굴은 식별 가능하되 손상 흔적이 분명하고, 종이 섬유와 물방울이 사실적이다. 사진 속 글자와 날짜는 비워 둔다.
- **PROMPT_EN**: Vertical 9:16 live-action Korean mystery-romance prop shot. A worn matte 4x6 print, soaked by rain and dirty water, curled edges and partially bloomed emulsion. Inside the print, the exact locked identities CHAR-SEOHA-LOCK and CHAR-DOYUN-LOCK stand shoulder-to-shoulder with the natural proximity of former lovers, never a suggestive pose. In the present scene, a work glove or bare hand carefully holds one corner. Both faces remain recognizable while water damage, paper fibers and droplets feel physically real. Leave all dates and writing blank for post.
- **NEGATIVE**: NEG-GLOBAL, NEG-CHARACTER, NEG-TEXT, glossy new photo, illegible faces, different actors, wedding photo, explicit intimacy
- **POST TEXT**: 필요한 회차에서만 사진 뒷면 날짜 또는 분류 번호를 별도 레이어로 합성
- **CONTINUITY CHECK**: 사진 속 얼굴·의상·구도는 전 회차 동일, 젖음은 발견 직후 가장 심하고 이후 건조 상태로만 감소

### PROP-PHOTO-DRY | 건조·보존된 커플 사진

- **SOURCE**: PROP-PHOTO-WET의 후속 상태
- **PURPOSE**: 증거 보관과 감정 변화의 연속성 유지
- **LOCKS**: PROP-PHOTO-WET
- **VARIABLES**: 투명 보존 봉투, 증거 테이블, 손의 주인
- **ASPECT**: 9:16
- **COMPOSITION**: 투명 봉투 안 사진과 손가락 끝, 봉투 반사를 피한 상단 30도 시점
- **PROMPT_KO**: PROP-PHOTO-WET과 완전히 같은 사진이 자연 건조되어 물결 모양으로 휘고 얼룩 경계가 굳어진 상태. 무산성 투명 보존 봉투 안에 넣으며 새것처럼 복원하지 않는다. 사진 속 두 얼굴과 어깨 구도, 손상 위치를 정확히 고정한다. 봉투 라벨 영역은 비워 둔다. 9:16 세로 클로즈업, 차가운 관리센터 조명, 손가락과 사진을 동시에 선명하게.
- **PROMPT_EN**: The exact same image and damage map as PROP-PHOTO-WET, now naturally dried, wavy and fixed with tide marks, sealed inside a clear archival sleeve. Never restore it to new condition. Lock both faces, shoulder arrangement and every damaged area. Keep the label field blank. Vertical 9:16 close-up under cool center lighting, with fingertips and the print simultaneously readable.
- **NEGATIVE**: NEG-GLOBAL, NEG-CHARACTER, NEG-TEXT, repaired photo, changed pose, changed crop, new stains
- **POST TEXT**: 보존 봉투 분류번호는 후반 합성
- **CONTINUITY CHECK**: PROP-PHOTO-WET의 손상 위치와 이미지 내용 1:1 유지

### PROP-WATCH-RESIDUAL | 100일 기념 손목시계

- **SOURCE**: 100일 기억 및 잔여 시간 장면
- **PURPOSE**: 사랑의 사적 기억과 버려진 시간의 연결 매개
- **LOCKS**: STYLE-MASTER, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 착용 손목, 정지 시각, 잔여 시간 입자 강도
- **ASPECT**: 9:16
- **COMPOSITION**: 손목과 시계면을 화면 중앙, 다른 인물의 손끝은 프레임 가장자리
- **PROMPT_KO**: 과장되지 않은 중가형 아날로그 손목시계, 얇은 은색 케이스와 짙은 갈색 가죽 스트랩, 사용감 있는 미세 흠집. 특별한 각인이나 브랜드 로고는 없다. 잔여 시간에서는 시계 유리 가장자리와 초침 주변에만 절제된 마젠타-보랏빛 굴절이 얇게 맺힌다. 실제 물체처럼 무게와 반사가 느껴지는 9:16 매크로 클로즈업, 피부와 손가락의 자연스러운 질감.
- **PROMPT_EN**: A restrained mid-range analog wristwatch with a slim silver case, dark brown leather strap and fine wear scratches, no branding or engraving. In residual time only, a thin controlled magenta-violet refraction clings to the glass rim and second hand. Vertical 9:16 macro close-up with believable weight, reflections, natural skin and fingertips.
- **NEGATIVE**: NEG-GLOBAL, NEG-TEXT, luxury logo, smartwatch, fantasy magic aura, oversized glow, changed strap color
- **POST TEXT**: 시계 시각이 서사상 필요할 경우 바늘 위치만 후반 조정
- **CONTINUITY CHECK**: 은색 케이스·갈색 스트랩·흠집 지도 고정, 잔여 시간 밖에서는 발광 없음

### PROP-SHIRT-FOUND | 도윤의 셔츠와 떨어진 단추

- **SOURCE**: 사고 기억과 물증 장면
- **PURPOSE**: 과거 사고의 신체적 흔적과 도윤의 정체 확인
- **LOCKS**: CHAR-DOYUN-LOCK, WARD-DOYUN-A3
- **VARIABLES**: 혈흔 농도, 젖음, 단추 분리 여부
- **ASPECT**: 9:16
- **COMPOSITION**: 구겨진 셔츠 앞섶과 비어 있는 단추 자리, 별도 단추를 같은 초점면에 배치
- **PROMPT_KO**: WARD-DOYUN-A3 계열의 옅은 회청색 남성 셔츠, 사고로 젖고 구겨졌으며 앞섶 한 곳의 단추가 뜯겨 실밥이 남아 있다. 혈흔은 검붉게 마른 제한된 면적만 보이고 상처나 신체 훼손은 묘사하지 않는다. 떨어진 무광 자개 단추 하나가 가까이에 놓인다. 9:16 증거물 클로즈업, 섬유·실밥·물기·마른 얼룩이 사실적이며 선정적 폭력은 없다.
- **PROMPT_EN**: A pale blue-gray men’s shirt from the WARD-DOYUN-A3 family, wet and creased from an accident, with one front button torn away and loose threads remaining. A limited dark dried blood stain appears without wounds or bodily injury. One detached matte mother-of-pearl button rests nearby. Vertical 9:16 evidence close-up with realistic fibers, threads, moisture and dried staining, never graphic.
- **NEGATIVE**: NEG-GLOBAL, NEG-RATING, gore, open wound, excessive blood, different shirt color, multiple missing buttons, brand logo
- **POST TEXT**: 증거번호는 별도 카드 레이어로 합성
- **CONTINUITY CHECK**: 빠진 단추 위치·혈흔 모양·셔츠 색상 고정

### PROP-RECEIPTS | 두 사람의 영수증 묶음

- **SOURCE**: 관계 추적 몽타주 및 기록실 장면
- **PURPOSE**: 평범한 데이트의 시간·장소를 복원하는 생활 증거
- **LOCKS**: STYLE-MASTER, NEG-TEXT
- **VARIABLES**: 펼친 수량, 접힘, 봉투 수납
- **ASPECT**: 9:16
- **COMPOSITION**: 서로 다른 길이의 감열지 영수증 4~7장을 손과 함께 세로로 겹쳐 배치
- **PROMPT_KO**: 오래 보관되어 가장자리가 누렇게 변하고 접힌 한국 감열지 영수증 여러 장. 카페, 분식집, 버스 충전 같은 서로 다른 생활 흔적을 암시하되 상호·날짜·금액·주소 영역은 모두 비어 있거나 무의미한 회색 블록으로 남긴다. 종이 두께, 바랜 잉크 영역, 손때가 사실적인 9:16 탑뷰 소품 컷.
- **PROMPT_EN**: Several aged Korean thermal-paper receipts with yellowed edges, folds and handling wear. Their layouts suggest a café, snack shop and transit top-up, while every merchant name, date, price and address field stays blank or as neutral gray placeholders. Vertical 9:16 top-down prop shot with realistic paper thickness, faded print zones and fingerprints.
- **NEGATIVE**: NEG-GLOBAL, NEG-TEXT, readable fake language, duplicated receipt, modern pristine paper, floating paper
- **POST TEXT**: 확정된 회차·장소·금액을 한국어 벡터 텍스트로 후반 합성
- **CONTINUITY CHECK**: 같은 영수증 재등장 시 접힘·얼룩·크기와 후반 텍스트 유지

### PROP-AUDIO-TRACK | 음성 기억 유리 실린더

- **SOURCE**: 기억 보관 시스템 장면
- **PURPOSE**: 지워진 목소리가 물리적으로 보존된 세계관 핵심 소품
- **LOCKS**: STYLE-MASTER, LIGHT-CENTER-NIGHT, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 활성/비활성, 손에 든 상태, 보관 슬롯
- **ASPECT**: 9:16
- **COMPOSITION**: 손바닥 길이의 유리 실린더를 세로 중심축에 두고 내부 파형은 얇게
- **PROMPT_KO**: 손바닥 길이의 투명 유리 실린더, 양끝은 무광 알루미늄 캡, 내부에는 물질처럼 응축된 가느다란 음성 파형이 떠 있다. 비활성일 때는 회백색, 재생 직전에는 절제된 마젠타-보랏빛 한 줄만 점등된다. 라벨과 UI 문자는 비워 둔다. 9:16 실사 매크로, 차가운 연구시설 반사와 손 피부의 따뜻함을 대비한다.
- **PROMPT_EN**: A palm-length transparent glass cylinder with matte aluminum end caps. A thin voice waveform floats inside as condensed matter: gray-white when inactive, with only one restrained magenta-violet line before playback. Leave label and UI text blank. Vertical 9:16 live-action macro contrasting cool laboratory reflections with warm human skin.
- **NEGATIVE**: NEG-GLOBAL, NEG-TEXT, fantasy potion, neon tube, oversized hologram, liquid spill, extra caps
- **POST TEXT**: 소유자명·트랙번호·파형 시간은 UI 레이어로 합성
- **CONTINUITY CHECK**: 길이·캡 모양·내부 파형 방향 고정, 활성 상태에서만 보랏빛

### PROP-CONSENT-FORM | 관계 전체 폐기 동의서

- **SOURCE**: 핵심 진실 공개 및 합의 장면
- **PURPOSE**: 두 사람이 자발적으로 관계 기억을 버렸다는 결정적 문서
- **LOCKS**: STYLE-MASTER, NEG-TEXT
- **VARIABLES**: 펼침/봉인, 두 서명 위치, 손의 개입
- **ASPECT**: 9:16
- **COMPOSITION**: 문서 상단 제목 영역과 하단 두 서명란이 한 프레임에 읽히는 사선 탑뷰
- **PROMPT_KO**: 기관 표준 양식의 두꺼운 미색 A4 문서 두 장, 얇은 회색 격자와 두 개의 서명란, 접힌 흔적과 오래된 보관 얼룩. 생성 이미지에는 모든 문자를 비워 두고 제목·조항·서명 자리는 정돈된 빈 선과 박스로만 표현한다. 붉은 도장이나 음모물 같은 과장은 없다. 9:16 사선 탑뷰, 손끝 하나가 다음 장을 넘기기 직전 멈춘 순간.
- **PROMPT_EN**: Two sheets of thick warm-white A4 institutional paperwork with a fine gray grid, two signature fields, old fold marks and archival stains. Keep every character blank in generation; represent title, clauses and signatures only as clean empty rules and boxes. No sensational red stamp or conspiracy styling. Vertical 9:16 oblique top view, one fingertip frozen just before turning the page.
- **NEGATIVE**: NEG-GLOBAL, NEG-TEXT, readable gibberish, legal seal, horror document, torn paper, extra signatures
- **POST TEXT**: 제목 ‘관계 전체 폐기 동의서’, 조항, 서하·도윤 서명 및 날짜를 확정 원고대로 합성
- **CONTINUITY CHECK**: 문서 얼룩·접힘·서명란 위치 고정, 서명은 항상 두 개

### PROP-LIST-43 | 43명 기억 목록과 모니터 월

- **SOURCE**: 43명 기억 회수 위기 장면
- **PURPOSE**: 개인 로맨스가 타인의 삶과 연결됐음을 시각화
- **LOCKS**: LOC-CENTER-ADMIN, NEG-TEXT
- **VARIABLES**: 경고 단계, 활성 모니터 수, 현석의 위치
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 상단에 43개 상태 타일의 리듬, 하단에 인물 실루엣 또는 조작 손
- **PROMPT_KO**: 관리센터의 얇은 베젤 모니터 월과 반투명 상태 패널. 정확히 43개의 작은 상태 타일이 규칙적인 격자로 존재하되 이름·번호·문장은 모두 빈 자리 또는 단순 색상 블록이다. 정상은 회청색, 위험은 제한된 호박색, 잔여 시간 간섭은 소수의 절제된 마젠타 타일로만 표시한다. 9:16 광각, UI가 배우 얼굴보다 밝지 않게.
- **PROMPT_EN**: A memory-center wall of slim-bezel monitors and translucent status panels. Exactly 43 small status tiles form an orderly grid, while every name, number and sentence remains blank or a simple color block. Normal tiles are blue-gray, risk is restrained amber, and residual-time interference appears only on a few controlled magenta tiles. Vertical 9:16 wide shot; the interface never outshines the actor’s face.
- **NEGATIVE**: NEG-GLOBAL, NEG-TEXT, incorrect tile count, cyberpunk overload, bright rainbow UI, floating screens, stock market graphics
- **POST TEXT**: 43명 이름·상태·경고 문구는 확정 목록 기반 후반 합성
- **CONTINUITY CHECK**: 총 타일 수 43 고정, 경고 상태 변화는 회차 순서와 일치

### PROP-HANDHELD | 현장 작업 단말기

- **SOURCE**: 수거·분류·시스템 확인 장면
- **PURPOSE**: 인물의 직무와 기억 관리 절차를 연결
- **LOCKS**: STYLE-MASTER, LOC-CENTER-SORT
- **VARIABLES**: 사용자, 화면 상태, 장갑 착용
- **ASPECT**: 9:16
- **COMPOSITION**: 한 손 크기 단말기와 엄지, 화면은 카메라 쪽 20도
- **PROMPT_KO**: 충격 방지 회색 고무 프레임의 한 손 크기 산업용 단말기, 작은 카메라·측면 버튼·무광 화면. 화면에는 텍스트 없이 상태 막대와 단순 도형만 남긴다. 여러 해 사용한 모서리 마모와 소독 자국이 있으며 미래형 스마트폰처럼 매끈하지 않다. 9:16 손 중심 클로즈업.
- **PROMPT_EN**: A one-hand industrial terminal with a shock-resistant gray rubber frame, small camera, side keys and matte display. Keep the screen text-free with only status bars and neutral shapes. Show years of corner wear and disinfectant marks; it must not resemble a sleek futuristic phone. Vertical 9:16 hand-focused close-up.
- **NEGATIVE**: NEG-GLOBAL, NEG-TEXT, consumer smartphone, brand logo, hologram, extra fingers, floating device
- **POST TEXT**: 분류 코드·경고·대상 정보는 후반 UI 합성
- **CONTINUITY CHECK**: 회색 프레임·버튼 위치·마모 지도 고정

### PROP-ID-CARD | 관리센터 출입증

- **SOURCE**: 출입·신분 확인 장면
- **PURPOSE**: 조직 위계와 서하·도윤의 직무 차이 표시
- **LOCKS**: CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-HYUNSUK-LOCK, NEG-TEXT
- **VARIABLES**: 소유자, 권한색, 목걸이/클립
- **ASPECT**: 9:16
- **COMPOSITION**: 가슴 높이 출입증과 옷깃, 얼굴 하단을 함께 포함
- **PROMPT_KO**: 무광 반투명 폴리카보네이트 출입증, 세로형 카드와 짙은 회색 스트랩. 사진 영역은 해당 CHAR-LOCK의 동일 얼굴을 사용하되 이름·부서·번호는 빈 칸으로 둔다. 권한색은 서하 회청색, 도윤 먹색, 현석 짙은 남색으로 절제한다. 9:16 가슴 높이 클로즈업, 카드와 인물 턱선이 함께 보인다.
- **PROMPT_EN**: A matte translucent polycarbonate access badge on a dark gray lanyard. The portrait field uses the exact matching CHAR-LOCK identity, while name, division and ID number remain blank. Restrained clearance colors: Seo-ha blue-gray, Do-yun charcoal, Hyun-seok deep navy. Vertical 9:16 chest-height close-up showing both badge and lower face.
- **NEGATIVE**: NEG-GLOBAL, NEG-CHARACTER, NEG-TEXT, wrong portrait, bright corporate colors, logo, horizontal card
- **POST TEXT**: 이름·부서·사번·기관명은 확정 캐논대로 합성
- **CONTINUITY CHECK**: 인물별 얼굴·권한색·스트랩 방식 고정

### PROP-KEYCHAIN-WORN | 수진의 낡은 열쇠고리

- **SOURCE**: 01_script/ep13.md S#2, ep14.md S#1
- **PURPOSE**: 도윤이 수진의 사고와 연결됐음을 증명하고 반출 대가의 선택을 촉발하는 생활 물증
- **LOCKS**: STYLE-MASTER
- **VARIABLES**: 아이가 건네는 상태, 수진이 돌려주는 상태, 도윤 또는 서하의 손에 놓인 상태
- **ASPECT**: 9:16
- **COMPOSITION**: 작은 손과 성인 손 사이에 매달린 열쇠고리를 중앙 하단 1/3에 배치, 얼굴 반응은 위쪽 얕은 초점
- **PROMPT_KO**: 오래 사용한 작은 금속 열쇠고리. 무광 황동 고리와 모서리가 닳은 납작한 짙은 청록색 플라스틱 표찰 하나, 작은 균열과 손때가 있고 브랜드나 문자는 없다. 아이의 손에서 도윤의 손으로 건너갈 때 실제 무게로 아래로 처지며, 다음 회차에 수진이 서하에게 돌려줄 때도 흠집·균열·고리 방향이 완전히 같다. 9:16 실사 매크로, 자연광과 현실적인 손 피부.
- **PROMPT_EN**: A small heavily used keychain: a matte brass ring and one flat dark-teal plastic tag with worn corners, a fine crack and handling grime, no brand or writing. It hangs with believable weight while passing from a child’s hand to Do-yun’s hand, and its exact scratches, crack and ring direction remain identical when Su-jin returns it to Seo-ha in the next episode. Vertical 9:16 live-action macro with natural daylight and realistic hands.
- **NEGATIVE**: NEG-GLOBAL, NEG-CHARACTER, NEG-TEXT, car key, luxury charm, bright toy colors, changed damage, floating object
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: ep13 전달 상태에서 ep14 반환 상태까지 황동 고리·청록 표찰·균열 위치 고정

---

<!-- SOURCE: 06_visual_prompts/04_episode-keyframes.md -->

# 《없던 사이》 24화·93씬 9:16 키프레임 프롬프트

> 각 씬 최소 1개의 대표 정지 프레임이다. 대사는 이미지에 쓰지 않고, 대본의 결정적 동작·시선·중단을 시각화한다. LOCKS는 승인 참조를 반드시 불러오며 VARIABLES만 변경한다.
> 자동 대조 기준 씬 수: 93개

### KF-EP01-S01-01 | 호텔 807호의 버려진 시간 / 내부 / 밤

- **SOURCE**: 01_script/ep01.md S#1
- **PURPOSE**: 1화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-HOTEL-807, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, PROP-PHOTO-WET, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 세로 화면 가득, 침대 아래로 떨어진 커플 사진. 사진 속 얼굴은 빛에 타 보이지 않는다. 침대 가장자리에는 웨딩드레스 차림의 여자가, 바닥에는 턱시도 차림의 남자가 앉아 서로 다른 이름을 부른다. 숨소리만 가까워진다. 서하는 도윤의 손부터 본다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a restrained hotel room with fixed bed, wardrobe, corridor threshold and practical lamps. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-HOTEL-807의 문·가구·광원 방향을 유지

### KF-EP01-S02-01 | 호텔 복도 / 내부 / 버려진 밤

- **SOURCE**: 01_script/ep01.md S#2
- **PURPOSE**: 1화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-HOTEL-807, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, CHAR-SUJIN-LOCK, PROP-PHOTO-WET, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 같은 37초가 반복된다. 신부가 울고, 신랑이 “수진아”라고 부르고, 사진이 침대 아래로 미끄러진다. 도윤이 즉시 놓는다. 그런데 두 사람의 손가락이 떨어지는 순서가 이상할 만큼 느리다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed hotel room and corridor system under practical night lighting. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-SUJIN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-HOTEL-807의 문·가구·광원 방향을 유지

### KF-EP01-S03-01 | 잔시물 관리센터 분류실 / 내부 / 새벽

- **SOURCE**: 01_script/ep01.md S#3
- **PURPOSE**: 1화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-SORT, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, CHAR-HYUNSUK-LOCK, PROP-PHOTO-WET, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 형광등 아래 젖은 사진이 봉투 안으로 들어간다. 장현숙이 봉인 도장을 찍는다. 둘 사이, 봉투 속 사진의 코팅이 서서히 마른다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed memory-item center sorting floor and adjoining staff rooms. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-HYUNSUK-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-SORT의 문·가구·광원 방향을 유지

### KF-EP01-S04-01 | 잔시물 관리센터 분류실·세척대 / 내부 / 연속

- **SOURCE**: 01_script/ep01.md S#4
- **PURPOSE**: 1화 4씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-SORT, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, PROP-PHOTO-DRY, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 서하가 봉투를 들어 조명에 비춘다. 물기가 빠진 사진 속 얼굴이 드러난다. 봉인기 경고음. 화면 암전. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed memory-item center sorting floor and adjoining staff rooms. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-SORT의 문·가구·광원 방향을 유지

### KF-EP02-S01-01 | 잔시물 관리센터 분류실 / 내부 / 새벽

- **SOURCE**: 01_script/ep02.md S#1
- **PURPOSE**: 2화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-SORT, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 도윤이 라벤더 커피를 쓰레기통에 버린다. 서하가 컵을 낚아챈다. 한 모금. 서하의 미간이 즉시 찌푸려진다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed memory-item center sorting floor and adjoining staff rooms. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-SORT의 문·가구·광원 방향을 유지

### KF-EP02-S02-01 | 호텔 로비 / 내부 / 새벽

- **SOURCE**: 01_script/ep02.md S#2
- **PURPOSE**: 2화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-HOTEL-807, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, CHAR-MINSEOK-LOCK, PROP-PHOTO-DRY, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 현재의 신랑 민석이 회수 확인서에 서명한다. 도윤을 보자 펜이 멈춘다. 민석이 휴대폰을 뒤진다. 사진 폴더에는 도윤이 찍어 준 웨딩 사진만 있고, 함께 찍은 셀카 자리만 회색 오류 화면이다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed hotel room and corridor system under practical night lighting. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-MINSEOK-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-HOTEL-807의 문·가구·광원 방향을 유지

### KF-EP02-S03-01 | 센터 엘리베이터 / 내부 / 새벽

- **SOURCE**: 01_script/ep02.md S#3
- **PURPOSE**: 2화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-OFFICE-ELEVATOR, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, PROP-PHOTO-DRY, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 좁은 화면. 두 사람 어깨 사이로 층수만 오른다. 문이 열린다. 둘은 동시에 떨어진다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a narrow mirrored service elevator with realistic metal reflections. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-OFFICE-ELEVATOR의 문·가구·광원 방향을 유지

### KF-EP02-S04-01 | 기록실 앞 / 내부 / 연속

- **SOURCE**: 01_script/ep02.md S#4
- **PURPOSE**: 2화 4씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-ADMIN, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, CHAR-MINJU-LOCK, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 오민주가 오래된 필름 봉투를 들고 기다린다. 도윤은 대답 대신 자기 글씨를 만진다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's fixed administrative, archive, security and system wing. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-MINJU-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-ADMIN의 문·가구·광원 방향을 유지

### KF-EP03-S01-01 | 오피스 엘리베이터의 버려진 시간 / 내부 / 밤

- **SOURCE**: 01_script/ep03.md S#1
- **PURPOSE**: 3화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-OFFICE-ELEVATOR, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, PROP-SHIRT-FOUND, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 문이 닫힐 때마다 남자 직원이 고백하려다 재채기한다. 37초가 반복된다. 바닥은 비에 젖고, 손잡이에는 립스틱 자국. 도윤이 놓는다. 서하는 그대로 서 있지만 손이 닿았던 옆구리의 셔츠 주름만 편다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a narrow mirrored service elevator with realistic metal reflections. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-OFFICE-ELEVATOR의 문·가구·광원 방향을 유지

### KF-EP03-S02-01 | 오피스 엘리베이터의 버려진 시간 / 내부 / 버려진 밤

- **SOURCE**: 01_script/ep03.md S#2
- **PURPOSE**: 3화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-OFFICE-ELEVATOR, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 태그는 천장 점검구 안. 도윤이 서하를 들어 올리려 무릎을 굽힌다. 과거의 도윤이 서하를 같은 자세로 올려 둔 채 웃는다. 과거의 서하가 내려오지 않고 그의 얼굴을 내려다본다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a narrow mirrored service elevator with realistic metal reflections. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-OFFICE-ELEVATOR의 문·가구·광원 방향을 유지

### KF-EP03-S03-01 | 오피스 엘리베이터 거울 앞 / 내부 / 버려진 밤

- **SOURCE**: 01_script/ep03.md S#3
- **PURPOSE**: 3화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-OFFICE-ELEVATOR, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 현재의 서하는 내려왔지만 도윤의 어깨에서 손을 떼지 못했다. 도윤도 허리에 손을 대지 않은 채 기다린다. 거울 속 과거의 두 사람은 이미 입을 맞추고 있다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a narrow mirrored service elevator with realistic metal reflections. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-OFFICE-ELEVATOR의 문·가구·광원 방향을 유지

### KF-EP04-S01-01 | 잔시물 관리센터 보안실 / 내부 / 새벽

- **SOURCE**: 01_script/ep04.md S#1
- **PURPOSE**: 4화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-ADMIN, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 구형 CCTV 화면에 과거의 서하와 도윤이 복도를 걷는다. 프레임이 튈 때마다 둘의 거리가 가까워진다. 마지막 프레임, 입맞춤. 현재의 서하가 정지 버튼을 누른다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's fixed administrative, archive, security and system wing. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-ADMIN의 문·가구·광원 방향을 유지

### KF-EP04-S02-01 | 잔시물 관리센터 보안실 / 내부 / 연속

- **SOURCE**: 01_script/ep04.md S#2
- **PURPOSE**: 4화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-ADMIN, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, PROP-LIST-43, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 서하가 영상을 한 프레임씩 돌린다. 도윤은 모니터보다 서하의 옆얼굴을 본다. 서하가 의자를 돌린다. 무릎이 도윤의 무릎 사이에 들어간다. 둘 다 움직이지 않는다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's fixed administrative, archive, security and system wing. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-ADMIN의 문·가구·광원 방향을 유지

### KF-EP04-S03-01 | 잔시물 관리센터 보안실 문 앞 / 내부 / 연속

- **SOURCE**: 01_script/ep04.md S#3
- **PURPOSE**: 4화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-ADMIN, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, PROP-SHIRT-FOUND, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 서하가 일어난다. 도윤이 길을 비키지 않아 거리가 더 좁다. 서하가 대답하지 않는다. 대신 도윤 셔츠의 비뚤어진 사원증을 바로 세운다. 손끝이 목 가까이 머문다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's fixed administrative, archive, security and system wing. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-ADMIN의 문·가구·광원 방향을 유지

### KF-EP04-S04-01 | CCTV 화면 / 내부 / 연속

- **SOURCE**: 01_script/ep04.md S#4
- **PURPOSE**: 4화 4씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-ADMIN, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 멈춰 있던 영상이 혼자 재생된다. 과거 도윤이 키스 뒤 카메라를 똑바로 본다. 화면이 끊긴다. 서하의 손은 아직 도윤 사원증 위에 있다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's fixed administrative, archive, security and system wing. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-ADMIN의 문·가구·광원 방향을 유지

### KF-EP05-S01-01 | 센터 전 직원 채팅방의 버려진 시간 / 내부 / 낮

- **SOURCE**: 01_script/ep05.md S#1
- **PURPOSE**: 5화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CHAT-RESIDUAL, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, PROP-AUDIO-TRACK, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 공중에 떠 있는 거대한 음성 메시지 파형. 28초마다 전송 버튼이 눌리고, 직원들의 휴대폰이 동시에 울린다. 서하가 파형 안으로 손을 넣는다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in an abstracted but physically grounded residual chat-time space with restrained magenta refraction. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CHAT-RESIDUAL의 문·가구·광원 방향을 유지

### KF-EP05-S02-01 | 채팅방 잔시 내부 / 내부 / 연속

- **SOURCE**: 01_script/ep05.md S#2
- **PURPOSE**: 5화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CHAT-RESIDUAL, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, PROP-AUDIO-TRACK, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 두 사람은 삭제 키를 찾으려 파형 사이를 비집고 지나간다. 음성이 반복될 때마다 공간이 좁아진다. 서하가 웃음을 참다가 파형에 손을 베인다. 도윤이 손가락을 잡아 살핀다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in an abstracted but physically grounded residual chat-time space with restrained magenta refraction. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CHAT-RESIDUAL의 문·가구·광원 방향을 유지

### KF-EP05-S03-01 | 파형 중심 / 내부 / 연속

- **SOURCE**: 01_script/ep05.md S#3
- **PURPOSE**: 5화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CHAT-RESIDUAL, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, PROP-AUDIO-TRACK, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 서하가 손을 빼지 않는다. 잡음. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in an abstracted but physically grounded residual chat-time space with restrained magenta refraction. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CHAT-RESIDUAL의 문·가구·광원 방향을 유지

### KF-EP05-S04-01 | 잔시 붕괴 직전 / 내부 / 연속

- **SOURCE**: 01_script/ep05.md S#4
- **PURPOSE**: 5화 4씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CHAT-RESIDUAL, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 도윤이 서하의 손을 놓는다. 파형이 둘 사이를 가른다. 암전. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in an abstracted but physically grounded residual chat-time space with restrained magenta refraction. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CHAT-RESIDUAL의 문·가구·광원 방향을 유지

### KF-EP06-S01-01 | 잔시물 관리센터 분류실 / 내부 / 새벽

- **SOURCE**: 01_script/ep06.md S#1
- **PURPOSE**: 6화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-SORT, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, PROP-AUDIO-TRACK, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 과거 도윤의 음성 트랙이 유리 실린더 안에서 빛난다. 반출 승인 화면에는 경고가 뜬다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed memory-item center sorting floor and adjoining staff rooms. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-SORT의 문·가구·광원 방향을 유지

### KF-EP06-S02-01 | 개인 장비실 / 내부 / 새벽

- **SOURCE**: 01_script/ep06.md S#2
- **PURPOSE**: 6화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-SORT, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, PROP-AUDIO-TRACK, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 도윤이 몰래 휴대 반출기에 트랙을 꽂는다. 서하가 문을 잠근다. 도윤의 손이 멈춘다. 서하가 그의 손 위에 자기 손을 얹고 함께 버튼을 누른다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed memory-item center sorting floor and adjoining staff rooms. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-SORT의 문·가구·광원 방향을 유지

### KF-EP06-S03-01 | 잔시물 관리센터 분류실 / 내부 / 연속

- **SOURCE**: 01_script/ep06.md S#3
- **PURPOSE**: 6화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-SORT, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, PROP-AUDIO-TRACK, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 트랙이 현실에 안착한다. 도윤의 눈이 잠깐 초점을 잃는다. 서하는 화면을 촬영해 기록한다. 도윤은 그 손이 아주 조금 떨리는 것을 본다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed memory-item center sorting floor and adjoining staff rooms. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-SORT의 문·가구·광원 방향을 유지

### KF-EP06-S04-01 | 음성 재생실 / 내부 / 연속

- **SOURCE**: 01_script/ep06.md S#4
- **PURPOSE**: 6화 4씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-SORT, CHAR-SEOHA-LOCK, WARD-SEOHA-A1, CHAR-DOYUN-LOCK, WARD-DOYUN-A1, PROP-WATCH-RESIDUAL, PROP-AUDIO-TRACK, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 과거 도윤의 음성이 끝까지 재생된다. 서하가 그의 손목시계를 본다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed memory-item center sorting floor and adjoining staff rooms. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-SORT의 문·가구·광원 방향을 유지

### KF-EP07-S01-01 | 모텔방의 버려진 시간 / 내부 / 밤

- **SOURCE**: 01_script/ep07.md S#1
- **PURPOSE**: 7화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-HOTEL-807, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 천장에서 검은 비가 내린다. 바닥과 벽은 닿는 즉시 같은 9분을 반복한다. 마른 곳은 싱글 침대 하나뿐이다. 서하가 침대 끝, 도윤이 반대 끝에 앉는다. 매트리스가 꺼지며 둘이 중앙으로 미끄러진다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a restrained hotel room with fixed bed, wardrobe, corridor threshold and practical lamps. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-HOTEL-807의 문·가구·광원 방향을 유지

### KF-EP07-S02-01 | 모텔방의 버려진 시간 / 내부 / 연속

- **SOURCE**: 01_script/ep07.md S#2
- **PURPOSE**: 7화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-HOTEL-807, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, PROP-WATCH-RESIDUAL, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 반복 속 연인이 서로 등을 돌린 채 “아무 사이도 아니야”라고 말한다. 침대 아래에서 금속성 진동이 난다. 도윤의 손목에 남은 옅은 자국과 정확히 맞는다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a restrained hotel room with fixed bed, wardrobe, corridor threshold and practical lamps. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-HOTEL-807의 문·가구·광원 방향을 유지

### KF-EP07-S03-01 | 모텔방의 버려진 시간·침대 / 내부 / 연속

- **SOURCE**: 01_script/ep07.md S#3
- **PURPOSE**: 7화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-HOTEL-807, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, PROP-WATCH-RESIDUAL, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 검은 비가 침대 가장자리까지 번진다. 둘은 어깨를 붙이고 앉는다. 침대 위로 과거의 서하와 도윤이 겹쳐 눕는다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a restrained hotel room with fixed bed, wardrobe, corridor threshold and practical lamps. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-HOTEL-807의 문·가구·광원 방향을 유지

### KF-EP08-S01-01 | 100일의 버려진 시간 / 내부 / 밤

- **SOURCE**: 01_script/ep08.md S#1
- **PURPOSE**: 8화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-FOOD-TENT, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, PROP-WATCH-RESIDUAL, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 좁은 포장마차. 과거의 서하가 시계 상자를 내민다. 현재의 서하와 도윤이 같은 테이블 반대편에서 본다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the established production location specified by the source scene. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-SORT의 문·가구·광원 방향을 유지

### KF-EP08-S02-01 | 포장마차 뒤편 / 외부 / 버려진 밤

- **SOURCE**: 01_script/ep08.md S#2
- **PURPOSE**: 8화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-FOOD-TENT, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, PROP-WATCH-RESIDUAL, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 과거의 두 사람이 빗소리 아래 선다. 현재의 도윤이 현재 서하의 손을 본다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a warm late-night street-food tent and its narrow service alley. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-FOOD-TENT의 문·가구·광원 방향을 유지

### KF-EP08-S03-01 | 포장마차 / 내부 / 연속

- **SOURCE**: 01_script/ep08.md S#3
- **PURPOSE**: 8화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-FOOD-TENT, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, PROP-WATCH-RESIDUAL, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 잔시가 흔들린다. 반출 경고가 뜬다. 서하는 시계를 놓으려 하지만 도윤이 채운 채다. 서하의 손끝이 그의 맥박 위에 머문다. 잠금쇠는 풀렸는데 손이 떨어지지 않는다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a warm late-night street-food tent and its narrow service alley. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-FOOD-TENT의 문·가구·광원 방향을 유지

### KF-EP08-S04-01 | 잔시물 관리센터 분류실 / 내부 / 새벽

- **SOURCE**: 01_script/ep08.md S#4
- **PURPOSE**: 8화 4씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-SORT, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, PROP-WATCH-RESIDUAL, PROP-SHIRT-FOUND, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 둘은 빈손으로 돌아온다. 그런데 도윤의 손목에는 시계 자국이 더 짙어져 있다. 서하의 사물함 안에서 남성용 셔츠 소매가 흘러나온다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed memory-item center sorting floor and adjoining staff rooms. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-SORT의 문·가구·광원 방향을 유지

### KF-EP09-S01-01 | 여자 탈의실 / 내부 / 새벽

- **SOURCE**: 01_script/ep09.md S#1
- **PURPOSE**: 9화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-SORT, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-MINJU-LOCK, PROP-SHIRT-FOUND, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 서하가 남성용 셔츠를 들어 냄새를 맡으려다 멈춘다. 소매에는 석 달 전 날짜가 찍힌 센터 세탁표가 달려 있다. 문틈으로 민주가 본다. 서하가 문을 닫는다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed memory-item center sorting floor and adjoining staff rooms. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-MINJU-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-SORT의 문·가구·광원 방향을 유지

### KF-EP09-S02-01 | 휴게실 / 내부 / 새벽

- **SOURCE**: 01_script/ep09.md S#2
- **PURPOSE**: 9화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-SORT, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, PROP-SHIRT-FOUND, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 도윤이 다른 팀 직원에게 상처 난 손을 내준다. 직원이 밴드를 붙인다. 서하는 셔츠를 든 채 멈춘다. 서하가 셔츠를 그의 얼굴에 던진다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed memory-item center sorting floor and adjoining staff rooms. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-SORT의 문·가구·광원 방향을 유지

### KF-EP09-S03-01 | 잔시물 관리센터 분류실 / 내부 / 연속

- **SOURCE**: 01_script/ep09.md S#3
- **PURPOSE**: 9화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-SORT, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, PROP-SHIRT-FOUND, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 도윤이 셔츠를 입어 본다. 정확히 맞는다. 두 번째 단추가 없다. 도윤의 웃음이 짧아진다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed memory-item center sorting floor and adjoining staff rooms. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-SORT의 문·가구·광원 방향을 유지

### KF-EP09-S04-01 | 셔츠 안주머니 / 내부 / 연속

- **SOURCE**: 01_script/ep09.md S#4
- **PURPOSE**: 9화 4씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-SORT, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, CHAR-HYUNSUK-LOCK, PROP-SHIRT-FOUND, PROP-RECEIPTS, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 서하가 접힌 영수증을 꺼낸다. 날짜는 3개월 전, 새벽 2시 17분. 뒷면에 서하의 글씨. 서하가 대답하려는 순간 현숙의 방송. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the established production location specified by the source scene. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-HYUNSUK-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-SORT의 문·가구·광원 방향을 유지

### KF-EP10-S01-01 | 센터 복도 / 내부 / 새벽

- **SOURCE**: 01_script/ep10.md S#1
- **PURPOSE**: 10화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-SORT, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 바닥 중앙에 노란 분리선. 서하와 도윤이 각자 반대편으로 걷는다. 서로의 속도에 맞추다 둘 다 멈춘다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed memory-item center sorting floor and adjoining staff rooms. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-SORT의 문·가구·광원 방향을 유지

### KF-EP10-S02-01 | 물류 하역장 / 내부 / 새벽

- **SOURCE**: 01_script/ep10.md S#2
- **PURPOSE**: 10화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-INDUSTRIAL, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, CHAR-TAESIK-LOCK, PROP-RECEIPTS, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 박태식이 낡은 종이 영수증 묶음을 내민다. 영수증 장소를 선으로 잇자 포장마차, 세탁소, 모텔, 센터가 하나의 데이트 동선처럼 이어진다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's industrial loading and vehicle zone under cold practical light. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-TAESIK-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-INDUSTRIAL의 문·가구·광원 방향을 유지

### KF-EP10-S03-01 | 하역장 기둥 뒤 / 내부 / 연속

- **SOURCE**: 01_script/ep10.md S#3
- **PURPOSE**: 10화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-INDUSTRIAL, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 다른 직원이 오자 둘이 좁은 기둥 뒤로 숨는다. 서하의 손바닥이 도윤 가슴에 닿는다. 도윤은 웃지 않는다. 얼굴이 가까워진다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's industrial loading and vehicle zone under cold practical light. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-INDUSTRIAL의 문·가구·광원 방향을 유지

### KF-EP10-S04-01 | 하역장 / 내부 / 연속

- **SOURCE**: 01_script/ep10.md S#4
- **PURPOSE**: 10화 4씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-INDUSTRIAL, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-HYUNSUK-LOCK, CHAR-MINJU-LOCK, PROP-RECEIPTS, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 불이 켜진다. 현숙이 서 있다. 민주가 멀리서 그 번호를 수첩에 적는다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's industrial loading and vehicle zone under cold practical light. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-HYUNSUK-LOCK, CHAR-MINJU-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-INDUSTRIAL의 문·가구·광원 방향을 유지

### KF-EP11-S01-01 | 장현숙 팀장실 / 내부 / 새벽

- **SOURCE**: 01_script/ep11.md S#1
- **PURPOSE**: 11화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-ADMIN, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, CHAR-HYUNSUK-LOCK, PROP-PHOTO-DRY, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 책상 위, 서하와 도윤의 사원증이 나란히 놓인다. 현숙은 더 말하지 않는다. 사원증을 뒤집어 사진을 가린다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's fixed administrative, archive, security and system wing. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-HYUNSUK-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-ADMIN의 문·가구·광원 방향을 유지

### KF-EP11-S02-01 | 종이 기록창고 / 내부 / 아침

- **SOURCE**: 01_script/ep11.md S#2
- **PURPOSE**: 11화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-ADMIN, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-MINJU-LOCK, PROP-CONSENT-FORM, LIGHT-PRESENT-MORNING
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 민주가 안경을 닦으며 철문을 연다. 빽빽한 종이 상자 사이, 특정 장만 2밀리미터 튀어나와 있다. 서하가 튀어나온 장을 뽑는다. `전관계 폐기 사전동의서`. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's fixed administrative, archive, security and system wing. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-MINJU-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-ADMIN의 문·가구·광원 방향을 유지

### KF-EP11-S03-01 | 기록창고 통로 / 내부 / 연속

- **SOURCE**: 01_script/ep11.md S#3
- **PURPOSE**: 11화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-ADMIN, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, CHAR-MINJU-LOCK, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 도윤이 첫 장을 읽는다. 서하가 서류를 접어 품에 넣으려 한다. 도윤이 막는다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's fixed administrative, archive, security and system wing. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-MINJU-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-ADMIN의 문·가구·광원 방향을 유지

### KF-EP11-S04-01 | 기록창고 문 / 내부 / 연속

- **SOURCE**: 01_script/ep11.md S#4
- **PURPOSE**: 11화 4씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-ADMIN, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, CHAR-HYUNSUK-LOCK, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 철문 밖에서 현숙의 발소리. 서하와 도윤은 서가 사이 좁은 틈에 선다. 숨이 닿는 거리. 도윤의 손전등이 마지막 줄을 비춘다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's fixed administrative, archive, security and system wing. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-HYUNSUK-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-ADMIN의 문·가구·광원 방향을 유지

### KF-EP12-S01-01 | 종이 기록창고 / 내부 / 아침

- **SOURCE**: 01_script/ep12.md S#1
- **PURPOSE**: 12화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-ADMIN, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, LIGHT-PRESENT-MORNING
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 서하와 도윤의 서명이 세로 화면 위아래로 놓인다. 필압까지 선명하다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's fixed administrative, archive, security and system wing. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-ADMIN의 문·가구·광원 방향을 유지

### KF-EP12-S02-01 | 기록창고 / 내부 / 연속

- **SOURCE**: 01_script/ep12.md S#2
- **PURPOSE**: 12화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-ADMIN, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 도윤이 서류를 덮는다. 둘의 거리가 가까워지지만, 이번에는 도윤이 먼저 반걸음 물러난다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's fixed administrative, archive, security and system wing. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-ADMIN의 문·가구·광원 방향을 유지

### KF-EP12-S03-01 | 장현숙 팀장실 / 내부 / 아침

- **SOURCE**: 01_script/ep12.md S#3
- **PURPOSE**: 12화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-ADMIN, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-HYUNSUK-LOCK, PROP-LIST-43, LIGHT-PRESENT-MORNING
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 현숙이 마지막 장을 책상 위에 놓는다. 마지막 장에는 `연결 기억 보존 대상 43명 / 안정화 완료`. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's fixed administrative, archive, security and system wing. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-HYUNSUK-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-ADMIN의 문·가구·광원 방향을 유지

### KF-EP12-S04-01 | 장현숙 팀장실·모니터 앞 / 내부 / 연속

- **SOURCE**: 01_script/ep12.md S#4
- **PURPOSE**: 12화 4씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-ADMIN, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, CHAR-HYUNSUK-LOCK, PROP-PHOTO-DRY, PROP-LIST-43, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 모니터에 43명의 현재 생활 사진이 뜬다. 생일상, 등굣길, 병실, 결혼식. 서하와 도윤이 무의식적으로 떨어진다. 안정도는 멈추지 않고 `88%`. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's fixed administrative, archive, security and system wing. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-HYUNSUK-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-ADMIN의 문·가구·광원 방향을 유지

### KF-EP13-S01-01 | 서울 여러 장소 / 내·외 / 낮

- **SOURCE**: 01_script/ep13.md S#1
- **PURPOSE**: 13화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-SEOUL-MONTAGE, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, CHAR-CHILD-LOCK, PROP-LIST-43, LIGHT-PRESENT-MORNING
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 세로 화면을 빠르게 채우는 43개의 이름. 서하와 도윤은 명단 속 사람들을 멀리서 확인한다. 아이 손을 잡은 여자, 버스 운전사, 수술을 앞둔 노인. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a coherent vertical montage of ordinary Seoul streets and interiors. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-CHILD-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-SEOUL-MONTAGE의 문·가구·광원 방향을 유지

### KF-EP13-S02-01 | 동네 세탁소 / 내부 / 낮

- **SOURCE**: 01_script/ep13.md S#2
- **PURPOSE**: 13화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-LAUNDROMAT, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, CHAR-SUJIN-LOCK, CHAR-CHILD-LOCK, PROP-KEYCHAIN-WORN, LIGHT-PRESENT-MORNING
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 김수진이 아이 교복을 다린다. 도윤을 보자 다리미가 멈춘다. 수진의 아이가 도윤에게 낡은 열쇠고리를 건넨다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a modest neighborhood laundromat with a fixed rear room and daylight storefront. Preserve CHAR-DOYUN-LOCK, CHAR-SUJIN-LOCK and CHAR-CHILD-LOCK plus the exact damage map of PROP-KEYCHAIN-WORN. Freeze the instant just before the child releases the worn keychain into Do-yun's hand while Su-jin watches. Natural skin and hands, practical daylight, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-LAUNDROMAT의 문·가구·광원 방향을 유지

### KF-EP13-S03-01 | 세탁소 뒷방 / 내부 / 연속

- **SOURCE**: 01_script/ep13.md S#3
- **PURPOSE**: 13화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-LAUNDROMAT, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, CHAR-SUJIN-LOCK, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 수진은 사고 당시 하루를 통째로 기억하지 못한다. 서하가 답하지 못한다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a modest neighborhood laundromat with a fixed rear room and daylight storefront. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-SUJIN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-LAUNDROMAT의 문·가구·광원 방향을 유지

### KF-EP13-S04-01 | 세탁소 앞 / 외부 / 낮

- **SOURCE**: 01_script/ep13.md S#4
- **PURPOSE**: 13화 4씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-LAUNDROMAT, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, CHAR-SUJIN-LOCK, PROP-SHIRT-FOUND, LIGHT-PRESENT-MORNING
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 서하가 명단을 접는다. 도윤의 셔츠 아래 옆구리에 오래된 흉터가 드러난다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a modest neighborhood laundromat with a fixed rear room and daylight storefront. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-SUJIN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-LAUNDROMAT의 문·가구·광원 방향을 유지

### KF-EP14-S01-01 | 세탁소 뒷방 / 내부 / 낮

- **SOURCE**: 01_script/ep14.md S#1
- **PURPOSE**: 14화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-LAUNDROMAT, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-SUJIN-LOCK, CHAR-CHILD-LOCK, PROP-KEYCHAIN-WORN, LIGHT-PRESENT-MORNING
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 수진이 잔시물 열쇠고리를 돌려준다. 수진의 아이가 문밖에서 “엄마”를 부른다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a modest neighborhood laundromat with a fixed rear room and daylight storefront. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-SUJIN-LOCK, CHAR-CHILD-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-LAUNDROMAT의 문·가구·광원 방향을 유지

### KF-EP14-S02-01 | 센터 귀환 차량 / 내부 / 저녁

- **SOURCE**: 01_script/ep14.md S#2
- **PURPOSE**: 14화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-INDUSTRIAL, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 도윤이 창가, 서하가 운전석. 신호등의 붉은빛이 둘 얼굴을 번갈아 가른다. 서하가 급브레이크를 밟는다. 도윤의 팔이 서하 앞을 막아 안전벨트처럼 버틴다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's industrial loading and vehicle zone under cold practical light. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-INDUSTRIAL의 문·가구·광원 방향을 유지

### KF-EP14-S03-01 | 센터 주차장 / 내부 / 저녁

- **SOURCE**: 01_script/ep14.md S#3
- **PURPOSE**: 14화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-INDUSTRIAL, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 차 안 불이 꺼진다. 둘은 내리지 않는다. 도윤이 숨을 내쉰다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's industrial loading and vehicle zone under cold practical light. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-INDUSTRIAL의 문·가구·광원 방향을 유지

### KF-EP15-S01-01 | 옥상의 버려진 시간 / 외부 / 밤

- **SOURCE**: 01_script/ep15.md S#1
- **PURPOSE**: 15화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-ROOFTOP, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 과거 서하와 도윤이 첫 키스 직전 마주 서 있다. 현재의 둘은 좁은 옥상 창고 그늘에 숨는다. 현재 도윤도 무심코 같은 말을 입 모양으로 따라 한다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a Seoul service rooftop with water tank, exit door and wind-shaped practical light. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-ROOFTOP의 문·가구·광원 방향을 유지

### KF-EP15-S02-01 | 옥상 물탱크 뒤 / 외부 / 연속

- **SOURCE**: 01_script/ep15.md S#2
- **PURPOSE**: 15화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-ROOFTOP, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 과거 도윤이 묻는다. 서하는 “네” 대신 그의 넥타이 매듭을 느슨하게 푼다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a Seoul service rooftop with water tank, exit door and wind-shaped practical light. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-ROOFTOP의 문·가구·광원 방향을 유지

### KF-EP15-S03-01 | 옥상 출입문 / 외부 / 연속

- **SOURCE**: 01_script/ep15.md S#3
- **PURPOSE**: 15화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-ROOFTOP, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 두 사람의 얼굴이 가까워진다. 서하가 도윤의 입술 바로 앞에서 멈춘다. 현재 서하가 열쇠를 보고 굳는다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a Seoul service rooftop with water tank, exit door and wind-shaped practical light. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-ROOFTOP의 문·가구·광원 방향을 유지

### KF-EP16-S01-01 | 서하의 집에 붙은 버려진 시간 / 내부 / 아침

- **SOURCE**: 01_script/ep16.md S#1
- **PURPOSE**: 16화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-SEOHA-HOME, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, PROP-SHIRT-FOUND, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 사람은 없다. 세로 화면 아래, 남자 구두와 여자 구두가 뒤섞여 있다. 식탁에는 두 잔의 커피, 소파에는 도윤의 셔츠, 욕실 거울에는 손가락으로 쓴 `늦음`. 현재의 서하와 도윤이 현관에 선다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in Seo-ha's compact apartment with fixed kitchen, bedroom threshold and dining table. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-SEOHA-HOME의 문·가구·광원 방향을 유지

### KF-EP16-S02-01 | 부엌 / 내부 / 버려진 아침

- **SOURCE**: 01_script/ep16.md S#2
- **PURPOSE**: 16화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-SEOHA-HOME, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 과거 서하의 손만 나타나 도윤의 커피에서 시럽을 빼고, 과거 도윤의 손만 나타나 서하의 머그 손잡이를 오른쪽으로 돌린다. 도윤이 손을 빼지 않는다. 서하가 먼저 손가락 하나를 움직여 그의 손등을 누른다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in Seo-ha's compact apartment with fixed kitchen, bedroom threshold and dining table. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-SEOHA-HOME의 문·가구·광원 방향을 유지

### KF-EP16-S03-01 | 침실 문 앞 / 내부 / 연속

- **SOURCE**: 01_script/ep16.md S#3
- **PURPOSE**: 16화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-SEOHA-HOME, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, CHAR-DOYUN-LOCK, WARD-DOYUN-A2, PROP-SHIRT-FOUND, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 문은 반쯤 열려 있다. 침대에는 흐트러진 이불, 바닥에는 없어진 단추 하나. 서하가 문을 닫는다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in Seo-ha's compact apartment with fixed kitchen, bedroom threshold and dining table. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-SEOHA-HOME의 문·가구·광원 방향을 유지

### KF-EP16-S04-01 | 식탁 / 내부 / 연속

- **SOURCE**: 01_script/ep16.md S#4
- **PURPOSE**: 16화 4씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-SEOHA-HOME, CHAR-SEOHA-LOCK, WARD-SEOHA-A2, PROP-LIST-43, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 식탁 밑에서 접힌 쪽지. 서하가 편다. 부엌 창밖이 붉은 경보등으로 변한다. 고밀도 잔시가 열린다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in Seo-ha's compact apartment with fixed kitchen, bedroom threshold and dining table. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-SEOHA-HOME의 문·가구·광원 방향을 유지

### KF-EP17-S01-01 | 고밀도 잔시 발생실 / 내부 / 과거 밤

- **SOURCE**: 01_script/ep17.md S#1
- **PURPOSE**: 17화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-ACCIDENT-CORE, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, CHAR-SUJIN-LOCK, PROP-LIST-43, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 경보등. 43개의 모니터에서 각기 다른 가족의 기억이 끊긴다. 과거 도윤은 옆구리에 피를 흘리고, 과거 서하는 불안정한 코어를 붙든다. 서하가 그 농담에 웃지 않는다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed industrial memory core where the past accident and consent procedure occurred. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-SUJIN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-ACCIDENT-CORE의 문·가구·광원 방향을 유지

### KF-EP17-S02-01 | 발생실 / 내부 / 과거 밤

- **SOURCE**: 01_script/ep17.md S#2
- **PURPOSE**: 17화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-ACCIDENT-CORE, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, CHAR-HYUNSUK-LOCK, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 과거 현숙이 소리친다. 과거 서하와 도윤이 서로를 본다. 말없이 답을 알아챈다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed industrial memory core where the past accident and consent procedure occurred. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-HYUNSUK-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-ACCIDENT-CORE의 문·가구·광원 방향을 유지

### KF-EP17-S03-01 | 코어 앞 / 내부 / 연속

- **SOURCE**: 01_script/ep17.md S#3
- **PURPOSE**: 17화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-ACCIDENT-CORE, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, CHAR-HYUNSUK-LOCK, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 과거 도윤이 서하에게 손을 내민다. 현재 도윤도 무의식적으로 현재 서하에게 손을 내민다. 서하가 잡는다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed industrial memory core where the past accident and consent procedure occurred. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-HYUNSUK-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-ACCIDENT-CORE의 문·가구·광원 방향을 유지

### KF-EP17-S04-01 | 동의 단말기 앞 / 내부 / 연속

- **SOURCE**: 01_script/ep17.md S#4
- **PURPOSE**: 17화 4씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-ACCIDENT-CORE, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, PROP-CONSENT-FORM, PROP-HANDHELD, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 과거 도윤이 먼저 손을 올리려 하자 과거 서하가 막는다. 과거의 두 사람이 펜을 든다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed industrial memory core where the past accident and consent procedure occurred. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-ACCIDENT-CORE의 문·가구·광원 방향을 유지

### KF-EP18-S01-01 | 동의 단말기 / 내부 / 과거 밤

- **SOURCE**: 01_script/ep18.md S#1
- **PURPOSE**: 18화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-ACCIDENT-CORE, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, CHAR-HYUNSUK-LOCK, PROP-CONSENT-FORM, PROP-LIST-43, PROP-HANDHELD, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 과거 서하와 도윤이 각자 서명한다. 43개 모니터의 깨진 얼굴들이 천천히 돌아온다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed industrial memory core where the past accident and consent procedure occurred. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-HYUNSUK-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-ACCIDENT-CORE의 문·가구·광원 방향을 유지

### KF-EP18-S02-01 | 코어 앞 / 내부 / 연속

- **SOURCE**: 01_script/ep18.md S#2
- **PURPOSE**: 18화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-ACCIDENT-CORE, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, PROP-SHIRT-FOUND, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 두 사람의 100일이 빛의 조각으로 빠져나간다. 첫 식사, 첫 다툼, 첫 키스, 같은 침대의 아침. 현재의 둘은 서로 손만 잡고 그 장면을 본다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed industrial memory core where the past accident and consent procedure occurred. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-ACCIDENT-CORE의 문·가구·광원 방향을 유지

### KF-EP18-S03-01 | 소거 직전 / 내부 / 과거 밤

- **SOURCE**: 01_script/ep18.md S#3
- **PURPOSE**: 18화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-ACCIDENT-CORE, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 도윤의 농담기가 완전히 사라진다. 빛이 두 사람 사이를 가른다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed industrial memory core where the past accident and consent procedure occurred. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-ACCIDENT-CORE의 문·가구·광원 방향을 유지

### KF-EP18-S04-01 | 잔시물 관리센터 분류실 / 내부 / 새벽

- **SOURCE**: 01_script/ep18.md S#4
- **PURPOSE**: 18화 4씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-SORT, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, CHAR-HYUNSUK-LOCK, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 현재로 돌아온 서하와 도윤. 손은 여전히 잡혀 있다. 현숙이 들어와 둘의 손을 본다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed memory-item center sorting floor and adjoining staff rooms. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-HYUNSUK-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-SORT의 문·가구·광원 방향을 유지

### KF-EP19-S01-01 | 센터 아카이브 / 내부 / 새벽

- **SOURCE**: 01_script/ep19.md S#1
- **PURPOSE**: 19화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-ADMIN, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-HYUNSUK-LOCK, PROP-PHOTO-DRY, PROP-WATCH-RESIDUAL, PROP-SHIRT-FOUND, PROP-RECEIPTS, PROP-LIST-43, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 100일의 잔시물 상자들이 동시에 덜컹댄다. 시계, 셔츠, 사진, 영수증이 상자 틈으로 빛난다. 모니터 속 43명의 이름 옆에 작은 균열 표시가 켜진다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's fixed administrative, archive, security and system wing. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-HYUNSUK-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-ADMIN의 문·가구·광원 방향을 유지

### KF-EP19-S02-01 | 격리 복도 / 내부 / 새벽

- **SOURCE**: 01_script/ep19.md S#2
- **PURPOSE**: 19화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-ADMIN, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 투명 유리벽을 사이에 두고 서하와 도윤이 마주 선다. 인터폰은 꺼져 있다. 서하가 한참 뒤 쓴다. `안 됩니다.` 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's fixed administrative, archive, security and system wing. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-ADMIN의 문·가구·광원 방향을 유지

### KF-EP19-S03-01 | 장현숙 팀장실 / 내부 / 연속

- **SOURCE**: 01_script/ep19.md S#3
- **PURPOSE**: 19화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-ADMIN, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-HYUNSUK-LOCK, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 서하가 현숙 앞에 선다. 서하가 대답하지 못한다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's fixed administrative, archive, security and system wing. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-HYUNSUK-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-ADMIN의 문·가구·광원 방향을 유지

### KF-EP19-S04-01 | 격리 복도 / 내부 / 연속

- **SOURCE**: 01_script/ep19.md S#4
- **PURPOSE**: 19화 4씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-ADMIN, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 유리 너머 도윤이 사라져 있다. 바닥에는 가슴에 붙였던 분리 이송표만 놓여 있다. 서하가 유리에 손을 댄다. 반대편 빈 유리에 다른 손자국이 천천히 나타난다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's fixed administrative, archive, security and system wing. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-ADMIN의 문·가구·광원 방향을 유지

### KF-EP20-S01-01 | 잔시물 관리센터 분류실 / 내부 / 밤

- **SOURCE**: 01_script/ep20.md S#1
- **PURPOSE**: 20화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-SORT, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, CHAR-HYUNSUK-LOCK, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 도윤은 전근하지 않았다. 대신 현숙이 밤새 붙인 빨간 작업선이 두 사람 사이 바닥을 가른다. 봉투를 동시에 잡는다. 손끝은 선 위에서 닿는다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed memory-item center sorting floor and adjoining staff rooms. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-HYUNSUK-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-SORT의 문·가구·광원 방향을 유지

### KF-EP20-S02-01 | 버스 정류장의 버려진 시간 / 외부 / 밤

- **SOURCE**: 01_script/ep20.md S#2
- **PURPOSE**: 20화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-BUS-STOP, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 둘은 서로 모르는 척 각자 태그를 찾는다. 하지만 서하가 고개를 들기 전 도윤이 떨어지는 간판을 막고, 도윤이 돌아서기 전 서하가 열린 맨홀을 발로 닫는다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a quiet Seoul bus stop with a fixed bench, shelter glass and wet road reflections. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-BUS-STOP의 문·가구·광원 방향을 유지

### KF-EP20-S03-01 | 정류장 벤치 / 외부 / 연속

- **SOURCE**: 01_script/ep20.md S#3
- **PURPOSE**: 20화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-BUS-STOP, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 반복 속 노인이 먼저 떠난 아내에게 빈자리를 남겨 둔다. 서하와 도윤도 한 자리씩 떨어져 앉는다. 도윤이 빈자리를 건너오지 않는다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a quiet Seoul bus stop with a fixed bench, shelter glass and wet road reflections. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-BUS-STOP의 문·가구·광원 방향을 유지

### KF-EP20-S04-01 | 센터 시스템실 / 내부 / 새벽

- **SOURCE**: 01_script/ep20.md S#4
- **PURPOSE**: 20화 4씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-ADMIN, CHAR-MINJU-LOCK, PROP-LIST-43, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 민주가 모니터를 켠다. 자동 해결안이 떠 있다. 화면이 스스로 펜 입력을 활성화한다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's fixed administrative, archive, security and system wing. Preserve the exact approved identities and wardrobe of CHAR-MINJU-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-ADMIN의 문·가구·광원 방향을 유지

### KF-EP21-S01-01 | 시스템실 / 내부 / 새벽

- **SOURCE**: 01_script/ep21.md S#1
- **PURPOSE**: 21화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-ADMIN, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 서명란 앞. 도윤이 펜을 든다. 서하가 빼앗아 부러뜨린다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's fixed administrative, archive, security and system wing. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-ADMIN의 문·가구·광원 방향을 유지

### KF-EP21-S02-01 | 종이 기록창고 / 내부 / 새벽

- **SOURCE**: 01_script/ep21.md S#2
- **PURPOSE**: 21화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-ADMIN, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, CHAR-MINJU-LOCK, PROP-PHOTO-DRY, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 민주가 숨겨 둔 부록을 펼친다. 그는 이미 문을 연다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's fixed administrative, archive, security and system wing. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-MINJU-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-ADMIN의 문·가구·광원 방향을 유지

### KF-EP21-S03-01 | 호텔 807호의 버려진 시간 / 내부 / 밤

- **SOURCE**: 01_script/ep21.md S#3
- **PURPOSE**: 21화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-HOTEL-807, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, PROP-PHOTO-WET, LIGHT-RESIDUAL-TIME
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 사진이 침대 아래 있다. 도윤이 집는다. 서하가 손을 겹친다. 그가 서하 손을 천천히 떼고 반출 버튼을 누른다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a restrained hotel room with fixed bed, wardrobe, corridor threshold and practical lamps. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING, NEG-RESIDUAL-TIME
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-HOTEL-807의 문·가구·광원 방향을 유지

### KF-EP21-S04-01 | 현실 호텔방 / 내부 / 밤

- **SOURCE**: 01_script/ep21.md S#4
- **PURPOSE**: 21화 4씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-HOTEL-807, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, PROP-PHOTO-DRY, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 도윤이 사진을 든 채 눈을 뜬다. 안정도 `94%`. 반출기 화면에 뒤늦게 소실 진단이 뜬다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed hotel room and corridor system under practical night lighting. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-HOTEL-807의 문·가구·광원 방향을 유지

### KF-EP22-S01-01 | 호텔 807호 / 내부 / 밤

- **SOURCE**: 01_script/ep22.md S#1
- **PURPOSE**: 22화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-HOTEL-807, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, PROP-PHOTO-DRY, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 서하가 커플 사진을 도윤 앞에 내밀려다 뒤집는다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a restrained hotel room with fixed bed, wardrobe, corridor threshold and practical lamps. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-HOTEL-807의 문·가구·광원 방향을 유지

### KF-EP22-S02-01 | 호텔 자판기 앞 / 내부 / 밤

- **SOURCE**: 01_script/ep22.md S#2
- **PURPOSE**: 22화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-HOTEL-807, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 서하가 커피 두 잔을 뽑는다. 라벤더 버튼 앞에서 멈추고 평범한 블랙을 건넨다. 도윤이 잔을 받는다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed hotel room and corridor system under practical night lighting. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-HOTEL-807의 문·가구·광원 방향을 유지

### KF-EP22-S03-01 | 호텔 복도 / 내부 / 연속

- **SOURCE**: 01_script/ep22.md S#3
- **PURPOSE**: 22화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-HOTEL-807, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 둘이 나란히 걷는다. 도윤이 무심코 서하의 위험한 쪽을 막는 자리로 바꿔 선다. 서하가 멈춘다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed hotel room and corridor system under practical night lighting. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-HOTEL-807의 문·가구·광원 방향을 유지

### KF-EP22-S04-01 | 호텔 엘리베이터 / 내부 / 연속

- **SOURCE**: 01_script/ep22.md S#4
- **PURPOSE**: 22화 4씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-HOTEL-807, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 문이 닫힌다. 서하가 도윤을 정면으로 본다. 그 순간 센터 호출. `안정도 재하락 87% / 잔여 증거 전량 폐기 필요`. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed hotel room and corridor system under practical night lighting. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-HOTEL-807의 문·가구·광원 방향을 유지

### KF-EP23-S01-01 | 센터 소각실 / 내부 / 새벽

- **SOURCE**: 01_script/ep23.md S#1
- **PURPOSE**: 23화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-INDUSTRIAL, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-HYUNSUK-LOCK, PROP-PHOTO-DRY, PROP-WATCH-RESIDUAL, PROP-SHIRT-FOUND, PROP-RECEIPTS, PROP-AUDIO-TRACK, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 투명 상자 안에 100일의 증거가 쌓인다. `21화 반출 봉인` 표찰이 붙은 사진, 시계, 셔츠, 단추, 영수증, 음성 트랙. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's sober industrial disposal room with safety rails and furnace controls. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-HYUNSUK-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-INDUSTRIAL의 문·가구·광원 방향을 유지

### KF-EP23-S02-01 | 소각 대기실 / 내부 / 새벽

- **SOURCE**: 01_script/ep23.md S#2
- **PURPOSE**: 23화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-INDUSTRIAL, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, PROP-WATCH-RESIDUAL, PROP-SHIRT-FOUND, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 도윤은 기억하지 못하는 자기 시계를 든다. 서하가 셔츠 단추를 손바닥에 올린다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's sober industrial disposal room with safety rails and furnace controls. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-INDUSTRIAL의 문·가구·광원 방향을 유지

### KF-EP23-S03-01 | 소각로 앞 / 내부 / 연속

- **SOURCE**: 01_script/ep23.md S#3
- **PURPOSE**: 23화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-INDUSTRIAL, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, CHAR-MINJU-LOCK, PROP-PHOTO-DRY, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 민주는 각 물건의 마지막 기록 번호를 읽고 상자에 넣는다. 마지막 사진에서 멈춘다. 도윤이 사진을 보려 하자 서하가 뒤집어 넣는다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's sober industrial disposal room with safety rails and furnace controls. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, CHAR-MINJU-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-INDUSTRIAL의 문·가구·광원 방향을 유지

### KF-EP23-S04-01 | 소각 버튼 앞 / 내부 / 연속

- **SOURCE**: 01_script/ep23.md S#4
- **PURPOSE**: 23화 4씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-INDUSTRIAL, CHAR-SEOHA-LOCK, WARD-SEOHA-A3, CHAR-DOYUN-LOCK, WARD-DOYUN-A3, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 두 사람이 나란히 손을 올린다. 이번에는 서하가 먼저 묻는다. 버튼이 붉게 빛난다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's sober industrial disposal room with safety rails and furnace controls. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-INDUSTRIAL의 문·가구·광원 방향을 유지

### KF-EP24-S01-01 | 센터 소각실 / 내부 / 새벽

- **SOURCE**: 01_script/ep24.md S#1
- **PURPOSE**: 24화 1씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-INDUSTRIAL, CHAR-SEOHA-LOCK, WARD-SEOHA-A4, CHAR-DOYUN-LOCK, WARD-DOYUN-A4, CHAR-HYUNSUK-LOCK, PROP-PHOTO-DRY, PROP-LIST-43, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 서하와 도윤이 동시에 버튼을 누른다. 증거들이 불꽃이 아니라 흰빛으로 부서진다. 모니터의 43개 균열 표시가 하나씩 꺼진다. 현숙이 뒤집어 두었던 사원증을 사진 면으로 돌린다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the center's sober industrial disposal room with safety rails and furnace controls. Preserve CHAR-SEOHA-LOCK and CHAR-DOYUN-LOCK at the shared controls and CHAR-HYUNSUK-LOCK turning her badge in the middle background; Min-ju remains off-frame. Freeze both leads pressing the paired buttons as evidence breaks into controlled white light and the 43 blank status tiles go dark. Natural skin and hands, practical light, controlled depth, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-INDUSTRIAL의 문·가구·광원 방향을 유지

### KF-EP24-S02-01 | 센터 출입구 / 내부 / 아침

- **SOURCE**: 01_script/ep24.md S#2
- **PURPOSE**: 24화 2씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CENTER-SORT, CHAR-SEOHA-LOCK, WARD-SEOHA-A4, CHAR-DOYUN-LOCK, WARD-DOYUN-A4, LIGHT-PRESENT-MORNING
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 근무가 끝난다. 도윤이 문을 열고 기다린다. 서하가 지나가다 멈춘다. 서하는 웃지만 먼저 걷는다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in the fixed memory-item center sorting floor and adjoining staff rooms. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CENTER-SORT의 문·가구·광원 방향을 유지

### KF-EP24-S03-01 | 작은 카페 / 내부 / 아침

- **SOURCE**: 01_script/ep24.md S#3
- **PURPOSE**: 24화 3씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CAFE-ALLEY, CHAR-SEOHA-LOCK, WARD-SEOHA-A4, CHAR-DOYUN-LOCK, WARD-DOYUN-A4, LIGHT-PRESENT-MORNING
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 세로 창 너머 출근 인파. 둘은 작은 원형 테이블에 마주 앉는다. 과거 물건은 하나도 없다. 서하가 컵을 내려놓는다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a small morning café and its narrow calm alley. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CAFE-ALLEY의 문·가구·광원 방향을 유지

### KF-EP24-S04-01 | 카페 골목 / 외부 / 아침

- **SOURCE**: 01_script/ep24.md S#4
- **PURPOSE**: 24화 4씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CAFE-ALLEY, CHAR-SEOHA-LOCK, WARD-SEOHA-A4, CHAR-DOYUN-LOCK, WARD-DOYUN-A4, LIGHT-PRESENT-MORNING
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 둘이 마주 선다. 도윤은 움직이지 않고 기다린다. 말을 뱉은 서하의 표정이 먼저 굳는다. 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a small morning café and its narrow calm alley. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CAFE-ALLEY의 문·가구·광원 방향을 유지

### KF-EP24-S05-01 | 골목 / 외부 / 연속

- **SOURCE**: 01_script/ep24.md S#5
- **PURPOSE**: 24화 5씬의 핵심 감정 전환과 다음 행동 직전의 미완결 긴장을 한 장으로 고정
- **LOCKS**: STYLE-MASTER, CAM-VERTICAL-MASTER, LOC-CAFE-ALLEY, CHAR-SEOHA-LOCK, WARD-SEOHA-A4, CHAR-DOYUN-LOCK, WARD-DOYUN-A4, PROP-AUDIO-TRACK, PROP-HANDHELD, LIGHT-CENTER-NIGHT
- **VARIABLES**: 대본에 명시된 표정 강도, 손 위치, 시선 방향, 소품의 현재 상태만 변경 가능
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙 60%에 얼굴·손·핵심 소품을 우선 배치하고 상단 12%와 하단 18%를 자막·UI 안전영역으로 유지
- **PROMPT_KO**: STYLE-MASTER와 위 LOCKS의 승인 정체성·의상·공간 구조를 정확히 유지한 한국 실사 드라마 스틸. 서하의 업무용 단말기가 진동한다. 단말기 화면: `보존 완료.` 행동이 끝난 뒤가 아니라 끝나기 직전의 호흡을 포착한다. 표정은 절제하고 인물 간 거리와 손의 중단으로 성인 로맨스의 긴장을 표현한다. 자연스러운 피부와 손, 실제 광원, 얕되 과하지 않은 심도, 9:16 세로 구도. 대사와 설명 문자는 이미지에 넣지 않는다.
- **PROMPT_EN**: A vertical 9:16 live-action Korean drama still in a small morning café and its narrow calm alley. Preserve the exact approved identities and wardrobe of CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK, the locked set geometry, and every referenced prop state. Freeze the source scene at its decisive unfinished breath, just before the scripted gesture or revelation resolves. Express mature romantic tension through restrained eye lines, interrupted hand movement and plausible physical distance, never explicit contact. Natural skin and hands, practical light, controlled shallow depth of field, face-hand-prop priority, no dialogue or explanatory text in the image.
- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT
- **POST TEXT**: 대본상 모니터·문서·단말·간판 글자가 필요한 경우에만 원문 그대로 후반 합성; 생성 단계 문자 금지
- **CONTINUITY CHECK**: 직전·직후 씬의 얼굴, 헤어, WARD 상태, 젖음·혈흔·손상·소품 소유자를 대조하고 LOC-CAFE-ALLEY의 문·가구·광원 방향을 유지

---

<!-- SOURCE: 06_visual_prompts/05_negative-prompts.md -->

# 《없던 사이》 공통 네거티브 프롬프트

### NEG-GLOBAL | 전 자산 공통

- **SCOPE**: 배우, 배경, 소품, 회차별 키프레임 전체
- **NEGATIVE_KO**: 일러스트, 애니메이션, 3D 렌더, 게임 시네마틱, 과도한 HDR, 플라스틱 피부, 뷰티 필터, 인공적인 보케, 네온 사이버펑크, 과포화, 저해상도, 흐린 얼굴, 이중 노출, 워터마크, 로고, 프레임, 콜라주, 분할 화면, 카메라 응시, 정면 포즈 사진, 무관한 엑스트라, 시대착오 물건
- **NEGATIVE_EN**: illustration, anime, 3D render, game cinematic, excessive HDR, plastic skin, beauty filter, artificial bokeh, neon cyberpunk, oversaturation, low resolution, blurred face, double exposure, watermark, logo, decorative frame, collage, split screen, looking at camera, posed portrait, unrelated extras, anachronistic objects

### NEG-CHARACTER | 얼굴·신체 일관성

- **SCOPE**: 인물이 등장하는 모든 자산
- **NEGATIVE_KO**: 다른 배우, 얼굴 교체, 회차마다 달라지는 얼굴형, 눈 색 변화, 머리 길이 급변, 가발 티, 과도한 보정, 비대칭 눈, 중복 인물, 복제 얼굴, 손가락 추가·누락·융합, 뒤틀린 손목, 떠 있는 손, 나이 급변, 실존 연예인 닮은꼴 강요
- **NEGATIVE_EN**: different actor, face swap, changing face shape, changing eye color, sudden hair-length change, obvious wig, over-retouching, asymmetric eyes, duplicate person, cloned face, extra missing or fused fingers, twisted wrist, floating hand, sudden age change, forced resemblance to any celebrity

### NEG-RATING | 15세 성인 긴장 연출 경계

- **SCOPE**: 썸, 밀착, 사고, 부상 장면
- **NEGATIVE_KO**: 노출, 속옷 강조, 투명 의상, 성행위, 강압적 접촉, 동의 없는 키스, 신체 부위 집착, 포르노그래피, 페티시 구도, 침대 위 노골적 자세, 고어, 열린 상처, 절단, 과도한 혈액, 폭력 미화
- **NEGATIVE_EN**: nudity, emphasized underwear, transparent clothing, sexual act, coercive touch, non-consensual kiss, fetishized body parts, pornography, fetish framing, explicit bed pose, gore, open wound, dismemberment, excessive blood, glamorized violence

### NEG-TEXT | 생성 단계 문자 금지

- **SCOPE**: 문서, 영수증, 출입증, 모니터, 단말기, 간판
- **NEGATIVE_KO**: 읽을 수 있는 가짜 한글, 깨진 글자, 무작위 알파벳, 오탈자, 뒤집힌 글자, 임의 날짜, 임의 숫자, 브랜드명, 서명, 자막, 말풍선
- **NEGATIVE_EN**: readable fake Korean, broken glyphs, random alphabet, typo, mirrored text, invented dates, invented numbers, brand name, signature, subtitle, speech bubble

### NEG-RESIDUAL-TIME | 버려진 시간 효과 절제

- **SCOPE**: 잔여 시간 및 기억 물질 장면
- **NEGATIVE_KO**: 마법진, 판타지 주문, 번개 폭발, 거대한 포털, 우주 배경, 별가루 폭포, 유령, 공포 괴물, 전신 오라, 무지개 발광, 배우 얼굴을 가리는 입자, 화면 전체 보라색 틴트
- **NEGATIVE_EN**: magic circle, fantasy spell, lightning explosion, giant portal, outer-space background, waterfall of stardust, ghost, horror creature, full-body aura, rainbow glow, particles covering faces, full-frame purple tint

### NEG-CONTINUITY | 씬·회차 연속성

- **SCOPE**: 93개 전 키프레임과 반복 자산
- **NEGATIVE_KO**: 승인되지 않은 의상 변경, 좌우 반전된 상처, 사라진 소품, 갑자기 수리된 소품, 젖었다가 즉시 마른 옷, 시간대와 맞지 않는 빛, 장소 구조 변경, 문 위치 변경, 가구 재배치, 동일 씬 내 헤어 변화, 설명되지 않은 혈흔, 인물 키 차이 변화
- **NEGATIVE_EN**: unapproved wardrobe change, mirrored injury, missing prop, suddenly repaired prop, instantly dry clothing, wrong time-of-day light, changed location layout, moved doorway, rearranged furniture, hairstyle change within one scene, unexplained blood, changing height difference

---

<!-- SOURCE: 06_visual_prompts/06_handoff-guide.md -->

# 《없던 사이》 AI 이미지 프롬프트 제작팀 인수인계서

## 납품 범위

이 패키지는 이미지를 생성하지 않는다. 승인된 대본·배우 아이덴티티·공간·소품을 실제 생성 도구에 투입할 수 있도록 한국어/영어 프롬프트와 연속성 규칙을 제공한다. 생성 모델, 계정, 시드, LoRA, 얼굴 참조 이미지, 해상도, 업스케일러는 제작팀이 확정한다.

## 승인 순서

1. `00_style-bible.md`의 화풍·조명·9:16 구도를 승인한다.
2. `01_character-prompts.md`의 캐릭터 시트와 얼굴 기준 이미지를 먼저 생성·승인한다.
3. 승인 얼굴을 참조 슬롯에 고정한 뒤 의상 A1~A4를 승인한다.
4. `02_location-prompts.md`의 빈 공간 마스터를 승인한다.
5. `03_prop-prompts.md`의 소품 정면·후면·상태 변형을 승인한다.
6. 위 승인 자산만 참조해 `04_episode-keyframes.md`의 93개 씬 키프레임을 생성한다.
7. 모든 생성 결과는 `07_prompt-audit.md`의 연속성 체크 항목으로 사람이 재검수한다.

## 참조 슬롯 등록표

| 슬롯 | 대상 ID | 제작팀 입력값 | 승인 상태 |
|---|---|---|---|
| FACE-01 | CHAR-SEOHA-LOCK | 기준 얼굴 이미지/모델 참조값 | 제작팀 확정 |
| FACE-02 | CHAR-DOYUN-LOCK | 기준 얼굴 이미지/모델 참조값 | 제작팀 확정 |
| FACE-03 | CHAR-HYUNSUK-LOCK | 기준 얼굴 이미지/모델 참조값 | 제작팀 확정 |
| FACE-04 | CHAR-MINJU-LOCK | 기준 얼굴 이미지/모델 참조값 | 제작팀 확정 |
| FACE-05~07 | CHAR-SUJIN/TAESIK/MINSEOK-LOCK | 기준 얼굴 이미지/모델 참조값 | 제작팀 확정 |
| FACE-08 | CHAR-CHILD-LOCK | 보호자·제작 승인 기준 이미지/참조값 | 제작팀 확정 |
| LOC-01~15 | LOC-* | 승인 공간 기준 이미지/참조값 | 제작팀 확정 |
| PROP-01~10 | PROP-* | 승인 소품 기준 이미지/참조값 | 제작팀 확정 |

## 생성기 어댑터

| 항목 | 입력 규칙 | 현재 값 |
|---|---|---|
| 모델/버전 | 동일 프로젝트 전 회차 고정 | 제작팀 확정 |
| 얼굴 참조 방식 | character reference, LoRA 등 한 방식 우선 | 제작팀 확정 |
| 시드 정책 | 인물·장소별 기준 시드 기록 | 제작팀 확정 |
| 원본 해상도 | 9:16, 얼굴과 손 검수 가능한 최소치 | 제작팀 확정 |
| 업스케일/보정 | 얼굴 재생성 금지, 승인 정체성 보존 | 제작팀 확정 |
| 색관리 | STYLE-MASTER와 GRADE-ARC-MASTER 기준 | 제작팀 확정 |

## 프롬프트 조립법

각 키프레임은 다음 순서로 조립한다.

`STYLE-MASTER + CHAR/LOC/PROP LOCKS + 해당 키프레임 PROMPT + NEG-GLOBAL + 분야별 NEG-*`

`LOCKS`는 승인 자산을 교체하라는 뜻이 아니라 반드시 불러오라는 뜻이다. `VARIABLES`에 적힌 표정, 젖음, 손 위치, 카메라 거리만 해당 씬에서 바꿀 수 있다. 같은 씬의 대체 컷을 만들 때도 얼굴·헤어·의상·소품 상태는 고정한다.

## 파일명 규칙

- 캐릭터: `DISCARDED-US_CHAR-SEOHA-LOCK_v001_ref01.png`
- 의상: `DISCARDED-US_WARD-SEOHA-A2_v001_front.png`
- 장소: `DISCARDED-US_LOC-HOTEL-807_v001_empty.png`
- 소품: `DISCARDED-US_PROP-PHOTO-WET_v001_front.png`
- 키프레임: `DISCARDED-US_KF-EP01-S01-01_v001.png`
- 수정본: 기존 파일을 덮어쓰지 않고 `v002`, `v003`으로 증가

## 후반 문자 합성

생성 단계에서 한글·숫자·서명·UI 문구를 만들지 않는다. `POST TEXT`에 기재된 문구만 편집 프로그램에서 벡터 레이어로 합성한다. 소스 대본과 다른 날짜·이름·수치를 임의로 추가하지 않는다.

## 9:16 안전영역

- 얼굴의 눈·입, 맞닿기 직전의 손, 핵심 소품은 중앙 60% 안에 둔다.
- 상단 12%와 하단 18%는 플랫폼 UI·자막 안전영역으로 비운다.
- 투샷은 키 차이와 시선을 유지하며 인물을 양 끝으로 밀어내지 않는다.
- 휴대폰 크롭에서 사라질 장식 정보는 서사의 핵심 증거로 사용하지 않는다.

## 검수 게이트

- 캐릭터 승인 전 키프레임 생성 금지
- 소품 상태 전환은 `CONTINUITY CHECK`와 회차 순서 대조
- 93개 씬 모두 최소 1개 키프레임 보유
- 실존 배우 이름·브랜드·워터마크 금지
- 15세 경계: 욕망은 시선·호흡·거리·중단으로 표현하고 노출·강압·노골적 성행위 금지
- 최종 상태가 `READY`가 아니면 제작팀 전달 보류

---

<!-- SOURCE: 06_visual_prompts/07_prompt-audit.md -->

# 비주얼 프롬프트 검수 — 《없던 사이》 v1

> 범위: `06_visual_prompts/00_style-bible.md`~`06_handoff-guide.md` · 2026-08-06 · 이미지 생성/생성 이미지 품질 검수 미포함

## 요약

- 미해결 치명 0 · 중대 0 · 경미 0
- 교정 완료: 중대 3개 유형 · 경미 1개 유형
- 씬 커버리지: 93/93
- 키프레임: 93개, 전부 9:16
- 주요·기능 인물 잠금: 8/8
- 반복 장소 마스터: 15개
- 소품 상태 마스터: 11개
- 기계 점검: 자산 ID 60개, 오류 0

## 기계 점검 결과

```text
대본 씬: 93
커버 씬: 93
키프레임: 93
자산 ID: 60
오류: 0
```

## 교정 완료 결함

### VP-C01 | 관리센터와 잔여 시간 조명 혼동

- **위치**: ep01·02·04·06·08·09·18·20의 관리센터 키프레임 및 이어지는 잔여 시간 연속 씬
- **대본·캐논 근거**: 현실 센터는 4300K 형광등, 버려진 시간은 물건 내부에서 새는 제한된 자주색 측광
- **프롬프트 사실**: 장소명 `잔시물 관리센터`의 ‘잔시’ 문자열 때문에 일부 현실 씬이 `LIGHT-RESIDUAL-TIME`을 참조했고, 반대로 `연속` 헤딩의 잔여 시간 후속 씬은 현실 조명을 참조했다.
- **문제**: 같은 시퀀스에서 광원과 시공간 구분이 뒤집히는 중대 연속성 충돌
- **교정안 A**: 해당 씬의 LIGHT ID만 개별 교체
- **교정안 B**: 장소명 문자열이 아닌 시퀀스 시작·종료와 대본 시간축을 기준으로 LIGHT를 할당
- **반영**: A를 즉시 반영하고 B를 향후 자동화 규칙으로 기록. 미해결 0.

### VP-C02 | 젖은 사진 상태가 후반까지 지속

- **위치**: ep01 S#4 이후 현실의 사진 재등장 씬
- **대본·캐논 근거**: ep01 S#3 봉투 안에서 코팅이 마르고 S#4에 얼굴이 드러난 뒤 보관·소각됨
- **프롬프트 사실**: 사진을 언급한 후속 씬 일부가 `PROP-PHOTO-WET`을 계속 참조
- **문제**: 물증의 건조·봉인 상태가 되돌아가는 중대 소품 연속성 충돌
- **교정안 A**: ep01 S#4 및 현실 후속 씬을 `PROP-PHOTO-DRY`로 교체하고 잔여 시간 재현 컷만 WET 유지
- **교정안 B**: PHOTO 상태 전이를 WET → DRY/SEALED → DISPOSAL로 별도 상태표 관리
- **반영**: A 반영. `PROP-PHOTO-WET`은 ep01 S#1~3, ep21 S#3의 버려진 시간에만 유지. 미해결 0.

### VP-C03 | 핵심 열쇠고리 마스터 누락

- **위치**: ep13 S#2, ep14 S#1
- **대본·캐논 근거**: 아이가 도윤에게 건네고 다음 회차에 수진이 서하에게 돌려주는 사고 관련 물증
- **프롬프트 사실**: 씬 문장에는 있었으나 고정 재질·흠집·이동 상태 ID가 없었음
- **문제**: 회차를 건너 이동하는 소품의 외형이 바뀔 수 있는 중대 위험
- **교정안 A**: `PROP-KEYCHAIN-WORN` 마스터와 두 키프레임 LOCK 추가
- **교정안 B**: 대본의 ‘건넨다/돌려준다/보관한다’ 동사를 기준으로 이동 소품 자동 추출
- **반영**: A 반영. 황동 고리·청록 표찰·균열 위치를 고정. 미해결 0.

### VP-C04 | 한 키프레임 인물 수 초과

- **위치**: ep13 S#2, ep24 S#1
- **대본·캐논 근거**: 키프레임 스키마는 전경 인물 최대 3명
- **프롬프트 사실**: 각 컷에 CHAR 잠금 4개가 포함됨
- **문제**: 세로 프레임에서 얼굴·손·소품 우선순위가 흐려지는 경미 구성 결함
- **교정안 A**: 대표 행동에 필요한 3명만 잠그고 나머지는 오프프레임 처리
- **교정안 B**: 동일 씬 보조 키프레임을 추가해 반응 컷 분리
- **반영**: A 반영. ep13은 도윤·수진·아이, ep24는 서하·도윤·현숙을 전경 기준으로 확정. 미해결 0.

## 연속성 매트릭스

| ID | 회차·씬 | CHAR | WARD | LOC | PROP STATE | 시간·빛 | 판정 |
|---|---|---|---|---|---|---|---|
| ARC-01 | ep01–06 | 서하·도윤 A1 | A1 | 센터/호텔/엘리베이터/채팅 잔시 | PHOTO WET→DRY, AUDIO | 잔시와 센터 분리 | 통과 |
| ARC-02 | ep07–12 | 서하·도윤 A2 | A2 | 모텔/포장마차/센터/기록창고 | WATCH, SHIRT, PHOTO DRY | 연속 씬 LIGHT 고정 | 통과 |
| ARC-03 | ep13–16 | 서하·도윤 A2, 수진·아이 | A2/기능복 | 서울/세탁소/옥상/서하 집 | KEYCHAIN 전달→반환 | 낮 현실/잔시 분리 | 통과 |
| ARC-04 | ep17–18 | 과거·현재 동일 얼굴 | A3+사고 상태 | ACCIDENT-CORE | CONSENT, LIST-43, SHIRT | 과거 잔시 측광 | 통과 |
| ARC-05 | ep19–23 | 서하·도윤 A3 | A3 | 아카이브/정류장/호텔/소각실 | PHOTO DRY 및 증거 묶음 | 현실·재진입 분리 | 통과 |
| ARC-06 | ep24 | 서하·도윤 A4 | A4 | 소각실→카페→골목 | 증거 소각 후 생활 소품 | 새벽 형광등→아침 자연광 | 통과 |

## 등급·동의·문자 검수

- 친밀감은 시선, 호흡, 손이 닿기 직전의 중단, 허락 후 접촉으로 제한되어 `RATING-15-CONSENT`와 일치한다.
- 대본에 없는 키스·노출·강압적 접촉·상처 확대를 추가하지 않았다.
- 문서, 영수증, 출입증, UI, 상태 숫자는 `NEG-TEXT`와 `POST TEXT`로 생성 단계에서 분리했다.
- 실존 배우·브랜드·특정 생성기 옵션은 사용하지 않았다.
- 과거와 현재의 서하·도윤은 같은 `CHAR-LOCK`을 사용하며 얼굴 교체 없이 의상·빛·행동 상태로 구분한다.

## 제작팀 전달 판정

- **READY**
- 범위: 프롬프트 텍스트·대본 충실도·자산 연속성만 검증했다. 실제 생성 이미지의 얼굴 유사도, 손 오류, 해상도, 모델 편향은 제작팀 생성 후 별도 검수해야 한다.

---

<!-- SOURCE: 06_visual_prompts/08_prompt-fix-log.md -->

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
