# T-497: Serbia — Build outbound mobility datasets (Eurostat + UIS) and update mobility notes

Status: done
Type: data
Priority: P1
Dependencies: (none)
Claimed-by: evoticketresolver_chd00__r
Claimed-at: 2025-12-22T20:41:15Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Replace Serbia outbound mobility placeholders with real, reproducible data extracts (Eurostat + UNESCO UIS) and update Serbia’s mobility notes to use those numbers.

---

## Context

- Current placeholders:
  - `countries/serbia/market/outbound-mobility.md`
  - `countries/serbia/reports/2025-12-20 - Serbia Outbound Mobility Baseline.md` (scaffold)
- Data is explicitly missing today (see both files). The repo needs:
  - a destination-split dataset for Serbia outbound tertiary mobility
  - methodology notes (what series, filters, limitations)
  - Greece (EL) and Cyprus (CY) extraction explicitly called out

---

## Allowed write paths

- `countries/serbia/data/outbound/**`
- `countries/serbia/market/outbound-mobility.md`
- `countries/serbia/reports/2025-12-20 - Serbia Outbound Mobility Baseline.md`
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

- `countries/serbia/data/outbound/serbia-eurostat-outbound.csv`
- `countries/serbia/data/outbound/serbia-eurostat-outbound-dictionary.md`
- `countries/serbia/data/outbound/serbia-uis-outbound.csv`
- `countries/serbia/data/outbound/serbia-uis-outbound-dictionary.md`
- `countries/serbia/market/outbound-mobility.md`
- `countries/serbia/reports/2025-12-20 - Serbia Outbound Mobility Baseline.md`

---

## Acceptance criteria

- [x] The two new CSVs exist and are readable (UTF-8) with consistent schemas documented in the dictionary files.
- [x] Eurostat extract includes at least 2020–2023 (or 2020–latest available) and includes separate rows for Greece (EL) and Cyprus (CY).
- [x] Methodology section states the exact Eurostat dataset code(s) and filters used, with source links.
- [x] `countries/serbia/market/outbound-mobility.md` no longer contains “expected/placeholder” claims and instead references the new CSVs and summarizes the top destinations + EL/CY shares.
- [x] `countries/serbia/reports/2025-12-20 - Serbia Outbound Mobility Baseline.md` is updated from scaffold to a sourced baseline summary with tables/charts expressed as markdown tables (no binaries).
- [x] No edits outside allowed write paths.

---

## What changed
- Added Eurostat + UIS outbound mobility extracts and data dictionaries under `countries/serbia/data/outbound/`.
- Replaced placeholders with sourced numbers in `countries/serbia/market/outbound-mobility.md`.
- Upgraded the Serbia outbound mobility report from scaffold to a sourced baseline with methodology + tables.
