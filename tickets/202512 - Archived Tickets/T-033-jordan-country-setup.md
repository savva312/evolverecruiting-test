# T-033: Jordan country setup and migration

Status: archived
Type: structure
Priority: P1
Dependencies: (none)
Claimed-by:
Claimed-at:
Last-updated: 2025-12-21

---

## Goal

Add Jordan as a first-class country directory that mirrors the Bulgaria structure while adjusting country-specific references (e.g., major cities, country naming). Update the roadmap map to reflect the new country. Ensure all required subfolders and stub content exist for Jordan with Jordan-specific context where relevant.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` — repo map and change policy
- External constraints (if any): none
- Assumptions: Jordan should follow the same country-first layout used for Bulgaria with localized details.

---

## Allowed write paths

- `tickets/T-028-jordan-country-setup.md`
- `jordan/**`
- `ROADMAP.md`
- `research/**` (optional; only for notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- Any country directories other than `jordan/**`

---

## Required outputs

- `jordan/` top-level directory with subfolders matching Bulgaria’s structure (data, entities, go-to-market, market, program-clusters, reports, skills).
- Jordan-specific copies of Bulgaria’s markdown and CSV assets with country references updated to Jordan where applicable (e.g., city lists).
- Updated `ROADMAP.md` repo map mentioning Jordan as a top-level country directory.

---

## Acceptance criteria

- [ ] `jordan/` directory exists with the same subfolder structure as `bulgaria/`.
- [ ] Content within `jordan/**` references Jordan (not Bulgaria) where applicable, including major cities/regions.
- [ ] No files outside `Allowed write paths` are modified.
- [ ] `ROADMAP.md` repo map reflects Jordan as a top-level country directory.
- [ ] All CSV/MD files added remain valid text and keep original formatting.

---

## Execution notes (optional)

- What changed (short):
- Any open questions:
- Follow-up tickets suggested:

---

## Closure notes

- Closed and superseded by T-231.
