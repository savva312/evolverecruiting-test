---
name: ticket-boundaries
description: "Strict boundary enforcement for parallel and sequential EvoBuilder runs: how to interpret allowed_write_paths, avoid overlap, and handle cross-cutting changes safely."
compatibility: Any agent that can read tickets and edit repo files.
metadata:
  author: canonical
  version: "1.0"
---

## The rule
If you are working a ticket, you may only create/edit files inside that ticket’s `allowed_write_paths`.

This is the core mechanism that enables safe parallel work.

## How to interpret allowed_write_paths
- Treat each entry as an allowlist prefix (or glob).
- Writing outside the allowlist is forbidden even if it “seems harmless” (e.g., formatting a shared file).

## What to do if you need to change something outside scope
1. Add a note in the ticket under “Out of scope / follow-ups”.
2. Propose a new ticket:
   - with its own `allowed_write_paths`
   - with a clear rationale
3. If it’s a truly critical blocker, set the current ticket `status: blocked` and explain what is needed.

## Conflict avoidance in parallel runs
- Always “claim” the ticket before editing.
- If two tickets must touch the same file:
  - merge them into one ticket, or
  - refactor into a shared “base file” ticket first, then split follow-on tickets

## Safe shared files
Treat these as shared and only edit them in dedicated tickets:
- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- shared indexes under `/docs/` (unless partitioned)

## Finishing the ticket
Before marking done:
- verify no edits occurred outside allowlisted paths
- list outputs and links inside the ticket
