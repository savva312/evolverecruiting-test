# T-335: “Ioannis Tsiamoulis” Private Lyceum profile

Status: done
Type: content
Priority: P2
Dependencies: T-300-greece-affordability-school-extraction
Claimed-by: work
Claimed-at: 2025-12-21T19:07:07Z
Last-updated: 2025-12-21

---

## Goal

Draft a world-class school profile for **“Ioannis Tsiamoulis” Private Lyceum** using the global high school profile template, capturing affordability signals and international pathways highlighted in the 2025-12-21 affordability report.

## Context

- City/Region: West Athens, Attica (Attica (Athens metro)).
- Signal: Greek private Lyceum; fees not published.
- Source: `countries/greece/reports/20251221-Greek High Schools for UNIC Affordability.md` (see Section 4–6 for detailed listings).
- Align profile fields with the row for `sch-gr-athens-tsiamoulis-001` in `countries/greece/data/entities/schools.csv`. Aggregate README/index updates are handled by T-356 after profile delivery.

## Allowed write paths

- `countries/greece/entities/schools/profiles/athens/sch-gr-athens-tsiamoulis-001/**`
- `tickets/T-323-sch-gr-athens-tsiamoulis-001-profile.md`
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

- `countries/greece/entities/schools/profiles/athens/sch-gr-athens-tsiamoulis-001/README.md` populated using `skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`, including `last_verified` and sources.
- Optional run notes in `executions/` if discovery requires follow-ups.

## Acceptance criteria

- Profile follows the global template with accurate metadata for `sch-gr-athens-tsiamoulis-001` and cites sources from the affordability report or official school channels.
- No personal contact details beyond publicly listed organizational emails/phones.
- Work stays within allowed paths; CSV/index/README changes are deferred to T-356.
- `last_verified` date and sources are provided.

## What changed (2025-12-21)

- Delivered `countries/greece/entities/schools/profiles/athens/sch-gr-athens-tsiamoulis-001/README.md` using the global template with `last_verified` date and sources.
- Populated core metadata (location, contact details, curriculum, outreach plan) from the Attica Directorate listing, school website, and the 2025-12-21 affordability report; noted unknown items for follow-up.
