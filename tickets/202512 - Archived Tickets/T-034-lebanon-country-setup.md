# T-034 — Lebanon country setup

- **Status:** archived
- **Claimed-by:** work
- **Claimed-at:** 2025-12-20T17:00:47+00:00
- **Type:** structure
- **Priority:** P1

## Scope

- **Allowed write paths:**
  - `tickets/T-028-lebanon-country-setup.md`
  - `lebanon/**`
  - `ROADMAP.md`
- **Forbidden write paths:**
  - `README.md`
  - `AGENTS.md`
  - `skills/**`
  - `tickets/README.md`
  - `bulgaria/**`
  - `greece/**`
  - `nigeria/**`
  - `UNIC/**`

## Required outputs

- New top-level `lebanon/` directory mirroring the current Bulgaria subtree structure (program clusters, market, entities, go-to-market, skills, data, reports).
- Within `lebanon/`, content adjusted to Lebanon context (e.g., major cities, local framing) rather than Bulgarian references.
- `ROADMAP.md` updated to reflect Lebanon as a supported country in the repo map.

## Acceptance criteria

- `lebanon/` exists at the repository root and includes subdirectories/files corresponding to the Bulgaria layout without references to Bulgaria that would mislead a reader.
- Text inside Lebanon files refers to Lebanese context (e.g., Beirut/Tripoli/Saida for large cities) and does not retain Bulgarian city or country mentions except where contrast is explicitly stated for Lebanon.
- `ROADMAP.md` lists Lebanon in the country-first layout description.
- No changes occur outside the allowed write paths.

## Dependencies

- None.

## Notes/Context

- This is a structure ticket to onboard Lebanon as a new country namespace by templating existing Bulgaria materials. Adjust placeholders to Lebanese context; do not duplicate Bulgaria-specific claims without localization.

## What changed
- Added a Lebanon top-level directory mirroring the Bulgaria structure with localized content, data dictionaries, and playbooks.
- Renamed and rewrote skills, entities, program clusters, go-to-market materials, and reports to reflect Lebanese context (cities, agents, schools, visa/affordability notes).
- Updated `ROADMAP.md` to list Lebanon in the country-first layout.
