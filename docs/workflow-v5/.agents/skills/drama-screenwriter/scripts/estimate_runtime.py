#!/usr/bin/env python3
"""Estimate episode runtime and enforce the manifest target.

This is a conservative preflight, not a substitute for a recorded table read.
Exit 1 when any episode's credible range misses the target tolerance.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


SPEAKER_RE = re.compile(r"^\*\*[^*]+\*\*$")
SCENE_RE = re.compile(r"^## S#", re.M)
HOLD_RE = re.compile(r"(?<!\d)(\d+(?:\.\d+)?)\s*초")


@dataclass
class Metrics:
    scenes: int = 0
    dialogue_chars: int = 0
    dialogue_blocks: int = 0
    action_units: int = 0
    explicit_seconds: float = 0.0


def count_visible_chars(text: str) -> int:
    return sum(ch.isalnum() for ch in text)


def analyze(text: str) -> Metrics:
    m = Metrics(scenes=len(SCENE_RE.findall(text)))
    in_dialogue = False
    for raw in text.splitlines():
        line = raw.strip()
        if SPEAKER_RE.fullmatch(line):
            in_dialogue = True
            m.dialogue_blocks += 1
            continue
        if not line:
            in_dialogue = False
            continue
        if line.startswith(("#", ">")):
            continue
        if in_dialogue:
            if not (line.startswith("(") and line.endswith(")")):
                m.dialogue_chars += count_visible_chars(line)
            continue
        if line.startswith("`") and line.endswith("`"):
            continue
        clean = line.strip(" []")
        m.action_units += max(1, sum(clean.count(ch) for ch in ".!?"))
        # Count only authored holds, not story facts such as "37초가 반복된다".
        if line.startswith("[") or "정적" in clean or "홀드" in clean or "침묵" in clean:
            m.explicit_seconds += sum(float(x) for x in HOLD_RE.findall(clean))
    return m


def estimate(m: Metrics) -> tuple[float, float, float]:
    low = (
        m.dialogue_chars / 4.8
        + m.dialogue_blocks * 0.25
        + m.action_units * 1.5
        + m.scenes * 1.0
        + m.explicit_seconds
    )
    point = (
        m.dialogue_chars / 4.1
        + m.dialogue_blocks * 0.5
        + m.action_units * 1.6
        + m.scenes * 1.5
        + m.explicit_seconds
    )
    high = (
        m.dialogue_chars / 3.5
        + m.dialogue_blocks * 0.8
        + m.action_units * 3.0
        + m.scenes * 2.0
        + m.explicit_seconds
    )
    return low, point, high


def clock(seconds: float) -> str:
    seconds = int(round(seconds))
    return f"{seconds // 60}:{seconds % 60:02d}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("work", help="work folder containing manifest.json and 01_script/")
    ap.add_argument("--target-min", type=float, help="override manifest runtime_min")
    ap.add_argument("--tolerance-sec", type=float, help="default: 10%% of target, minimum 15s")
    ap.add_argument("--output", help="optional UTF-8 Markdown report path")
    args = ap.parse_args()

    work = Path(args.work).resolve()
    manifest_path = work / "manifest.json"
    script_dir = work / "01_script"
    if not manifest_path.is_file() or not script_dir.is_dir():
        print("manifest.json 또는 01_script/를 찾을 수 없습니다.", file=sys.stderr)
        return 2
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    target_min = args.target_min if args.target_min is not None else float(manifest["runtime_min"])
    target = target_min * 60
    tolerance = args.tolerance_sec if args.tolerance_sec is not None else max(15.0, target * 0.10)
    acceptable_low, acceptable_high = target - tolerance, target + tolerance

    rows = []
    failures = 0
    for path in sorted(script_dir.glob("ep[0-9][0-9].md")):
        metrics = analyze(path.read_text(encoding="utf-8"))
        low, point, high = estimate(metrics)
        if point < acceptable_low:
            verdict = "SHORT"
            failures += 1
        elif point > acceptable_high:
            verdict = "LONG"
            failures += 1
        else:
            verdict = "PLAUSIBLE"
        rows.append((path.name, metrics, low, point, high, verdict))

    report = [
        "# 대본 러닝타임 사전 검증",
        "",
        f"> 목표: 회당 {target_min:g}분 · 허용 범위 {clock(acceptable_low)}–{clock(acceptable_high)} · 실제 촬영 전 낭독 검증 별도",
        "",
        "| 회차 | 씬 | 대사 유효문자 | 대사 블록 | 행동 단위 | 명시 정적 | 중앙 추정 | 참고 범위 | 판정 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for name, m, low, point, high, verdict in rows:
        report.append(
            f"| {name} | {m.scenes} | {m.dialogue_chars} | {m.dialogue_blocks} | "
            f"{m.action_units} | {clock(m.explicit_seconds)} | {clock(point)} | {clock(low)}–{clock(high)} | {verdict} |"
        )
    report += [
        "",
        f"- 회차 수: {len(rows)}",
        f"- 실패: {failures}",
        "- `PLAUSIBLE`은 중앙 추정치가 허용 범위에 들어온다는 뜻이며 정확한 러닝타임 보증이 아니다.",
        "- 최종 촬영 전 배우 낭독 또는 보이스 프리비즈로 실측한다.",
    ]
    output = "\n".join(report) + "\n"
    if args.output:
        out = Path(args.output)
        if not out.is_absolute():
            out = work / out
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(output, encoding="utf-8")
    print(output, end="")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
