# T-467: Serbia — Build a 2026 recruiting budget model (channels, fairs, travel)

Status: done
Type: data
Priority: P1
Dependencies: (optional) T-451 / T-452
Claimed-by: run-20251222-codex
Claimed-at: 2025-12-22T10:00:00Z
Completed-at: 2025-12-22T11:30:00Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Populate Serbia’s budget model with a practical 2026 plan across digital spend, fairs/events, school travel, and agent enablement so leadership can fund Serbia execution predictably.

---

## Context

- Target file (currently header-only):
  - `countries/serbia/data/operations/budget-model.csv`
- Should align to:
  - Serbia fair priorities under `countries/serbia/entities/fairs-events/**`
  - Channel guardrails under `countries/serbia/data/marketing/channel-benchmarks.csv`

---

## Allowed write paths

- `countries/serbia/data/operations/budget-model.csv`
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

- `countries/serbia/data/operations/budget-model.csv`

---

## Acceptance criteria

- [x] Budget includes at least these categories: digital media, fairs/events, travel (schools/agents), collateral/printing, webinars/production, contingency.
- [x] Each row has `period` (e.g., `2026-Q1` or `2026-02`) and `as_of` populated.
- [x] Assumptions are explicit (e.g., expected number of fairs, cost per city, monthly media budget range).
- [x] No edits outside allowed write paths.

## What changed

- Populated `countries/serbia/data/operations/budget-model.csv` with 2026 quarterly budgets across digital media, priority fairs, travel loops, collateral, webinars, and contingency buffers aligned to Serbia channel benchmarks.
