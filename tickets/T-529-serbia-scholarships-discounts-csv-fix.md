# T-529: Serbia — Fix scholarships/discounts dataset (remove wrong-country entries; add Serbia financing)

Status: open
Type: data
Priority: P0
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

Correct and strengthen Serbia’s scholarships/discounts dataset so counselors and admissions staff can use it without propagating errors.

---

## Context

- Target file:
  - `countries/serbia/data/programs/scholarships-discounts.csv`
- Known issues:
  - Contains a Bulgaria bank product (`dskbank.bg`) incorrectly labeled for Serbia.
  - Some entries blur “policy” vs “tactics” and need clearer sourcing and scope (UNIC Nicosia vs UNIC Athens).
- Reference sources (read-only inputs):
  - `UNIC/unicnicosia/scholarships/README.md`
  - `UNIC/unicathens/scholarships/README.md`

---

## Allowed write paths

- `countries/serbia/data/programs/scholarships-discounts.csv`
- `executions/**` (optional; notes only)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)

---

## Required outputs

- `countries/serbia/data/programs/scholarships-discounts.csv`

---

## Acceptance criteria

- [ ] Removes any Serbia-irrelevant bank/loan products and replaces with Serbia-relevant financing options **only if source-backed** (Serbian bank pages or reputable sources).
- [ ] Each UNIC/UNIC Athens scholarship/discount row clearly states eligibility scope and includes an official source URL.
- [ ] No fabricated deadlines or % ranges; if uncertain, leave blank and add a “verify” note.
- [ ] CSV remains valid and consistent with its header (no extra/missing columns).
- [ ] No edits outside allowed write paths.

