# T-587: RTB architecture photos — shorten filenames + rename index to photoindex (2025-12-22)

- Status: done
- Type: content
- Priority: P2
- Agent: EvoTicket Resolver
- Claimed-by: evoticketresolver_45zrkxa4
- Claimed-at: 2025-12-22T21:51:24Z
- Completed-at: 2025-12-22T21:54:59Z

## Allowed write paths
- Infrastructure/UNIC Nicosia/RTB (Research and Technology Building)/architecture/**
- tickets/T-587-rtb-photos-shorter-filenames-and-photoindex.md

## Forbidden write paths
- AGENTS.md
- ROADMAP.md
- README.md
- skills/**
- tickets/README.md

## Required outputs
- Infrastructure/UNIC Nicosia/RTB (Research and Technology Building)/architecture/photos/photoindex.md

## Acceptance criteria
- All 20 photo files in `Infrastructure/UNIC Nicosia/RTB (Research and Technology Building)/architecture/photos/` are renamed to a shorter, still-descriptive scheme (no redundant `UNIC Nicosia - RTB` prefix).
- `Infrastructure/UNIC Nicosia/RTB (Research and Technology Building)/architecture/photos/photoindex.md` lists all 20 renamed filenames and preserves the existing detailed per-photo descriptions.
- Any in-scope markdown references to the old filenames or `photos/index.md` are updated to the new filenames and `photos/photoindex.md`.

## Dependencies
- None

## Notes / context
- Current filenames are very long (`20251222 - UNIC Nicosia - RTB - ...`); request is to keep them descriptive but meaningfully shorter.
- `photoindex.md` currently exists as `index.md` and must be updated to reflect the renamed files.

## What changed
- Renamed the 20 RTB photos to shorter `20251222-rtb-...` kebab-case filenames (removing redundant `UNIC Nicosia - RTB`).
- Renamed `photos/index.md` to `photos/photoindex.md` and updated the inventory to match the new filenames.
