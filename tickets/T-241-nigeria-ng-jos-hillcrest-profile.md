# T-241: Nigeria — Hillcrest School world-class profile build

Status: dropped
Type: content
Priority: P1
Dependencies: T-026-high-school-profile-template
Claimed-by:
Claimed-at:
Last-updated: 2025-12-21

---

## Goal

Produce a world-class, deeply researched high school profile for **Hillcrest School** in **Jos, Nigeria**, aligned to the global template and synced with the country schools dataset so recruiting teams can execute outreach with confidence.

---

## Context

- Source report: `countries/nigeria/reports/20251220-Nigeria Premium Secondary School Pipeline.md` (use as starting evidence; update with any verified contacts, fees, and curriculum details)
- Datasets: `countries/nigeria/data/entities/schools.csv`
- Templates/skills: `/skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`, `/skills/schools-and-feeders/SKILL.md`, `countries/nigeria/skills/nigeria-schools-and-feeders/SKILL.md`
- Priority tier / notes: Priority Tier1 from Nigeria Premium Secondary School Pipeline (school_id: ng-jos-hillcrest)

---

## Allowed write paths

- `tickets/T-208-nigeria-ng-jos-hillcrest-profile.md`
- `countries/nigeria/entities/schools/profiles/**`
- `countries/nigeria/entities/schools/README.md`
- `countries/nigeria/data/entities/schools.csv`
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
- Country directories other than `countries/nigeria/**`

---

## Required outputs

- `countries/nigeria/entities/schools/profiles/jos/hillcrest-school/README.md` created or refreshed using the global high school profile template with completed snapshot, affordability, curriculum, outcomes, outreach plan, and sources.
- `countries/nigeria/data/entities/schools.csv` row for `ng-jos-hillcrest` updated with city/region, curriculum, priority tier, affordability evidence, and last_verified tied to the source report.
- Ticket status moved to `done` with a short "what changed" note once the profile and data are in place.

---

## Acceptance criteria

- [ ] Profile follows `/skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md` with filled sections (identity, governance, academics, fees, outcomes, contacts, visit logistics, risks, sources) and clearly labeled assumptions.
- [ ] Data rows in `countries/nigeria/data/entities/schools.csv` (and any country-specific high-potential CSV) mirror the profile for `Hillcrest School`: slug, city, tier, curricula, affordability signals, program-fit tags, evidence/source references, and `last_verified` date are consistent.
- [ ] Only allowed paths for `countries/nigeria` and this ticket were modified; no control-plane files were touched.
- [ ] Links to source report(s) and internal references resolve, and any new directories use the stable school_id-based slug noted in this ticket.

---

## Notes / reminders

- Emphasize affordability signals, curricula, program-fit tags, outbound evidence, and counselor/visit logistics to support UNIC Nicosia and UNIC Athens positioning.
- Label assumptions and verification needs; capture sources with dates inside the profile.
- Current run is updating the school profile only (index/README/CSV updates intentionally deferred to avoid collisions).

---

## Closure notes

- Closed and superseded by T-258.
