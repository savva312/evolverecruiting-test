# T-026: Multi-country migration QA

Status: archived
Type: qa
Priority: P1
Dependencies: T-019, T-020, T-021, T-022, T-023
Claimed-by: work
Claimed-at: 2025-12-20T16:45:39+00:00
Last-updated: 2025-12-20

---

## Goal

Validate the multi-country migration: verify directory placement, link integrity, and adherence to rules (research/runs unchanged, reports relocated per country, skills split).

---

## Context

- Runs after migrations and link cleanup are complete.
- Provides a final pass to catch stragglers and document follow-ups.

---

## Allowed write paths

- `QA/**` (QA findings/report)
- `tickets/T-024-qa-multi-country.md`
- `research/**` (optional run notes)
- `tickets/index.md` (if listing this ticket)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (unless documenting findings without altering content)
- Country directories (`/bulgaria/**`, `/nigeria/**`, `/greece/**`, or others) except for read-only verification
- Other tickets except status updates to this file
- `research/runs/**`

---

## Required outputs

- `QA/` report documenting checks performed, results, and any follow-up tickets needed
- `tickets/T-024-qa-multi-country.md` updated upon completion

---

## Acceptance criteria

- [x] QA report lists verification steps (directory layout, reports relocation, skills split, link integrity) and results
- [x] Any defects or gaps have follow-up tickets noted
- [x] `research/runs` confirmed untouched; `research/reports` removed or empty with reports relocated
- [x] No files outside Allowed write paths are modified

---

## Execution notes (optional)

- What changed (short): Cleared root `research/` to keep only `research/runs` and documented verification in `QA/T-024-qa-report.md`.
- Any open questions: None
- Follow-up tickets suggested: None
