#!/usr/bin/env python3
"""Build one production-ready visual prompt record for every scripted scene."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


SCENE_RE = re.compile(r"^## S#(?P<num>\d+)\. (?P<head>.+)$", re.M)
CHAR_RE = re.compile(r"^\*\*(?P<name>[^*]+)\*\*$", re.M)

ACTION_EN = {
1:["A damaged faceless couple photo slides beneath the bed as Seoha tags the wardrobe and Doyun enters the loop.","Inside the cramped wardrobe, Doyun braces the wall beside Seoha rather than touching her waist while a tuxedo covers them.","The thirty-seven-second hotel loop resets as they watch the photograph and argue over the cost of extraction.","Their fingertips overlap on the photograph beneath the bed as Doyun pulls Seoha deeper into hiding and immediately releases her wrist.","With eighteen seconds left, Seoha seals the photograph inside a non-real quarantine capsule as the groom recognizes Doyun.","Hyunsuk seals the capsule in the fluorescent sorting room while Doyun instinctively swaps Seoha's lavender coffee for black.","The drying photograph reveals Seoha and Doyun as lovers, leaving their present faces stunned above it."],
2:["Seoha snatches the discarded lavender coffee, tastes it and visibly confirms Doyun's impossible knowledge.","They scan the couple photo and open Doyun's clean personnel record across the transparent sealing table.","In the empty dawn lobby, Minseok freezes over the form when he recognizes Doyun as the old photographer.","Minseok shows a phone gallery of gray error tiles while Doyun remembers the missing lavender detail.","A jolt in the narrow elevator makes Doyun brace the wall beside Seoha, repeating their first impossible distance.","Minju holds out an old film envelope but refuses to release it until Seoha accepts the consequence of looking.","Under red archive light, a negative shows Doyun's handwriting and a reflected Seoha in their old elevator rhythm."],
3:["In the wet mirrored elevator loop, Doyun catches Seoha at the waist without looking when the car jolts.","Doyun kneels as a human step beneath the ceiling hatch while Seoha marks the exact permitted support zone.","Seoha balances on Doyun's thigh and shoulder as his hands hold only the explicitly permitted area.","The mirror overlays past Doyun holding past Seoha in the same pose while present Seoha studies her lost smile.","Current Seoha rests a hand on Doyun's shoulder as both pause one step before testing what their bodies remember.","Past Seoha closes the distance for a kiss in the mirror while the present pair remain separated in front of it.","The elevator doors close on the current pair while one red CCTV indicator continues watching them."],
4:["Old CCTV monitors already show the past couple kissing as present Seoha freezes the frame.","Seoha turns her chair until her knee rests between Doyun's knees, making the evidence review uncomfortably intimate.","A silent close-up of past Doyun's lips plays while present Seoha and Doyun hold their distance over the console.","At the narrow security-room doorway, Seoha straightens Doyun's crooked ID badge and pauses near his collar.","Their fingers wait on opposite sides of the playback control before pressing it together.","Past Doyun looks directly into the security camera and warns the future pair to ask rather than reenact.","The dead monitor reflects present Seoha and Doyun as a new audio-residue alert lights the console."],
5:["A giant glass-like confession waveform rises through the discarded chat room and catches Seoha's probe.","The transparent waveform walls narrow until Seoha and Doyun must stand back-to-chest without touching.","Doyun holds Seoha's cut gloved finger and wraps it with a disinfecting pad while she allows the care.","Magenta waveform bands bind their arms as they pull the deletion key together on Seoha's count.","The hidden waveform resolves into past Doyun's voice while Seoha slowly withdraws her bandaged finger.","The collapsing glass-wave corridor separates them as Seoha throws a safety tether toward Doyun.","At the closing exit, Seoha catches Doyun's wrist and both emerge holding one safety tether and a glowing audio cylinder."],
6:["A glowing audio cylinder lies beneath a red extraction warning as Seoha closes the approval screen.","Hyunsuk holds the cylinder over the sealing box while both leads reach for it from opposite sides.","In the equipment room, Seoha blocks the door and places her palm beside Doyun's on separate approval controls.","Two hands hover above twin buttons during the final three-count before pressing together.","After the lights return, Doyun studies Seoha's badge because her name alone has vanished from his memory.","A diagnostic screen identifies the thirty-second loss while Seoha photographs the blank UI area with shaking hands.","They sit equally distant from one speaker as the sealed cylinder plays and an old watch display wakes inside the evidence bag."],
7:["Black rain floods a cheap motel room, leaving one dry single bed where Seoha and Doyun slide toward the center.","The looping couple argues on the far side of the bed while the real exit disappears beneath black rain.","Seoha reaches beneath the mattress while Doyun holds only her ankle and she anchors her foot against his knee.","They crowd into the last dry patch as Seoha pulls Doyun's soaked shirt inward and he shields her from rain.","A worn rectangular watch aligns exactly with the pale mark on Doyun's wrist under Seoha's fingertips.","Seoha fastens the watch around Doyun's wrist while the past couple gradually overlays the same bed.","The watch display wakes to DAY 100 as a warm food-tent memory replaces the black motel rain around them."],
8:["At a steamed street-food table, the past couple exchange a watch while the present pair watch from the same seats.","Past Doyun holds one end of the gift box as past Seoha straightens a cup instead of answering him.","In rain behind the tent, past Doyun asks permission to stay and past Seoha answers by holding his wrist.","Past Seoha locks the watch onto Doyun as the same clasp closes around present Doyun's wrist.","Present Seoha tries to release the watch before the residual exit materializes it, her fingers paused over his pulse.","The watch falls back onto the table as the past Seoha seems to look toward her present self.","Back in the sorting room, matching pale wrist marks appear while a blue-gray men's sleeve slips from Seoha's locker."],
9:["In the women's locker room, Seoha almost smells the found shirt before Minju reveals the hidden D mark and old laundry tag.","Seoha holds the oversized shirt against herself in the mirror while Minju watches the collar being carefully smoothed.","At the break-room doorway, Seoha sees another employee bandaging Doyun's hand and throws the shirt toward his chest.","Doyun wears the faded shirt over his work tee as Seoha checks the collar and pauses at the missing second button.","Their fingertips meet on one mother-of-pearl button above the wash table before Doyun returns it to Seoha's palm.","A folded receipt emerges from the shirt pocket, held between both their hands without either pulling.","A yellow safety line lights between them as Seoha places the button in Doyun's hand and they walk apart at equal speed."],
10:["Seoha and Doyun walk on opposite sides of a yellow line at exactly the same pace and stop face-to-face without crossing.","Taesik drops a bundle of faded receipts across the yellow line while both leads turn toward him.","Receipts form a map of food tent, laundry, motel and center locations across a transparent worktable.","Hidden behind a loading-bay column, Seoha's palm rests on Doyun's chest while his hand braces concrete beside her.","They remain pressed into the column's narrow shadow as Doyun quietly offers a present-day coffee date.","Hyunsuk catches them, takes one receipt and tears it while neither lead crosses the yellow line.","Each lead holds one torn half revealing the disposal record number as Minju slides a key between them."],
11:["Hyunsuk turns Seoha and Doyun's ID cards face-down on her bare desk before ordering one transfer.","Outside the office, Minju secretly pushes the archive key along the corridor floor toward the arguing pair.","Inside the paper archive, a ledger page protrudes exactly two millimeters as Minju cleans already spotless glasses.","Doyun reads the hundred-day relationship record while Minju admits she witnessed the original disposal.","Both read opposite sides of the residual document without carrying it across the archive boundary.","In the shelf gap, Seoha pulls Doyun inward by his tie while Hyunsuk's shadow passes outside.","Two hands stop over the carbon outlines of their separate signatures on the same disposal form."],
12:["Their two signatures fill the vertical frame, one above the other, as both verify the handwriting.","Doyun steps back to give distance but remains against the archive shelf while Seoha advances one step.","Hyunsuk blocks the archive exit with the sealed final page held between all three adults.","In her office, Hyunsuk turns over the page that reveals forty-three preserved lives.","Forty-three ordinary life images fill the monitor wall while Doyun recognizes Sujin's bodily gaze toward him.","Seoha's hand stops on the document as Hyunsuk warns that one child could forget a parent.","The pair stand apart yet the monitor stability falls from blue-gray toward amber behind them."],
13:["A vertical montage of forty-three ordinary Seoul lives surrounds Seoha and Doyun as they fold the first name out of sight.","Outside the laundry, Doyun hesitates at the door while Sujin irons her child's uniform behind steamed glass.","Sujin recognizes Doyun's name with her mouth before her memory, repeatedly ironing the same sleeve.","A child offers Doyun a worn teal keychain while Seoha keeps her hand nearby without deciding for him.","In the back room, Sujin covers the missing accident-day photo space with a current picture of her child.","Sujin answers her child immediately and refuses an extraction that might endanger that living knowledge.","Outside, Sujin's hand stops short of Doyun's left-flank scar while Seoha tracks the exact location."],
14:["Sujin places the worn keychain before Seoha and asks whether an old choice still belongs to her present self.","Doyun grips then releases the keychain as Sujin keeps ironing and chooses tomorrow's breakfast over lost evidence.","The keychain enters an evidence envelope with its owner field blank while all three adults leave the choice open.","Red traffic light alternates across Seoha and Doyun inside the parked return vehicle as neither opens the door.","During a sudden brake, Doyun's arm crosses before Seoha like a seatbelt and she later holds his wrist.","The vehicle interior light goes dark on their joined hands after both explicitly choose to continue together.","At the parking entrance, Doyun holds the door as the next residual coordinate appears on the handheld terminal."],
15:["On a wet rooftop, past Doyun says he likes Seoha while present Doyun silently forms the same words behind a water tank.","Past Doyun steps aside rather than block Seoha, while present Seoha mirrors her old lifted chin.","Past Seoha pulls Doyun by the tie and kisses him only after his final pause for confirmation.","Present Seoha loosens Doyun's tie and permits exactly one step while he remains still.","Against the access-door wall, Seoha grips Doyun's collar and stops one breath before his lips.","Seoha ends the approach herself and folds the loose tie against Doyun's chest while he accepts the boundary.","A silver house key bounces across the rooftop and opens a residual doorway onto their shared morning home."],
16:["At the threshold of Seoha's residual apartment, crossed men's shoes and women's safety shoes precede the empty shared interior.","Doyun folds the old shirt on the sofa while Seoha hides one stray sock beneath it with her shoe.","Their hands repeat the same coffee ritual and remain layered over one mug handle in the kitchen.","Seoha gives Doyun coffee across the wooden table and touches her cup against his without invoking the past.","Both hold the half-open bedroom doorknob before Doyun closes it at Seoha's present request.","At the bathroom mirror, a wiped finger mark reveals a blank arrow area pointing toward the table.","A four-fold note marked for post text burns away between their hands as the windows turn red with alarm."],
17:["Forty-three faces fracture across vertical monitors as past Doyun bleeds and present Seoha touches the observation glass.","Past Hyunsuk turns a cooling valve while one monitor shows a child failing to recognize a mother.","Behind the cooler, past Seoha presses Doyun's left-flank wound while present Seoha rests a hand over his healed scar.","A relationship-density screen places their hundred days above the danger line as past Doyun moves toward the core alone.","Past and present Doyun each offer an open palm, and both Seoha versions choose to take it.","Two past palms touch the consent terminal together while present Seoha refuses to leave before seeing the process.","Two pen tips hover above the signature fields as forty-three broken voices continue behind them."],
18:["Past Seoha and Doyun read separate consent statements into two glass cylinders and sign at the same instant.","Fragments of meals, arguments, kisses and mornings leave their faces while they keep holding hands.","Past Doyun pauses before embracing Seoha, then holds her only after she grips his shirt in answer.","A no-disclosure clause fills the blank document layout as Hyunsuk turns her ID card face-down and signs witness.","A blade of light divides the pair while they promise to leave any future choice to their future selves.","After erasure, the bleeding strangers face each other and Doyun still holds the door without knowing why.","Present Seoha and Doyun return hand-in-hand as amber status tiles and a separation order appear beneath them."],
19:["Archive boxes holding the hundred-day evidence shake and split with magenta light as a clear barrier drops between the leads.","Hyunsuk offers blue and rust transfer tags while Seoha stops her from attaching Doyun's tag for him.","Across a glass isolation wall, handwritten notes trade decisions while their palms miss each other by one handspan.","Seoha places her isolation pass on Hyunsuk's desk as the current-relationship disposal option is revealed.","A simulation monitor lists every new emotional memory while the blank consent button waits below.","Doyun's isolation bay stands empty except for his transfer tag and a handwritten note on the floor.","On the transfer elevator screen, Doyun removes his hand from close and waits until Seoha asks him to return."],
20:["Across Hyunsuk's red floor line, Seoha and Doyun release one envelope too late and it drops between their feet.","Separate scanners sound together as both mark the exact same defect on opposite worktables.","In the bus-stop loop, each protects the other from a falling sign and open manhole before either can warn them.","They sit with one empty bench space until Seoha explicitly permits Doyun to move exactly one seat closer.","Under the bench, their shoulders touch only after Doyun pauses and Seoha says yes beneath the old man's umbrella.","They return to opposite sides of the red line while the stability display remains at seventy percent.","A blank current-relationship disposal form activates and Seoha breaks the electronic pen into two parallel pieces."],
21:["The two broken pen pieces lie beneath a sixty-nine-percent display as Seoha covers the signature field with her palm.","Minju reveals a protruding appendix and the locked quarantine record for the first couple photograph.","Seoha blocks the archive doorway while Minju awkwardly offers two folded lots for a possible draw.","Back in hotel residual time, Doyun reaches for the photograph while Seoha anchors the exit, reversing their first roles.","Inside the wardrobe, the photograph lies between them as Seoha says she exists inside Doyun's present memory.","Doyun moves Seoha's hand from the photograph to his chest before pressing the extraction control alone.","In the real hotel room, Doyun reads Seoha's badge with polite unfamiliarity while the materialized photograph remembers them."],
22:["Seoha extends the couple photograph toward memory-lost Doyun, then turns its image face-down before he can see.","At the wash basin, Doyun folds his wet sleeve in the familiar way as their fingertips pause over a towel.","At the vending machine, Doyun withdraws from the lavender button without knowing why and accepts Seoha's black coffee.","Walking the corridor, Doyun instinctively moves Seoha to the safe side of a service cart before asking what to do now.","By the corridor window, Seoha asks present Doyun for tomorrow's coffee and waits through the risk of refusal.","Inside the elevator, Seoha steps closer after telling Doyun she is interested in the person standing there now.","Doyun holds the elevator door as a new warning demands destruction of every remaining past-life artifact."],
23:["All hundred-day evidence sits inside one transparent disposal box while Hyunsuk stands back from the couple's choice.","Doyun presses the crown of a watch he cannot remember as Seoha holds the detached shirt button.","Minju inventories photograph, watch, shirt, receipts and two audio tracks without cleaning her tear-filled glasses.","Doyun reaches toward the face-down photograph, then chooses not to see it while Seoha's hand rests on the print.","At the control desk, Seoha distinguishes destroying evidence from destroying their relationship as both face the two buttons.","Their little fingers link while the other fingers hover over separate controls and they fix tomorrow's coffee time.","The two hands descend toward white-lit buttons, then pause when Doyun asks whether tomorrow is only coffee."],
24:["The evidence dissolves into white light and all forty-three status tiles return to blue-gray as Hyunsuk turns her ID forward.","At the disposal-room exit, Seoha asks permission before straightening Doyun's badge and admits she anticipates tomorrow.","Doyun holds the center exit door until Seoha passes, then leaves the doorway to walk beside her.","At a small morning cafe, their differently flawed ceramic cups almost touch as Doyun asks permission for one question.","Doyun asks directly about a kiss while Seoha refuses only the indoor location and takes the bill toward the alley.","In a narrow band of alley sunlight, Seoha pulls Doyun's loose tie and initiates a brief consensual kiss.","A work terminal offers disposal of the last twelve seconds; Seoha cancels it and takes Doyun's offered hand."],
}

CHAR_CODES = {
    "서하": "CHAR-SEOHA-LOCK", "과거 서하": "CHAR-SEOHA-LOCK", "현재 서하": "CHAR-SEOHA-LOCK",
    "도윤": "CHAR-DOYUN-LOCK", "과거 도윤": "CHAR-DOYUN-LOCK", "현재 도윤": "CHAR-DOYUN-LOCK",
    "현숙": "CHAR-HYUNSUK-LOCK", "과거 현숙": "CHAR-HYUNSUK-LOCK", "민주": "CHAR-MINJU-LOCK",
    "수진": "CHAR-SUJIN-LOCK", "태식": "CHAR-TAESIK-LOCK", "민석": "CHAR-MINSEOK-LOCK", "아이": "CHAR-CHILD-LOCK",
}

LOC_RULES = [
    (("호텔",), "LOC-HOTEL-807", "the aging Hotel 807 room and corridor system"),
    (("오피스 엘리베이터", "엘리베이터 제어반", "엘리베이터 천장"), "LOC-OFFICE-ELEVATOR", "the wet three-mirror office elevator loop"),
    (("채팅방", "파형", "삭제 키", "잔시 붕괴 통로"), "LOC-CHAT-RESIDUAL", "the narrowing glass-waveform message residue"),
    (("모텔방",), "LOC-MOTEL-ROOM", "the black-rain motel room with one dry bed"),
    (("포장마차",), "LOC-FOOD-TENT", "the steamed Seoul street-food tent"),
    (("세탁소",), "LOC-LAUNDROMAT", "Sujin's working neighborhood laundry"),
    (("옥상",), "LOC-ROOFTOP", "the wet ordinary rooftop between water tank and access door"),
    (("거실", "부엌", "식탁", "침실", "욕실", "서하의 집"), "LOC-SEOHA-HOME", "Seoha's carefully maintained residual apartment"),
    (("발생실", "코어", "기억 추출", "동의 단말기", "소거", "소실"), "LOC-ACCIDENT-CORE", "the industrial high-density memory accident chamber"),
    (("버스 정류장", "정류장 벤치"), "LOC-BUS-STOP", "the wet outer-Seoul bus-stop loop"),
    (("카페", "골목"), "LOC-CAFE-ALLEY", "the ordinary present-day cafe and narrow morning alley"),
    (("서울 여러 장소",), "LOC-SEOUL-MONTAGE", "a grounded montage of ordinary present-day Seoul lives"),
    (("보안실", "기록실", "기록창고", "팀장실", "격리", "시스템실", "아카이브", "이송 엘리베이터"), "LOC-CENTER-ADMIN", "the narrow administrative, archive and isolation zone of the center"),
    (("장비실", "하역장", "소각", "센터 출입구", "주차장", "귀환 차량"), "LOC-CENTER-INDUSTRIAL", "the worn industrial equipment, loading and disposal zone of the center"),
]

PROP_RULES = [
    (("사진",), "PROP-PHOTO-WET"), (("격리 캡슐",), "PROP-QUARANTINE-CAPSULE"),
    (("시계", "손목"), "PROP-WATCH-RESIDUAL"), (("셔츠", "단추"), "PROP-SHIRT-FOUND"),
    (("영수증",), "PROP-RECEIPTS"), (("실린더", "음성 트랙"), "PROP-AUDIO-TRACK"),
    (("동의서", "폐기 신청서", "서명란"), "PROP-CONSENT-FORM"), (("43명", "마흔셋", "안정도"), "PROP-LIST-43"),
    (("단말기", "스캐너", "반출기"), "PROP-HANDHELD"), (("사원증", "명찰"), "PROP-ID-CARD"),
    (("열쇠고리",), "PROP-KEYCHAIN-WORN"), (("검은 태그", "태그 신호", "태그를"), "PROP-TAG-BLACK"),
    (("빨간 선", "노란 선", "부러진 펜", "펜촉"), "PROP-LINES-PEN"), (("메모", "이송표"), "PROP-ISOLATION-NOTES"),
    (("02:17", "쪽지", "집 열쇠"), "PROP-NOTE-0217"), (("도자기 컵", "컵이", "커피 컵"), "PROP-COFFEE-PRESENT"),
]

def ward(ep: int, text: str) -> list[str]:
    out=[]
    if any(x in text for x in ("과거 서하", "과거의 서하")): out.append("WARD-SEOHA-PAST")
    if any(x in text for x in ("과거 도윤", "과거의 도윤")):
        out.append("WARD-DOYUN-PAST-ACCIDENT" if ep >= 17 else "WARD-DOYUN-PAST")
    if "서하" in text and not ("과거 서하" in text and "현재 서하" not in text):
        out.append(f"WARD-SEOHA-A{1 if ep<=6 else 2 if ep<=16 else 3 if ep<=23 else 4}")
    if "도윤" in text and not ("과거 도윤" in text and "현재 도윤" not in text):
        out.append(f"WARD-DOYUN-A{1 if ep<=6 else 2 if ep<=16 else 3 if ep<=23 else 4}")
    return list(dict.fromkeys(out))

def loc(head: str) -> tuple[str,str]:
    for keys, code, desc in LOC_RULES:
        if any(k in head for k in keys): return code, desc
    return "LOC-CENTER-SORT", "the worn discarded-time sorting floor and adjoining center corridor"

def visual_ko(body: str) -> str:
    paras = re.split(r"\n\s*\n", body.strip())
    picked=[]
    for p in paras:
        q=" ".join(x.strip() for x in p.splitlines()).strip()
        if not q or q.startswith("**") or q.startswith("[") or q.startswith("    ["): continue
        q=re.sub(r"`([^`]+)`", r"[후반 합성 영역]", q)
        picked.append(q)
        if len(" ".join(picked)) >= 110 or len(picked) == 2: break
    return " ".join(picked) or "대본의 인물들이 다음 선택 직전에 멈춘 핵심 시각 순간."

def build(work: Path) -> str:
    entries=[]
    for ep in range(1,25):
        path=work/"01_script"/f"ep{ep:02d}.md"
        text=path.read_text(encoding="utf-8")
        matches=list(SCENE_RE.finditer(text))
        assert len(matches)==7, f"{path.name}: expected 7 scenes"
        assert len(ACTION_EN[ep])==7
        for idx,m in enumerate(matches):
            sn=int(m.group("num")); head=m.group("head").strip()
            body=text[m.end():matches[idx+1].start() if idx+1<len(matches) else len(text)]
            full=head+"\n"+body
            loc_id,loc_en=loc(head)
            speaker_chars=[]
            for n in CHAR_RE.findall(body):
                base=n.replace("(방송)","").strip()
                if base in CHAR_CODES: speaker_chars.append(CHAR_CODES[base])
            chars=[]
            if "서하" in full: chars.append("CHAR-SEOHA-LOCK")
            if "도윤" in full: chars.append("CHAR-DOYUN-LOCK")
            if ep == 1 and sn <= 5: speaker_chars.append("CHAR-MINSEOK-LOCK")
            chars=list(dict.fromkeys(chars + speaker_chars))[:3]
            props=[]
            for keys,code in PROP_RULES:
                if any(k in full for k in keys): props.append(code)
            props=list(dict.fromkeys(props))
            if "PROP-PHOTO-WET" in props and not (ep == 1 and sn <= 6):
                props=["PROP-PHOTO-DRY" if p=="PROP-PHOTO-WET" else p for p in props]
            residual = (
                ep == 3 or ep == 5 or ep == 7 or ep == 15 or ep == 16 or ep == 17
                or (ep == 1 and sn <= 5) or (ep == 8 and sn <= 6)
                or (ep == 18 and sn <= 6) or (ep == 20 and 3 <= sn <= 5)
                or (ep == 21 and 4 <= sn <= 6)
            )
            if ep == 24 and sn >= 3:
                light = "LIGHT-PRESENT-MORNING"
            elif residual:
                light = "LIGHT-RESIDUAL-TIME"
            elif ep in (13, 14) and (loc_id in ("LOC-LAUNDROMAT", "LOC-SEOUL-MONTAGE")):
                light = "LIGHT-REALITY-DAY"
            elif loc_id == "LOC-HOTEL-807" or (ep == 14 and loc_id == "LOC-CENTER-INDUSTRIAL"):
                light = "LIGHT-REALITY-NIGHT"
            else:
                light = "LIGHT-CENTER-NIGHT"
            locks=["STYLE-MASTER","CAM-VERTICAL-MASTER",loc_id,*chars,*ward(ep,full),*props,light]
            locks=list(dict.fromkeys(locks))
            ko=visual_ko(body)
            post=", ".join(dict.fromkeys(re.findall(r"`([^`]+)`", body))) or "없음"
            purpose="오프닝 훅" if sn==1 else "회차 클리프행어" if sn==7 else "씬 핵심 전환"
            char_en="the locked adult Korean characters named in LOCKS"
            action=ACTION_EN[ep][sn-1]
            entries.append(f'''### KF-EP{ep:02d}-S{sn:02d}-01 | {head}\n\n- **SOURCE**: 01_script/ep{ep:02d}.md S#{sn}, characters.md, costumes.md, locations.md, props.md\n- **PURPOSE**: {ep}화 {sn}씬 {purpose} 대표 정지 프레임\n- **LOCKS**: {", ".join(locks)}\n- **VARIABLES**: 대본에 명시된 표정 강도, 시선, 손 위치, 젖음·혈흔·소품 상태만 변경\n- **ASPECT**: 9:16\n- **COMPOSITION**: 얼굴은 상단 중앙, 허락을 기다리는 손과 핵심 소품은 하단 35%, 인물은 좌우 분산보다 전후 깊이로 배치, 상단 12%·하단 18% 안전영역\n- **PROMPT_KO**: `STYLE-MASTER와 모든 LOCKS의 승인 정체성·의상·공간·소품을 정확히 유지한 한국 실사 드라마 스틸. {ko} 한 이미지에는 이 순간의 주행동 하나와 보조 반응 하나만 담는다. 손가락 간격과 시선 방향이 모바일 화면에서도 읽히며, 동의 전 접촉은 벽·문·소품에서 멈춘다. 자연스러운 피부와 사용감 있는 재질, 실제 광원, 절제된 잔시 효과, 9:16 세로 구도. 생성 단계 문자 금지.`\n- **PROMPT_EN**: `Vertical 9:16 live-action Korean drama still in {loc_en}. Preserve {char_en}, every approved wardrobe ID, exact prop state and fixed set geometry from LOCKS. {action} Freeze one primary action and no more than one supporting reaction at the unfinished breath before resolution. Keep eye direction, finger spacing and consent state readable on a phone screen; hands pause on walls, doors or props before permission. Natural skin, worn physical materials, practical light, restrained discarded-time effects, no generated text.`\n- **NEGATIVE**: NEG-GLOBAL, NEG-CONTINUITY, NEG-CHARACTER, NEG-TEXT, NEG-RATING{", NEG-RESIDUAL-TIME" if light=="LIGHT-RESIDUAL-TIME" else ""}\n- **POST TEXT**: {post}\n- **CONTINUITY CHECK**: ep{ep:02d} 직전·직후 씬과 CHAR 얼굴·헤어, {", ".join(ward(ep,full)) or "기능 인물 의상"}, {loc_id} 구조, {", ".join(props) or "소품 없음"}의 소유·젖음·파손 상태를 동일하게 유지\n''')
    assert len(entries)==168
    return "# 《없던 사이》 24화·168씬 9:16 키프레임 프롬프트 v2\n\n> 모든 씬 최소 1개. 이미지 생성 미실행. LOCKS는 승인 자산만 사용하며 화면 문자는 POST TEXT로 후반 합성한다.\n\n"+"\n".join(entries)

def main()->int:
    p=argparse.ArgumentParser(); p.add_argument("work_dir",type=Path); p.add_argument("--output",type=Path,default=Path("07_visual_prompts/02_episode-keyframes.md")); a=p.parse_args()
    out=a.output if a.output.is_absolute() else a.work_dir/a.output
    out.write_text(build(a.work_dir),encoding="utf-8")
    print(f"wrote {out} with 168 scene keyframes")
    return 0

if __name__=="__main__": raise SystemExit(main())
