# T-022: Global skills split

Status: archived
Type: structure
Priority: P0
Dependencies: T-017, T-018
Claimed-by: work
Claimed-at: 2025-12-20T16:03:34Z
Last-updated: 2025-12-20

---

## Goal

Separate global, cross-country skills from country-specific procedures by keeping only general guidance in `/skills/**` and preparing to relocate country-specific items to `/skills/<country>/**`.

---

## Context

- Relies on the multi-country policies from T-017.
- Country-specific moves will occur in country tickets; this ticket ensures the global skills set is clearly scoped.
- Prevents overlap by avoiding edits to country directories.

---

## Allowed write paths

- `skills/**` (global/general skills only; do not place country-specific content here)
- `tickets/T-020-global-skills-split.md`
- `research/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- Any country directories (e.g., `/bulgaria/**`, `/nigeria/**`, `/greece/**`)
- Country skill folders (e.g., `/bulgaria/skills/**`, `/nigeria/skills/**`, `/greece/skills/**`)
- Other tickets except status updates to this file

---

## Required outputs

- `/skills/` contains only global, cross-country procedures
- Country-specific skill items identified and noted for relocation to country tickets
- `tickets/T-020-global-skills-split.md` updated upon completion

---

## Acceptance criteria

- [x] Global skills remain in `/skills/**`; no country-specific guidance left there
- [x] Country-specific items are cataloged for handoff to respective country tickets (without moving them here)
- [x] No files outside Allowed write paths are modified

---

## Execution notes (optional)

- What changed (short): Removed Bulgaria-specific skills from `/skills/`, staged them under `research/work/tickets/T-020/staged-country-skills/bulgaria/` (later relocated to `/bulgaria/skills/`), updated `skills/README.md`, and cataloged relocation targets in `research/work/tickets/T-020/notes.md`.
- Any open questions: None.
- Follow-up tickets suggested: When country skill namespaces are introduced (per T-017/T-018), move each staged Bulgaria skill folder into `/bulgaria/skills/`.
