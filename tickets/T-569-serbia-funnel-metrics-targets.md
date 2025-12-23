# T-569: Serbia — Populate funnel metrics targets (lead → start) for 2026

Status: open
Type: data
Priority: P1
Dependencies: (none)
Claimed-by:
Claimed-at:
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Populate the Serbia funnel metrics dataset with measurable targets and definitions so the enrollment team can manage Serbia performance week-to-week.

---

## Context

- Target file (currently header-only):
  - `countries/serbia/data/operations/funnel-metrics.csv`
- Should align to Serbia plan language in:
  - `countries/serbia/reports/2025-12-20 - UNIC Athens Serbia Recruitment Plan.md`
- Constraints:
  - This is a **targets/benchmark** table, not a performance table; mark periods clearly and label assumptions.

---

## Allowed write paths

- `countries/serbia/data/operations/funnel-metrics.csv`
- `executions/**` (optional; notes only)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)

---

## Required outputs

- `countries/serbia/data/operations/funnel-metrics.csv`

---

## Acceptance criteria

- [ ] Adds a minimum viable target set across stages (example): inquiry → qualified lead → application started → application complete → offer → deposit → start.
- [ ] Includes at least one “time” metric (e.g., median days inquiry→offer, offer→deposit) and one “quality” metric (e.g., % qualified).
- [ ] Each row has `period` (e.g., `2026-Q1`) and `as_of` populated; assumptions are recorded in `notes`.
- [ ] No edits outside allowed write paths.

