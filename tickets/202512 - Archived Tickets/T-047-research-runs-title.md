# T-047: Rename research/runs title to "/agent runs/"

Status: archived
Type: content
Priority: P3
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T17:55:04+00:00
Last-updated: 2025-12-20

---

## Goal

Retitle the research run workspace to emphasize agent runs by updating the visible heading in the root `research/runs` documentation.

---

## Context

- Request to change the current "EvoBuilder Runs (Archive)" title to "/agent runs/".
- `research/runs` remains the global location for run artifacts; the rename should not alter structure or placement.
- No structural moves; this is a wording update only.

---

## Allowed write paths

- `research/runs/README.md`
- `research/runs/index.md`
- `tickets/T-032-research-runs-title.md`
- `tickets/index.md` (for ticket list updates)
- `research/**` (optional run notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file and `tickets/index.md`)
- `.github/**`
- `scripts/**`
- Any path not explicitly listed under Allowed write paths

---

## Required outputs

- `research/runs/README.md` updated so the main title reads "/agent runs/" (or equivalent clear phrasing).
- `research/runs/index.md` adjusted if needed to align with the updated title.
- `tickets/T-032-research-runs-title.md` updated upon completion.
- `tickets/index.md` lists this ticket in the appropriate section.

---

## Acceptance criteria

- [x] `research/runs/README.md` main heading reads "/agent runs/".
- [x] Related references in `research/runs/index.md` (if any) reflect the updated title.
- [x] No files outside Allowed write paths are modified.
- [x] Directory structure for `research/runs/**` remains unchanged.

---

## Execution notes (optional)

- What changed (short): Updated `research/runs/README.md` heading to `/agent runs/` and aligned the index title without touching structure.
- Any open questions: None.
- Follow-up tickets suggested: None.
