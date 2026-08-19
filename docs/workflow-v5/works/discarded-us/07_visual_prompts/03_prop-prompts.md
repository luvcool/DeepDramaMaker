# 《없던 사이》 소품 마스터 프롬프트 v2

> 모든 문자·숫자·서명은 생성 단계에서 비워 두고 `POST TEXT` 지시에 따라 후반 합성한다. 소품의 흠집, 젖음, 밀봉, 혈흔 등 상태 변화는 연속성 정보다.

### PROP-PHOTO-WET | 젖은 커플 사진

- **SOURCE**: 01_script 전반, 05_design/props.md 1번
- **PURPOSE**: 두 사람이 실제로 연인이었다는 최초의 물증
- **LOCKS**: STYLE-MASTER, CHAR-SEOHA-LOCK, CHAR-DOYUN-LOCK
- **VARIABLES**: 젖음 정도, 손에 들린 방향, 봉투 수납 여부
- **ASPECT**: 9:16
- **COMPOSITION**: 세로 프레임 중앙의 작은 인화 사진, 사진을 쥔 손과 번진 표면을 함께 클로즈업
- **PROMPT_KO**: 9:16 실사 한국 미스터리 로맨스 소품 사진. 오래된 무광 4x6 인화지, 빗물과 오염수에 젖어 가장자리가 말리고 표면 유제가 부분적으로 번졌다. 내부에는 CHAR-SEOHA-LOCK과 CHAR-DOYUN-LOCK이 어깨를 맞댄 연인 구도로 존재하지만 ep01 S#1–6에는 두 얼굴 부위만 빛에 타 식별되지 않는다. 사진이 마른 ep01 S#7부터 PROP-PHOTO-DRY 상태로 전환해 얼굴을 공개한다. 종이 섬유와 물방울은 사실적이며 날짜·글자는 비워 둔다.
- **PROMPT_EN**: Vertical 9:16 live-action Korean mystery-romance prop shot. A worn matte 4x6 print soaked by rain and dirty water, with curled edges and partially bloomed emulsion. The locked identities CHAR-SEOHA-LOCK and CHAR-DOYUN-LOCK exist in a shoulder-to-shoulder lovers' composition, but in episode 1 scenes 1–6 only the two facial areas are burned out by light and cannot be identified. Switch to PROP-PHOTO-DRY when the faces are revealed from episode 1 scene 7 onward. Realistic paper fibers and droplets; leave dates and writing blank.
- **NEGATIVE**: NEG-GLOBAL, NEG-CHARACTER, NEG-TEXT, glossy new photo, illegible faces, different actors, wedding photo, explicit intimacy
- **POST TEXT**: 필요한 회차에서만 사진 뒷면 날짜 또는 분류 번호를 별도 레이어로 합성
- **CONTINUITY CHECK**: ep01 S#1–6 얼굴 비식별·WET, ep01 S#7 이후 동일 얼굴 공개·DRY, 구도·손상 지도 고정

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
- **PROMPT_KO**: 과장되지 않은 중가형 아날로그 손목시계, 작은 사각 은색 문자판과 얇은 검정 가죽 스트랩, 사용감 있는 미세 흠집. 뒷면에는 글자를 생성하지 않고 각인용 빈 금속 면을 확보한다. 잔시에서는 유리 가장자리와 초침 주변에만 절제된 마젠타-보랏빛 굴절이 얇게 맺힌다. 실제 물체처럼 무게와 반사가 느껴지는 9:16 매크로 클로즈업, 피부와 손가락의 자연스러운 질감.
- **PROMPT_EN**: A restrained mid-range analog wristwatch with a small rectangular silver dial, thin black leather strap and fine wear scratches. Keep a blank metal engraving area on the back without generated lettering. In discarded time only, a thin controlled magenta-violet refraction clings to the glass rim and second hand. Vertical 9:16 macro close-up with believable weight, reflections, natural skin and fingertips.
- **NEGATIVE**: NEG-GLOBAL, NEG-TEXT, luxury logo, smartwatch, fantasy magic aura, oversized glow, changed strap color
- **POST TEXT**: 뒷면 `D에게, 100일은 안 버리기`, 화면 `DAY 100`은 후반 합성
- **CONTINUITY CHECK**: 사각 은색 문자판·검정 스트랩·흠집 지도 고정, 잔시 밖에서는 발광 없음

### PROP-SHIRT-FOUND | 도윤의 셔츠와 떨어진 단추

- **SOURCE**: 사고 기억과 물증 장면
- **PURPOSE**: 과거 사고의 신체적 흔적과 도윤의 정체 확인
- **LOCKS**: CHAR-DOYUN-LOCK, WARD-DOYUN-A2
- **VARIABLES**: 접힘, 착용, 단추 분리 여부
- **ASPECT**: 9:16
- **COMPOSITION**: 구겨진 셔츠 앞섶과 비어 있는 단추 자리, 별도 단추를 같은 초점면에 배치
- **PROMPT_KO**: 여러 번 빨아 목깃이 부드러운 회청색 남성 셔츠, 두 번째 단추가 없어 짧은 실밥만 남고 안쪽에는 표식 합성용 빈 면이 있다. 석 달 전 센터 세탁표를 붙일 빈 영역과 희미한 라벤더 향을 암시하는 생활 얼룩, 혈흔과 사고 손상은 없다. 무광 자개 단추 하나를 같은 초점면에 둔 9:16 증거물 클로즈업.
- **PROMPT_EN**: A repeatedly washed blue-gray men's shirt with a softened collar, the second button missing with short loose threads, and a blank inner area reserved for a later mark. Include a blank area for the three-month-old center laundry tag and subtle everyday staining that suggests a faint lavender scent; no blood or accident damage. Place one matte mother-of-pearl button on the same focal plane in a vertical 9:16 evidence close-up.
- **NEGATIVE**: NEG-GLOBAL, NEG-RATING, blood, gore, different shirt color, multiple missing buttons, brand logo
- **POST TEXT**: 안쪽 `D`, 석 달 전 세탁표, 증거번호는 후반 합성
- **CONTINUITY CHECK**: 두 번째 단추 자리·셔츠 색상·목깃 주름·자개 단추 흠집 고정

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
- **VARIABLES**: 경고 단계, 활성 모니터 수, 현숙의 위치
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
- **PROMPT_EN**: A matte translucent polycarbonate access badge on a dark gray lanyard. The portrait field uses the exact matching CHAR-LOCK identity, while name, division and ID number remain blank. Restrained clearance colors: Seoha blue-gray, Doyun charcoal, Hyunsuk deep navy. Vertical 9:16 chest-height close-up showing both badge and lower face.
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

### PROP-QUARANTINE-CAPSULE | 잔시 격리 캡슐
- **SOURCE**: world.md 규칙 5, props.md P-10, ep01·19·21
- **PURPOSE**: 비현실 보관과 현실 반출 경계 시각화
- **LOCKS**: STYLE-MASTER, PROP-PHOTO-WET
- **VARIABLES**: 잠금/해제, 내부 소품
- **ASPECT**: 9:16
- **COMPOSITION**: 투명 캡슐과 잠금부, 내부 사진 가장자리를 손과 함께 하단 중앙에 배치
- **PROMPT_KO**: `손바닥 두 개 너비의 투명 폴리카보네이트 격리 캡슐, 무광 회색 잠금부와 반복 사용으로 생긴 미세 흠집, 잠금 상태에서는 내부 사진의 가장자리만 저채도 자주색으로 굴절되고 캡슐 밖으로 꺼내지지 않음, 화면 문구용 빈 표시창, 현실적인 공공기관 장비`
- **PROMPT_EN**: `transparent polycarbonate quarantine capsule two palms wide, matte gray lock and fine repeated-use scratches; while locked, only the edge of the photograph inside refracts muted magenta and the object never exists outside the capsule; blank status window for post text, realistic public-service equipment`
- **NEGATIVE**: `NEG-GLOBAL, NEG-TEXT, sci-fi pod, hologram, magic box`
- **POST TEXT**: `현실 반출 없음`, 상태 코드는 후반 합성
- **CONTINUITY CHECK**: ep01–20 잠금, ep21에서만 현실 물질화

### PROP-TAG-BLACK | 검은 잔시 태그·탐침
- **SOURCE**: props.md P-11, 전편 진입 씬
- **PURPOSE**: 잔시 진입·출구·원인 물품 추적
- **LOCKS**: STYLE-MASTER
- **VARIABLES**: 활성 테두리, 손 소유자
- **ASPECT**: 9:16
- **COMPOSITION**: 장갑 낀 손과 무광 검정 태그를 같은 초점면에
- **PROMPT_KO**: `신용카드보다 작은 무광 검정 산업용 태그와 짧은 금속 탐침, 모서리 도장 벗겨짐과 소독 흔적, 활성 시 숫자 없이 얇은 저채도 자주색 테두리만 점등, 미래형 스마트 기기보다 오래된 현장 장비의 무게감`
- **PROMPT_EN**: `matte black industrial tag smaller than a credit card with a short metal probe, worn corner coating and disinfectant marks; when active, only a thin muted-magenta rim lights up with no generated numbers, grounded aging field equipment rather than futuristic technology`
- **NEGATIVE**: `NEG-GLOBAL, NEG-TEXT, smartphone, neon gadget, brand logo`
- **POST TEXT**: 시간·장소 코드와 카운트다운은 후반 합성
- **CONTINUITY CHECK**: 크기·마모·버튼 위치 전편 고정

### PROP-LINES-PEN | 노란·빨간 분리선과 부러진 펜
- **SOURCE**: props.md P-15, ep09–10·19–21
- **PURPOSE**: 관계 통제와 두 번째 폐기 거부
- **LOCKS**: STYLE-MASTER
- **VARIABLES**: 노란 선/빨간 선/펜 두 조각
- **ASPECT**: 9:16
- **COMPOSITION**: 바닥 선은 하단 세로축, 손과 펜촉은 중앙 클로즈업
- **PROMPT_KO**: `사용감 있는 산업용 바닥 테이프, ep09~10은 노란 안전선, ep19~20은 현숙이 손으로 붙여 가장자리가 미세하게 뜬 빨간 작업선, ep20 말미에는 무광 검정 전자펜이 정확히 두 조각으로 부러져 펜촉 두 개가 나란히 놓임`
- **PROMPT_EN**: `worn industrial floor tape: yellow safety line only in episodes 9–10, red work line only in episodes 19–20 with slightly lifted hand-applied edges; at the end of episode 20 a matte black electronic pen is broken into exactly two pieces, its two tips lying parallel`
- **NEGATIVE**: `NEG-GLOBAL, NEG-TEXT, mixed line colors, extra pen fragments, glowing laser line`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: ep21 S#1까지 펜 두 조각 유지, 색상 회차 혼용 금지

### PROP-ISOLATION-NOTES | 유리벽 메모·이송표
- **SOURCE**: props.md P-16, ep19
- **PURPOSE**: 소리 없이 합의와 이탈을 시각화
- **LOCKS**: LOC-CENTER-ADMIN, NEG-TEXT
- **VARIABLES**: 메모 순서, 동관/서관 표 색
- **ASPECT**: 9:16
- **COMPOSITION**: 유리 양쪽 손과 흰 메모지, 어긋난 손바닥을 한 세로축에
- **PROMPT_KO**: `굵은 검정 펜 자국용 빈 영역이 있는 흰 메모지 여러 장, 동관은 저채도 청색 이송표, 서관은 적갈색 이송표, 투명 유리벽 양쪽에서 성인 손이 종이를 들며 손바닥 위치는 한 뼘 어긋남, 실제 종이 섬유와 유리 손자국`
- **PROMPT_EN**: `several white memo sheets with blank areas reserved for thick black handwriting, muted blue transfer tag for the east wing and rust-red tag for the west wing; adult hands hold the papers on opposite sides of transparent glass, palms offset by one handspan, realistic paper fibers and fingerprints`
- **NEGATIVE**: `NEG-GLOBAL, NEG-TEXT, readable generated writing, perfect clean glass`
- **POST TEXT**: ep19 메모 대사와 이송표 정보는 후반 합성
- **CONTINUITY CHECK**: 메모 앞뒤 순서와 이송표 색 고정

### PROP-NOTE-0217 | 집 열쇠·02:17 쪽지
- **SOURCE**: props.md P-14, ep15–16
- **PURPOSE**: 친밀한 일상에서 사고 밤으로 연결
- **LOCKS**: STYLE-MASTER, NEG-TEXT
- **VARIABLES**: 열쇠 낙하/쪽지 펼침/빛 소실
- **ASPECT**: 9:16
- **COMPOSITION**: 은색 집 열쇠와 네 번 접힌 메모를 손 사이 하단 1/3에
- **PROMPT_KO**: `일상적인 작은 은색 집 열쇠와 네 번 접혀 섬유가 닳은 미색 메모지, 손글씨와 시간 표시가 들어갈 충분한 빈 면, ep16 마지막에는 종이가 가장자리부터 빛에 사라지되 숫자 합성 영역만 잠시 남는 절제된 잔시 효과`
- **PROMPT_EN**: `ordinary small silver house key and warm-white note folded four times with worn paper fibers, ample blank area for handwriting and a time stamp in post; at the end of episode 16 the paper disappears from the edges in restrained discarded-time light while the blank time-code area lingers briefly`
- **NEGATIVE**: `NEG-GLOBAL, NEG-TEXT, ornate key, magic parchment, readable fake writing`
- **POST TEXT**: `오늘 밤, 43명부터 살린다. 우리 얘기는 그다음.`, `02:17`
- **CONTINUITY CHECK**: 접힘 네 번·열쇠 흠집·소실 방향 고정

### PROP-COFFEE-PRESENT | 현재형 커피 컵 두 개
- **SOURCE**: props.md P-17, ep24 S#4–5
- **PURPOSE**: 과거 유품 없이 새 관계가 만드는 첫 공동 물건
- **LOCKS**: LOC-CAFE-ALLEY, LIGHT-PRESENT-MORNING
- **VARIABLES**: 컵 간격, 손 소유자
- **ASPECT**: 9:16
- **COMPOSITION**: 하단 중앙 두 컵과 상단 두 얼굴을 같은 세로축에
- **PROMPT_KO**: `작은 도자기 커피 컵 두 개, 하나는 손잡이 오른쪽과 세로 유약 흠집, 다른 하나는 손잡이 왼쪽과 둥근 유약 흐름, 브랜드·문자·과거 상징 없음, 서로 부딪히기 직전의 한 손가락 거리, 서울 아침 자연광과 실제 도자기 질감`
- **PROMPT_EN**: `two small ceramic coffee cups: one handle facing right with a vertical glaze flaw, the other facing left with a rounded glaze run, no brand, text or symbol from the past; one finger-width apart just before touching, real ceramic texture in Seoul morning daylight`
- **NEGATIVE**: `NEG-GLOBAL, NEG-TEXT, matching romantic mugs, heart symbols, luxury tableware`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: 손잡이 방향·흠집 지도 ep24 S#4–5 고정
