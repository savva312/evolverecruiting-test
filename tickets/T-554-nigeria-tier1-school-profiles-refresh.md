# T-554: Nigeria — Tier1 school profile refresh (11 schools)

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

Improve operational usability of the **Tier1** Nigeria school profiles by reducing critical `TBD` gaps (calendar, counseling contacts, outcomes signals) for the 11 Tier1 schools already in the roster.

---

## Context

- Tier1 roster (from `countries/nigeria/data/entities/schools.csv`): 11 schools across Lagos, Abuja, and Jos.
- Many Tier1 profiles still contain significant `TBD` fields, which blocks effective counselor outreach planning and visit scheduling.
- Constraints:
  - No personal mobile numbers/emails; use role-based contacts only.
  - Add sources + last-updated stamps; label unknowns explicitly.

---

## Allowed write paths

- `countries/nigeria/entities/schools/profiles/abuja/american-international-school-of-abuja-aisa/README.md`
- `countries/nigeria/entities/schools/profiles/abuja/international-community-school-ics-abuja/README.md`
- `countries/nigeria/entities/schools/profiles/abuja/lyc-e-fran-ais-marcel-pagnol-d-abuja-lfmpa/README.md`
- `countries/nigeria/entities/schools/profiles/jos/hillcrest-school/README.md`
- `countries/nigeria/entities/schools/profiles/lagos/american-international-school-of-lagos-aisl/README.md`
- `countries/nigeria/entities/schools/profiles/lagos/british-international-school-lagos-bis/README.md`
- `countries/nigeria/entities/schools/profiles/lagos/charterhouse-lagos/README.md`
- `countries/nigeria/entities/schools/profiles/lagos/children-s-international-school-cis/README.md`
- `countries/nigeria/entities/schools/profiles/lagos/lekki-british-school-high-school/README.md`
- `countries/nigeria/entities/schools/profiles/lagos/lyc-e-fran-ais-louis-pasteur/README.md`
- `countries/nigeria/entities/schools/profiles/lagos/rugby-school-nigeria/README.md`
- `executions/T-462-nigeria-tier1-school-profiles-refresh/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket for status updates)
- Any other files under `countries/nigeria/entities/schools/` (do not touch `schools.csv` or `index.md` in this ticket)

---

## Required outputs

- Updated Tier1 profile files listed above

---

## Acceptance criteria

- [ ] For each Tier1 school profile, the Snapshot table includes: website, main email (role-based), and best outreach months (or a sourced note if unknown)
- [ ] “Academic calendar captured” is completed where possible (or has a clearly explained blocker + next action)
- [ ] Each profile includes at least 2 credible sources/links with date stamps (or `last_checked`)
- [ ] No personal contact details are added (only role-based inboxes and published switchboards if needed)

