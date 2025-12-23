---
name: ticket-archiving
description: "How to archive tickets safely: set Status: archived, move files into monthly archive folders, and update indices so archived items stay discoverable."
compatibility: Repos that keep tickets under /tickets with monthly archive subfolders.
metadata:
  author: canonical
  version: "1.0"
---

## Goal
Provide a deterministic, auditable workflow for archiving tickets without colliding with active work.

## When to use this skill
- You need to retire one or more tickets after completion or deprecation.
- You need to move tickets out of the active `/tickets/` folder while keeping them discoverable through `tickets/index.md`.

## Required inputs
- Ticket IDs to archive (single or range).
- Target archive month (`YYYYMM`) and folder name (`YYYYMM - Archived Tickets/`).
- Current `tickets/index.md` so you can add the archive entry.

## Steps
1) **Decide the archive window.** Determine the appropriate `YYYYMM` folder (e.g., `202512 - Archived Tickets/`). Create it under `/tickets/` if it does not exist.  
2) **Update ticket metadata.** For every ticket being archived, set `Status: archived` (use batch edit carefully). Leave other metadata intact for history.  
3) **Move the files.** Relocate the ticket files into the monthly archive folder under `/tickets/` (e.g., `git mv tickets/T-001-example.md "tickets/202512 - Archived Tickets/"`).  
4) **Refresh the index.** Add the archive to `tickets/index.md` under an **archived** section (distinct from done/dropped). Summarize the IDs moved and link to the monthly folder. Remove archived tickets from other status sections.  
5) **Validate.** Confirm paths resolve, statuses show `archived`, and no references remain in open/on-deck/in-progress/blocked/done/dropped lists.  
6) **Document follow-ups.** If any archived ticket needs revival, create a new ticket instead of editing the archived file.

## Notes and guardrails
- Archiving is an explicit action; do not auto-archive without a ticket.
- Keep `done`/`dropped` tickets in the active `/tickets/` folder until an archive run deliberately relocates them.
- Use relative links with URL-encoded spaces when pointing to archive folders from Markdown.
