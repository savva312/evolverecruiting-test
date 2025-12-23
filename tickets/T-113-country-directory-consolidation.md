# T-113: Consolidate country directories under `countries/`

Status: done
Type: structure
Priority: P0
Dependencies: (none)
Claimed-by: assistant
Claimed-at: 2025-12-20T20:02:30Z
Last-updated: 2025-12-20
Last-updated: 2025-12-20

---

## Goal

Relocate all existing country directories into a unified `countries/` folder (e.g., `/countries/bulgaria`, `/countries/greece`, `/countries/nigeria`) and update control-plane guidance to reflect the new layout.

---

## Context

- Current layout keeps country folders at the repo root; the target state nests them under `countries/` while keeping shared assets (e.g., `UNIC/`, `skills/`, `tickets/`) at root.
- The move must preserve all country content and update navigation references in control-plane docs.
- This is a structure change (top-level directory moves) and requires explicit scope and control-plane updates.

---

## Allowed write paths

- `tickets/T-091-country-directory-consolidation.md`
- `tickets/index.md`
- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `bulgaria/**`
- `greece/**`
- `nigeria/**`
- `lebanon/**`
- `jordan/**`
- `romania/**`
- `serbia/**`
- `countries/**`

---

## Forbidden write paths

- `.github/**`
- `skills/**`
- `tickets/**` (except this ticket and `tickets/index.md`)
- `scripts/**`
- `UNIC/**`
- `agent runs/**`
- Any other paths not explicitly listed in Allowed write paths

---

## Required outputs

- `countries/` directory exists containing the prior country folders (`bulgaria`, `greece`, `nigeria`, `lebanon`, `jordan`, `romania`, `serbia`).
- No country directories remain at repo root; their contents are preserved in `countries/<country>/`.
- Control-plane docs (`README.md`, `AGENTS.md`, `ROADMAP.md`) reflect the new country directory layout.
- `tickets/T-091-country-directory-consolidation.md` updated with status notes upon completion.

---

## Execution notes (optional)

- What changed (short): Relocated all country directories into `/countries/` and updated control-plane docs to reflect the nested layout.
- Any open questions: None.
- Follow-up tickets suggested: If any downstream references point to old root-level paths, schedule a small cleanup ticket to update them.

---

## Acceptance criteria

- [x] All country directories reside under `countries/` with content intact; root no longer contains standalone country folders.
- [x] Control-plane docs describe the `countries/<country>/` layout and updated navigation paths.
- [x] No files modified outside Allowed write paths.
- [x] Internal references updated to avoid broken navigation to moved directories (control-plane at minimum).
- [x] Git history shows the moves (e.g., via `git mv`) to preserve history.

---

## Execution notes (optional)

- What changed (short):
- Any open questions:
- Follow-up tickets suggested:
