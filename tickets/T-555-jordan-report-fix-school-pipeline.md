# T-555: Jordan report — replace incorrect school pipeline table with Jordan schools

Status: open
Type: qa
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

Fix the highest-risk factual error in the Jordan recruitment plan report by replacing the incorrect “school pipeline” section (currently populated with Bulgaria school names/emails/phone numbers) with a Jordan-correct pipeline table derived from the Jordan school index and profiles.

---

## Context

Report:
- `countries/jordan/reports/2025-12-20 - UNIC Athens Jordan Recruitment Plan.md`

Evidence of issue:
- The report contains Bulgaria emails/phone numbers (e.g., `+359...`) and Bulgaria school artifacts mapped to “Amman”.

Jordan source of truth for schools:
- `countries/jordan/entities/schools/README.md`
- `countries/jordan/entities/schools/profiles/**`
- `countries/jordan/data/entities/schools.csv`

---

## Allowed write paths

- `tickets/T-462-jordan-report-fix-school-pipeline.md`
- `countries/jordan/reports/2025-12-20 - UNIC Athens Jordan Recruitment Plan.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/jordan/**`)

---

## Required outputs

- `countries/jordan/reports/2025-12-20 - UNIC Athens Jordan Recruitment Plan.md` updated:
  - removes Bulgaria school artifacts in the school pipeline section
  - replaces with Jordan schools and correct contact channels (from profiles/CSV), with sources where possible

---

## Acceptance criteria

- [ ] The report contains **no** Bulgaria phone codes (`+359`) and no Bulgaria school emails/domains in the Jordan schools pipeline section.
- [ ] All schools in the pipeline table exist in `countries/jordan/entities/schools/README.md` and/or `countries/jordan/data/entities/schools.csv`.
- [ ] Any school-contact details included are sourced from the school profile or official school pages (avoid inventing contacts).

