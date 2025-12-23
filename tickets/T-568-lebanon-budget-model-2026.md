# T-568: Lebanon — build `budget-model.csv` (planning baseline for 2026 cycle)

Status: open
Type: data
Priority: P1
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

Populate `countries/lebanon/data/operations/budget-model.csv` with a **defensible, documented planning baseline** for Lebanon recruiting spend (marketing, events, travel, scholarships/discounts, and partner/agent-related costs) for the 2026 recruitment cycle.

This is a planning artifact: it should cite internal repo sources and explicitly label assumptions.

---

## Context

Inputs already in the repo:
- `countries/lebanon/go-to-market/digital-playbook/channel-strategy.md` (channel mix assumptions)
- `countries/lebanon/data/marketing/channel-benchmarks.csv` (guardrails)
- Budget table exists but is empty: `countries/lebanon/data/operations/budget-model.csv`
- Dictionary: `countries/lebanon/data/operations/budget-model-dictionary.md`

---

## Allowed write paths

- `tickets/T-466-lebanon-budget-model-2026.md`
- `countries/lebanon/data/operations/budget-model.csv`
- `countries/lebanon/data/operations/budget-model-dictionary.md` (only if needed to clarify categories like scholarships/commissions)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/lebanon/**`)

---

## Required outputs

- `countries/lebanon/data/operations/budget-model.csv` populated with **≥15 rows** spanning at least:
  - paid media
  - events/fairs
  - travel
  - scholarships/discounts budget envelope
  - partner/agent costs (e.g., commission budget placeholder as a planning line)

---

## Acceptance criteria

- [ ] Every row has `category`, `period`, `amount_eur`, `assumptions`, `owner`, and `as_of`.
- [ ] No fabricated “actuals”: values are framed as budget/planning assumptions with the source file path referenced in `notes`.
- [ ] No files outside `Allowed write paths` were modified.

