# T-107: Recognition and licensure skill standardization

Status: done
Type: structure
Priority: P1
Dependencies: T-020, T-026, T-022, T-019
Claimed-by: work
Claimed-at: 2025-03-17T00:00:00Z
Last-updated: 2025-03-17

---

## Goal

Create a global recognition-and-licensure skill and align Greece and Bulgaria recognition/licensure skills to reference the global standard while preserving country-specific regulators and pathways.

---

## Context

- The repo now uses a country-first layout with global skills separated from country-specific procedures.
- Bulgaria and Greece recognition/licensure skills currently hold country detail; we need a neutral global procedure plus country addenda that link back to it.
- Work must retain authority-profile outputs, compliance cautions, and the existing dataset schema.

---

## Allowed write paths

- `tickets/T-087-recognition-licensure-global-standardization.md`
- `skills/**`
- `bulgaria/skills/bulgaria-recognition-and-licensure/**`
- `greece/skills/greece-recognition-and-licensure/**`
- `research/**` (optional execution notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/git-pr-hygiene/**` (leave as reference only)
- `tickets/**` except this ticket file
- `.github/**`
- `scripts/**`
- Country directories outside the allowed scope above

---

## Required outputs

- `/skills/recognition-and-licensure/SKILL.md` with neutral, global guidance incorporating authority-profile outputs, compliance cautions, and dataset schema.
- Updated `/greece/skills/greece-recognition-and-licensure/SKILL.md` referencing the global procedure and adding Greece-specific regulators/paths as country notes.
- Updated `/bulgaria/skills/bulgaria-recognition-and-licensure/SKILL.md` referencing the global standard plus a Bulgaria-specific addendum retaining authorities/examples.
- Ticket updated to `Status: done` with brief change summary.

---

## Acceptance criteria

- Global skill exists under `/skills/recognition-and-licensure/SKILL.md` with neutral language, preserved authority-profile outputs, compliance cautions, and dataset schema.
- Greece and Bulgaria recognition/licensure skills defer to the global standard for process/structure and only add country-specific regulators, pathways, and examples.
- No forbidden paths are modified; changes stay within the allowed directories.
- Ticket file reflects completion with status update and short what-changed note.

---

## Execution notes (optional)

- What changed (short): Added global recognition-and-licensure skill, updated Greece and Bulgaria skills to reference it while keeping country-specific addenda, and aligned Nigeria, Serbia, Jordan, and Romania recognition skills to the global workflow with local authority examples.
- Open questions: None.
