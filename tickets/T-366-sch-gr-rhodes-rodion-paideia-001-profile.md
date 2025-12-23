# T-366: Rodion Paideia Educational Group, General Lyceum profile

Status: done
Type: content
Priority: P2
Dependencies: T-300-greece-affordability-school-extraction
Claimed-by: work
Claimed-at: 2025-12-21T23:21:30Z
Last-updated: 2025-12-21

---

## Goal

Draft a world-class school profile for **Rodion Paideia Educational Group, General Lyceum** using the global high school profile template, capturing affordability signals and international pathways highlighted in the 2025-12-21 affordability report.

## Context

- City/Region: Rhodes, South Aegean (Islands).
- Signal: Private Lyceum; premium island option; fees not captured.
- Source: `countries/greece/reports/20251221-Greek High Schools for UNIC Affordability.md` (see Section 4–6 for detailed listings).
- Align profile fields with the row for `sch-gr-rhodes-rodion-paideia-001` in `countries/greece/data/entities/schools.csv`. Aggregate README/index updates are handled by T-356 after profile delivery.

## Allowed write paths

- `countries/greece/entities/schools/profiles/rhodes/sch-gr-rhodes-rodion-paideia-001/**`
- `tickets/T-354-sch-gr-rhodes-rodion-paideia-001-profile.md`
- `executions/**` (optional run notes)

## Forbidden write paths

- `countries/greece/data/entities/schools.csv`
- `countries/greece/entities/schools/index.md`
- `countries/greece/entities/schools/README.md`
- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- Other country directories (e.g., `countries/bulgaria/**`, `countries/nigeria/**`, etc.)

## Required outputs

- `countries/greece/entities/schools/profiles/rhodes/sch-gr-rhodes-rodion-paideia-001/README.md` populated using `skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`, including `last_verified` and sources.
- Optional run notes in `executions/` if discovery requires follow-ups.

## Acceptance criteria

- Profile follows the global template with accurate metadata for `sch-gr-rhodes-rodion-paideia-001` and cites sources from the affordability report or official school channels.
- No personal contact details beyond publicly listed organizational emails/phones.
- Work stays within allowed paths; CSV/index/README changes are deferred to T-356.
- `last_verified` date and sources are provided.

## What changed

- Added initial profile for `sch-gr-rhodes-rodion-paideia-001` using the global template, grounded in the affordability report and sch.gr registry entry, with open questions flagged for tuition, calendar, and counselor contacts.
