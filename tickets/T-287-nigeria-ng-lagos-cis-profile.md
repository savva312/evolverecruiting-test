# T-287: Nigeria — Children’s International School (CIS) world-class profile build

Status: done
Type: content
Priority: P1
Dependencies: T-026-high-school-profile-template
Claimed-by: codex-gpt5
Claimed-at: 2025-12-23T15:00:00Z
Last-updated: 2025-12-23
Agent: EvoTicket Resolver

---

## Goal

Produce a world-class, deeply researched high school profile for **Children’s International School (CIS)** in **Lagos, Nigeria**, aligned to the global template and synced with the country schools dataset so recruiting teams can execute outreach with confidence.

---

## Context

- Source report: `countries/nigeria/reports/20251220-Nigeria Premium Secondary School Pipeline.md` (use as starting evidence; update with any verified contacts, fees, and curriculum details)
- Datasets: `countries/nigeria/data/entities/schools.csv`
- Templates/skills: `/skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`, `/skills/schools-and-feeders/SKILL.md`, `countries/nigeria/skills/nigeria-schools-and-feeders/SKILL.md`
- Priority tier / notes: Priority Tier1 from Nigeria Premium Secondary School Pipeline (school_id: ng-lagos-cis)

---

## Allowed write paths

- `tickets/T-255-nigeria-ng-lagos-cis-profile.md`
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

- `countries/nigeria/entities/schools/profiles/lagos/children-s-international-school-cis/README.md` created or refreshed using the global high school profile template with completed snapshot, affordability, curriculum, outcomes, outreach plan, and sources.
- `countries/nigeria/data/entities/schools.csv` row for `ng-lagos-cis` updated with city/region, curriculum, priority tier, affordability evidence, and last_verified tied to the source report.
- Ticket status moved to `done` with a short "what changed" note once the profile and data are in place.

---

## Acceptance criteria

- [ ] Profile follows `/skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md` with filled sections (identity, governance, academics, fees, outcomes, contacts, visit logistics, risks, sources) and clearly labeled assumptions.
- [ ] Data rows in `countries/nigeria/data/entities/schools.csv` (and any country-specific high-potential CSV) mirror the profile for `Children’s International School (CIS)`: slug, city, tier, curricula, affordability signals, program-fit tags, evidence/source references, and `last_verified` date are consistent.
- [ ] Only allowed paths for `countries/nigeria` and this ticket were modified; no control-plane files were touched.
- [ ] Links to source report(s) and internal references resolve, and any new directories use the stable school_id-based slug noted in this ticket.

---

## Notes / reminders

- Emphasize affordability signals, curricula, program-fit tags, outbound evidence, and counselor/visit logistics to support UNIC Nicosia and UNIC Athens positioning.
- Label assumptions and verification needs; capture sources with dates inside the profile.
- This run updates the school profile only (index/README/CSV left untouched per coordination request).

### What changed (2025-12-23)
- Built a full CIS profile aligned to the global template with refreshed governance, logistics, affordability signals, and clearly tagged assumptions/sources.
- Updated `countries/nigeria/data/entities/schools.csv` for `ng-lagos-cis` (curriculum detail, fee evidence, sources, `last_verified=2025-12-23`).
