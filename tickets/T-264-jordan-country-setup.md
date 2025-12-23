# T-264: Jordan country setup and migration

Status: done
Type: structure
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2026-02-04
Last-updated: 2026-02-04

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

- `tickets/T-231-jordan-country-setup.md`
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

- [x] `jordan/` directory exists with the same subfolder structure as `bulgaria/`.
- [x] Content within `jordan/**` references Jordan (not Bulgaria) where applicable, including major cities/regions.
- [x] No files outside `Allowed write paths` are modified.
- [x] `ROADMAP.md` repo map reflects Jordan as a top-level country directory.
- [x] All CSV/MD files added remain valid text and keep original formatting.

---

## Execution notes (optional)

- What changed (short):
  - Built out `countries/jordan/data/**` to mirror Bulgaria (entities, marketing, programs, operations) with Jordan-specific dictionaries and starter CSVs.
  - Localized market materials (affordability, outbound mobility) and digital playbook elements to remove Bulgarian references and flag data gaps transparently.
  - Updated the Jordan outbound baseline report to document missing Eurostat/UIS data and the remediation plan; ROADMAP already reflected Jordan so no change needed.
- Any open questions:
  - None.
- Follow-up tickets suggested:
  - None.
