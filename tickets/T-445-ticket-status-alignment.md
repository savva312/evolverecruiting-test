# T-445: Ticket status terminology alignment

Status: done
Type: structure
Priority: P1
Agent: EvoTicket Resolver
Claimed-by: work
Claimed-at: 2025-12-22T17:13:54+00:00
Last-updated: 2025-12-22
Completed-at: 2025-12-22T17:18:11+00:00

---

## Goal

Ensure every place that documents the ticket lifecycle uses the canonical status list (`open`, `on-deck`, `in-progress`, `blocked`, `done`, `dropped`, `archived`), with consistent lower-case spelling and matching meanings.

---

## Allowed write paths

- `AGENTS.md`
- `ROADMAP.md`
- `README.md`
- `tickets/**`
- `skills/**`
- `executions/**` (optional run notes)

---

## Forbidden write paths

- `countries/**`
- `UNIC/**`
- `reports/**`
- `scripts/**`
- `.github/**`
- `data/**`
- `Infrastructure/**`

---

## Required outputs

- Updated control-plane docs to reflect the canonical ticket status list with consistent lower-case spelling and aligned meanings.
- Ticket template and ticket folder documentation refreshed to match the canonical status definitions.
- Any other repo documentation mentioning ticket statuses aligned to the canonical list and spelling.

---

## Acceptance criteria

- [x] All documentation files that describe ticket statuses list the canonical statuses with lower-case spelling and matching meanings.
- [x] Ticket template and ticket README show the corrected statuses and definitions.
- [x] No edits occur outside Allowed write paths.
- [x] Ticket status set to `done` with a short summary once work is complete.

---

## Notes/Context

- Canonical statuses and meanings are defined in `AGENTS.md` and should be treated as the source of truth.
- Alignment complete across AGENTS, ROADMAP, README, ticket docs/index, project manager guidance, and the archiving skill.
