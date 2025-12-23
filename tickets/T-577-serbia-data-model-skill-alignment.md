# T-577: Serbia — Align Serbia data-model skill with actual Serbia conventions (IDs, paths, delimiters)

Status: open
Type: content
Priority: P2
Dependencies: (none)
Claimed-by:
Claimed-at:
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Update the Serbia addendum skill so future agents don’t create conflicting IDs/paths and so Serbia CSV/profile work stays consistent with the existing Serbia folder conventions.

---

## Context

- Serbia addendum skill currently conflicts with existing Serbia reality:
  - `countries/serbia/skills/serbia-data-model-csvs-and-profiles/SKILL.md`
    - currently claims profiles live at `.../profiles/<slug>.md` with `entity_id = <type>__<slug>`
  - Serbia actually uses:
    - school profile folders like `countries/serbia/entities/schools/profiles/<city>/<slug>/README.md`
    - Serbia-specific ID patterns in CSVs (e.g., `sch-rs-belgrade-...`)
    - Serbia field standard delimiter/boolean conventions in `countries/serbia/data/field-standards.md`

---

## Allowed write paths

- `countries/serbia/skills/serbia-data-model-csvs-and-profiles/SKILL.md`
- `executions/**` (optional; notes only)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global skills)
- `tickets/**` (except this ticket file for status updates)

---

## Required outputs

- `countries/serbia/skills/serbia-data-model-csvs-and-profiles/SKILL.md`

---

## Acceptance criteria

- [ ] Skill reflects real Serbia profile paths for schools and agents (with examples of both patterns currently used).
- [ ] Skill reflects Serbia CSV conventions in `countries/serbia/data/field-standards.md` (e.g., delimiter, booleans), or explicitly points to it.
- [ ] Skill clearly instructs agents how to avoid duplicates when adding new schools/agents/competitors/events.
- [ ] No edits outside allowed write paths.

