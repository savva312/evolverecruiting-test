# T-048: Centralize UNIC program datasets

Status: archived
Type: structure
Priority: P1
Dependencies: T-025
Claimed-by: main
Claimed-at: 2025-12-20T17:49:57Z
Last-updated: 2025-12-20
What changed: Centralized the UNIC program CSV + dictionary under `UNIC/data/programs/`, removed country-level copies, and updated country data READMEs to point to the shared dataset.

---

## Goal

Remove UNIC-specific program datasets from country `data/programs` folders and host a single shared copy under the root `UNIC/` workspace so countries reference the same CSV + dictionary for campus programs.

## Context

Country data directories currently include placeholder `unic-programs.csv` files and dictionaries. These should live with other campus materials at the root `UNIC/` level to avoid duplication and keep cross-country updates consistent.

## Allowed write paths

- `tickets/T-032-unic-program-data-centralization.md`
- `tickets/index.md`
- `UNIC/**`
- `bulgaria/data/programs/**`
- `romania/data/programs/**`
- `jordan/data/programs/**`
- `serbia/data/programs/**`
- `greece/data/**`
- `research/T-032-unic-program-data-centralization/**` (optional notes)

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket and `tickets/index.md`)
- `.github/**`
- `scripts/**`
- Any other directories not explicitly allowed above

## Required outputs

- `UNIC/data/programs/unic-programs.csv` and `unic-programs-dictionary.md` created as the shared UNIC dataset location (with a short README if helpful).
- Country-level `data/programs` folders no longer contain `unic-programs.csv` or its dictionary; any references point to the root `UNIC/` path instead.
- Country data README files direct users to the centralized UNIC program dataset.
- Ticket updated to reflect completion status and summary.

## Acceptance criteria

- Single authoritative UNIC program CSV + dictionary lives under `UNIC/data/programs/`.
- No `unic-programs.csv` or `unic-programs-dictionary.md` remain under `bulgaria/`, `romania/`, `jordan/`, or `serbia` data folders; any future additions in `greece/data` point to the shared location.
- Data READMEs in affected countries mention the centralized UNIC dataset path.
- All edits stay within Allowed write paths.

## Execution notes (optional)

- Shared UNIC program data lives at `UNIC/data/programs/unic-programs.csv` with `unic-programs-dictionary.md`; countries now reference this instead of local copies.
- Nigeria currently has no `data/` directory, so no UNIC program CSV or dictionary existed to migrate there.
