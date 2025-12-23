# T-504: Lebanon — seed `keywords.csv` (AR/FR/EN keyword pack for acquisition)

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

Create a Lebanon-ready search keyword seed list for demand gen by populating `countries/lebanon/data/marketing/keywords.csv` with Arabic, French, and English keywords across:
- campus intent (Athens vs Nicosia)
- destination intent (Greece/Cyprus)
- program intent (Medicine, CS/Data, Business, Psychology, Design, Health)
- pricing intent (scholarships, fees, cost of living)

This is a planning dataset; it should not fabricate CPC/volume. Unknown numeric fields can be left blank with a note indicating “KW Planner needed.”

---

## Context

- Empty file: `countries/lebanon/data/marketing/keywords.csv`
- Dictionary: `countries/lebanon/data/marketing/keywords-dictionary.md`
- Channel strategy and creative angles (for vocabulary): `countries/lebanon/go-to-market/digital-playbook/channel-strategy.md`

---

## Allowed write paths

- `tickets/T-450-lebanon-keywords-csv-seed.md`
- `countries/lebanon/data/marketing/keywords.csv`
- `countries/lebanon/data/marketing/keywords-dictionary.md` (only if field guidance needs minor clarification)

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

- `countries/lebanon/data/marketing/keywords.csv` populated with **≥90 rows**.

---

## Acceptance criteria

- [ ] Every row has `keyword`, `intent_stage`, `priority`, and `as_of`.
- [ ] Arabic keywords use Arabic script where appropriate; French and English variants are included for parents/diaspora.
- [ ] `est_cpc_eur` and `search_volume_lb` are blank unless sourced; when blank, `notes` indicates the intended source (e.g., “TODO: Google KW Planner”).
- [ ] No files outside `Allowed write paths` were modified.

