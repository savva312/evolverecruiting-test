# T-180: Nigeria premium secondary feeder ingestion (report-driven)

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T22:05:00Z
Last-updated: 2025-12-20

---

## Goal

Convert the “Nigeria Premium Secondary School Pipeline” report (Dec 20, 2025) into ticket-ready feeder school assets for Nigeria using the global schools-and-feeders skill: structured roster (CSV + index) and per-school profiles aligned to the high school profile template.

---

## Context

- Source: `countries/nigeria/reports/20251220-Nigeria Premium Secondary School Pipeline.md`.
- Follow the global workflow in `skills/schools-and-feeders/SKILL.md`, the profile template in `skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`, and Nigeria guidance in `countries/nigeria/skills/nigeria-schools-and-feeders/SKILL.md`.
- Keep scope within Nigeria; no cross-country edits.
- Label evidence strength (fees published vs. on request vs. proxy) per the source report.

---

## Allowed write paths

- `countries/nigeria/entities/schools/**`
- `countries/nigeria/data/entities/**`
- `countries/nigeria/reports/**`
- `research/**`
- `tickets/T-148-nigeria-premium-secondary-feeders.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global skills)
- Other country directories (e.g., `countries/bulgaria/**`, `countries/greece/**`, etc.)
- Other tickets (except status updates to this file)
- `.github/**`
- `scripts/**`

---

## Required outputs

- `countries/nigeria/entities/schools/README.md` updated with Nigeria-specific tiering rubric, city coverage, and links to roster/profile assets.
- `countries/nigeria/entities/schools/profiles/<city>/<school-slug>/README.md` created for all schools enumerated in the source report, aligned to the global high school profile template with evidence-strength notes and open questions.
- `countries/nigeria/data/entities/schools.csv` populated with roster entries for every covered school, aligned to an updated `countries/nigeria/data/entities/schools-dictionary.md` that reflects the captured fields.
- Ticket updated on completion with status = done and a short “What changed” summary.

---

## Acceptance criteria

- [ ] All schools from the source report appear in `schools.csv` with IDs, cities, regions, evidence/tier notes, sources, and last_verified dates.
- [ ] Per-school markdown profiles exist under `countries/nigeria/entities/schools/profiles/**` following the global template structure (sections present; data filled where available; open questions listed).
- [ ] Index README documents the tiering rubric used, city list, and links to profiles/CSV.
- [ ] No files outside `Allowed write paths` are modified.
- [ ] Ticket status updated to `done` with a concise “What changed” entry when outputs are complete.

---

## Execution notes (optional)

- What changed (short): Ingested the December 20, 2025 premium secondary school pipeline into Nigeria schools assets: populated `schools.csv` and dictionary with 61 tiered feeders, generated per-school profiles following the global template, and refreshed the schools README with rubric, counts, and links to data and profiles.
- Any open questions: Fee and contact validation pending for opaque/proxy schools; add counselor details and current fee sheets as outreach progresses.
- Follow-up tickets suggested: Create a validation sprint for “fees on request” schools (Lagos, Abuja, Port Harcourt) and add counselor contact capture once confirmed.
