# T-108: Lebanon recognition and licensure alignment

Status: done
Type: structure
Priority: P2
Dependencies: T-020, T-026
Claimed-by: work
Claimed-at: 2025-03-18T00:00:00Z
Last-updated: 2025-03-18

---

## Goal

Add Lebanon recognition-and-licensure skill aligned to the global procedure, preserving compliance guardrails, dataset schema, and country authority examples.

---

## Context

- Global recognition-and-licensure skill exists; Lebanon is not yet covered.
- Need a country addendum that defers to the global workflow while listing Lebanon authorities and documentation nuances.

---

## Allowed write paths

- `tickets/T-088-lebanon-recognition-and-licensure-alignment.md`
- `skills/**`
- `lebanon/skills/lebanon-recognition-and-licensure/**`
- `research/**` (optional execution notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- Other tickets (except status updates to this file)
- `.github/**`
- `scripts/**`
- Country directories other than `lebanon/skills/lebanon-recognition-and-licensure/**`

---

## Required outputs

- `/lebanon/skills/lebanon-recognition-and-licensure/SKILL.md` referencing the global skill, with Lebanon country notes, authority examples, and compliance cautions.
- Ticket updated to `Status: done` with brief change summary.

---

## Acceptance criteria

- Lebanon skill links to the global recognition-and-licensure skill for workflow, quality bar, and dataset schema.
- Country addendum lists Lebanon authorities and regulated-profession examples without inventing timelines or requirements.
- Changes stay within allowed paths; no control-plane files touched.
- Ticket file reflects completion with status update and short notes.

---

## Execution notes (optional)

- What changed (short): Created Lebanon recognition-and-licensure skill aligned to the global workflow with country addendum, compliance cautions, and authority examples.
- Open questions: None.
