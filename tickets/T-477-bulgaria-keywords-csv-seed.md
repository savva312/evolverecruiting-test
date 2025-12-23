# T-477: Bulgaria — seed `keywords.csv` (BG/EN keyword pack for acquisition)

Status: done
Type: data
Priority: P1
Dependencies: (none)
Claimed-by: evoticketresolver_qme9iizl
Claimed-at: 2025-12-22T20:36:16Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Create a Bulgaria-ready search keyword seed list for demand gen by populating `countries/bulgaria/data/marketing/keywords.csv` with Bulgarian and English keywords across:
- campus intent (Athens vs Nicosia)
- destination intent (Greece/Cyprus)
- program intent (Medicine, CS/Data, Business, Psychology, Design)
- pricing intent (scholarships, fees, cost of living)

This is a planning dataset; it should not fabricate CPC/volume. Unknown numeric fields can be left blank with a note indicating “KW Planner needed.”

---

## Context

- File exists but is empty: `countries/bulgaria/data/marketing/keywords.csv`
- Dictionary: `countries/bulgaria/data/marketing/keywords-dictionary.md`

---

## Allowed write paths

- `tickets/T-477-bulgaria-keywords-csv-seed.md`
- `countries/bulgaria/data/marketing/keywords.csv`
- `countries/bulgaria/data/marketing/keywords-dictionary.md` (only if field guidance needs clarification)

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

- `countries/bulgaria/data/marketing/keywords.csv` populated with **≥80 rows**.

---

## Acceptance criteria

- [ ] Every row has `keyword`, `intent_stage`, `priority`, and `as_of`.
- [ ] Bulgarian keywords use Bulgarian Cyrillic where appropriate (e.g., “медицина в Гърция”), and English variants are included for diaspora/parents.
- [ ] `est_cpc_eur` and `search_volume_bg` are left blank unless sourced; when blank, `notes` indicates the intended source (e.g., “TODO: Google KW Planner”).
- [ ] No files outside `Allowed write paths` were modified.
- [x] Every row has `keyword`, `intent_stage`, `priority`, and `as_of`.
- [x] Bulgarian keywords use Bulgarian Cyrillic where appropriate (e.g., “медицина в Гърция”), and English variants are included for diaspora/parents.
- [x] `est_cpc_eur` and `search_volume_bg` are left blank unless sourced; when blank, `notes` indicates the intended source (e.g., “TODO: Google KW Planner”).
- [x] No files outside `Allowed write paths` were modified.

---

## What changed

- Populated `countries/bulgaria/data/marketing/keywords.csv` with 133 BG/EN seed keywords spanning campus, destination, program, and pricing intent (all numeric fields left blank with `notes` pointing to KW Planner).  
