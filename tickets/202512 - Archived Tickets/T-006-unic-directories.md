# T-006: Add UNIC campus directories and placeholders

Status: archived
Type: structure
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T14:49:05+00:00
Last-updated: 2025-12-20

---

## Goal

Create top-level `UNIC/` directory with campus-specific subfolders for UNIC Nicosia and UNIC Athens, including placeholder program files to scaffold future recruiting content.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` sections on repo map and structure-change policy
- External constraints: Creating a new top-level directory requires a structure ticket.
- Assumptions: Only stub markdown placeholders are needed for this change.

---

## Allowed write paths

- `UNIC/**`
- `tickets/T-004-unic-directories.md`
- `research/**` (optional; for notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `data/**`
- `entities/**`
- `market/**`
- `go-to-market/**`
- `program-clusters/**`

---

## Required outputs

- `UNIC/README.md`
- `UNIC/UNIC Nicosia/programs.md`
- `UNIC/UNIC Athens/programs.md`

---

## Acceptance criteria

- [x] `UNIC/` directory exists at repo root with subdirectories for `UNIC Nicosia` and `UNIC Athens`.
- [x] Each campus subdirectory contains a `programs.md` placeholder with a short heading describing intended content.
- [x] `UNIC/README.md` summarizes the folder purpose and links to both campus placeholders.
- [x] No files outside `Allowed write paths` are modified.
- [x] Ticket status updated to `done` with a brief summary once work completes.

---

## Execution notes (optional)

- What changed (short): Created `UNIC/` with campus subfolders for UNIC Nicosia and UNIC Athens, added placeholder `programs.md` files, and documented the folder in `UNIC/README.md`.
- Any open questions:
- Follow-up tickets suggested:
