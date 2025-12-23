# T-023: Nigeria migration to country-first layout

Status: archived
Type: structure
Priority: P1
Dependencies: T-017, T-018
Claimed-by:
Claimed-at:
Last-updated: 2025-12-20

---

## Goal

Create the `/nigeria/` subtree, move any Nigeria-specific content into it (including reports), and place Nigeria-specific skills under `/nigeria/skills/**` while keeping global skills unchanged.

---

## Context

- Follows the control-plane changes from T-017 and scaffolding from T-018.
- Designed to be non-overlapping with Bulgaria and Greece migrations.
- Even if Nigeria content does not yet exist, this ticket establishes the structure and move rules.

---

## Allowed write paths

- `nigeria/**` (including `reports/`)
- `nigeria/skills/**` (Nigeria-specific skills only)
- `tickets/T-021-nigeria-migration.md`
- `research/T-021-nigeria-migration/**` (optional run notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- Global skills (`skills/**`)
- Other country directories (e.g., `/bulgaria/**`, `/greece/**`)
- Other tickets except status updates to this file

---

## Required outputs

- `/nigeria/` directory established; Nigeria content (if present) relocated under it
- `/nigeria/reports/` created for Nigeria reports; old report paths retired
- `/nigeria/skills/` contains Nigeria-specific procedures; global `/skills` remains general
- Updated internal Nigeria-scope links to the new paths
- `tickets/T-021-nigeria-migration.md` updated upon completion

---

## Acceptance criteria

- [x] Nigeria content (if any) exists only under `nigeria/**`
- [x] Nigeria reports live under `nigeria/reports`; `research/runs` untouched
- [x] Nigeria-specific skills reside in `nigeria/skills/**`; global skills remain country-agnostic
- [x] Internal Nigeria-scope links resolve to new paths
- [x] No files outside Allowed write paths are modified

---

## Execution notes (optional)

- What changed (short): Created `nigeria/` country subtree with `reports/` placeholder guidance, added Nigeria-only skill scaffolding under `nigeria/skills/`, and ensured acceptance criteria are satisfied.
- Any open questions: None.
- Follow-up tickets suggested: Add Nigeria-specific content and reports as they are developed using the new structure.
