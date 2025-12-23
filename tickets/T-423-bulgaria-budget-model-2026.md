# T-423: Bulgaria — build `budget-model.csv` (planning baseline for 2026 cycle)

Status: done
Type: data
Priority: P1
Dependencies: (none)
Claimed-by: evoticketresolver_3ks6fmay
Claimed-at: 2025-12-22T17:50:14Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Populate `countries/bulgaria/data/operations/budget-model.csv` with a **defensible, documented planning baseline** for Bulgaria recruiting spend (marketing, events, travel, scholarships/discounts, and partner/agent-related costs) for the 2026 recruitment cycle.

This is a planning artifact: it should cite internal repo sources (e.g., the Athens recruitment plan report) and explicitly label assumptions.

---

## Context

Inputs already in the repo:
- `countries/bulgaria/reports/2025-12-20 - UNIC Athens Bulgaria Recruitment Plan.md` (contains budget ranges and acquisition cost guardrails)
- `countries/bulgaria/go-to-market/digital-playbook/channel-strategy.md` (channel mix assumptions)
- Budget table exists but is empty: `countries/bulgaria/data/operations/budget-model.csv`
- Dictionary: `countries/bulgaria/data/operations/budget-model-dictionary.md`

---

## Allowed write paths

- `tickets/T-423-bulgaria-budget-model-2026.md`
- `countries/bulgaria/data/operations/budget-model.csv`
- `countries/bulgaria/data/operations/budget-model-dictionary.md` (only if needed to clarify categories like scholarships/commissions)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/bulgaria/**`)

---

## Required outputs

- `countries/bulgaria/data/operations/budget-model.csv` populated with **≥15 rows** spanning at least:
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

What changed (2025-12-22):
- Populated `countries/bulgaria/data/operations/budget-model.csv` with a 2026 planning baseline (paid media; events; travel; scholarships/discounts envelope; partner/agent cost placeholders) referencing internal repo sources and labeling assumptions.
- Expanded `countries/bulgaria/data/operations/budget-model-dictionary.md` category guidance to explicitly include `scholarships_discounts` and `partners_agents`.
