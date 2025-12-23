# T-424: Bulgaria — create `funnel-metrics.csv` template (definitions + reporting skeleton)

Status: done
Type: data
Priority: P0
Dependencies: (none)
Claimed-by: evoticketresolver_yqr5g__4
Claimed-at: 2025-12-22T17:49:49Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Turn `countries/bulgaria/data/operations/funnel-metrics.csv` from an empty table into a **ready-to-fill reporting skeleton** with:
- agreed stage names
- metric definitions (what counts, what doesn’t)
- units and suggested periods

This is the “scorecard spine” for weekly Bulgaria pipeline reviews. Values may be blank unless sourced; the key is that definitions are explicit and consistent.

---

## Context

- Empty file: `countries/bulgaria/data/operations/funnel-metrics.csv`
- Dictionary: `countries/bulgaria/data/operations/funnel-metrics-dictionary.md`
- Related playbooks:
  - `countries/bulgaria/go-to-market/offerholder-and-yield/deposit-deadlines.md`
  - `countries/bulgaria/go-to-market/digital-playbook/channel-strategy.md`

---

## Allowed write paths

- `tickets/T-424-bulgaria-funnel-metrics-template.md`
- `countries/bulgaria/data/operations/funnel-metrics.csv`
- `countries/bulgaria/data/operations/funnel-metrics-dictionary.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/bulgaria/**`)

---

## Required outputs

- `countries/bulgaria/data/operations/funnel-metrics.csv` populated with **≥25 rows** covering:
  - stages: awareness, leads, applications, offers, deposits, enrollments (and optional: show-ups/starts)
  - metrics: count, conversion_rate, cost_per, yield (as applicable)
  - periods: at least `2026-Q1` through `2026-Q4` rows

---

## Acceptance criteria

- [x] Rows can have blank `value`, but every row must have a clear `notes` definition of how the metric should be computed and what it excludes.
- [x] Units are consistent (`students`, `%`, `EUR`) and align with `field-standards.md` conventions.
- [x] No files outside `Allowed write paths` were modified.

---

## What changed

- Populated `countries/bulgaria/data/operations/funnel-metrics.csv` with a 2026 quarterly reporting skeleton (counts, conversion rates, cost-per, and offer-to-enrollment yield) and explicit computation notes.
- Tightened `countries/bulgaria/data/operations/funnel-metrics-dictionary.md` to align allowed stages/metrics/units with the populated template.
