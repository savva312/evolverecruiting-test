# T-223: Jordan — King's Academy world-class profile build

Status: done
Type: content
Priority: P1
Dependencies: T-026-high-school-profile-template
Claimed-by: work
Claimed-at: 2025-12-20
Last-updated: 2025-12-20

---

## Goal

Produce a world-class, deeply researched high school profile for **King's Academy** in **Madaba, Jordan**, aligned to the global template and synced with the country schools dataset so recruiting teams can execute outreach with confidence.

---

## Context

- Source report: `countries/jordan/reports/20251220-Jordan Premium High-School Feeders.md` (use as starting evidence; update with any verified contacts, fees, and curriculum details)
- Datasets: `countries/jordan/data/entities/schools.csv`
- Templates/skills: `/skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`, `/skills/schools-and-feeders/SKILL.md`, `countries/jordan/skills/jordan-schools-and-feeders/SKILL.md`
- Priority tier / notes: Priority tier Tier 1; evidence A (school_id: jordan-kings-academy)

---

## Allowed write paths

- `tickets/T-190-jordan-jordan-kings-academy-profile.md`
- `countries/jordan/entities/schools/profiles/**`
- `countries/jordan/entities/schools/README.md`
- `countries/jordan/data/entities/schools.csv`
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
- Country directories other than `countries/jordan/**`

---

## Required outputs

- `countries/jordan/entities/schools/profiles/madaba/kings-academy/README.md` created or refreshed using the global high school profile template with completed snapshot, affordability, curriculum, outcomes, outreach plan, and sources.
- `countries/jordan/data/entities/schools.csv` row for `jordan-kings-academy` updated with city/region, curriculum, priority tier, affordability evidence, and last_verified tied to the source report.
- Ticket status moved to `done` with a short "what changed" note once the profile and data are in place.

---

## Acceptance criteria

- [x] Profile follows `/skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md` with filled sections (identity, governance, academics, fees, outcomes, contacts, visit logistics, risks, sources) and clearly labeled assumptions.
- [x] Data rows in `countries/jordan/data/entities/schools.csv` (and any country-specific high-potential CSV) mirror the profile for `King's Academy`: slug, city, tier, curricula, affordability signals, program-fit tags, evidence/source references, and `last_verified` date are consistent.
- [x] Only allowed paths for `countries/jordan` and this ticket were modified; no control-plane files were touched.
- [x] Links to source report(s) and internal references resolve, and any new directories use the stable school_id-based slug noted in this ticket.

---

## Notes / reminders

- Emphasize affordability signals, curricula, program-fit tags, outbound evidence, and counselor/visit logistics to support UNIC Nicosia and UNIC Athens positioning.
- Label assumptions and verification needs; capture sources with dates inside the profile.
- What changed (2025-12-20): Built full King’s Academy profile with AP catalog, counseling/visit contacts, logistics, and affordability signals; updated CSV row for jordan-kings-academy with curriculum, contacts, sources, and visit notes.
