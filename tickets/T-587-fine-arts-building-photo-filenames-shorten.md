Status: done
Type: structure
Priority: P1
Agent: EvoTicket Resolver
Claimed-by: evoticketresolver_qhn0h0f0
Claimed-at: 2025-12-22T21:52:31Z

# T-587: Fine Arts Building photo filenames — shorten + keep descriptive (UNIC Nicosia)

## Goal
Shorten the Fine Arts Building photo filenames (still descriptive) and update the photo index to match.

## Allowed write paths
- `Infrastructure/UNIC Nicosia/Fine Arts Building/architecture/photos/**`
- `tickets/T-587-fine-arts-building-photo-filenames-shorten.md`

## Forbidden write paths
- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`

## Required outputs
- `Infrastructure/UNIC Nicosia/Fine Arts Building/architecture/photos/photoindex.md` updated to reference the new filenames
- 31 renamed `.jpeg` files in `Infrastructure/UNIC Nicosia/Fine Arts Building/architecture/photos/` following `20251222 - NN-<short-slug>.jpeg`

## Acceptance criteria
- Exactly 31 `.jpeg` files exist in `Infrastructure/UNIC Nicosia/Fine Arts Building/architecture/photos/`.
- All 31 filenames start with `20251222 - ` and include a two-digit sequence `NN-`.
- `Infrastructure/UNIC Nicosia/Fine Arts Building/architecture/photos/photoindex.md` lists all 31 photos using the final filenames.

## Notes / context
- User request (2025-12-22): existing set is good but filenames are too long; rename to shorter (still descriptive) and update `photoindex.md`.

## What changed
- Renamed the 31 Fine Arts Building photos to a shorter numbered scheme: `20251222 - NN-<short-slug>.jpeg`.
- Updated `Infrastructure/UNIC Nicosia/Fine Arts Building/architecture/photos/photoindex.md` to reference the new filenames.
