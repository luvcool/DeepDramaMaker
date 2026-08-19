#!/usr/bin/env python3
"""Validate deterministic structure and scene coverage of drama visual prompts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path


SCENE_RE = re.compile(r"^##\s+S#(?P<number>\d+)\.", re.MULTILINE)
KF_RE = re.compile(r"^###\s+(?P<id>KF-EP(?P<ep>\d{2})-S(?P<scene>\d{2})-(?P<take>\d{2}))\b", re.MULTILINE)
ASSET_ID_RE = re.compile(r"^###\s+(?P<id>(?:STYLE|CAM|LIGHT|GRADE|RATING|CHAR|WARD|LOC|PROP|NEG)-[A-Z0-9-]+)\b", re.MULTILINE)

V4_REQUIRED_FILES = (
    "00_style-bible.md",
    "01_asset-locks.md",
    "02_episode-keyframes.md",
    "03_negative-prompts.md",
    "04_handoff-guide.md",
)

LEGACY_REQUIRED_FILES = (
    "00_style-bible.md",
    "01_character-prompts.md",
    "02_location-prompts.md",
    "03_prop-prompts.md",
    "04_episode-keyframes.md",
    "05_negative-prompts.md",
    "06_handoff-guide.md",
)

REQUIRED_KF_FIELDS = (
    "SOURCE",
    "PURPOSE",
    "LOCKS",
    "VARIABLES",
    "ASPECT",
    "COMPOSITION",
    "PROMPT_KO",
    "PROMPT_EN",
    "NEGATIVE",
    "POST TEXT",
    "CONTINUITY CHECK",
)


def scene_keys(script_dir: Path) -> set[str]:
    keys: set[str] = set()
    for path in sorted(script_dir.glob("ep*.md")):
        ep_match = re.fullmatch(r"ep(\d{2})\.md", path.name)
        if not ep_match:
            continue
        ep = ep_match.group(1)
        text = path.read_text(encoding="utf-8")
        for match in SCENE_RE.finditer(text):
            keys.add(f"EP{ep}-S{int(match.group('number')):02d}")
    return keys


def parse_blocks(text: str) -> list[tuple[str, str]]:
    matches = list(KF_RE.finditer(text))
    blocks: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks.append((match.group("id"), text[match.start():end]))
    return blocks


def validate(work_dir: Path) -> dict[str, object]:
    prompt_dir = work_dir / "07_visual_prompts"
    issues: list[dict[str, str]] = []
    is_v4 = (prompt_dir / "01_asset-locks.md").is_file() or (prompt_dir / "02_episode-keyframes.md").is_file()
    required_files = V4_REQUIRED_FILES if is_v4 else LEGACY_REQUIRED_FILES
    for filename in required_files:
        if not (prompt_dir / filename).is_file():
            issues.append({"level": "fatal", "location": filename, "message": "필수 파일 없음"})

    scripts = scene_keys(work_dir / "01_script")
    keyframe_path = prompt_dir / ("02_episode-keyframes.md" if is_v4 else "04_episode-keyframes.md")
    text = keyframe_path.read_text(encoding="utf-8") if keyframe_path.is_file() else ""
    blocks = parse_blocks(text)
    ids = [item[0] for item in blocks]
    for duplicate, count in sorted(Counter(ids).items()):
        if count > 1:
            issues.append({"level": "fatal", "location": duplicate, "message": "중복 키프레임 ID"})

    covered = {"-".join(item_id.split("-")[1:3]) for item_id in ids}
    if keyframe_path.is_file():
        for missing in sorted(scripts - covered):
            issues.append({"level": "fatal", "location": missing, "message": "대본 씬 키프레임 누락"})
        for extra in sorted(covered - scripts):
            issues.append({"level": "major", "location": extra, "message": "대본에 없는 씬 키프레임"})

    for item_id, block in blocks:
        for field in REQUIRED_KF_FIELDS:
            if not re.search(rf"^- \*\*{re.escape(field)}\*\*:", block, re.MULTILINE):
                issues.append({"level": "major", "location": item_id, "message": f"필드 누락: {field}"})

    asset_ids: list[str] = []
    for filename in required_files:
        path = prompt_dir / filename
        if path.is_file():
            asset_ids.extend(match.group("id") for match in ASSET_ID_RE.finditer(path.read_text(encoding="utf-8")))
    for duplicate, count in sorted(Counter(asset_ids).items()):
        if count > 1:
            issues.append({"level": "major", "location": duplicate, "message": "중복 자산 ID"})

    return {
        "work_dir": str(work_dir.resolve()),
        "script_scene_count": len(scripts),
        "covered_scene_count": len(scripts & covered),
        "keyframe_count": len(ids),
        "asset_id_count": len(asset_ids),
        "issues": issues,
    }


def to_markdown(report: dict[str, object]) -> str:
    issues = report["issues"]
    lines = [
        "# 비주얼 프롬프트 기계 검증",
        "",
        f"- 대본 씬: {report['script_scene_count']}",
        f"- 커버 씬: {report['covered_scene_count']}",
        f"- 키프레임: {report['keyframe_count']}",
        f"- 자산 ID: {report['asset_id_count']}",
        f"- 오류: {len(issues)}",
        "",
        "| 등급 | 위치 | 내용 |",
        "|---|---|---|",
    ]
    if issues:
        for issue in issues:
            lines.append(f"| {issue['level']} | {issue['location']} | {issue['message']} |")
    else:
        lines.append("| - | - | 없음 |")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("work_dir", type=Path)
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        report = validate(args.work_dir)
    except (OSError, UnicodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    output = json.dumps(report, ensure_ascii=False, indent=2) + "\n" if args.format == "json" else to_markdown(report)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)
    return 1 if report["issues"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
