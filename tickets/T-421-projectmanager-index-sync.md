# T-421: EvoManager ticket index synchronization guidance

Status: done
Type: structure
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-22T16:43:32Z
Last-updated: 2025-12-22
Completed-at: 2025-12-22T16:45:20Z
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Make the EvoManager control file (`tickets/projectmanager.md`) explicitly require syncing `tickets/index.md` whenever EvoManager creates new tickets, reclassifies tickets to `on-deck`, or closes/otherwise changes ticket statuses, so the index reflects its actions.

---

## Context

- Relevant governance files: `AGENTS.md`, `ROADMAP.md`, `tickets/README.md`
- Control file to update: `tickets/projectmanager.md`
- Index that must stay in sync: `tickets/index.md`
- Repo expectation: ticket-driven execution with clear scopes and up-to-date indices for reviewers.

---

## Allowed write paths

- `tickets/T-421-projectmanager-index-sync.md`
- `tickets/projectmanager.md`
- `tickets/index.md`
- `executions/T-421-projectmanager-index-sync/**`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/README.md`
- `.github/**`
- `scripts/**`
- `countries/**`
- `UNIC/**`
- `reports/**`
- `Infrastructure/**`

---

## Required outputs

- `tickets/projectmanager.md` updated with explicit instructions for EvoManager to sync `tickets/index.md` after creating/reclassifying/closing tickets (including `on-deck` actions).
- `tickets/index.md` updated if needed to align with the new guidance.
- `tickets/T-421-projectmanager-index-sync.md` marked `done` with completion notes when finished.

---

## Acceptance criteria

- [x] `tickets/projectmanager.md` contains explicit guidance directing EvoManager to update `tickets/index.md` whenever it creates new tickets, reclassifies tickets to `on-deck`, or closes/changes ticket statuses.
- [x] `tickets/index.md` remains accurate and consistent with the guidance (updated if necessary).
- [x] No files outside `Allowed write paths` were modified.
- [x] Ticket metadata (Status/Claimed-by/Claimed-at) is populated; ticket is marked `done` with a short summary before merge.

---

## Execution notes (optional)

- What changed (short): Added explicit EvoManager instructions in `tickets/projectmanager.md` to sync `tickets/index.md` after creating/reclassifying/closing tickets; added an index maintenance note and `on-deck` placeholder section in `tickets/index.md`.
- Any open questions: None.
- Follow-up tickets suggested: None.
