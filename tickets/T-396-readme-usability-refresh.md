# T-396: README usability refresh

Status: done
Type: structure
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-21T21:26:47+00:00
Last-updated: 2025-12-21
Completed-at: 2025-12-21T21:27:00+00:00

---

## Goal

Improve the root `README.md` so new contributors can quickly understand the control plane, navigate the country-first layout, and follow the ticket-first operating model without digging through multiple files.

---

## Context

- The README currently outlines the mission and ticket process but lacks a concise navigation section for the most-used paths (countries, UNIC, skills, executions).
- The quickstart can better emphasize protected files, claiming tickets, and respecting country scopes.
- A refreshed structure should surface the country-first layout while keeping the text-only expectation visible.

---

## Allowed write paths

- `README.md`
- `tickets/T-375-readme-usability-refresh.md`
- `executions/work/**` (optional run notes)

---

## Forbidden write paths

- Any file or directory not listed in Allowed write paths

---

## Required outputs

- `README.md` updated with clearer navigation, country-first layout cues, and reinforced ticket-first guidance.
- `tickets/T-375-readme-usability-refresh.md` updated with final status/notes once work is done.

---

## Acceptance criteria

- README contains a concise navigation section that links to the control plane, country directories, shared UNIC content, skills, tickets, and executions.
- Ticket workflow and protected-file cautions are explicitly highlighted in the quickstart/contributing sections.
- Country-first layout remains consistent with `ROADMAP.md` and `AGENTS.md`, including guidance on reports under `/countries/<country>/reports` and run notes in `/executions/`.
- Text-only expectations remain documented.
- No files outside Allowed write paths are modified.

---

## Execution notes (optional)

- What changed: Added a navigation section that surfaces control-plane links, country directories, shared UNIC content, skills, tickets, and executions; strengthened quickstart and contributing guidance with protected-file and country-scope reminders; retained country-first and text-only expectations while clarifying where reports and run notes belong.
- Open questions: None.
- Follow-ups needed: None.
