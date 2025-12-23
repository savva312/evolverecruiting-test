# T-546: Romania — school profile placeholder cleanup + navigation hardening

Status: open
Type: qa
Priority: P2
Dependencies: T-308
Claimed-by:
Claimed-at:
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Reduce operational confusion in `countries/romania/entities/schools/profiles/**` by:
- identifying non-standard/legacy placeholder folders (e.g., `bucharest-american-international-school/`, `bucharest-national-college-of-math-and-science/`, city folders that suggest “one file per school”)
- ensuring each placeholder clearly points to the **canonical** `sch-ro-*` profile where it exists
- updating `countries/romania/entities/schools/profiles/README.md` to document the correct current pattern and mark legacy paths as deprecated

This ticket should avoid destructive deletes unless strictly necessary; prefer “DEPRECATED → canonical link” guidance.

---

## Context

Romania has strong canonical school profiles under `countries/romania/entities/schools/profiles/sch-ro-*/README.md`, but there are legacy folders that look like alternate profile locations.

---

## Allowed write paths

- `tickets/T-460-romania-school-profiles-cleanup-navigation.md`
- `countries/romania/entities/schools/profiles/**`
- `countries/romania/entities/schools/README.md` (optional: if adding a short “canonical path” note)
- `executions/**` (optional for notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`
- `tickets/**` (except this ticket file)
- `countries/**` (except `countries/romania/entities/schools/**`)

---

## Required outputs

- Updated `countries/romania/entities/schools/profiles/README.md` with:
  - canonical pattern
  - deprecated/legacy pattern(s)
  - “how to add a new school profile” guidance (short)
- For each legacy placeholder profile folder that overlaps a canonical profile:
  - Add a short `README.md` note marking it deprecated and linking to the canonical profile

---

## Acceptance criteria

- [ ] No duplicate “active” profiles remain for the same school without an explicit canonical pointer.
- [ ] A new contributor can find the correct place to add a school profile in <60 seconds by reading `countries/romania/entities/schools/profiles/README.md`.
- [ ] No edits outside allowed paths.

