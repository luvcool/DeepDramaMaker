# 《없던 사이》 배우·캐릭터 생성 프롬프트 v2
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
- **VARIABLES**: ep17 붉은 잔시 측광·ep21 명찰 위치
- **ASPECT**: 전신
- **COMPOSITION**: 끝까지 잠근 작업 재킷과 중앙 명찰, 소매는 손상 없이 유지
- **PROMPT_KO**: `먹색 작업 재킷을 목 아래까지 잠근 한서하, ep17 사고 잔시에서는 붉은 경보광만 소매 위에 반사되고 실제 그을음이나 손상 없음, ep21 이후 사원증은 가리지 않고 가슴 중앙에 정면 배치, 검정 팬츠와 안전화 유지`
- **PROMPT_EN**: `Han Seoha with the charcoal work jacket zipped to the base of the neck; in the episode 17 accident residue only red alarm light reflects across the sleeve, with no actual scorch or damage; ID card displayed face-forward at the center of her chest from episode 21 onward, same black trousers and safety shoes`
- **NEGATIVE**: `scorch mark, battle damage, torn clothing, tactical costume`
- **POST TEXT**: 사원증 이름은 후반 합성
- **CONTINUITY CHECK**: ep17–23 실제 의상 손상 없음, ep21부터 명찰 정면

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

### WARD-SEOHA-PAST | 과거 서하 ep03–18
- **SOURCE**: `costumes.md WARD-PAST-SH`, ep03–18
- **PURPOSE**: 과거 서하 의상 잠금
- **LOCKS**: CHAR-SEOHA-LOCK
- **VARIABLES**: 데이트/근무/사고 밤, 도윤 혈흔 접촉
- **ASPECT**: 전신
- **COMPOSITION**: 현재와 같은 직선 실루엣이되 소매선과 색온도만 부드럽게
- **PROMPT_KO**: `CHAR-SEOHA-LOCK과 완전히 같은 얼굴과 헤어, 현재보다 한 톤 따뜻한 청록 면 셔츠와 검정 작업 팬츠, 소매 접힘은 덜 각지고 생활 주름이 부드러움, 사고 밤 ep17~18에만 손과 소매 일부에 도윤의 제한된 검붉은 혈흔, 얼굴·체형·머리 길이 변화 없음`
- **PROMPT_EN**: `exact same face and hair as CHAR-SEOHA-LOCK, teal cotton shirt one shade warmer than the present timeline with black work trousers, softer sleeve folds and lived-in creases; only during the episode 17–18 accident, a limited dark blood transfer from Doyun appears on one hand and sleeve; no change in face, body or hair length`
- **NEGATIVE**: `different younger actress, romantic dress, long hair, excessive blood`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: 과거·현재 동일 배우, 색온도와 혈흔 상태만 구분

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

### WARD-DOYUN-PAST | 과거 도윤 ep03–16
- **SOURCE**: `costumes.md WARD-PAST-DY`, ep03–16
- **PURPOSE**: 과거 도윤 평상시 의상 잠금
- **LOCKS**: CHAR-DOYUN-LOCK, PROP-WATCH-RESIDUAL
- **VARIABLES**: 근무/데이트, 셔츠 젖음
- **ASPECT**: 전신
- **COMPOSITION**: 회청색 셔츠·가는 넥타이·왼손목 시계를 같은 프레임에
- **PROMPT_KO**: `CHAR-DOYUN-LOCK과 완전히 같은 얼굴과 헤어, 여러 번 세탁한 회청색 셔츠, 가는 회색 넥타이, 남색 작업 팬츠, 왼손목의 PROP-WATCH-RESIDUAL, 현재보다 상대를 예상하는 편안한 어깨와 손, 얼굴 나이 변화 없음`
- **PROMPT_EN**: `exact same face and hair as CHAR-DOYUN-LOCK, repeatedly washed blue-gray shirt, narrow gray tie, navy work trousers, PROP-WATCH-RESIDUAL on the left wrist, shoulders and hands more familiar with the other person without making him younger`
- **NEGATIVE**: `different younger actor, new shirt, smartwatch, formal suit`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: ep03–16 과거 도윤만 실제 시계 착용

### WARD-DOYUN-PAST-ACCIDENT | 과거 도윤 ep17–18
- **SOURCE**: `costumes.md WARD-PAST-DY`, ep17–18
- **PURPOSE**: 사고 밤 부상 상태 잠금
- **LOCKS**: CHAR-DOYUN-LOCK, WARD-DOYUN-PAST
- **VARIABLES**: 혈흔 건조 정도
- **ASPECT**: 전신
- **COMPOSITION**: 왼쪽 옆구리의 제한된 얼룩은 보이되 상처 자체는 가림
- **PROMPT_KO**: `WARD-DOYUN-PAST와 같은 의상, 왼쪽 옆구리 셔츠에 손바닥 두 개보다 작은 검붉은 혈흔과 젖은 주름, 열린 상처나 과도한 피 없음, 손목시계와 얼굴 정체성 고정`
- **PROMPT_EN**: `same wardrobe as WARD-DOYUN-PAST, a dark wet blood stain smaller than two palms on the left-flank area of the shirt, no open wound and no excessive blood, wristwatch and exact facial identity preserved`
- **NEGATIVE**: `gore, torn torso, heroic battle damage, blood on present Doyun`
- **POST TEXT**: 없음
- **CONTINUITY CHECK**: ep17–18 과거 사고 장면에만 사용

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
