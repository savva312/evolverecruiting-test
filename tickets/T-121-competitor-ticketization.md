# T-121: Country competitor documentation tickets

Status: done
Type: structure
Priority: P1
Dependencies: T-017
Claimed-by: work
Claimed-at: 2025-12-20T20:29:31Z
Last-updated: 2025-12-20

---

## Goal

Create dedicated tickets for competitor research and documentation in each active country so work can proceed in parallel within the existing `entities/competitors` sections.

---

## Context

- The country-first layout places competitor content under `countries/<country>/entities/competitors/`.
- Per `AGENTS.md`, work must be ticketed with explicit scopes to avoid collisions across countries.
- This scaffolding ticket ensures Bulgaria, Nigeria, Greece, Jordan, Lebanon, Romania, and Serbia each have a scoped competitor documentation ticket.

---

## Allowed write paths

- `tickets/**` (for creating the new competitor tickets and status updates)
- `tickets/index.md`
- `research/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- Country directories outside `tickets/**`
- `.github/**`
- `scripts/**`

---

## Required outputs

- New competitor documentation tickets for:
  - Bulgaria
  - Nigeria
  - Greece
  - Jordan
  - Lebanon
  - Romania
  - Serbia
- `tickets/index.md` updated to list the new tickets.

---

## Acceptance criteria

- [x] All new country competitor tickets exist with clear allowed/forbidden paths scoped to the relevant `countries/<country>/entities/competitors/**` directory.
- [x] Each new ticket includes dependencies, priorities, and required outputs aligned to competitor research.
- [x] No files outside `tickets/**` (and optional `research/**`) are modified.
- [x] `tickets/index.md` lists the new tickets in the Open section.

---

## Execution notes (optional)

- What changed (short): Added competitor documentation tickets for Bulgaria, Nigeria, Greece, Jordan, Lebanon, Romania, and Serbia and listed them in the ticket index.
- Any open questions: None.
- Follow-up tickets suggested: Execute new country-specific competitor tickets; consider adding guidance under country skills once patterns emerge.
