# T-408: Ticket renumbering sweep

Status: done
Type: structure
Priority: P0
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-21T23:30:15Z
Last-updated: 2025-12-21

---

## Goal

Eliminate numbering gaps and duplicates across all tickets by assigning a single sequential series, updating filenames and ticket headers to match, and refreshing the ticket index accordingly.

---

## Context

- Current ticket IDs include duplicates and missing numbers, making cross-referencing difficult.
- Governance rules live in `AGENTS.md`, `ROADMAP.md`, and `tickets/README.md`.
- This is a control-plane cleanup; scope stays within `tickets/**`.

---

## Allowed write paths

- `tickets/**`
- `executions/**` (optional run notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `countries/**`
- `UNIC/**`
- `reports/**`

---

## Required outputs

- All ticket filenames and header IDs updated to a single, gapless sequential series.
- `tickets/index.md` refreshed to reflect the renumbered tickets.
- Notes in this ticket summarizing the renumbering approach.

---

## Acceptance criteria

- [x] Ticket IDs run sequentially without gaps or duplicates across `tickets/*.md` files (template included as the first entry).
- [x] Each ticket’s filename and header use the same new ID.
- [x] `tickets/index.md` lists the renumbered tickets with matching IDs and slugs.
- [x] Edits stay within `Allowed write paths`.

---

## Execution notes (optional)

- Renumbered all 409 tickets to a contiguous T-000–T-408 series, sorted by the original ID then slug; filenames and header IDs now match.
- Stored an old→new mapping and run summary in `executions/ticket-renumbering-sweep/mapping.csv` and `executions/ticket-renumbering-sweep/summary.txt`.
- Regenerated `tickets/index.md` from ticket metadata (Open/In Progress/Dropped) to reflect the new numbering.
- Normalized a handful of Lebanon and structure tickets whose headers still contained legacy IDs.
