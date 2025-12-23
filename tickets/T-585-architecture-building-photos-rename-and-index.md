# T-585 — Architecture Building photos: rename + index (2025-12-22)

- Status: done
- Type: structure
- Priority: P1
- Agent: EvoTicket Resolver
- Claimed-by: evoticketresolver_3nmm1h2b
- Claimed-at: 2025-12-22T20:53:09Z
- Completed-at: 2025-12-22T21:13:03Z

## Allowed write paths
- `Infrastructure/UNIC Nicosia/Architecture Building/architecture/photos/**`
- `tickets/T-585-architecture-building-photos-rename-and-index.md`

## Forbidden write paths
- `AGENTS.md`
- `ROADMAP.md`
- `README.md`
- `skills/**`
- `tickets/README.md`
- `**` (everything else)

## Required outputs
- `Infrastructure/UNIC Nicosia/Architecture Building/architecture/photos/index.md`
- All `*.jpeg` files in `Infrastructure/UNIC Nicosia/Architecture Building/architecture/photos/` renamed to the format `20251222 - <substantive description>.jpeg`

## Acceptance criteria
- [ ] Folder contains **54** `.jpeg` photos after rename (no duplicates/missing).
- [ ] Every photo filename starts with `20251222 - ` and is substantively descriptive.
- [ ] `Infrastructure/UNIC Nicosia/Architecture Building/architecture/photos/index.md` lists all 54 filenames (case-sensitive match to disk) with detailed per-photo descriptions and a wishlist/gaps section.
- [ ] No repo changes outside `Allowed write paths`.

## Notes / context
User request: rename the Architecture Building photo set and create a world-class per-photo index (architecture/engineering/design/facilities lens).

## What changed
- Renamed 54 photos to `20251222 - <substantive description>.jpeg`.
- Added `Infrastructure/UNIC Nicosia/Architecture Building/architecture/photos/index.md` with per-photo descriptions and a wishlist/gaps section.
