# T-389: Greece competitor links to new UNIC directory names

Status: done  
Type: content  
Priority: P1  
Dependencies: T-025, T-128  
Claimed-by: work  
Claimed-at: 2025-12-21T00:00:00Z  
Last-updated: 2025-12-21T00:35:00Z

---

## Goal

Update Greece competitor files to reference the new space-free UNIC campus directories (`UNIC/unicnicosia/` and `UNIC/unicathens/`) instead of the old `UNIC/UNIC Nicosia` and `UNIC/UNIC Athens` paths.

## Allowed write paths

- `countries/greece/entities/competitors/**`
- `UNIC/**` (only if needed to support the new link targets)
- `tickets/T-371-greece-competitor-link-updates.md`
- `research/T-371-greece-competitor-link-updates/**` (optional notes)

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- Other country directories outside Greece
- `.github/**`
- `scripts/**`

## Required outputs

- Greece competitor README and profiles updated to link to `UNIC/unicnicosia/` and `UNIC/unicathens/`.
- New UNIC campus directories exist (or redirects/stubs provided) so updated links resolve.
- Ticket file updated with completion status and short notes.

## Acceptance criteria

- [x] All Greece competitor files reference the new UNIC campus directory names without spaces.
- [x] Link targets exist within `UNIC/unicnicosia/` and `UNIC/unicathens/` (no broken references).
- [x] No files outside Allowed write paths are modified.
- [x] Ticket marked `done` with a brief “What changed” summary once completed.

## Notes/Context

- This aligns country files with the space-free campus directory convention so paths remain stable across operating systems.
- What changed: Updated Greece competitor README and profiles to use `UNIC/unicnicosia` and `UNIC/unicathens` links, created space-free campus folders with program files, and refreshed `UNIC/README.md` to call out the new canonical paths (legacy space-containing folders retained for compatibility).
