# T-452: Romania — define funnel metrics + targets in `countries/romania/data/operations/funnel-metrics.csv`

Status: done
Type: data
Priority: P1
Dependencies: (none)
Claimed-by: codex-20251222-run1
Claimed-at: 2025-12-22T17:55Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Turn `countries/romania/data/operations/funnel-metrics.csv` from a blank scaffold into a practical “weekly cockpit” by:
- defining pipeline stages and core metrics (lead → MQL → 상담/meeting → application → offer → deposit → enrolled)
- setting initial **targets** and **measurement notes** for Romania
- ensuring every metric is clearly defined so two people compute it the same way

---

## Context

Romania already has playbooks that reference measurement (e.g., webinars, deposit deadlines), but there is no shared metric definition or targets file.

Related files:
- `countries/romania/data/operations/funnel-metrics.csv` (empty)
- `countries/romania/data/operations/funnel-metrics-dictionary.md`
- `countries/romania/go-to-market/offerholder-and-yield/deposit-deadlines.md`

---

## Allowed write paths

- `tickets/T-452-romania-funnel-metrics-targets.md`
- `countries/romania/data/operations/funnel-metrics.csv`
- `countries/romania/data/operations/funnel-metrics-dictionary.md`
- `executions/**` (optional for notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`
- `tickets/**` (except this ticket file)
- `countries/**` (except `countries/romania/data/operations/**`)

---

## Required outputs

- Updated `countries/romania/data/operations/funnel-metrics.csv` (minimum: 15 rows with stage/metric/definition + target)
- Updated `countries/romania/data/operations/funnel-metrics-dictionary.md`

---

## Acceptance criteria

- [x] Funnel stages are explicitly defined and ordered.
- [x] Each metric includes a definition and a measurement note (what system it comes from / how it’s counted).
- [x] Targets are provided (even if labeled “initial assumption”).
- [x] Dictionary matches dataset exactly.
- [x] No edits outside allowed paths.

## What changed (2025-12-22)

- Populated `countries/romania/data/operations/funnel-metrics.csv` with 16 weekly target rows covering lead through enrollment counts, conversion rates, cost per lead, and yield metrics for Romania’s UNIC Nicosia + UNIC Athens funnel.
- Rebuilt `countries/romania/data/operations/funnel-metrics-dictionary.md` to lock the stage order, schema, and required notes template so definitions and targets stay synchronized with the dataset.
