# T-112: Lebanon skills alignment with global standards

Status: done
Type: qa
Priority: P1
Dependencies: T-020, T-026, T-088, T-089
Claimed-by: work
Claimed-at: 2025-12-20T19:45:14Z

---

## Goal

Audit and realign all Lebanon-specific skills so they defer to the corresponding global skills (structure, links, and guardrails) in the same way other countries do. Fix any drift, missing references, or inconsistent formatting.

---

## Allowed write paths

- `tickets/T-090-lebanon-skills-alignment.md`
- `lebanon/skills/**`
- `research/**` (optional execution notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `.github/**`
- `scripts/**`
- Country directories other than `lebanon/**`
- Other tickets

---

## Required outputs

- Lebanon skill files updated to reference the appropriate global skills with matching headers, link patterns, and guardrails.
- Any country-specific notes preserved but clearly scoped beneath the global workflow links.
- Ticket updated to `Status: done` with brief execution notes.

---

## Acceptance criteria

- Each Lebanon skill that has a global counterpart explicitly links to the global skill and mirrors its section order (purpose, when to use, workflow/steps, quality bar, deliverables/templates).
- Country notes stay Lebanon-specific, avoid speculative claims, and do not contradict global guidance.
- No changes occur outside the Allowed write paths.
- Ticket file records completion status and a concise summary of adjustments.

---

## Execution notes (optional)

- What changed (short): Reworked Lebanon skills as addenda to the relevant global skills (agents/partners, data model, paid media, program clusters/competitors, schools/counselor mapping, recognition/licensure, UNIC portfolio) and refreshed the education-system description for Lebanon terminology.
- Open questions: None.
