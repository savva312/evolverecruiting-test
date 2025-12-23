# T-384: Collapse multiple blank lines in canonicalize workflow

Status: done  
Type: integration  
Priority: P2  
Dependencies: (none)  
Claimed-by: work  
Claimed-at: 2025-12-21T18:31:33Z  
Last-updated: 2025-12-21T18:32:07Z

---

## Goal

Ensure the Markdown canonicalization workflow collapses sequences of two or more consecutive blank lines into a single blank line and includes inline checks to guard the behavior.

---

## Context

- The canonicalization script already normalizes headings, bullets, trailing whitespace, and EOF newlines, but it currently preserves multi-blank-line runs.
- PRs occasionally contain large gaps of empty lines; the workflow should standardize them to a single blank line to keep formatting consistent.
- Inline, unit-style checks in the workflow script will catch regressions if the collapsing logic is broken.

---

## Allowed write paths

- `.github/workflows/canonicalize-md.yml`
- `tickets/T-368-canonicalize-blank-lines.md`
- `executions/**` (optional run notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- Other `tickets/**` files
- Country directories (`countries/**`)
- `.github/**` files not listed in Allowed write paths

---

## Required outputs

- Updated canonicalization workflow that collapses runs of multiple blank lines to a single blank line when rewriting Markdown files.
- Inline unit-style checks in the Python block confirming the blank-line rule is enforced.
- Ticket updated to `done` with brief execution notes once changes merge.

---

## Acceptance criteria

- The Python canonicalization logic rewrites any sequence of two or more consecutive blank lines to exactly one blank line while preserving other normalization rules.
- Inline checks (e.g., assertions) in the Python block validate the blank-line collapsing behavior and fail the workflow if the rule stops working.
- Workflow continues to operate only on changed `.md` files and preserves existing functionality (headings, bullets, trailing whitespace, single EOF newline).
- Ticket marked `done` with concise execution notes; no files outside Allowed write paths are modified.

---

## Execution notes (optional)

- Added blank-line collapsing to the canonicalization script and inline assertions to verify the behavior alongside existing formatting checks.
