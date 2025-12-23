# T-171: Jordan premium high-school feeders (tiering + profiles)

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T21:57:28Z
Last-updated: 2025-12-20

---

## Goal

Use the December 20, 2025 Jordan premium high-school feeder report to build a country-level view of high-potential secondary schools for UNIC/UNIC Athens. Align outputs to the global schools-and-feeders skill by refreshing the Jordan schools index, adding a structured CSV, and seeding Tier 1 profiles that follow the global high school template.

---

## Context

- Primary source: `countries/jordan/reports/20251220-Jordan Premium High-School Feeders.md`.
- Follow the global workflow in `skills/schools-and-feeders/SKILL.md` and the Jordan addendum in `countries/jordan/skills/jordan-schools-and-feeders/SKILL.md`.
- Replace placeholder Bulgaria content currently sitting under `countries/jordan/entities/schools/`.

---

## Allowed write paths

- `tickets/T-147-jordan-premium-high-school-feeders.md`
- `countries/jordan/entities/schools/**`
- `countries/jordan/data/entities/schools*`
- `countries/jordan/reports/**` (read-only unless notes are added)
- `research/**` (optional execution notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (outside references only)
- `tickets/**` (except this ticket file)
- `.github/**`
- `scripts/**`
- Country directories other than `countries/jordan/**`

---

## Required outputs

- `countries/jordan/entities/schools/README.md` updated with a tiered, Jordan-specific high-potential feeder list grounded in the 2025-12-20 report and aligned to the global skill structure.
- `countries/jordan/data/entities/schools.csv` populated with Tier 1 and Tier 2 schools, including curricula, fee/evidence tags, program-fit notes, and last verified dates.
- At least three Tier 1 profile stubs under `countries/jordan/entities/schools/profiles/<city>/<slug>/README.md` that follow the global high school template (with unknowns marked).
- Legacy Bulgaria-oriented placeholders removed or renamed to avoid confusion.

---

## Acceptance criteria

- [x] Ticket fields reflect current status and ownership.
- [x] Updated schools index documents tiering logic, cites the 2025-12-20 feeder report, and links to CSV/profiles.
- [x] `schools.csv` contains entries for all Tier 1 and Tier 2 schools with evidence tags and program-fit cues.
- [x] At least three Tier 1 profile stubs exist, using the global template headings and noting missing data explicitly.
- [x] No changes occur outside `Allowed write paths`.

---

## Execution notes (optional)

- What changed (short): Rebuilt the Jordan schools index using the 2025-12-20 premium feeder report, populated `schools.csv` with Tier 1/2 targets and evidence tags, added four Tier 1 profile stubs (King’s Academy, ACS, ICS, ABS), and removed Bulgaria placeholders.
- Open questions: Need fee schedules and counselor contacts for B/C evidence schools (IAA, Mashrek, AMS, British International Academy, Cambridge High School, Sands, Aqaba International School).
- Follow-ups: Build remaining Tier 1 profiles (IAA, NES, MAS, Amman Academy) and verify fees/contacts before drafting Tier 2 stubs.
