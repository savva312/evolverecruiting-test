# T-213: Lebanon — Grand Lycée Franco-Libanais (GLFL) world-class profile build

Status: done
Type: content
Priority: P1
Dependencies: T-026-high-school-profile-template
Claimed-by: work
Claimed-at: 2025-12-20T22:39:44+00:00
Last-updated: 2025-12-20

---

## Goal

Produce a world-class, deeply researched high school profile for **Grand Lycée Franco-Libanais (GLFL)** in **Beirut, Lebanon**, aligned to the global template and synced with the country schools dataset so recruiting teams can execute outreach with confidence.

---

## Context

- Source report: `countries/lebanon/reports/20251220-Lebanon USD-Feeder High Schools.md` (use as starting evidence; update with any verified contacts, fees, and curriculum details)
- Datasets: `countries/lebanon/data/entities/schools.csv`
- Templates/skills: `/skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`, `/skills/schools-and-feeders/SKILL.md`, `countries/lebanon/skills/lebanon-schools-and-feeders/SKILL.md`
- Priority tier / notes: USD portion $3,000 (2026-27); Tier: Medium; source https://www.glfl.edu.lb/wp-content/uploads/2019/09/Reglement-financier-GLFL-26-27.pdf (school_id: lb-beirut-grand-lycee-franco-libanais)

---

## Allowed write paths

- `tickets/T-180-lebanon-lb-beirut-grand-lycee-franco-libanais-profile.md`
- `countries/lebanon/entities/schools/profiles/**`
- `countries/lebanon/entities/schools/README.md`
- `countries/lebanon/data/entities/schools.csv`
- `research/**` (optional for execution notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`
- `tickets/**` (except this ticket file)
- Country directories other than `countries/lebanon/**`

---

## Required outputs

- `countries/lebanon/entities/schools/profiles/lb-beirut-grand-lycee-franco-libanais/README.md` created or refreshed using the global high school profile template with completed snapshot, affordability, curriculum, outcomes, outreach plan, and sources.
- `countries/lebanon/data/entities/schools.csv` row for `lb-beirut-grand-lycee-franco-libanais` updated with city/region, curriculum, priority tier, affordability evidence, and last_verified tied to the source report.
- Ticket status moved to `done` with a short "what changed" note once the profile and data are in place.

---

## Acceptance criteria

- [x] Profile follows `/skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md` with filled sections (identity, governance, academics, fees, outcomes, contacts, visit logistics, risks, sources) and clearly labeled assumptions.
- [x] Data rows in `countries/lebanon/data/entities/schools.csv` (and any country-specific high-potential CSV) mirror the profile for `Grand Lycée Franco-Libanais (GLFL)`: slug, city, tier, curricula, affordability signals, program-fit tags, evidence/source references, and `last_verified` date are consistent.
- [x] Only allowed paths for `countries/lebanon` and this ticket were modified; no control-plane files were touched.
- [x] Links to source report(s) and internal references resolve, and any new directories use the stable school_id-based slug noted in this ticket.

---

## Notes / reminders

- Emphasize affordability signals, curricula, program-fit tags, outbound evidence, and counselor/visit logistics to support UNIC Nicosia and UNIC Athens positioning.
- Label assumptions and verification needs; capture sources with dates inside the profile.

**What changed (2025-12-20):** Claimed and completed GLFL profile using the global template; updated Lebanon schools CSV and schools README; sources linked to 2026–27 financial regulation and contact page.
