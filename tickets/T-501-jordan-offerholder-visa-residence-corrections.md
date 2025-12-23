# T-501: Jordan — correct offerholder visa/residence assumptions (Cyprus + Greece)

Status: open
Type: content
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

Correct compliance-sensitive inaccuracies in Jordan offerholder materials by:
- Removing incorrect visa/residence assumptions (especially “Jordanian passport holders are visa-free”).
- Rewriting guidance to be safe, sourced, and explicitly campus-specific (UNIC Nicosia/Cyprus vs UNIC Athens/Greece).
- Removing placeholder/fake contact addresses (e.g., `*.example`).

---

## Context

The following files include incorrect or placeholder visa statements:
- `countries/jordan/go-to-market/offerholder-and-yield/deposit-deadlines.md`
- `countries/jordan/go-to-market/offerholder-and-yield/housing-and-arrival.md`

These documents must be treated as compliance-sensitive:
- Do not provide legal advice; always include “verify with embassy/consulate/authority” language.
- Do not state processing times/fees unless sourced.

---

## Allowed write paths

- `tickets/T-449-jordan-offerholder-visa-residence-corrections.md`
- `countries/jordan/go-to-market/offerholder-and-yield/deposit-deadlines.md`
- `countries/jordan/go-to-market/offerholder-and-yield/housing-and-arrival.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/jordan/**` and referenced `UNIC/**` links)

---

## Required outputs

- `countries/jordan/go-to-market/offerholder-and-yield/deposit-deadlines.md` updated with Jordan-correct visa/arrival assumptions and clear “verify with authority” language.
- `countries/jordan/go-to-market/offerholder-and-yield/housing-and-arrival.md` updated similarly; remove fake contact details.

---

## Acceptance criteria

- [ ] No statements claim or imply Jordanian nationals are visa-free for Cyprus/Greece unless a primary source is linked and the claim is accurate.
- [ ] All visa/residence guidance is clearly separated by campus (Cyprus vs Greece) and by applicant type where relevant (Jordanian nationals vs EU nationals residing in Jordan).
- [ ] No fake/placeholder domains remain (e.g., `example`, `example.com`, `*.example`).
- [ ] The docs include primary-source links (embassy/consulate/government pages) and `last_verified` dates for the most important claims.

