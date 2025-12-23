# T-221: Lebanon — Collège Notre Dame de Louaizé world-class profile build

Status: done
Type: content
Priority: P1
Dependencies: T-026-high-school-profile-template
Claimed-by: work
Claimed-at: 2025-12-20T22:41:51Z
Last-updated: 2025-12-20
What changed: Profile created for Collège Notre Dame de Louaizé; CSV row enriched; school index updated.

---

## Goal

Produce a world-class, deeply researched high school profile for **Collège Notre Dame de Louaizé** in **Zouk Mosbeh, Lebanon**, aligned to the global template and synced with the country schools dataset so recruiting teams can execute outreach with confidence.

---

## Context

- Source report: `countries/lebanon/reports/20251220-Lebanon USD-Feeder High Schools.md` (use as starting evidence; update with any verified contacts, fees, and curriculum details)
- Datasets: `countries/lebanon/data/entities/schools.csv`
- Templates/skills: `/skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`, `/skills/schools-and-feeders/SKILL.md`, `countries/lebanon/skills/lebanon-schools-and-feeders/SKILL.md`
- Priority tier / notes: USD tuition $3,450–$3,930 (G10–G12, 2025-26); Tier: Medium; source https://www.cndl.edu.lb/fr/tuition-fees/?utm_source=openai (school_id: lb-zouk-mosbeh-college-notre-dame-de-louaize)

---

## Allowed write paths

- `tickets/T-188-lebanon-lb-zouk-mosbeh-college-notre-dame-de-louaize-profile.md`
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

- `countries/lebanon/entities/schools/profiles/lb-zouk-mosbeh-college-notre-dame-de-louaize/README.md` created or refreshed using the global high school profile template with completed snapshot, affordability, curriculum, outcomes, outreach plan, and sources.
- `countries/lebanon/data/entities/schools.csv` row for `lb-zouk-mosbeh-college-notre-dame-de-louaize` updated with city/region, curriculum, priority tier, affordability evidence, and last_verified tied to the source report.
- Ticket status moved to `done` with a short "what changed" note once the profile and data are in place.

---

## Acceptance criteria

- [x] Profile follows `/skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md` with filled sections (identity, governance, academics, fees, outcomes, contacts, visit logistics, risks, sources) and clearly labeled assumptions.
- [x] Data rows in `countries/lebanon/data/entities/schools.csv` (and any country-specific high-potential CSV) mirror the profile for `Collège Notre Dame de Louaizé`: slug, city, tier, curricula, affordability signals, program-fit tags, evidence/source references, and `last_verified` date are consistent.
- [x] Only allowed paths for `countries/lebanon` and this ticket were modified; no control-plane files were touched.
- [x] Links to source report(s) and internal references resolve, and any new directories use the stable school_id-based slug noted in this ticket.

---

## Notes / reminders

- Emphasize affordability signals, curricula, program-fit tags, outbound evidence, and counselor/visit logistics to support UNIC Nicosia and UNIC Athens positioning.
- Label assumptions and verification needs; capture sources with dates inside the profile.
