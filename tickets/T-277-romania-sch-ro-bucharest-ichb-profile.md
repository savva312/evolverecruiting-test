# T-277: Romania — International Computer High School of Bucharest world-class profile build

Status: done
Type: content
Priority: P1
Dependencies: T-026-high-school-profile-template
Claimed-by: work
Claimed-at: 2025-12-21T10:15:18Z
Last-updated: 2025-12-21

---

## Goal

Produce a world-class, deeply researched high school profile for **International Computer High School of Bucharest** in **Bucharest, Romania**, aligned to the global template and synced with the country schools dataset so recruiting teams can execute outreach with confidence.

---

## Context

- Source report: `countries/romania/reports/20251220-Romania High-School Feeder Map.md` (use as starting evidence; update with any verified contacts, fees, and curriculum details)
- Datasets: `countries/romania/data/entities/schools.csv`, `countries/romania/data/entities/schools/romania-high-potential-feeder-high-schools.csv`
- Templates/skills: `/skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`, `/skills/schools-and-feeders/SKILL.md`, `countries/romania/skills/romania-schools-and-feeders/SKILL.md`
- Priority tier / notes: Priority tier A per feeder map (school_id: sch-ro-bucharest-ichb)

---

## Allowed write paths

- `tickets/T-245-romania-sch-ro-bucharest-ichb-profile.md`
- `countries/romania/entities/schools/profiles/**`
- `countries/romania/entities/schools/README.md`
- `countries/romania/data/entities/schools.csv`
- `countries/romania/data/entities/schools/romania-high-potential-feeder-high-schools.csv`
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
- Country directories other than `countries/romania/**`

---

## Required outputs

- `countries/romania/entities/schools/profiles/sch-ro-bucharest-ichb/README.md` created or refreshed using the global high school profile template with completed snapshot, affordability, curriculum, outcomes, outreach plan, and sources.
- `countries/romania/data/entities/schools/romania-high-potential-feeder-high-schools.csv` entry for `sch-ro-bucharest-ichb` aligned to the profile (tier, affordability signal, program-fit tags, sources).
- `countries/romania/data/entities/schools.csv` row for `sch-ro-bucharest-ichb` updated with city/region, curriculum, priority tier, affordability evidence, and last_verified tied to the source report.
- Ticket status moved to `done` with a short "what changed" note once the profile and data are in place.

---

## Acceptance criteria

- [x] Profile follows `/skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md` with filled sections (identity, governance, academics, fees, outcomes, contacts, visit logistics, risks, sources) and clearly labeled assumptions.
- [x] Data rows in `countries/romania/data/entities/schools.csv` (and any country-specific high-potential CSV) mirror the profile for `International Computer High School of Bucharest`: slug, city, tier, curricula, affordability signals, program-fit tags, evidence/source references, and `last_verified` date are consistent.
- [x] Only allowed paths for `countries/romania` and this ticket were modified; no control-plane files were touched.
- [x] Links to source report(s) and internal references resolve, and any new directories use the stable school_id-based slug noted in this ticket.

---

## Notes / reminders

- Emphasize affordability signals, curricula, program-fit tags, outbound evidence, and counselor/visit logistics to support UNIC Nicosia and UNIC Athens positioning.
- Label assumptions and verification needs; capture sources with dates inside the profile.

## What changed (2025-12-21)

- Created full profile for `sch-ro-bucharest-ichb` with tuition, campus contacts, outreach plan, and sources.
- Synced `countries/romania/data/entities/schools.csv` and `romania-high-potential-feeder-high-schools.csv` rows to the profile (tier, affordability, contacts, sources).
- Updated schools index to move ICHB into live Bucharest profiles.
