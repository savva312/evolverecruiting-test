# T-021: Bulgaria migration to country-first layout

Status: archived
Type: structure
Priority: P0
Dependencies: T-017, T-018
Claimed-by: assistant-dec20-fix
Claimed-at: 2025-12-20T17:14:49Z
Last-updated: 2025-12-20
What changed: Moved stray Sofia and Plovdiv school profile folders into the correct city directories under `bulgaria/entities/schools/profiles/` and refreshed the affected files.

---

## Goal

Move all Bulgaria content into `/bulgaria/**`, relocate Bulgaria reports to `/bulgaria/reports`, and split Bulgaria-specific skills into `/bulgaria/skills/**` while keeping shared skills global.

---

## Context

- Implements the multi-country layout defined in T-017.
- Current Bulgaria materials live at the repo root (e.g., `market/`, `entities/`, `go-to-market/`, `program-clusters/`, `UNIC/`, `data/`).
- `research/reports` should be replaced by `/bulgaria/reports` for Bulgaria artifacts.

---

## Allowed write paths

- `bulgaria/**` (new country subtree, including `reports/`)
- `bulgaria/skills/**` (Bulgaria-specific skills only)
- `market/**`
- `entities/**`
- `go-to-market/**`
- `program-clusters/**`
- `UNIC/**`
- `data/**`
- `research/reports/**` (only to move/remove Bulgaria reports)
- `tickets/T-019-bulgaria-migration.md`
- `research/T-019-bulgaria-migration/**` (optional run notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global skills outside Bulgaria scope)
- Any other country directories (e.g., `/nigeria/**`, `/greece/**`)
- Other tickets except status updates to this file

---

## Required outputs

- `bulgaria/` populated with Bulgaria content previously at root (market, entities, go-to-market, program-clusters, UNIC, data as applicable)
- `bulgaria/reports/` containing Bulgaria reports formerly under `research/reports`
- `bulgaria/skills/` containing Bulgaria-specific procedures; global skills left in `/skills`
- Updated internal links within Bulgaria scope to new paths
- `tickets/T-019-bulgaria-migration.md` updated upon completion

---

## Acceptance criteria

- [x] All Bulgaria content resides under `bulgaria/**`
- [x] Bulgaria reports live under `bulgaria/reports`; `research/runs` remains untouched
- [x] Global vs country-specific skills are separated; no Bulgaria-specific skills remain in global `/skills`
- [x] Internal links within the Bulgaria scope resolve to the new paths
- [x] No files outside Allowed write paths are modified

---

## Execution notes (optional)

- What changed (short): Moved all Bulgaria directories (market, entities, go-to-market, program-clusters, UNIC, data) into `bulgaria/`, relocated Bulgaria reports to `bulgaria/reports/` with a redirect note in `research/reports/`, and consolidated Bulgaria-only skills under `bulgaria/skills/` with an index.
- Any open questions: None.
- Follow-up tickets suggested: Consider a cross-link cleanup pass to update any future references outside Bulgaria scope once other countries are added.
