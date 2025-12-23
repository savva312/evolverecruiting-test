# T-024: Greece migration to country-first layout

Status: archived
Type: structure
Priority: P1
Dependencies: T-017, T-018
Claimed-by:
Claimed-at:
Last-updated: 2025-12-20

---

## Goal

Create the `/greece/` subtree, move any Greece-specific content into it (including reports), and place Greece-specific skills under `/greece/skills/**` while keeping global skills unchanged.

---

## Context

- Relies on T-017 control-plane updates and T-018 ticket scaffolding.
- Scoped to Greece to avoid collisions with Bulgaria and Nigeria migrations.
- Establishes structure even if Greece content is not yet present.

---

## Allowed write paths

- `greece/**` (including `reports/`)
- `greece/skills/**` (Greece-specific skills only)
- `tickets/T-022-greece-migration.md`
- `research/T-022-greece-migration/**` (optional run notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- Global skills (`skills/**`)
- Other country directories (e.g., `/bulgaria/**`, `/nigeria/**`)
- Other tickets except status updates to this file

---

## Required outputs

- `/greece/` directory established; Greece content (if present) relocated under it
- `/greece/reports/` created for Greece reports; old report paths retired
- `/greece/skills/` contains Greece-specific procedures; global `/skills` remains general
- Updated internal Greece-scope links to the new paths
- `tickets/T-022-greece-migration.md` updated upon completion

---

## Acceptance criteria

- [x] Greece content (if any) exists only under `greece/**`
- [x] Greece reports live under `greece/reports`; `research/runs` untouched
- [x] Greece-specific skills reside in `greece/skills/**`; global skills remain country-agnostic
- [x] Internal Greece-scope links resolve to new paths
- [x] No files outside Allowed write paths are modified

---

## Execution notes (optional)

- What changed (short): Created the `greece/` tree with a top-level README and `reports/` home, added Greece-specific skills area with placement procedure skill, and left a README to govern future Greece-only skills. No pre-existing Greece content was found to relocate.
- Any open questions: None.
- Follow-up tickets suggested: Add Greece content once available (market intel, entities, reports) under the new structure.
