# T-544: Nigeria — Competitor profiles expansion (6 new dossiers)

Status: open
Type: content
Priority: P1
Dependencies: T-459
Claimed-by:
Claimed-at:
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Add **6 new** competitor dossiers under `countries/nigeria/entities/competitors/profiles/` that are materially relevant to Nigerian prospects comparing against UNIC / UNIC Athens.

---

## Context

- Existing competitor folder: `countries/nigeria/entities/competitors/`
- Current profiles cover only 3 competitors (onshore + distance + tuition-free online).
- Priority is to cover “actually chosen” alternatives for Nigeria, especially for:
  - Medicine (regional/Europe/TRNC)
  - Business/CS (UK/Canada/EU + online)
- Keep each profile sourced and dated (`last_checked`).

---

## Allowed write paths

- `countries/nigeria/entities/competitors/profiles/**`
- `countries/nigeria/entities/competitors/README.md` (required to link new profiles)
- `executions/T-460-nigeria-competitor-profiles-expansion/**` (optional notes)

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

- 6 new profile files under `countries/nigeria/entities/competitors/profiles/` (pick competitors with strong Nigeria relevance; example set to consider):
  - 2–3 Cyprus/TRNC universities recruiting in Nigeria (especially medicine)
  - 1–2 EU medicine destinations popular with Nigerians (e.g., Central/Eastern Europe)
  - 1 online/low-cost alternative with Nigeria reach
- `countries/nigeria/entities/competitors/README.md` updated to list and link the new profiles

---

## Acceptance criteria

- [ ] Each new profile includes: overview, why Nigerians choose it, programs relevant to UNIC overlap, pricing/scholarships cues, admissions requirements, and sources with `last_checked`
- [ ] All claims are sourced or clearly labeled as assumptions; no fabricated tuition numbers
- [ ] README links resolve to the new profile files

