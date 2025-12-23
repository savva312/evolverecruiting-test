# T-215: Lebanon — Collège Notre Dame des Sœurs Antonines (Hazmieh–Jamhour) world-class profile build

Status: done
Type: content
Priority: P1
Dependencies: T-026-high-school-profile-template
Claimed-by: work
Claimed-at: 2025-12-20T22:40:51Z
Last-updated: 2025-12-20

---

## Goal

Produce a world-class, deeply researched high school profile for **Collège Notre Dame des Sœurs Antonines (Hazmieh–Jamhour)** in **Hazmieh/Mount Lebanon, Lebanon**, aligned to the global template and synced with the country schools dataset so recruiting teams can execute outreach with confidence.

---

## Context

- Source report: `countries/lebanon/reports/20251220-Lebanon USD-Feeder High Schools.md` (use as starting evidence; update with any verified contacts, fees, and curriculum details)
- Datasets: `countries/lebanon/data/entities/schools.csv`
- Templates/skills: `/skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`, `/skills/schools-and-feeders/SKILL.md`, `countries/lebanon/skills/lebanon-schools-and-feeders/SKILL.md`
- Priority tier / notes: Parent support $3,250 (S1–S3) / $3,550 (IB1–IB2) for 2025-26; Tier: Medium; source https://antohj.b-cdn.net/wp/wp-content/uploads/2025/09/%D8%A7%D9%84%D8%A3%D9%82%D8%B3%D8%A7%D8%B7-%D8%A7%D9%84%D9%85%D8%AF%D8%B1%D8%B3%D9%8A%D8%A9-%D9%84%D9%84%D8%B9%D8%A7%D9%85-2025-2026.pdf (school_id: lb-hazmieh-antonines)

---

## Allowed write paths

- `tickets/T-182-lebanon-lb-hazmieh-antonines-profile.md`
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

- `countries/lebanon/entities/schools/profiles/lb-hazmieh-antonines/README.md` created or refreshed using the global high school profile template with completed snapshot, affordability, curriculum, outcomes, outreach plan, and sources.
- `countries/lebanon/data/entities/schools.csv` row for `lb-hazmieh-antonines` updated with city/region, curriculum, priority tier, affordability evidence, and last_verified tied to the source report.
- Ticket status moved to `done` with a short "what changed" note once the profile and data are in place.

---

## Acceptance criteria

- [x] Profile follows `/skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md` with filled sections (identity, governance, academics, fees, outcomes, contacts, visit logistics, risks, sources) and clearly labeled assumptions.
- [x] Data rows in `countries/lebanon/data/entities/schools.csv` (and any country-specific high-potential CSV) mirror the profile for `Collège Notre Dame des Sœurs Antonines (Hazmieh–Jamhour)`: slug, city, tier, curricula, affordability signals, program-fit tags, evidence/source references, and `last_verified` date are consistent.
- [x] Only allowed paths for `countries/lebanon` and this ticket were modified; no control-plane files were touched.
- [x] Links to source report(s) and internal references resolve, and any new directories use the stable school_id-based slug noted in this ticket.

---

## What changed (2025-12-20)

- Created a full high school profile at `countries/lebanon/entities/schools/profiles/lb-hazmieh-antonines/README.md` following the global template.
- Updated `countries/lebanon/data/entities/schools.csv` for `lb-hazmieh-antonines` with refreshed city/region, curricula, tier, affordability evidence, and sources.
- Linked the new profile from `countries/lebanon/entities/schools/README.md` for navigation.

---

## Notes / reminders

- Emphasize affordability signals, curricula, program-fit tags, outbound evidence, and counselor/visit logistics to support UNIC Nicosia and UNIC Athens positioning.
- Label assumptions and verification needs; capture sources with dates inside the profile.
