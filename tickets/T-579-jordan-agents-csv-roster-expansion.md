# T-579: Jordan — expand agents CSV to match Jordan roster + profiles

Status: open
Type: data
Priority: P2
Dependencies: (none)
Claimed-by:
Claimed-at:
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Expand `countries/jordan/data/entities/agents.csv` so it fully represents the Jordan agent ecosystem already documented in profiles/rosters, enabling CRM segmentation and partner management.

---

## Context

Current mismatch:
- `countries/jordan/entities/agents/README.md` lists 12+ agent profiles
- `countries/jordan/data/entities/agents.csv` contains only 3 rows

Schema reference:
- `countries/jordan/data/entities/agents-dictionary.md`

Agent sources:
- `countries/jordan/entities/agents/profiles/**`
- `countries/jordan/entities/agents/feeder-candidates.md`

---

## Allowed write paths

- `tickets/T-468-jordan-agents-csv-roster-expansion.md`
- `countries/jordan/data/entities/agents.csv`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/jordan/**`)

---

## Required outputs

- `countries/jordan/data/entities/agents.csv` updated to include one row per agent profile listed in `countries/jordan/entities/agents/README.md` (minimum 12 rows).

---

## Acceptance criteria

- [ ] CSV conforms to `agents-dictionary.md` (IDs, semicolon-separated multi-fields, `as_of` present).
- [ ] `agent_id` values are stable, lowercase ASCII, and use a consistent pattern (e.g., `ag-jo-amman-<slug>`).
- [ ] No contact info or claims are invented; if unknown, leave fields blank and record the gap in `notes`.

