# T-540: Nigeria — Seed `competitors.csv` (baseline roster)

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

Populate `countries/nigeria/data/entities/competitors.csv` with a baseline competitor roster (≥ 20) that reflects real alternatives Nigerian students consider (onshore, offshore, TRNC, online).

---

## Context

- Current competitor profiles exist but are minimal (3 files):
  - `countries/nigeria/entities/competitors/profiles/`
- CSV is header-only: `countries/nigeria/data/entities/competitors.csv`
- Program clusters needing competitor context:
  - `countries/nigeria/program-clusters/**/competitors.md`

---

## Allowed write paths

- `countries/nigeria/data/entities/competitors.csv`
- `executions/T-459-nigeria-competitors-csv-seed/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket for status updates)
- `countries/**` (except `countries/nigeria/**`)

---

## Required outputs

- `countries/nigeria/data/entities/competitors.csv`

---

## Acceptance criteria

- [ ] CSV contains **≥ 20 competitor rows** with `competitor_id`, `name`, `markets_served`, `focus_cluster`, and `as_of`
- [ ] Includes a mix of competitor types relevant to Nigeria decisioning (examples: Nigeria private premium, UK/Canada pathways, TRNC Cyprus options, online low-cost providers)
- [ ] Notes include short source links (official sites preferred) and do not include unverified claims as fact

