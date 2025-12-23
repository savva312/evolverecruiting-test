# T-551: Lebanon — build Medicine competitor set (program list + ops-ready dataset)

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

Make the Lebanon Medicine recruiting cluster operational by:
- replacing the template competitor notes with an evidence-backed competitor list in `medicine-md/competitors.md`
- populating `countries/lebanon/data/programs/competitor-programs.csv` with a medicine-focused set of comparable programs

---

## Context

- Medicine cluster docs:
  - `countries/lebanon/program-clusters/medicine-md/cluster.md`
  - `countries/lebanon/program-clusters/medicine-md/lebanon-playbook.md`
  - `countries/lebanon/program-clusters/medicine-md/competitors.md` (currently a template)
- Structured dataset exists but is empty: `countries/lebanon/data/programs/competitor-programs.csv`
- Dictionary: `countries/lebanon/data/programs/competitor-programs-dictionary.md`

---

## Allowed write paths

- `tickets/T-461-lebanon-medicine-competitor-programs.md`
- `countries/lebanon/program-clusters/medicine-md/competitors.md`
- `countries/lebanon/data/programs/competitor-programs.csv`
- `countries/lebanon/data/programs/competitor-programs-dictionary.md` (only if minor clarifications are needed)

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

- `countries/lebanon/program-clusters/medicine-md/competitors.md` updated with:
  - a prioritized list of competitor MD programs relevant to Lebanese applicants (Cyprus, Greece, and common CEE destinations)
  - tuition/intake language requirements only when sourced (include URLs)
  - “why this competes” notes and how UNIC should position against each
- `countries/lebanon/data/programs/competitor-programs.csv` populated with **≥20 rows** (medicine/MD-focused) using sourced tuition/language/intake info where available.

---

## Acceptance criteria

- [ ] No fabricated tuition or entry requirements; every numeric claim is sourced or omitted.
- [ ] Competitor list includes at least 5 Cyprus/Greece/nearshore options plus at least 5 CEE options commonly marketed in Lebanon.
- [ ] No files outside `Allowed write paths` were modified.

