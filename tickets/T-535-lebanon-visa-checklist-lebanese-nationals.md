# T-535: Lebanon — visa & travel checklist (Lebanese nationals + dual nationals) for Cyprus/Greece

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

Create a Lebanon-facing, campus-aware visa & travel checklist that admissions/recruiters can share internally and use to brief offerholders (and their parents) without confusion.

---

## Context

Lebanon offerholder workflow references visa assumptions but lacks a single checklist artifact:
- `countries/lebanon/go-to-market/offerholder-and-yield/housing-and-arrival.md`

Shared campus resources exist and should be referenced (not duplicated):
- `UNIC/unicnicosia/visas/README.md`
- `UNIC/unicathens/visas/README.md`

---

## Allowed write paths

- `tickets/T-457-lebanon-visa-checklist-lebanese-nationals.md`
- `countries/lebanon/go-to-market/offerholder-and-yield/visa-checklist.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/lebanon/**`)

---

## Required outputs

- `countries/lebanon/go-to-market/offerholder-and-yield/visa-checklist.md` created with:
  - separate sections for **Cyprus (Nicosia)** vs **Greece (Athens)**
  - separate flows for **Lebanese passport holders (non-EU)** vs **EU passport holders / dual nationals**
  - a “when to start” timeline aligned to Lebanon exams/results windows
  - an explicit “sources” section linking to official government/consulate guidance and the relevant `/UNIC/**` pages
  - clear disclaimer language (“requirements change; confirm with consulate/authority”)

---

## Acceptance criteria

- [ ] No legal advice language; framed as operational checklist + “verify with authority.”
- [ ] Avoids storing any applicant PII or document scans; points to secure systems instead.
- [ ] No files outside `Allowed write paths` were modified.

