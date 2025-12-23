# T-256: Serbia — Prva ruska međunarodna škola “Valentina Tereškova” world-class profile build

Status: done
Type: content
Priority: P1
Dependencies: T-026-high-school-profile-template
Claimed-by: work
Claimed-at: 2025-12-21T08:06:23+00:00
Last-updated: 2025-12-21
What changed: Captured published campus address from contact page, refreshed profile logistics/sources, and aligned `schools.csv` notes; tuition and named contacts still require verification during outreach.

---

## Goal

Produce a world-class, deeply researched high school profile for **Prva ruska međunarodna škola “Valentina Tereškova”** in **Belgrade, Serbia**, aligned to the global template and synced with the country schools dataset so recruiting teams can execute outreach with confidence.

---

## Context

- Source report: `countries/serbia/reports/20251220-Serbia High-School Pipeline Report.md` (use as starting evidence; update with any verified contacts, fees, and curriculum details)
- Datasets: `countries/serbia/data/entities/schools.csv`
- Templates/skills: `/skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`, `/skills/schools-and-feeders/SKILL.md`, `countries/serbia/skills/serbia-schools-and-feeders/SKILL.md`
- Priority tier / notes: Affordability tier Medium-High per Serbia pipeline index (school_id: prva-ruska-medunarodna-skola-valentina-tereskova)

---

## Allowed write paths

- `tickets/T-223-serbia-prva-ruska-medunarodna-skola-valentina-tereskova-profile.md`
- `countries/serbia/entities/schools/profiles/**`
- `countries/serbia/entities/schools/README.md`
- `countries/serbia/data/entities/schools.csv`
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
- Country directories other than `countries/serbia/**`

---

## Required outputs

- `countries/serbia/entities/schools/profiles/belgrade/prva-ruska-medunarodna-skola-valentina-tereskova/README.md` created or refreshed using the global high school profile template with completed snapshot, affordability, curriculum, outcomes, outreach plan, and sources.
- `countries/serbia/data/entities/schools.csv` row for `prva-ruska-medunarodna-skola-valentina-tereskova` updated with city/region, curriculum, priority tier, affordability evidence, and last_verified tied to the source report.
- Ticket status moved to `done` with a short "what changed" note once the profile and data are in place.

---

## Acceptance criteria

- [x] Profile follows `/skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md` with filled sections (identity, governance, academics, fees, outcomes, contacts, visit logistics, risks, sources) and clearly labeled assumptions.
- [x] Data rows in `countries/serbia/data/entities/schools.csv` (and any country-specific high-potential CSV) mirror the profile for `Prva ruska međunarodna škola “Valentina Tereškova”`: slug, city, tier, curricula, affordability signals, program-fit tags, evidence/source references, and `last_verified` date are consistent.
- [x] Only allowed paths for `countries/serbia` and this ticket were modified; no control-plane files were touched.
- [x] Links to source report(s) and internal references resolve, and any new directories use the stable school_id-based slug noted in this ticket.

---

## Notes / reminders

- Emphasize affordability signals, curricula, program-fit tags, outbound evidence, and counselor/visit logistics to support UNIC Nicosia and UNIC Athens positioning.
- Label assumptions and verification needs; capture sources with dates inside the profile.
- Current run: drafting the school profile only; dataset/index updates deferred per coordination request.
