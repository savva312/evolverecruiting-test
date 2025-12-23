---
name: infrastructure-building-folders
description: "Scaffold and extend UNIC campus building folders without creating unnecessary empty directories."
compatibility: Infrastructure/\<Campus>/\<Building>
metadata:
  author: canonical
  version: "1.0"
---

## Purpose and scope
- Use this skill when creating or refreshing building-level folders under `Infrastructure/<Campus>/<Building>/`.
- Default to a light, non-empty scaffold; grow the tree only when you have real content (plans, photos, SOPs, notes).

## Base scaffold (always create)
Create these items only:
1) `README.md` — brief description of the building, purpose, key contacts, and links to active work.
2) `planning/` — site/zoning/accessibility notes; add files when you have content (e.g., `master-plan.md`, `zoning-entitlements.md`).
3) `architecture/` with two subfolders:
   - `floorplans/` — store scaled drawings, annotated exports, and thumbnails. Add files when available; no placeholders.
   - `photos/` — building-level images (exterior, lobbies, circulation). Index each shoot per `skills/photo-documentation`.
4) `rooms/` — parent folder for room-specific content; add room subfolders only when documenting a room.

## Incremental expansion (add only when populated)
- **Architecture (beyond floorplans/photos):** add `sections-elevations/`, `finishes/`, or similar only when you have files to place.
- **Engineering:** add `engineering/` with subfolders (`mechanical/`, `electrical/`, `plumbing/`, `fire-life-safety/`, `it-telecom/`, `energy-sustainability/`) when corresponding schematics, schedules, or O&M notes exist.
- **Operations:** add `operations/` with `security/`, `custodial/`, `waste-management/`, `maintenance/`, `emergency-response/` as you gather SOPs or logs.
- **Compliance:** add `compliance/inspections/` or `compliance/regulations/` when you have certificates, inspection reports, or code references.
- **Governance/metadata:** add `metadata.yaml` (location, floors, GFA, occupancy, building codes, BIM links, last-audited) and `governance.md` (change control, inspection cadence) once data is known.
- Avoid creating empty subfolders. Create each folder at the moment you add the first file in it.

## Rooms (add per-space only when needed)
For each documented space, create `rooms/<room-name>/` with:
- `README.md` — purpose, capacity, environmental tolerances, quick stats.
- `analysis.md` — utilization, issues, change requests; create only when analysis exists.
- `photos/` — only when you have images; include `photoindex.md` per `skills/photo-documentation`.
- `equipment/` — create when at least one tracked asset exists; inside, add `<equipment-name>/` with `README.md` (specs, serials, warranty, maintenance cadence) and `logs.md` (calibration/maintenance history) when data exists.
- Add additional subfolders (e.g., `layout/`, `safety/`) only when placing real content.

## Drawing and photo handling
- Keep binary plans (PDF/DWG exports) with a short “how to open” note; include PNG/JPEG previews for quick reference.
- For photos, use the naming/indexing standard in `skills/photo-documentation` and place them under `architecture/photos/` or the room’s `photos/` folder, not mixed.
- Prefer Markdown for notes and indices; avoid large binaries unless they are source drawings or necessary visuals.

## Quick checklist
- [ ] Base scaffold limited to `README.md`, `planning/`, `architecture/` (`floorplans/`, `photos/`), and `rooms/`.
- [ ] New folders are created only when the first file for that domain is ready.
- [ ] Room/equipment subfolders exist only for documented spaces/assets.
- [ ] Floorplans, photos, and metadata follow naming and indexing conventions; no empty placeholder files.
