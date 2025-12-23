#!/usr/bin/env python3
"""Canonicalize Markdown formatting to match the repo's Markdown guardrails.

Behaviors:
- Normalize ATX headings: single space after hashes, no trailing hashes.
- Standardize unordered bullets to "-" with two-space indentation steps.
- Strip trailing whitespace.
- Collapse runs of blank lines to a single blank line.
- Enforce a single trailing newline at EOF.

Usage:
- Default (fix in-place): `python scripts/canonicalize_md.py`
- Explicit paths: `python scripts/canonicalize_md.py --fix docs/file.md README.md`
- Check-only (no writes): `python scripts/canonicalize_md.py --check`
- Auto-discovery uses `git diff --name-only` (staged + unstaged). Pass paths explicitly for new/untracked files.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable, List, Sequence, Set


HEADING_RE = re.compile(r"^(#{1,6})(\s*)(.*?)(\s*#+\s*)?$")
BULLET_RE = re.compile(r"^([ \t]*)([-*+])(\s+)(.*)$")


def normalize_line(line: str) -> str:
    """Apply per-line Markdown normalization rules."""
    line = line.rstrip(" \t")

    heading_match = HEADING_RE.match(line)
    if heading_match and heading_match.group(1):
        hashes = heading_match.group(1)
        text = (heading_match.group(3) or "").strip()
        return f"{hashes} {text}".rstrip()

    bullet_match = BULLET_RE.match(line)
    if bullet_match:
        indent_raw = bullet_match.group(1).replace("\t", "  ")
        indent_len = (len(indent_raw) // 2) * 2  # snap to multiples of 2
        indent = " " * indent_len
        content = bullet_match.group(4)
        return f"{indent}- {content}"

    return line


def canonicalize_text(text: str) -> str:
    """Canonicalize Markdown text according to repo rules."""
    lines = text.splitlines()
    new_lines: List[str] = []
    blank_run = 0

    for line in lines:
        normalized = normalize_line(line)
        if normalized.strip() == "":
            blank_run += 1
            if blank_run > 1:
                continue
            new_lines.append("")
            continue

        blank_run = 0
        new_lines.append(normalized)

    canonical = "\n".join(new_lines).rstrip("\n") + "\n"
    return canonical


def run_sanity_checks() -> None:
    """Quick self-checks to catch regressions."""
    sample = "One\n\n\nTwo\n \n\nThree\n"
    expected = "One\n\nTwo\n\nThree\n"
    assert (
        canonicalize_text(sample) == expected
    ), "Collapses multi-blank-line sequences"

    bullets = "#Title##\n\n* item\n\t+ sub\n"
    bullets_expected = "# Title\n\n- item\n  - sub\n"
    assert (
        canonicalize_text(bullets) == bullets_expected
    ), "Heading and bullet normalization preserved"

    trailing = "Line with space \nLine2"
    trailing_expected = "Line with space\nLine2\n"
    assert (
        canonicalize_text(trailing) == trailing_expected
    ), "Trailing whitespace removed and EOF newline enforced"


def discover_git_markdown_paths() -> List[Path]:
    """Return Markdown files changed in git (staged or unstaged)."""
    candidates: Set[Path] = set()
    commands = [
        ["git", "diff", "--name-only", "--cached"],
        ["git", "diff", "--name-only"],
    ]

    for cmd in commands:
        try:
            result = subprocess.run(
                cmd, check=False, capture_output=True, text=True
            )
        except FileNotFoundError:
            # git not available
            return []

        if result.returncode != 0:
            continue

        for line in result.stdout.splitlines():
            path = Path(line.strip())
            if path.suffix.lower() == ".md":
                candidates.add(path)

    return sorted(candidates)


def dedupe_preserve_order(paths: Iterable[Path]) -> List[Path]:
    seen: Set[Path] = set()
    ordered: List[Path] = []
    for p in paths:
        if p in seen:
            continue
        seen.add(p)
        ordered.append(p)
    return ordered


def canonicalize_file(path: Path) -> bool:
    """Rewrite file if needed. Returns True if content changed."""
    try:
        original = path.read_text(encoding="utf-8", errors="replace")
    except (FileNotFoundError, IsADirectoryError):
        return False

    updated = canonicalize_text(original)
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Canonicalize Markdown formatting (check or fix)."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Explicit Markdown file paths. If omitted, uses git diff --name-only (staged + unstaged).",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--check",
        action="store_true",
        help="Check for formatting drift (no writes).",
    )
    mode.add_argument(
        "--fix",
        action="store_true",
        help="Rewrite files in place.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    run_sanity_checks()

    mode = "check" if args.check else "fix"
    defaulted_mode = not args.check and not args.fix
    if defaulted_mode:
        print("No mode specified; defaulting to --fix.")

    explicit_paths = [Path(p) for p in args.paths]
    targets = dedupe_preserve_order(
        explicit_paths if explicit_paths else discover_git_markdown_paths()
    )

    # Filter to .md files only
    targets = [p for p in targets if p.suffix.lower() == ".md"]

    if not targets:
        if explicit_paths:
            print("No Markdown files matched the provided paths.")
        else:
            print("No staged or modified Markdown files found via git diff.")
        if defaulted_mode:
            print("Tip: provide paths explicitly to format new/untracked files.")
        return 0

    changed: List[Path] = []
    for path in targets:
        if not path.exists() or not path.is_file():
            print(f"Skipping missing path: {path}")
            continue

        if mode == "fix":
            if canonicalize_file(path):
                changed.append(path)
        else:
            original = path.read_text(encoding="utf-8", errors="replace")
            updated = canonicalize_text(original)
            if updated != original:
                changed.append(path)

    if mode == "check":
        if changed:
            print("Formatting drift detected in:")
            for p in changed:
                print(f"  {p}")
            return 1

        print("All checked Markdown files are canonical.")
        return 0

    # Fix mode
    if changed:
        print("Updated Markdown formatting in:")
        for p in changed:
            print(f"  {p}")
    else:
        print("No formatting changes were necessary.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
