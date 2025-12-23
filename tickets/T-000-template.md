# T-000: <Title>

Status: open
Type: content
Priority: P1
Dependencies: (none)
Claimed-by:
Claimed-at:
Last-updated: YYYY-MM-DD
Agent: EvoTicket Resolver | EvoResearcher
Research rounds: <integer or N/A>
Research sections: <integer or N/A>
Research output path: `<path>` (required if Agent = EvoResearcher)

---

> If your run starts without a referenced ticket, create a new ticket using this template (next available ID), set it to `in-progress`, commit the claim before other changes, and include the ticket marked `done` in the PR alongside the work.

## Goal

Describe the concrete outcome this ticket should produce.
Write it so a reviewer can clearly tell if it happened.
If `Agent: EvoResearcher`, the ticket body should include the research prompt.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` section(s):
  - Existing docs/data:
- External constraints (if any):
- Assumptions (label them):
- If `Agent: EvoResearcher`, confirm the report folder above is correct and include the prompt below.

---

## Allowed write paths

List the only paths that may be modified. Use globs.

- `docs/<area>/**`
- `data/<area>/**`
- `templates/<area>/**`
- `executions/**` (optional; only for notes)

---

## Forbidden write paths

List protected or off-limits paths. Use globs.

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**` (unless the ticket explicitly allows)
- `scripts/**` (unless the ticket explicitly allows)
- `<anything else to protect>`

---

## Required outputs

List exact file paths that must exist or be updated.

- `docs/<path>/<file>.md`
- `data/<path>/<file>.yml`
- `docs/index.md` (if applicable)

---

## Acceptance criteria

Objective checks. Examples:

- [ ] All required output files exist at the specified paths
- [ ] No files were modified outside `Allowed write paths`
- [ ] Internal links added by this ticket resolve to existing repo files
- [ ] Content follows repo writing conventions (headings, clarity, minimal boilerplate)
- [ ] If data files were modified: they remain valid YAML/JSON/CSV and are consistent with any local conventions
- [ ] `Agent` is set; if `EvoResearcher`, research rounds/sections/output path are populated and the prompt lives in the ticket body

---

## Execution notes (optional)

- What changed (short):
- Any open questions:
- Follow-up tickets suggested:
