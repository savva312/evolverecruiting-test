# T-556: Nigeria — Seed `keywords.csv` (search intent map)

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

Populate `countries/nigeria/data/marketing/keywords.csv` with a Nigeria-focused keyword map (≥ 80) grouped by intent stage and key program clusters.

---

## Context

- File is currently header-only: `countries/nigeria/data/marketing/keywords.csv`
- Dictionary: `countries/nigeria/data/marketing/keywords-dictionary.md`
- Use-case: inform Google Search campaigns, SEO topics, and landing page variants for Nigeria.

---

## Allowed write paths

- `countries/nigeria/data/marketing/keywords.csv`
- `executions/T-463-nigeria-keywords-csv-seed/**` (optional notes)

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

- `countries/nigeria/data/marketing/keywords.csv`

---

## Acceptance criteria

- [ ] CSV contains **≥ 80 rows** with `keyword`, `intent_stage`, `audience`, `priority`, and `as_of`
- [ ] Includes coverage for: “study in Cyprus”, “study in Greece”, UNIC brand terms, and cluster terms (medicine, CS/data, business)
- [ ] Leaves `search_volume_bg` and `est_cpc_eur` blank unless sourced; no fabricated volumes/CPCs

