# T-419: Project manager control file and automation guidance

Status: done
Type: structure
Priority: P1
Agent: EvoTicket Resolver
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-22T16:12:00Z
Last-updated: 2025-12-22
Completed-at: 2025-12-22T16:45:00Z

---

## Goal

Create a durable `tickets/projectmanager.md` control file that the recurring EvoManager automation can read every 30 minutes (UTC boundaries) to decide which tickets to open or close. Align the broader control-plane docs (AGENTS, README, ROADMAP, tickets README) so they reference this automation and the ticket-budget governance it enforces.

---

## Context

- The repo relies on ticket-driven execution; EvoManager acts as a meta-agent that inspects tickets and the repo to decide what to schedule next.
- EvoManager is never assigned regular tickets; it is only assigned the `projectmanager.md` guidance.
- The control file should include long-term repo goals, sprint tracking (active, on-deck, completed), and per-epoch ticket placement guidance (200 on-deck slots per 30-minute epoch; no daily cap).
- Control-plane docs should reflect the new automation pattern and where the EvoManager reads/writes.

---

## Allowed write paths

- `tickets/T-419-projectmanager-control.md`
- `tickets/projectmanager.md`
- `AGENTS.md`
- `README.md`
- `ROADMAP.md`
- `tickets/README.md`
- `tickets/index.md`
- `executions/T-419-projectmanager-control/**` (optional notes)

---

## Forbidden write paths

- All other files and directories not listed above

---

## Required outputs

- `tickets/projectmanager.md` created with a clear template/format for EvoManager, populated with current goals, sprints, and ticket budget values.
- Control-plane docs (`AGENTS.md`, `README.md`, `ROADMAP.md`, `tickets/README.md`) updated to mention the EvoManager process and the `projectmanager.md` control file.
- Ticket index updated if new ticket references are needed.
- This ticket updated to `Status: done` with completion notes.

---

## Acceptance criteria

- `tickets/projectmanager.md` is machine-readable and human-readable, covering: mission/goals, governance guardrails, per-epoch ticket budget (200 on-deck slots per 30-minute epoch), active sprints with per-country focus, on-deck sprints, completed sprints, and guidance on how EvoManager should open/close tickets.
- Control-plane docs explicitly reference the EvoManager cadence, its reliance on `projectmanager.md`, and that EvoManager is not assigned standard tickets.
- No changes occur outside Allowed write paths.
- Ticket status moved to `done` with a short “what changed” note when work is complete.

---

## Execution notes (optional)

- What changed (short): Added `tickets/projectmanager.md` with EvoManager cadence, budget tracking, and sprint priorities; updated control-plane docs (AGENTS, README, ROADMAP, tickets README/index) to reference the automation and ticket limits.
- Follow-ups: EvoManager should keep the budget tracker current and add/remove sprints as priorities shift.
