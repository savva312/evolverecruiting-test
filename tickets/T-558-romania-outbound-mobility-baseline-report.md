# T-558: Romania — outbound mobility baseline (replace templates with sourced analysis + data extract)

Status: open
Type: content
Priority: P0
Dependencies: (none)
Claimed-by:
Claimed-at:
Last-updated: 2025-12-22
Agent: EvoResearcher
Research rounds: 2
Research sections: 7
Research output path: `countries/romania/reports/`

---

## Goal

Replace the Romania outbound mobility placeholders with a **sourced baseline** that can be used for recruiting decisions:
- Update the narrative baseline report with Romania-specific numbers and rankings.
- Update the market “outbound mobility” page to summarize key implications for UNIC and UNIC Athens.
- Create a small structured extract (CSV) that includes the latest outbound counts by destination.

---

## Context

Current placeholders:
- `countries/romania/reports/2025-12-20 - Romania Outbound Mobility Baseline.md`
- `countries/romania/market/outbound-mobility.md`

The report must clearly call out Greece and Cyprus, but also include the dominant Romania outbound destinations for context.

---

## Allowed write paths

- `tickets/T-463-romania-outbound-mobility-baseline-report.md`
- `countries/romania/reports/2025-12-20 - Romania Outbound Mobility Baseline.md`
- `countries/romania/market/outbound-mobility.md`
- `countries/romania/data/market/**` (new files allowed)
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
- `countries/**` (except `countries/romania/**`)

---

## Required outputs

- Updated `countries/romania/reports/2025-12-20 - Romania Outbound Mobility Baseline.md`
- Updated `countries/romania/market/outbound-mobility.md`
- New CSV extract (choose a stable filename and document it in the report):
  - `countries/romania/data/market/romania-outbound-mobility-by-destination.csv`

---

## Acceptance criteria

- [ ] Report contains latest available outbound tertiary mobility totals for Romania and a ranked destination table (with Greece and Cyprus highlighted).
- [ ] Methodology is explicit (dataset IDs, filters, how totals were computed) and caveats are listed.
- [ ] Structured CSV extract exists and matches the report’s numbers.
- [ ] All material claims are source-backed with URLs; any estimates are labeled.
- [ ] No edits outside allowed paths.

---

## Research prompt (EvoResearcher)

You are producing a **Romania outbound mobility baseline** for enrollment strategy (UNIC Nicosia + UNIC Athens).

1) Use authoritative sources (Eurostat preferred; UNESCO UIS as a cross-check). Pull the latest available year(s) and compute:
   - total outbound tertiary students originating from Romania
   - top destination countries (ranked), explicitly highlighting Greece and Cyprus
   - a 3–5 year trend table if available with consistent methodology
2) Document methodology precisely (dataset name/table, filters, how you handled aggregates, missing destinations, confidentiality flags).
3) Write a clear “Implications for UNIC / UNIC Athens” section with:
   - which Romanian cities/segments to prioritize (tie to Bac calendar if relevant)
   - 3–6 “hero” program clusters and why (link to `countries/romania/program-clusters/`)
   - confidence levels (high/medium/low) for each recommendation
4) Create `countries/romania/data/market/romania-outbound-mobility-by-destination.csv` with columns that support operational reuse (year, destination, count, source, notes).
5) Update both required markdown files. Keep them concise and decision-ready.

