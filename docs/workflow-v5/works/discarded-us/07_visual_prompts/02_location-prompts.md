# 《없던 사이》 배경·로케이션 생성 프롬프트 v2
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
- **CONTINUITY CHECK**: ep03 S#1–7 거울·점검구·물 위치 동일

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
- **CONTINUITY CHECK**: ep15 S#1–7 동일 동선, 열쇠는 S#7에서만 바닥

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
- **CONTINUITY CHECK**: ep20 S#3–5 중앙 빈자리 유지

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
- **CONTINUITY CHECK**: ep24 S#4–7 같은 아침빛 방향

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
