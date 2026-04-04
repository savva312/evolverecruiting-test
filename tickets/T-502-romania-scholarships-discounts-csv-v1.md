# T-502: Romania — populate scholarships/discounts dataset (UNIC Nicosia + UNIC Athens)

Status: done
Type: data
Priority: P0
Dependencies: (none)
Claimed-by: codex-20251223-1
Claimed-at: 2025-12-23
Completed-at: 2025-12-23
Last-updated: 2025-12-23
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Populate `countries/romania/data/programs/scholarships-discounts.csv` with a Romania-usable view of:
- UNIC Nicosia scholarships/discounts (relevant to Romanian prospects)
- UNIC Athens scholarships/discounts (relevant to Romanian prospects)
- any Romania-specific constraints (e.g., program exclusions, deadlines, stacking rules)

The output must be accurate, source-backed, and easy for an enrollment manager to quote internally (with no overpromising).

---

## Context

Existing in-repo references:
- `countries/romania/go-to-market/schools-playbook/counselor-toolkit.md` currently contains placeholders for scholarship summaries.
- UNIC scholarship references live under:
  - `UNIC/unicnicosia/scholarships/README.md`
  - `UNIC/unicathens/scholarships/README.md`
- CSV scaffold: `countries/romania/data/programs/scholarships-discounts.csv`
- Dictionary scaffold: `countries/romania/data/programs/scholarships-discounts-dictionary.md`

---

## Allowed write paths

- `tickets/T-449-romania-scholarships-discounts-csv-v1.md`
- `countries/romania/data/programs/scholarships-discounts.csv`
- `countries/romania/data/programs/scholarships-discounts-dictionary.md`
- `executions/**` (optional for notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`
- `tickets/**` (except this ticket file)
- `countries/**` (except `countries/romania/data/**`)

---

## Required outputs

- Updated `countries/romania/data/programs/scholarships-discounts.csv` (minimum: a complete campus-level scholarship inventory for Nicosia and Athens as captured in-repo)
- Updated `countries/romania/data/programs/scholarships-discounts-dictionary.md`

---

## Acceptance criteria

- [x] Every row has a clear source reference (URL or repo path) and a `last_verified`/`as_of` date (define which in dictionary).
- [x] Campus is explicitly captured (`unic_nicosia` vs `unic_athens`) and any program exclusions are explicit.
- [x] Dictionary matches dataset exactly.
- [x] No edits outside allowed paths.

---

## Completion

- Populated `countries/romania/data/programs/scholarships-discounts.csv` with 21 rows covering UNIC Nicosia and UNIC Athens plus Romania-specific constraints, source links, and an `as_of` date.
- Updated `countries/romania/data/programs/scholarships-discounts-dictionary.md` to document the new `campus` field and range/other amount rules so the CSV stays in-sync.
