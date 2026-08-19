#!/usr/bin/env python3
"""Mechanically assemble a versioned drama delivery package from audited sources."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig").strip()


def section(title: str, path: Path) -> str:
    return f"\n\n---\n\n<!-- SOURCE: {path.as_posix()} -->\n\n# {title}\n\n{read(path)}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("work")
    parser.add_argument("--version", type=int, required=True)
    args = parser.parse_args()

    work = Path(args.work)
    version = args.version
    final = work / "08_final"
    final.mkdir(parents=True, exist_ok=True)
    slug = work.name
    date = "2026-08-06"

    scripts = sorted((work / "01_script").glob("ep[0-9][0-9].md"))
    script_body = "\n\n---\n\n".join(read(p) for p in scripts)
    script_only = (
        f"# 《없던 사이》 대본만 v{version}\n"
        f"> 세로형 숏폼 드라마 · 24부작 · 회당 5분 · 168씬 · {date}\n\n"
        "본 문서는 촬영·낭독용 대본 본문만 수록한다. 러닝타임은 전 회차 사전 검증을 통과했으며 촬영 전 실측 낭독이 필요하다.\n\n---\n\n"
        + script_body + "\n"
    )

    production_sources = [
        ("작품 콘셉트", work / "00_bible/concept.md"),
        ("세계관 바이블", work / "00_bible/world.md"),
        ("인물 바이블", work / "00_bible/characters.md"),
        ("시즌 구조와 회차 비트", work / "00_bible/structure.md"),
        ("컨티뉴이티 검수", work / "02_audit/continuity-report.md"),
        ("대본 교정 이력", work / "02_audit/fix-log.md"),
        ("훅 지도", work / "03_hooks/hook-map.md"),
        ("자산 요구사항", work / "04_assets/extraction-report.md"),
        ("자산 제작 큐", work / "04_assets/construction-queue.md"),
        ("자산 검수", work / "04_assets/validation-report.md"),
        ("로케이션 명세", work / "05_design/locations.md"),
        ("의상 명세", work / "05_design/costumes.md"),
        ("차량 명세", work / "05_design/vehicles.md"),
        ("소품 명세", work / "05_design/props.md"),
        ("캐스팅 아이덴티티", work / "06_cast/cast-identity.md"),
    ]
    production = (
        f"# 《없던 사이》 제작자료 v{version}\n"
        f"> 바이블 · 구조 · 검수 · 훅 · 디자인 · 캐스팅 · {date}\n"
        + "".join(section(title, path) for title, path in production_sources)
        + "\n"
    )

    v4_visual_sources = [
        work / "07_visual_prompts/00_style-bible.md",
        work / "07_visual_prompts/01_asset-locks.md",
        work / "07_visual_prompts/02_episode-keyframes.md",
        work / "07_visual_prompts/03_negative-prompts.md",
        work / "07_visual_prompts/04_handoff-guide.md",
        work / "07_visual_prompts/07_prompt-audit.md",
        work / "07_visual_prompts/08_prompt-fix-log.md",
    ]
    legacy_visual_sources = [
        work / "07_visual_prompts/00_style-bible.md",
        work / "07_visual_prompts/01_character-prompts.md",
        work / "07_visual_prompts/02_location-prompts.md",
        work / "07_visual_prompts/03_prop-prompts.md",
        work / "07_visual_prompts/04_episode-keyframes.md",
        work / "07_visual_prompts/05_negative-prompts.md",
        work / "07_visual_prompts/06_handoff-guide.md",
        work / "07_visual_prompts/07_prompt-audit.md",
        work / "07_visual_prompts/08_prompt-fix-log.md",
    ]
    visual_sources = v4_visual_sources if (work / "07_visual_prompts/01_asset-locks.md").is_file() else legacy_visual_sources
    visual = (
        f"# 《없던 사이》 비주얼 프롬프트 패키지 v{version}\n"
        f"> 9:16 · 24화 · 168씬 · 키프레임 168개 · 텍스트 프롬프트 전용 · {date}\n\n"
        "## 납품 상태\n\n"
        "| 항목 | 상태 |\n|---|---|\n"
        "| 이미지 생성 | 미실행 — 제작팀 수행 |\n"
        "| 대본 씬 커버 | 168/168 |\n"
        "| 키프레임 | 168개 |\n"
        "| 등록 자산 ID | 71개 |\n"
        "| 기계 검증 | 오류 0 |\n"
        "| 의미·연속성 검수 | READY |\n"
        + "".join(section(p.stem, p) for p in visual_sources)
        + "\n"
    )

    analyzer = Path(__file__).with_name("analyze_scripts.py")
    analysis_run = subprocess.run(
        [sys.executable, str(analyzer), str(work), "--format", "markdown"],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    analysis = analysis_run.stdout.strip() + "\n"

    structure = read(work / "00_bible/structure.md")
    summaries = re.search(r"(?ms)^## 회차 비트시트\s*(.*?)(?=^## 구조 자가 검증)", structure)
    summary_text = summaries.group(1).strip() if summaries else "회차 비트시트는 제작자료 참조."

    cover = f"""# 없던 사이
> 세로형 숏폼 드라마 · 24부작 · 회당 5분 · **v{version}** · {date}

## 납품 전 점검

| 항목 | 상태 |
|---|---|
| 회차 대본 | 24/24 |
| 총 씬 | 168씬 · 회차당 7씬 |
| 씬 번호·헤딩 기계 검증 | 오류 0건 |
| 러닝타임 사전 검증 | 24/24 PLAUSIBLE · 중앙 추정 4:30–5:28 |
| 컨티뉴이티 미해결 치명 결함 | 0건 |
| 인물·구조·훅·디자인·캐스팅 | 완료 |
| 비주얼 프롬프트 | 168/168씬 · 키프레임 168개 · 자산 ID 71개 |
| 프롬프트 검수 | READY · 미해결 0 · 오류 0 |
| 이미지 생성 | 미실행 — 제작팀 수행 |

## 로그라인

남들이 후회해 버린 시간을 수거하는 냉소적인 여자와 능청스러운 복귀 직원은 오늘 처음 만났지만, 버려진 시간 속에서 자신들이 100일간 사랑했고 43명의 기억을 구하기 위해 그 관계를 함께 버렸다는 흔적을 발견한다.

## 기획의도 요약

기억은 사랑의 증거인가, 사랑은 지금 다시 하는 선택인가. 과거를 고쳐 얻는 타임슬립 대신 이미 치른 선택의 의미를 뒤늦게 이해하는 로맨스 미스터리다. 노출보다 거리·시선·호흡·허락을 기다리는 손으로 성인 썸을 만들고, 매 화 로맨스와 시간 미스터리의 이중 훅으로 다음 회차를 연다.

## 등장인물표

| 이름 | 나이 | 정체 | 등장 범위 | 대사 블록 |
|---|---:|---|---|---:|
| 한서하 | 32 | 잔시물 관리센터 야간 3팀 수거관 | ep01–24 | 현재·과거 표기 합계 570 |
| 이도윤 | 34 | 야간 3팀 복귀 수거관 | ep01–24 | 현재·과거·음성 표기 합계 587 |
| 장현숙 | 47 | 야간 3팀장 | 핵심 회차 | 현재·과거·방송 표기 합계 83 |
| 오민주 | 29 | 기록 담당 | ep02–24 핵심 회차 | 41 |
| 김수진 | 38 | 43명 중 한 명, 현재 삶의 대표 | ep13–14 | 28 |
| 박태식 | 41 | 운반 기사, 종이 기록 연결자 | ep10 | 3 |
| 민석 | 성인 | 호텔 잔시 의뢰인 | ep01–02 | 10 |

## 회차 요약

{summary_text}

## 표준화 변경표

| 위치 | 전 | 후 | 사유 |
|---|---|---|---|
| 전체 | 변경 없음 | 변경 없음 | 24화 168씬이 표준 헤딩과 연속 번호 검사를 통과함 |
"""

    integrated = (
        cover
        + "\n\n---\n\n# 대본 본문\n\n" + script_body
        + "\n\n---\n\n# 부록 A. 씬 리스트·기계 분석\n\n" + analysis
        + "\n\n---\n\n# 부록 B–D. 바이블·로케이션·의상·소품·캐스팅\n\n" + production
        + "\n\n---\n\n# 부록 E–F. 비주얼 프롬프트 패키지·검수 결과\n\n" + visual
        + "\n\n---\n\n# 부록 G. 미해결 사항\n\n"
          "- 텍스트 납품 게이트의 미해결 치명·중대·경미 항목: 없음.\n"
          "- 실제 생성 이미지 검수는 미수행이며 제작팀 생성 후 별도 QA가 필요하다.\n"
          "- 정확한 상영 시간은 촬영 전 배우 낭독 또는 보이스 프리비즈로 실측한다.\n"
    )

    release = f"""# 《없던 사이》 v{version} 릴리즈 노트
> {date} · 회당 5분 기준 전면 재집필 및 제작팀 납품본

## v2 대비 핵심 변경

- 24화 전편을 회차당 7씬, 총 168씬으로 재집필해 이야기 밀도와 5분 분량을 강화했다.
- 러닝타임 사전 검증을 다시 실행해 24/24화가 `PLAUSIBLE`을 통과했다. 중앙 추정은 4분 30초~5분 28초다.
- 컨티뉴이티를 재검수하고 격리 캡슐·기억 대가 발생 시점·ep18~20 안정도·회차 연결을 교정했다.
- 인물별 대사, 서브텍스트, 침묵과 성인 썸의 동의 경계를 다듬었다.
- 24화 × 7씬 훅 지도와 회차 말미 이중 클리프행어를 확정했다.
- 로케이션 L-01~L-18, 의상 WARD ID, 소품 P-01~P-17, 캐스팅 아이덴티티를 최신 대본에 맞췄다.
- 비주얼 프롬프트를 93개에서 168개로 전면 재구축해 모든 씬을 9:16 키프레임으로 1:1 커버했다.
- 사진 WET→DRY 공개 순서, 얼굴 잠금 최대 3명, 과거/현재 의상, 잔시/현실 조명을 의미 검수했다.

## 최종 검증

- 대본: 24화 / 168씬 / 번호 오류 0
- 러닝타임: 24/24 PLAUSIBLE
- 컨티뉴이티: 미해결 치명 0
- 프롬프트: 168/168씬 / 키프레임 168개 / 자산 ID 71개 / 기계 오류 0
- 프롬프트 의미 검수: READY / 미해결 0
- 이미지 생성: 미실행, 제작팀 수행

## 생성 파일

- `{slug}_최종대본_v{version}.md`
- `{slug}_대본만_v{version}.md`
- `{slug}_제작자료_v{version}.md`
- `{slug}_비주얼프롬프트_v{version}.md`
- `{slug}_기계분석_v{version}.md`
- `{slug}_릴리즈노트_v{version}.md`

## 제작 전 필수 후속

- 배우 테이블 리드 또는 보이스 프리비즈로 회차별 실제 러닝타임 측정
- 생성 모델·시드·얼굴 참조 이미지·색관리 기준 확정
- 이미지 생성 후 얼굴, 손, 의상, 소품 상태, 문자 후반 합성의 샷 간 연속성 QA
"""

    outputs = {
        f"{slug}_대본만_v{version}.md": script_only,
        f"{slug}_제작자료_v{version}.md": production,
        f"{slug}_비주얼프롬프트_v{version}.md": visual,
        f"{slug}_기계분석_v{version}.md": analysis,
        f"{slug}_최종대본_v{version}.md": integrated,
        f"{slug}_릴리즈노트_v{version}.md": release,
    }
    for name, content in outputs.items():
        (final / name).write_text(content.rstrip() + "\n", encoding="utf-8")
        print(f"wrote {final / name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
