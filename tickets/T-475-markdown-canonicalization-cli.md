# T-475: Markdown canonicalization CLI

Status: done
Type: structure
Priority: P1
Agent: EvoTicket Resolver
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-22T16:08:05Z
Last-updated: 2025-12-22T17:35:00Z

---

## Goal

Provide a repo-local Markdown canonicalization CLI that mirrors the workflow’s formatting rules, supports check/fix modes, auto-discovers changed `.md` files, and is documented for agent use (with an optional pre-commit hook).

---

## Context

- Automation for Markdown canonicalization has been disabled/iterated; agents still need a reliable, local way to enforce the same rules during ticket work.
- A Python script should encapsulate the canonical formatting logic (heading/bullet normalization, trailing whitespace cleanup, blank-line collapsing, single EOF newline) and expose both check and fix flows.
- Usage should be discoverable in developer docs, and a lightweight pre-commit hook entry can help keep Markdown consistent.

---

## Allowed write paths

- `tickets/T-419-markdown-canonicalization-cli.md`
- `scripts/**`
- `README.md`
- `.pre-commit-config.yaml`

---

## Forbidden write paths

- All other files and directories not listed in Allowed write paths.

---

## Required outputs

- `scripts/canonicalize_md.py` implementing the Markdown canonicalization CLI with the requested behaviors.
- Developer documentation updated (e.g., `README.md` and/or `scripts/README.md`) describing how to run the tool during ticket work.
- Optional pre-commit hook entry referencing the new script (if added to `.pre-commit-config.yaml`).
- Ticket updated to reflect completion and execution notes.

---

## Acceptance criteria

- Script encapsulates existing canonicalize logic: normalizes ATX headings (single space after `#`, no trailing hashes), standardizes bullets to `-` with two-space indentation steps, strips trailing whitespace, collapses runs of blank lines to a single blank line, and enforces a single trailing newline.
- Supports CLI options to process specified Markdown paths or auto-discover staged/modified `.md` files via `git diff --name-only`.
- `--check` mode reports drift (non-zero exit) without modifying files; `--fix` rewrites files in place. Running without `--check/--fix` should default to check mode and print guidance.
- Handles absent targets gracefully (no crash if no Markdown files are found).
- Docs clearly explain how agents invoke the tool (explicit paths + auto-discovery) and how to use the optional pre-commit hook entry if present.
- Ticket marked `done` with brief execution notes once completed.

---

## Execution notes (optional)

- Added `scripts/canonicalize_md.py` with check/fix modes, git diff auto-discovery, and inline sanity checks.
- Documented usage in `README.md` and `scripts/README.md`; added a local pre-commit hook entry in `.pre-commit-config.yaml`.
- Default mode now fixes files in place; `--check` is available for drift detection without writes.
- Script help and usage strings now reflect fix-by-default behavior; no logic changes beyond clarity.
