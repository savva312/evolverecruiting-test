---
name: evobuilder-workflow
description: "End-to-end workflow for EvoBuilder-managed repos: how to read project context, select and claim tickets, respect write boundaries, implement changes, validate, and mark tickets done with clean diffs."
compatibility: Any filesystem-based agent with git access. Works best when ROADMAP.md and /tickets exist.
metadata:
  author: canonical
  version: "1.0"
---

## Goal
Produce high-quality repo contributions **by completing tickets**, not by writing a single monolithic report.

## Required inputs (always read these)
1. `README.md` (what this repo is)
2. `AGENTS.md` (how agents must behave here)
3. `ROADMAP.md` (what exists + what’s next)
4. One or more files in `/tickets/` (what to do now)

## The EvoBuilder ticket loop
### 1) Load context
- Skim `README.md` → understand repo purpose and conventions.
- Read `AGENTS.md` → obey guardrails (especially write boundaries).
- Open `ROADMAP.md` → see milestones and how tickets map to outputs.

### 2) Pick the ticket(s)
- Work **one ticket at a time** unless the ticket explicitly allows bundling.
- Prefer tickets with:
  - clear outputs
  - non-overlapping write boundaries

### 3) Claim the ticket (prevents overlap)
Edit the ticket file and set:
- `status: in_progress`
- `claimed_by: <agent-run-identifier>`
- `claimed_at: <ISO timestamp>`

If the ticket is already claimed and the claim looks active, **do not proceed**.

### 4) Execute the ticket
- Only write in paths allowed by the ticket (`allowed_write_paths`).
- If you discover a necessary change outside scope:
  - do not “just fix it”
  - add a note to the ticket under **Out of scope / follow-ups**
  - optionally create a new ticket file

### 5) Validate and self-review
- Ensure outputs exist at the specified paths.
- Check internal links are relative.
- Keep diffs minimal: avoid sweeping reformatting.

### 6) Close the ticket
Update the ticket:
- `status: done`
- add `completed_at: <ISO timestamp>`
- list outputs created/updated
- add brief notes + any follow-ups
- If retiring a ticket entirely, use the ticket-archiving skill: set `Status: archived`, move the ticket into `tickets/YYYYMM - Archived Tickets/`, and add it to the **Archived** section of `tickets/index.md` (separate from Closed/Done).

## Quality bar (non-negotiable)
- Follow write boundaries.
- Don’t introduce secrets, credentials, or personal data.
- Don’t delete or reorganize major folders unless the ticket explicitly says so.
