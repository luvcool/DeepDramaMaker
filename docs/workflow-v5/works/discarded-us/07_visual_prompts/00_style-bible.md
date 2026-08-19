# 《없던 사이》 비주얼 프롬프트 스타일 바이블 v2
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

### LIGHT-REALITY-DAY | 현실 낮
- **SOURCE**: ep13–14, locations.md L-14
- **PURPOSE**: 세탁소·서울 생활 몽타주 현실 낮 광원
- **LOCKS**: STYLE-MASTER
- **VARIABLES**: 흐린 낮·세탁소 증기·차량 저녁 직전
- **ASPECT**: 9:16
- **COMPOSITION**: 창 측면광과 실제 실내등이 얼굴·노동하는 손을 함께 읽게 함
- **PROMPT_KO**: `서울의 흐린 낮 자연광, 창에서 들어오는 5200K 안팎의 부드러운 측면광과 생활 공간의 따뜻한 실내등 혼합, 다림질 증기와 천·피부 질감을 보존하고 광고 촬영처럼 과도하게 따뜻하게 만들지 않음`
- **PROMPT_EN**: `soft overcast Seoul daylight around 5200K entering from a side window, mixed with warmer practical interior light, preserving steam, cloth and real skin texture without commercial golden warmth`
- **NEGATIVE**: `beauty daylight, sentimental golden wash, blown window`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: ep13–14 낮 장면의 창 방향 고정

### LIGHT-REALITY-NIGHT | 현실 밤·저녁
- **SOURCE**: ep02·14·21–22
- **PURPOSE**: 센터 밖 현실 호텔·차량 밤 광원
- **LOCKS**: STYLE-MASTER
- **VARIABLES**: 호텔 새벽, 차량 신호등, 현실 호텔 밤
- **ASPECT**: 9:16
- **COMPOSITION**: 장소의 실제 램프를 주광으로 사용하고 잔시 자주색 효과는 배제
- **PROMPT_KO**: `현실의 호텔·차량 밤, 값싼 전구와 복도등 또는 신호등 같은 실제 광원만 사용, 피부색을 유지하는 중성 저조도, 시간 잔시의 자주색 측광과 판타지 발광 없음`
- **PROMPT_EN**: `present-day hotel or vehicle at night using only practical room lamps, corridor fixtures or traffic signals, neutral low light that preserves skin tone, no magenta discarded-time edge and no fantasy glow`
- **NEGATIVE**: `magenta aura, noir darkness, luxury hotel lighting`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: 같은 현실 장소의 광원 방향과 색 유지

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
