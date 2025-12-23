# T-139: Jordan NGOs/SGOs landscape

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20
Last-updated: 2025-12-20

---

## Goal

Document Jordanian NGOs and SGOs that influence scholarships, mobility assistance, and counseling for prospective UNIC/UNIC Athens students. Produce an index and organization profiles under `countries/jordan/entities/ngos-sgos/` to guide partnership outreach and sponsorship targeting.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` — repo map for country-first entity documentation.
  - `countries/jordan/entities/ngos-sgos/README.md` — scope for NGO/SGO coverage in Jordan.
- External constraints (if any): none noted.
- Assumptions (label them): include national, Amman-focused, and refugee-support organizations that materially affect student mobility or funding.

---

## Allowed write paths

- `countries/jordan/entities/ngos-sgos/**`
- `countries/jordan/data/entities/**`
- `research/**` (optional; only for notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/bulgaria/**`
- `countries/greece/**`
- `countries/nigeria/**`
- `countries/lebanon/**`
- `countries/romania/**`
- `countries/serbia/**`
- `UNIC/**`

---

## Required outputs

- `countries/jordan/entities/ngos-sgos/index.md` summarizing priority NGOs/SGOs, thematic focus, geographies, and partnership status.
- `countries/jordan/entities/ngos-sgos/profiles/*.md` (minimum 5 organizations) with a standard profile structure: overview, programs, target students, partnership fit, contacts/sources, and next steps.
- `countries/jordan/entities/ngos-sgos/README.md` refreshed to link to the index and profile standards.
- `countries/jordan/data/entities/ngos-sgos.csv` listing the same organizations with columns for name, scope, focus area, audience, partnership notes, status, and last-reviewed date.

---

## Acceptance criteria

- [ ] Required files exist at the specified paths with Jordan-specific content and functioning links to profiles.
- [ ] At least five NGO/SGO profiles include mission, programs, reach, partnership fit, contacts/sources, and recommended next steps.
- [ ] The index highlights prioritization and links to each profile file.
- [ ] The CSV is populated, uses the specified columns, and rows align with the documented profiles.
- [ ] No files were modified outside `Allowed write paths` and content follows repo writing conventions.

---

## Execution notes (optional)

- What changed (short): Added Jordan NGO/SGO index, six organization profiles, updated README guidance, and populated ngos-sgos.csv with prioritized partners.
- Any open questions: None noted; revisit after first outreach to validate contacts and eligibility criteria.
- Follow-up tickets suggested: Add outreach tracking and meeting notes once partner responses arrive.
