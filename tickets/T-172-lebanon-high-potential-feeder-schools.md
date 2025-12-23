# T-172: Lebanon high-potential feeder high schools (USD-based)

Status: done
Type: content
Priority: P1
Dependencies: T-087, T-090
Claimed-by: work
Claimed-at: 2025-12-20T21:56:19Z
Last-updated: 2025-12-20

---

## Goal

Translate the “Lebanon USD-Feeder High Schools” report into an actionable, high-potential feeder list inside the Lebanon country folder, following the global schools-and-feeders skill (index + CSV alignment).

---

## Allowed write paths

- `tickets/T-147-lebanon-high-potential-feeder-schools.md`
- `countries/lebanon/entities/schools/**`
- `countries/lebanon/data/entities/schools.csv`
- `countries/lebanon/data/entities/schools-dictionary.md`
- `research/**` (execution notes, optional)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `.github/**`
- `scripts/**`
- `tickets/` other than this file
- Country directories other than `countries/lebanon/**`

---

## Required outputs

- `countries/lebanon/entities/schools/README.md` updated with a “High-potential feeder high schools” section that summarizes top targets, affordability tiers, and USD-requirement notes aligned to the global schools-and-feeders skill.
- `countries/lebanon/data/entities/schools.csv` populated with rows for the identified high-potential feeders using stable `school_id` slugs, cities/regions, type/ownership, USD affordability notes, and `as_of` dates.
- This ticket marked `done` with a short “What changed” note after completion.

---

## Acceptance criteria

- High-potential feeder section lists the schools surfaced in the USD-fee report with city/area grouping, affordability tiering (High/Medium), and USD-requirement notes; sources are referenced or linked.
- CSV rows exist for the same schools with `school_id`, `name`, `city`, `region`, `type`, `ownership`, `notes`, and `as_of` filled; slugs are consistent with the Lebanon schools skill guidance.
- Changes stay within allowed paths and reuse the global schools-and-feeders structure (index + CSV).
- Ticket status moved to `done` with a concise execution summary once outputs are in place.

---

## Notes/Context

- Use the `countries/lebanon/reports/20251220-Lebanon USD-Feeder High Schools.md` findings as the authoritative source for USD-based affordability signals.
- Align slugging and prioritization language to `skills/schools-and-feeders/SKILL.md` and `countries/lebanon/skills/lebanon-schools-and-feeders/SKILL.md`.

---

## What changed
- Added a USD-based high-potential feeder section to `countries/lebanon/entities/schools/README.md` with tiering aligned to the global schools-and-feeders skill and sourced from the Lebanon USD feeder report.
- Populated `countries/lebanon/data/entities/schools.csv` with high/medium-tier feeder schools, consistent slugs, and USD requirement notes for visit sequencing.
- Kept all edits within Lebanon paths; no report content was modified.
