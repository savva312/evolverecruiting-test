# T-387: Preserve Markdown canonicalization rules via skills

Status: done
Type: structure
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-21T18:55:58Z
Last-updated: 2025-12-21

---

## Goal

Capture the Markdown formatting guardrails previously enforced by the disabled canonicalize workflow inside a global skill that agents read by default, so style consistency is preserved even without automation.

## Context

- The canonicalize workflow was disabled (T-369), removing automatic fixes for Markdown formatting.
- We still need contributors to apply the same rules manually for headings, bullets, trailing whitespace, blank lines, and EOF newlines.
- The `skills/markdown-authoring` guide is referenced by many tickets and should house these rules.

## Allowed write paths

- `skills/markdown-authoring/**`
- `skills/README.md`
- `tickets/T-370-md-canonicalization-skill.md`
- `executions/**` (optional notes)

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- Country directories (e.g., `/countries/**`)
- Other tickets in `/tickets/**`
- `.github/**`
- `scripts/**`
- `skills/**` paths not listed above

## Required outputs

- Updated `skills/markdown-authoring/SKILL.md` that documents the canonical Markdown formatting rules previously enforced by automation.
- (If needed) `skills/README.md` entry updated to highlight the canonical formatting checklist.
- This ticket updated with execution notes and marked done.

## Acceptance criteria

- Markdown-authoring skill lists the canonical formatting rules: heading spacing (no trailing hashes), normalized unordered lists (hyphen markers, two-space indents), trailing whitespace removal, collapse runs of blank lines to one, and exactly one newline at EOF.
- Guidance includes a quick checklist so contributors can self-audit without the workflow.
- No files outside Allowed write paths are modified.
- Ticket marked `done` with a short summary of changes.

## Execution notes (optional)

- Captured the retired canonicalize workflow rules (headings spacing, `-` bullets with two-space indents, trailing whitespace removal, blank-line collapsing, single EOF newline) inside `skills/markdown-authoring/SKILL.md` with a quick pre-commit checklist.
- Indexed the updated skill in `skills/README.md` so readers know it houses the canonical formatting checklist.
