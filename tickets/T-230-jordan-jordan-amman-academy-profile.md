# T-230: Jordan — Amman Academy (Nord Anglia) world-class profile build

Status: done
Type: content
Priority: P1
Dependencies: T-026-high-school-profile-template
Claimed-by: work
Claimed-at: 2025-12-21
Last-updated: 2025-12-21

---

## Goal

Produce a world-class, deeply researched high school profile for **Amman Academy (Nord Anglia)** in **Amman, Jordan**, aligned to the global template and synced with the country schools dataset so recruiting teams can execute outreach with confidence.

---

## Context

- Source report: `countries/jordan/reports/20251220-Jordan Premium High-School Feeders.md` (use as starting evidence; update with any verified contacts, fees, and curriculum details)
- Datasets: `countries/jordan/data/entities/schools.csv`
- Templates/skills: `/skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`, `/skills/schools-and-feeders/SKILL.md`, `countries/jordan/skills/jordan-schools-and-feeders/SKILL.md`
- Priority tier / notes: Priority tier Tier 1; evidence A (school_id: jordan-amman-academy)

---

## Allowed write paths

- `tickets/T-197-jordan-jordan-amman-academy-profile.md`
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

- `countries/jordan/entities/schools/profiles/amman/amman-academy-nord-anglia/README.md` created or refreshed using the global high school profile template with completed snapshot, affordability, curriculum, outcomes, outreach plan, and sources.
- `countries/jordan/data/entities/schools.csv` row for `jordan-amman-academy` updated with city/region, curriculum, priority tier, affordability evidence, and last_verified tied to the source report.
- Ticket status moved to `done` with a short "what changed" note once the profile and data are in place.

---

## Acceptance criteria

- [ ] Profile follows `/skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md` with filled sections (identity, governance, academics, fees, outcomes, contacts, visit logistics, risks, sources) and clearly labeled assumptions.
- [ ] Data rows in `countries/jordan/data/entities/schools.csv` (and any country-specific high-potential CSV) mirror the profile for `Amman Academy (Nord Anglia)`: slug, city, tier, curricula, affordability signals, program-fit tags, evidence/source references, and `last_verified` date are consistent.
- [ ] Only allowed paths for `countries/jordan` and this ticket were modified; no control-plane files were touched.
- [ ] Links to source report(s) and internal references resolve, and any new directories use the stable school_id-based slug noted in this ticket.

---

## Notes / reminders

- Emphasize affordability signals, curricula, program-fit tags, outbound evidence, and counselor/visit logistics to support UNIC Nicosia and UNIC Athens positioning.
- Label assumptions and verification needs; capture sources with dates inside the profile.

What changed (2025-12-21):
- Built full Tier 1 profile for Amman Academy using global template, Nord Anglia tuition/enquiry sources, and 2025-12-20 premium feeders report.
- Updated `countries/jordan/data/entities/schools.csv` row for `jordan-amman-academy` with curricula, contact info, visit windows, tuition/fees, sources, and refreshed `last_verified`.
