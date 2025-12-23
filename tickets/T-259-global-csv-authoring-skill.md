# T-259: Global CSV authoring skill

Status: done
Type: structure
Priority: P1
Dependencies: T-020, T-087
Claimed-by: work
Claimed-at: 2025-12-21T08:49:46Z
Last-updated: 2025-12-21

---

## Goal

Create a global skill that standardizes how agents prompt, generate, and validate CSV outputs (delimiter rules, quoting, enums, schema locks, and self-checks) so datasets stay clean and interoperable across countries.

## Context

- Global CSV discipline is required before we expand country datasets; the skill must prevent schema drift and invented values.
- Root control-plane rules require a **structure** ticket to modify `skills/**`.

## Allowed write paths

- `skills/csv-authoring/**`
- `skills/README.md`
- `tickets/T-226-global-csv-authoring-skill.md`
- `executions/**` (optional run notes)

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- Any country directories (e.g., `/countries/**`)
- Other tickets in `/tickets/**` (except status updates to this file)
- `.github/**`
- `scripts/**`

## Required outputs

- `skills/csv-authoring/SKILL.md` capturing purpose, prompting patterns, generation checklist, validation steps, pitfalls, and a reusable prompt snippet.
- `skills/README.md` updated to include the new global CSV skill in the index.
- This ticket updated to `Status: done` with a brief “What changed” note when complete.

## Acceptance criteria

- Skill is global-only (no country-specific paths or examples) and enforces delimiter, quoting, enum, and schema-lock discipline.
- Skill includes a ready-to-paste prompt block and a self-checklist for generation and validation.
- `skills/README.md` lists the new skill with a concise label.
- No files outside Allowed write paths are modified.
- Ticket status set to `done` with a short completion note.

## Execution notes (optional)

- What changed (short): Added global CSV authoring skill with prompt pattern, generation and validation checklists, and indexed it in `skills/README.md`.
- Follow-ups: None.
