# T-588 — Photo indices: standardize naming + format + skill update (2025-12-22)

- Status: done
- Type: structure
- Priority: P1
- Agent: EvoTicket Resolver
- Claimed-by: evoticketresolver_zwryx9nk
- Claimed-at: 2025-12-22T22:19:21Z
- Completed-at: 2025-12-22T22:36:00Z

## Allowed write paths
- `Infrastructure/UNIC Nicosia/Architecture Building/architecture/photos/**`
- `Infrastructure/UNIC Nicosia/Fine Arts Building/architecture/photos/**`
- `Infrastructure/UNIC Nicosia/RTB (Research and Technology Building)/architecture/photos/**`
- `Infrastructure/UNIC Nicosia/Europa Building/New Teaching Kitchen/photos/**`
- `Infrastructure/UNIC Nicosia/Europa Building/New Teaching Kitchen/culinary-arts-lab-signage.md`
- `skills/photo-documentation/SKILL.md`
- `tickets/T-588-photo-indices-standardize-format-and-skill.md`

## Forbidden write paths
- `AGENTS.md`
- `ROADMAP.md`
- `README.md`
- `skills/**` (except `skills/photo-documentation/SKILL.md`)
- `tickets/README.md`
- `**` (everything else)

## Required outputs
- `Infrastructure/UNIC Nicosia/Architecture Building/architecture/photos/photoindex.md`
- `Infrastructure/UNIC Nicosia/Fine Arts Building/architecture/photos/photoindex.md` (updated format)
- `Infrastructure/UNIC Nicosia/RTB (Research and Technology Building)/architecture/photos/photoindex.md` (updated format)
- `Infrastructure/UNIC Nicosia/Europa Building/New Teaching Kitchen/photos/photoindex.md`
- `skills/photo-documentation/SKILL.md` updated to:
  - standardize canonical index filename (`photoindex.md`)
  - standardize a single “world-class” index format including stakeholder lenses (architect, engineer, facilities, marketer, educator)
  - encode filename-length guidance (keep descriptive but short)

## Acceptance criteria
- [x] No photo files are renamed or deleted in any in-scope folder.
- [x] Each in-scope `photos/` folder contains exactly one canonical photo index named `photoindex.md` (no `photos/index.md` used as the canonical index).
- [x] Each `photoindex.md` includes:
  - a short “How to use this index” section
  - a consistent per-photo entry template with labeled stakeholder lenses:
    - Architect
    - Engineer
    - Facilities
    - Marketing
    - Educator
  - a **Wishlist / gaps** section
- [x] Each `photoindex.md` lists all photo filenames present in its folder (case-sensitive):
  - Architecture Building: 54 `.jpeg`
  - Fine Arts Building: 31 `.jpeg`
  - RTB: 20 `.jpeg`
  - New Teaching Kitchen: 26 `.jpeg`
- [x] `Infrastructure/UNIC Nicosia/Europa Building/New Teaching Kitchen/culinary-arts-lab-signage.md` references the canonical photo index filename.
- [x] No repo changes outside `Allowed write paths`.

## Notes / context
User request (2025-12-22): review the Architecture / Fine Arts / RTB photo indices, standardize index filenames + format, and update the relevant global skill with the new standard.

## What changed
- Standardized photo index filename to `photoindex.md` across in-scope photo folders (removed/renamed legacy `index.md`).
- Rewrote the Architecture, Fine Arts, RTB, and New Teaching Kitchen photo indices to a single format with explicit stakeholder lenses (architect, engineer, facilities, marketing, educator) and consistent sections.
- Updated `skills/photo-documentation/SKILL.md` to codify the new filename, format, and shorter-filename guidance.
- Updated `Infrastructure/UNIC Nicosia/Europa Building/New Teaching Kitchen/culinary-arts-lab-signage.md` and the Teaching Kitchen photos README to reference `photos/photoindex.md`.
