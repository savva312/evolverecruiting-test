# T-307: Serbia high-priority schools profile sync

Status: done
Type: qa
Priority: P0
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-21
Last-updated: 2025-12-21

---

## Goal

Audit all high-priority Serbian high school profiles (premium tuition or international-intent schools) to confirm the schools README, school profile index, and `schools.csv` reflect the latest profiles and metadata. Capture any missing priority schools as new tickets so the pipeline stays complete.

---

## Context

- Source reference: `countries/serbia/reports/20251220-Serbia High-School Pipeline Report.md`
- Existing Serbia school profiles under `countries/serbia/entities/schools/profiles/**`.
- CSV standard defined in `countries/serbia/data/entities/schools-dictionary.md` and `field-standards.md`.
- Focus on premium/high-affordability schools already prioritized for UNIC/UNIC Athens outreach.

---

## Allowed write paths

- `tickets/T-275-serbia-high-priority-schools-sync.md`
- `tickets/T-22*-serbia-*.md` (new follow-up tickets for missing Serbian school profiles)
- `countries/serbia/entities/schools/**`
- `countries/serbia/data/entities/schools.csv`
- `executions/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/README.md`
- `.github/**`
- `scripts/**`

---

## Required outputs

- Updated `countries/serbia/entities/schools/README.md` reflecting the current high-priority list and links.
- Updated `countries/serbia/data/entities/schools.csv` with one row per high-priority school profile, following the dictionary.
- Any missing high-priority school tickets created under `tickets/` with Serbia scope.
- Profile index/link fixes inside `countries/serbia/entities/schools/profiles/**` if discrepancies are found.

---

## Acceptance criteria

- [x] Ticket status set to `in-progress` with claim metadata before substantive changes.
- [x] High-priority schools in Serbia have matching profile pages, README/index coverage, and CSV rows with `as_of` date.
- [x] No edits occur outside `Allowed write paths`.
- [x] New follow-up tickets exist for any missing high-priority school profiles, using the repo ticket format.
- [x] CSV validates against `schools-dictionary.md` (headers intact; rows populated for all priority schools).
- [x] Internal links resolve to existing files in `countries/serbia/entities/schools/profiles/**`.

---

## Execution notes (optional)

- What changed (short): Revalidated all 15 high-priority Serbia school profiles; refreshed schools README quick index and coverage notes; rebuilt `schools.csv` to match the Serbia dictionary with 2025-12-21 `as_of` dates and updated notes/contacts; confirmed all profile links resolve—no new tickets needed.
- Any open questions: None noted.
- Follow-up tickets suggested: None; revisit pricing/contact refresh in next data pull window.
