# T-110: Add Lebanon data-model skill addendum

Status: done
Type: structure
Priority: P2
Dependencies: T-087, T-088
Claimed-by: work
Claimed-at: 2025-12-20T20:00:00Z
Last-updated: 2025-12-20

---

## Goal

Create a Lebanon data-model Skill addendum that points to the global data-model Skill and documents Lebanon-specific path conventions for CSVs, dictionaries, and profiles. Add a Lebanon skills README referencing the global Skill.

---

## Allowed write paths

- `lebanon/**`
- `tickets/T-089-lebanon-data-model-addendum.md`
- `research/**`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `.github/**`
- `scripts/**`
- Other tickets
- Other country directories

---

## Required outputs

- `lebanon/skills/lebanon-data-model-csvs-and-profiles/SKILL.md`
- `lebanon/skills/README.md`
- Ticket updated to `Status: done` with execution notes.

---

## Acceptance criteria

- Lebanon data-model Skill defers to the global Skill and only documents local path conventions and ID/profile alignment.
- Lebanon skills README links to the global data-model Skill.
- No files outside Allowed write paths are modified.
- Ticket marked done with execution notes on completion.

---

## Execution notes (optional)

- What changed (short): Added Lebanon skills folder, created a Lebanon data-model addendum pointing to the global Skill, added a Lebanon skills README referencing the global standard, and kept guidance scoped to local paths/IDs.
- Any open questions: None.
- Follow-up tickets suggested: None.
