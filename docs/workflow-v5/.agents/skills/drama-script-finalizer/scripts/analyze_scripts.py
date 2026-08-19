#!/usr/bin/env python3
"""Extract deterministic production metadata from drama Markdown scripts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


SCENE_RE = re.compile(
    r"^##\s+S#(?P<number>\d+)\.\s*(?P<location>.+?)\s*/\s*"
    r"(?P<interior>내부|외부|내·외|내부·외부)\s*/\s*(?P<time>.+?)\s*$"
)
CHARACTER_RE = re.compile(r"^\*\*(?P<name>[^*]+)\*\*\s*$")
def parse_text(text: str, source: str) -> dict[str, Any]:
    """Parse one episode without performing file I/O; useful for validation tests."""
    scenes: list[dict[str, Any]] = []
    dialogue_blocks: Counter[str] = Counter()
    current_scene: dict[str, Any] | None = None
    pending_character: str | None = None

    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        scene_match = SCENE_RE.match(line)
        if scene_match:
            current_scene = {
                "number": int(scene_match.group("number")),
                "location": scene_match.group("location").strip(),
                "interior": scene_match.group("interior"),
                "time": scene_match.group("time").strip(),
                "characters": [],
                "line": line_number,
            }
            scenes.append(current_scene)
            pending_character = None
            continue

        character_match = CHARACTER_RE.match(line)
        if character_match and current_scene is not None:
            name = character_match.group("name").strip()
            if name not in current_scene["characters"]:
                current_scene["characters"].append(name)
            pending_character = name
            continue

        if pending_character is None or not line:
            continue
        if line.startswith("(") and line.endswith(")"):
            continue
        if line.startswith("[") or line.startswith("#"):
            pending_character = None
            continue

        dialogue_blocks[pending_character] += 1
        pending_character = None

    numbers = [scene["number"] for scene in scenes]
    expected = list(range(1, len(numbers) + 1))
    issues: list[str] = []
    if numbers != expected:
        issues.append(f"씬 번호가 1부터 연속이 아님: {numbers}")
    duplicates = sorted(number for number, count in Counter(numbers).items() if count > 1)
    if duplicates:
        issues.append(f"중복 씬 번호: {duplicates}")

    return {
        "source": source,
        "scene_count": len(scenes),
        "scenes": scenes,
        "dialogue_blocks": dict(sorted(dialogue_blocks.items())),
        "issues": issues,
    }


def analyze_work(work_dir: Path) -> dict[str, Any]:
    script_dir = work_dir / "01_script"
    if not script_dir.is_dir():
        raise FileNotFoundError(f"대본 폴더가 없음: {script_dir}")

    episode_files = sorted(script_dir.glob("ep*.md"))
    if not episode_files:
        raise FileNotFoundError(f"대본 파일이 없음: {script_dir / 'ep*.md'}")

    episodes = []
    character_totals: Counter[str] = Counter()
    location_usage: dict[str, list[str]] = defaultdict(list)

    for episode_file in episode_files:
        parsed = parse_text(episode_file.read_text(encoding="utf-8"), episode_file.name)
        episodes.append(parsed)
        character_totals.update(parsed["dialogue_blocks"])
        for scene in parsed["scenes"]:
            location_usage[scene["location"]].append(
                f"{episode_file.stem} S#{scene['number']}"
            )

    return {
        "work_dir": str(work_dir.resolve()),
        "episodes": episodes,
        "character_dialogue_blocks": dict(sorted(character_totals.items())),
        "location_usage": dict(sorted(location_usage.items())),
        "issue_count": sum(len(episode["issues"]) for episode in episodes),
    }


def to_markdown(report: dict[str, Any]) -> str:
    lines = ["# 대본 기계 분석", ""]
    lines.extend(["## 회차별 씬 점검", "", "| 회차 | 씬 수 | 오류 |", "|---|---:|---|"])
    for episode in report["episodes"]:
        issue_text = "<br>".join(episode["issues"]) if episode["issues"] else "없음"
        lines.append(f"| {episode['source']} | {episode['scene_count']} | {issue_text} |")

    lines.extend(["", "## 등장인물 대사 블록 수", "", "| 인물 | 블록 수 |", "|---|---:|"])
    for name, count in report["character_dialogue_blocks"].items():
        lines.append(f"| {name} | {count} |")

    lines.extend(["", "## 로케이션 사용표", "", "| 장소 | 사용 씬 |", "|---|---|"])
    for location, uses in report["location_usage"].items():
        lines.append(f"| {location} | {', '.join(uses)} |")

    lines.extend(["", "## 씬 리스트", ""])
    for episode in report["episodes"]:
        lines.extend([f"### {episode['source']}", "", "| 씬 | 장소 | 내외 | 시간 | 등장인물 |", "|---:|---|---|---|---|"])
        for scene in episode["scenes"]:
            characters = ", ".join(scene["characters"])
            lines.append(
                f"| {scene['number']} | {scene['location']} | {scene['interior']} | "
                f"{scene['time']} | {characters} |"
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="드라마 Markdown 대본에서 씬·인물·로케이션 메타데이터를 추출합니다."
    )
    parser.add_argument("work_dir", type=Path, help="manifest.json이 있는 작품 폴더")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--output", type=Path, help="결과 파일. 생략하면 표준 출력")
    args = parser.parse_args()

    try:
        report = analyze_work(args.work_dir)
    except (OSError, UnicodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.format == "json":
        output = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    else:
        output = to_markdown(report)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)

    return 1 if report["issue_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
