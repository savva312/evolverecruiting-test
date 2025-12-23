# T-174: Romania high-potential feeder high schools

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T21:58:00Z
Last-updated: 2025-12-20

---

## Goal

Use the existing “Romania High-School Feeder Map” report to populate a high-potential feeder high schools section for Romania that aligns with the global schools-and-feeders skill. Produce a structured CSV plus a narrative index so outreach teams can immediately act on the priority school list.

---

## Context

- Source material: `countries/romania/reports/20251220-Romania High-School Feeder Map.md`.
- Global reference: `skills/schools-and-feeders/SKILL.md` and `skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`.
- Emphasis: Bucharest/Ilfov first, then Cluj, Iași, Timișoara, and single-school cities flagged in the report (Constanța, Brașov, Oradea).

---

## Allowed write paths

- `countries/romania/entities/schools/**`
- `countries/romania/data/entities/**`
- `tickets/T-147-romania-high-potential-feeder-schools.md`
- `research/**`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket)
- `.github/**`
- `scripts/**`
- Any `countries/**` path outside `countries/romania/**`

---

## Required outputs

- `countries/romania/entities/schools/README.md` updated with a “High-potential feeder high schools” section that links to the dataset and summary.
- `countries/romania/entities/schools/high-potential-feeder-high-schools.md` summarizing the priority list, rubric, and next actions based on the source report.
- `countries/romania/data/entities/schools/romania-high-potential-feeder-high-schools.csv` capturing the prioritized schools with key fields (IDs, city/region, curriculum, tier, tuition/affordability signal, program fit tags, status, sources, last_verified).
- `countries/romania/data/entities/schools/romania-high-potential-feeder-high-schools-dictionary.md` defining the CSV columns and alignment to the global skill.

---

## Acceptance criteria

- [x] Summary and CSV both trace back to the cited report and follow the global schools-and-feeders conventions (IDs, tiering, program tags, `last_verified` dates, and sources).
- [x] High-potential section in `entities/schools/README.md` clearly directs readers to the dataset and summary, with scope limited to Romania.
- [x] CSV uses stable `school_id` slugs and includes city/region, school type/curriculum, affordability/tier signal, program-fit tags, status, and sources.
- [x] No edits occur outside Allowed write paths; protected files remain untouched.
- [x] Ticket updated to `done` with a brief “What changed” entry when completed.

---

## Execution notes (optional)

- What changed (short): Created Romania high-potential feeder summary and CSV aligned to the global schools-and-feeders skill; updated the schools README to link the new assets and documented tiering/rubric plus next actions.
- Any open questions: Confirm liceu delivery and current tuition for candidate/verify_fees rows (e.g., Maarif Bucharest, Cambridge School of Constanța, IOANID fee schedule, Avenor grade-level pricing, Oradea KS4/KS5 delivery).
- Follow-up tickets suggested: Add per-school profiles using the global template for Tier A Bucharest schools and BIST (Timișoara) once confirmations are gathered.
