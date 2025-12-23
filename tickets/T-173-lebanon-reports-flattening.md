# T-173: Flatten Lebanon report folder

Status: done
Type: structure
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-21T00:00:00Z
Last-updated: 2025-12-21
What changed: Flattened `countries/lebanon/reports/` by moving structured reports into the folder root, updating README and outbound mobility guidance, and removing the `structured/` subfolder.

---

## Goal

Remove the `reports/structured/` nesting in `countries/lebanon/` so reports live directly under `countries/lebanon/reports/`, and update in-country references to match the flattened layout.

---

## Context

Lebanon retains a `reports/structured/` subfolder pattern that was removed in other countries. Flattening the directory keeps report paths consistent and avoids broken references across market files.

---

## Allowed write paths

- `countries/lebanon/reports/**`
- `countries/lebanon/market/**`
- `tickets/T-147-lebanon-reports-flattening.md`
- `research/T-147-lebanon-reports-flattening/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file)
- `research/runs/**`
- `.github/**`
- `scripts/**`
- Any files outside the allowed paths above

---

## Required outputs

- Files currently under `countries/lebanon/reports/structured/` moved into `countries/lebanon/reports/` with filenames preserved.
- `countries/lebanon/reports/structured/` removed after migration (no lingering references).
- `countries/lebanon/reports/README.md` updated to describe the flat layout (no structured subsection).
- Any Lebanon files referencing `reports/structured/` updated to point to the new flat paths.
- Ticket status updated to `done` with a brief change note when complete.

---

## Acceptance criteria

- [x] No `countries/lebanon/reports/structured/` directory remains.
- [x] All reports previously under `structured/` reside directly in `countries/lebanon/reports/`.
- [x] README and in-country guidance reference the flat `reports/` path only.
- [x] No files outside the Allowed write paths are modified.
- [x] Ticket updated to `done` with change summary.

---

## Execution notes (optional)

- What changed (short):
- Any open questions:
- Follow-up tickets suggested:
