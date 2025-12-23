# T-543: Lebanon — refresh outbound mobility baseline (report + structured dataset)

Status: open
Type: data
Priority: P0
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

Turn the Lebanon outbound mobility baseline from a placeholder into a usable evidence pack by:
- updating the report with sourced numbers and implications for UNIC / UNIC Athens
- adding a tidy CSV dataset for destinations and trend snapshots (no fabricated numbers)

---

## Context

Placeholder report:
- `countries/lebanon/reports/2025-12-20 - Lebanon Outbound Mobility Baseline.md`

Market planning doc (helpful framing):
- `countries/lebanon/market/outbound-mobility.md`

---

## Allowed write paths

- `tickets/T-459-lebanon-outbound-mobility-baseline-refresh.md`
- `countries/lebanon/reports/2025-12-20 - Lebanon Outbound Mobility Baseline.md`
- `countries/lebanon/data/market/outbound-mobility.csv`
- `countries/lebanon/data/market/outbound-mobility-dictionary.md`

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

- `countries/lebanon/reports/2025-12-20 - Lebanon Outbound Mobility Baseline.md` updated with:
  - latest-year sourced totals (clearly labeled with year)
  - top destination countries (top 10) with source citation
  - explicit “data gaps” section if key sources are unavailable
  - 1–2 pages of implications for UNIC/UNIC Athens (program clusters, messaging, channel implications)
- `countries/lebanon/data/market/outbound-mobility.csv` created and populated with at least:
  - total outbound (by year if available)
  - top destinations table (destination + count + year + source)
- `countries/lebanon/data/market/outbound-mobility-dictionary.md` created defining fields and sources rules.

---

## Acceptance criteria

- [ ] No fabricated statistics: every numeric entry has a source URL and year.
- [ ] Report uses clear “as of” framing and cites the dataset file paths.
- [ ] No files outside `Allowed write paths` were modified.

