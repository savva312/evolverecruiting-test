# T-471: Ticket ID deduplication and renumbering

Status: in-progress
Type: structure
Priority: P0
Dependencies: (none)
Claimed-by: local-branch
Claimed-at: 2025-12-22
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Audit the current ticket set for duplicate IDs and renumber conflicting tickets to restore a unique, monotonic ticket ID sequence. Update supporting indices so they reference the new IDs.

---

## Context

- Tickets must use unique IDs to avoid collisions in scheduling and execution. Multiple duplicate IDs were observed in the `tickets/` directory listing.
- The ROADMAP tracks priorities by ticket ID; keeping IDs unique avoids ambiguity when agents claim work.

---

## Allowed write paths

- `tickets/**`
- `executions/**`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `UNIC/**`
- `countries/**`
- `reports/**`
- `.github/**`
- `scripts/**`

---

## Required outputs

- Updated ticket files with unique IDs and matching filenames/slugs.
- `tickets/index.md` updated to reflect any renumbered tickets.
- Optional execution note summarizing renumbering decisions, if helpful.

---

## Acceptance criteria

- [ ] No duplicate ticket IDs remain in `tickets/` (including subdirectories).
- [ ] Renumbered tickets have filenames and internal IDs that match.
- [ ] Links in `tickets/index.md` point to the correct renumbered files.
- [ ] No files outside `Allowed write paths` were modified.

---

## Execution notes (optional)

- What changed (short):
- Any open questions:
- Follow-up tickets suggested:
