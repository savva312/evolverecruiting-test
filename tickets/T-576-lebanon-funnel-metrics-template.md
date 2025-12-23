# T-576: Lebanon — create `funnel-metrics.csv` template (definitions + reporting skeleton)

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

Turn `countries/lebanon/data/operations/funnel-metrics.csv` from an empty table into a **ready-to-fill reporting skeleton** with:
- agreed stage names
- metric definitions (what counts, what doesn’t)
- units and suggested periods

This is the “scorecard spine” for weekly Lebanon pipeline reviews. Values may be blank unless sourced; the key is that definitions are explicit and consistent.

---

## Context

- Empty file: `countries/lebanon/data/operations/funnel-metrics.csv`
- Dictionary: `countries/lebanon/data/operations/funnel-metrics-dictionary.md`
- Related playbooks:
  - `countries/lebanon/go-to-market/offerholder-and-yield/deposit-deadlines.md`
  - `countries/lebanon/go-to-market/digital-playbook/channel-strategy.md`

---

## Allowed write paths

- `tickets/T-468-lebanon-funnel-metrics-template.md`
- `countries/lebanon/data/operations/funnel-metrics.csv`
- `countries/lebanon/data/operations/funnel-metrics-dictionary.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/lebanon/**`)

---

## Required outputs

- `countries/lebanon/data/operations/funnel-metrics.csv` populated with **≥25 rows** covering:
  - stages: awareness, leads, applications, offers, deposits, enrollments (and optional: show-ups/starts)
  - metrics: count, conversion_rate, cost_per, yield (as applicable)
  - periods: at least `2026-Q1` through `2026-Q4` rows

---

## Acceptance criteria

- [ ] Rows can have blank `value`, but every row must have a clear `notes` definition of how the metric should be computed and what it excludes.
- [ ] Units are consistent (`students`, `%`, `EUR`) and align with `field-standards.md` conventions.
- [ ] No files outside `Allowed write paths` were modified.

