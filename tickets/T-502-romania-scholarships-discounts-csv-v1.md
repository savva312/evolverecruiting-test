# T-502: Romania — populate scholarships/discounts dataset (UNIC Nicosia + UNIC Athens)

Status: in-progress
Type: data
Priority: P0
Dependencies: (none)
Claimed-by: work
Claimed-at: 2026-04-12T00:00:00Z
Last-updated: 2026-04-12
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

- [ ] Every row has a clear source reference (URL or repo path) and a `last_verified`/`as_of` date (define which in dictionary).
- [ ] Campus is explicitly captured (`unic_nicosia` vs `unic_athens`) and any program exclusions are explicit.
- [ ] Dictionary matches dataset exactly.
- [ ] No edits outside allowed paths.
