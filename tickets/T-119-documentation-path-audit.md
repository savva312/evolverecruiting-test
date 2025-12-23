# T-119: Documentation path audit after country folder relocation

Status: done
Type: structure
Priority: P0
Dependencies: T-091
Claimed-by: work
Claimed-at: 2025-02-03T00:00:00Z
Last-updated: 2025-02-03

---

## Goal

Find and fix any documentation or help references that still point to pre-migration paths (e.g., `/bulgaria/**` at repo root). Ensure all navigation, how-to guides, and readme files consistently reference `countries/<country>/`.

---

## Allowed write paths

- `tickets/T-096-documentation-path-audit.md`
- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `UNIC/**`
- `agent runs/**`
- `reports/**`
- `countries/**`
- `docs/**`
- `QA/**`

---

## Forbidden write paths

- `.github/**`
- `scripts/**`
- `skills/**/*.pdf`
- `assets/**`
- `data/**`
- `tickets/**` (except this ticket)
- `research/runs/**`

---

## Required outputs

- All documentation/help text references updated to use `countries/<country>/` paths.
- Any outdated navigation examples corrected (including control-plane readmes).
- `tickets/T-096-documentation-path-audit.md` updated with completion notes.

---

## Acceptance criteria

- [x] No references remain to old root-level country directories or deprecated report paths.
- [x] README/AGENTS/ROADMAP and other guide files point to `countries/<country>/...` locations.
- [x] Ticket file updated to `Status: done` with a short summary of edits when complete.
- [x] No files outside Allowed write paths are modified.

---

## Execution notes (optional)

- What changed (short): Updated control-plane docs, global skills, and country readmes/skills to use `countries/<country>/` paths; corrected partner/agent path guidance and shared UNIC location references; refreshed Bulgaria redirect notes and report links to the new country-first layout.
- Any open questions: None.
- Follow-up tickets suggested: None.
