# T-020: Country migration ticket scaffolding

Status: archived
Type: structure
Priority: P0
Dependencies: T-017
Claimed-by: work
Claimed-at: 2025-12-20T16:03:11Z
Last-updated: 2025-12-20

---

## Goal

Create non-overlapping migration tickets for each country to enable parallel execution under the new multi-country layout, with explicit allowed/forbidden paths per country.

---

## Context

- Depends on control-plane updates in T-017.
- Ensures future migration work is coordinated via country-specific tickets with minimal collision risk.
- Existing tickets queue does not yet include multi-country migration scopes.

---

## Allowed write paths

- `tickets/**` (creation and updates of new country migration tickets only)
- `research/**` (optional notes)
- `tickets/index.md` (if listing the new tickets)
- `tickets/T-018-ticket-scaffolding-multi-country.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- Any country content directories (`/**`) outside of `tickets/**`

---

## Required outputs

- New country migration tickets (e.g., Bulgaria, Nigeria, Greece) with strict allowed/forbidden paths and dependencies on T-017
- `tickets/T-018-ticket-scaffolding-multi-country.md` updated with status/notes upon completion

---

## Acceptance criteria

- [x] Country migration tickets exist with unique allowed write paths per country (no overlaps)
- [x] Each new ticket declares dependencies on T-017 (and T-018 where relevant)
- [x] No files outside `tickets/**` (and optional `research/**`) modified

---

## Execution notes (optional)

- What changed (short): Updated country migration tickets (T-019, T-021, T-022) with disjoint research paths and refreshed timestamps to enable parallel runs; dependencies remain on T-017/T-018; marked scaffolding ticket complete.
- Any open questions: None
- Follow-up tickets suggested: None
