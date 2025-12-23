# T-587 — Architecture Building photos: shorten filenames (2025-12-22)

- Status: done
- Type: structure
- Priority: P1
- Agent: EvoTicket Resolver
- Claimed-by: evoticketresolver__mpfxsjy
- Claimed-at: 2025-12-22T21:51:18Z
- Completed-at: 2025-12-22T21:54:37Z

## Allowed write paths
- `Infrastructure/UNIC Nicosia/Architecture Building/architecture/photos/**`
- `tickets/T-587-architecture-building-photos-shorten-filenames.md`

## Forbidden write paths
- `AGENTS.md`
- `ROADMAP.md`
- `README.md`
- `skills/**`
- `tickets/README.md`
- `**` (everything else)

## Required outputs
- All `*.jpeg` files in `Infrastructure/UNIC Nicosia/Architecture Building/architecture/photos/` renamed to shorter, still-descriptive filenames.
- `Infrastructure/UNIC Nicosia/Architecture Building/architecture/photos/index.md` updated to match renamed files (case-sensitive).

## Acceptance criteria
- [ ] Folder contains exactly **54** `.jpeg` photos after renaming.
- [ ] Every photo filename starts with `20251222 - ` and ends with `.jpeg`.
- [ ] Filenames are significantly shorter than the current verbose phrases while remaining descriptive (use concise keyword slugs; avoid filler words like “with/beside/view/alternate angle”).
- [ ] `index.md` lists all 54 filenames (exact match to disk) and no longer references the old long names.
- [ ] No repo changes outside `Allowed write paths`.

## Notes / context
User request: everything in the folder is good, but the current photo filenames are still absurdly long; shorten them while keeping them descriptive for GitHub browsing.

## What changed
- Renamed the 54 Architecture Building photos to shorter, keyword-style filenames (kept `20251222 - ` prefix).
- Updated `Infrastructure/UNIC Nicosia/Architecture Building/architecture/photos/index.md` to match the new filenames.
