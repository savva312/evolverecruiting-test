# T-390: Refresh UNIC campus structure with recruiting subfolders

Status: done
Type: structure
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-21T19:03:49+00:00

---

## Goal

Reorganize the shared `UNIC/` directory so each campus (UNIC Nicosia and UNIC Athens) lives in its own lowercase, URL-friendly folder and includes subfolders for core recruiting topics (programs, visas, housing, scholarships/aid, student life/onboarding). Move existing campus program content into the new structure.

## Context

- Current campus folders use spaced names (`UNIC Nicosia`, `UNIC Athens`) with program files at the top of each folder.
- Recruiters need predictable subfolder names for visas, housing, scholarships, and onboarding logistics to keep campus materials organized for all countries.
- This is a scoped structure change under the shared `UNIC/` workspace (no country directories change).

## Allowed write paths

- `UNIC/**`
- `tickets/T-371-unic-campus-structure-refresh.md`
- `executions/T-371-unic-campus-structure-refresh/**` (optional notes)

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket)
- `.github/**`
- `scripts/**`
- Any other paths not listed in Allowed write paths

## Required outputs

- `UNIC/unicnicosia/` directory created with subfolders for `programs/`, `visas/`, `housing/`, `scholarships/`, and `student-life/` (or equivalent onboarding/logistics); existing UNIC Nicosia `programs.md` moved into `programs/`.
- `UNIC/unicathens/` directory created with the same subfolder set; existing UNIC Athens `programs.md` moved into `programs/`.
- `UNIC/README.md` updated to describe the new campus folder names and subfolder purposes.
- Redirect or link updates inside `UNIC/` so internal references point to the new paths.

## Acceptance criteria

- Campus content resides under `UNIC/unicnicosia/` and `UNIC/unicathens/` with program files in their `programs/` subfolders; the original spaced folders are removed.
- Each campus folder contains clearly labeled subfolders for programs, visas, housing, scholarships/aid, and student life/onboarding (with stub README or placeholder files as needed).
- `UNIC/README.md` links resolve to the new campus paths and explain the subfolder layout.
- No files outside Allowed write paths are modified.

## Execution notes (optional)

- What changed (short): Renamed the campus folders to `unicnicosia/` and `unicathens/`, relocated the program files into `programs/`, and added admissions, visas, housing, scholarships, and student-life subfolders with placeholder READMEs. Updated `UNIC/README.md` to reflect the new layout.
- Open questions: None.
- Follow-up tickets suggested: Update country-level references that still point to the old spaced campus paths (e.g., `countries/greece/entities/competitors/**`) so links resolve to the new folder names.
