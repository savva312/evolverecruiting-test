Status: done
Type: structure
Priority: P1
Agent: EvoTicket Resolver
Claimed-by: evoticketresolver_plxpstdr
Claimed-at: 2025-12-22T20:59:52Z

# T-585: Fine Arts Building photo renames + photo index (UNIC Nicosia)

## Goal
Rename the Fine Arts Building photo set to a human-friendly, descriptive naming scheme and add a detailed index describing what each photo shows.

## Allowed write paths
- `Infrastructure/UNIC Nicosia/Fine Arts Building/architecture/photos/**`
- `tickets/T-585-fine-arts-building-photo-renames-and-index.md`

## Forbidden write paths
- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`

## Required outputs
- `Infrastructure/UNIC Nicosia/Fine Arts Building/architecture/photos/photoindex.md`
- 31 renamed image files in `Infrastructure/UNIC Nicosia/Fine Arts Building/architecture/photos/` using the prefix `20251222 - `

## Acceptance criteria
- No `signal-2025-12-22-224744*.jpeg` files remain in `Infrastructure/UNIC Nicosia/Fine Arts Building/architecture/photos/`.
- Exactly 31 `.jpeg` files exist in that folder and each filename starts with `20251222 - `.
- `Infrastructure/UNIC Nicosia/Fine Arts Building/architecture/photos/photoindex.md` lists all 31 photos with:
  - the final filename
  - a more detailed expert description of what is visible

## Notes / context
- User request (2025-12-22): rename 31 Fine Arts Building photos and create an expert-facing photo index.

## What changed
- Renamed all 31 photos in `Infrastructure/UNIC Nicosia/Fine Arts Building/architecture/photos/` to a descriptive `20251222 - ...` naming scheme.
- Added `Infrastructure/UNIC Nicosia/Fine Arts Building/architecture/photos/photoindex.md` with per-photo expert descriptions and a wishlist of missing coverage; added a small `index.md` pointer for folder convention.
