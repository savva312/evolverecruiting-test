# T-142: Serbia NGOs/SGOs landscape

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T20:55:18Z
Last-updated: 2025-12-20

---

## Goal

Document Serbian NGOs and SGOs that impact scholarships, mobility assistance, and counseling for prospective UNIC/UNIC Athens students. Create an index and organization profiles under `countries/serbia/entities/ngos-sgos/` to steer partnership outreach.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` — repo map for country-first entity documentation.
  - `countries/serbia/entities/ngos-sgos/README.md` — scope for NGO/SGO coverage in Serbia.
- External constraints (if any): none noted.
- Assumptions (label them): include national and city-level organizations with meaningful influence on outbound study funding or advising.

---

## Allowed write paths

- `countries/serbia/entities/ngos-sgos/**`
- `countries/serbia/data/entities/**`
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
- `countries/jordan/**`
- `countries/lebanon/**`
- `countries/romania/**`
- `UNIC/**`

---

## Required outputs

- `countries/serbia/entities/ngos-sgos/index.md` summarizing priority NGOs/SGOs, thematic focus, geographies, and partnership status.
- `countries/serbia/entities/ngos-sgos/profiles/*.md` (minimum 5 organizations) with a standard profile structure: overview, programs, target students, partnership fit, contacts/sources, and next steps.
- `countries/serbia/entities/ngos-sgos/README.md` refreshed to link to the index and profile standards.
- `countries/serbia/data/entities/ngos-sgos.csv` listing the same organizations with columns for name, scope, focus area, audience, partnership notes, status, and last-reviewed date.

---

## Acceptance criteria

- [ ] Required files exist at the specified paths with Serbia-specific content and functioning links to profiles.
- [ ] At least five NGO/SGO profiles include mission, programs, reach, partnership fit, contacts/sources, and recommended next steps.
- [ ] The index highlights prioritization and links to each profile file.
- [ ] The CSV is populated, uses the specified columns, and rows align with the documented profiles.
- [ ] No files were modified outside `Allowed write paths` and content follows repo writing conventions.

---

## Execution notes (optional)

- What changed (short): Added Serbia NGO/SGO index, six detailed profiles, refreshed README guidance, and populated NGOs/SGOs CSV to match documented organizations.
- Any open questions: None currently.
- Follow-up tickets suggested: Consider a joint webinar pipeline ticket once first partner intros are scheduled.
