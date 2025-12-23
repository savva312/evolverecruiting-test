# T-400: Add Infrastructure root directory for campus facilities scaffolding

Status: done
Type: structure
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-21T22:15:40+00:00
Last-updated: 2025-12-21

---

## Goal

Create a top-level `Infrastructure/` directory to house campus facility documentation. Add campus-specific subfolders for `UNIC Nicosia`, `UNIC Athens`, and `UNIC Evolve`, and scaffold facility subfolders for UNIC Nicosia per the requested list (e.g., Main Building, Fine Arts Building, Architecture Building, Medical Block 1-3, Unifit, RTB, Europa Building, Humanities Building, Millennium Building, Library, KESY).

---

## Context

- Request: establish a dedicated `Infrastructure/` root with campus folders and detailed UNIC Nicosia facility subfolders.
- Current state: no `Infrastructure/` directory exists; creating a new top-level folder requires a structure ticket per `AGENTS.md` and `ROADMAP.md` change policy.
- Scope alignment: change is shared/global (not country-specific) and should not touch existing `UNIC/` academic program content.

---

## Allowed write paths

- `Infrastructure/**`
- `tickets/T-403-infrastructure-directory.md`
- `executions/T-403-infrastructure-directory/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- Any other paths not listed in Allowed write paths

---

## Required outputs

- `Infrastructure/` top-level directory created.
- `Infrastructure/UNIC Nicosia/` directory with subdirectories:
  - `Main Building/`
  - `Fine Arts Building/`
  - `Architecture Building/`
  - `Medical Block 1/`
  - `Medical Block 2/`
  - `Medical Block 3/`
  - `Unifit/`
  - `RTB (Research and Technology Building)/`
  - `Europa Building/`
  - `Humanities Building/`
  - `Millenium Building/`
  - `Library/`
  - `KESY/`
- `Infrastructure/UNIC Athens/` directory created.
- `Infrastructure/UNIC Evolve/` directory created.
- (Optional) Stub `README.md` files in new directories if needed for navigation.

---

## Acceptance criteria

- [x] `Infrastructure/` exists at the repo root with campus folders `UNIC Nicosia/`, `UNIC Athens/`, and `UNIC Evolve/`.
- [x] All listed UNIC Nicosia facility subdirectories exist and use the exact names specified above.
- [x] No files outside `Allowed write paths` are modified.
- [x] If any placeholder README files are added, they clearly state purpose and contain no speculative content.

---

## Execution notes (optional)

- What changed (short): Added root `Infrastructure/` directory with campus folders for UNIC Nicosia, UNIC Athens, and UNIC Evolve; scaffolded UNIC Nicosia facility subdirectories with placeholder READMEs.
- Any open questions: None.
- Follow-up tickets suggested: Populate facility documentation and add Athens/Evolve facility details when available.
