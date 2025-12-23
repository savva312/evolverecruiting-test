# T-515: Jordan — add professional licensing bodies (profiles + regulators.csv)

Status: open
Type: integration
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

Fill Jordan regulator coverage gaps for regulated professions by:
- Adding profiles for key Jordan professional licensing bodies (Medicine, Pharmacy, Nursing, Engineering, etc.).
- Updating `countries/jordan/data/entities/government-regulators.csv` to include these bodies with accurate domains and contact points.

---

## Context

The government/regulators area explicitly calls out missing professional licensure bodies:
- `countries/jordan/entities/government-regulators/README.md`

Schema reference:
- `countries/jordan/data/entities/government-regulators-dictionary.md`

---

## Allowed write paths

- `tickets/T-452-jordan-professional-bodies-regulators-pack.md`
- `countries/jordan/entities/government-regulators/README.md`
- `countries/jordan/entities/government-regulators/profiles/**`
- `countries/jordan/data/entities/government-regulators.csv`

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

- At least 4 new regulator profiles under `countries/jordan/entities/government-regulators/profiles/` for professional/licensure bodies.
- `countries/jordan/data/entities/government-regulators.csv` updated with matching rows for those bodies.
- `countries/jordan/entities/government-regulators/README.md` updated to reflect expanded coverage.

---

## Acceptance criteria

- [ ] Each new profile includes: mandate, relevance to UNIC/UNIC Athens applicants, contact channels, and `last_verified` + sources.
- [ ] CSV rows match the dictionaries (required fields present; country codes; valid URLs/emails).
- [ ] No timelines/fees are asserted unless sourced; no legal advice language.

