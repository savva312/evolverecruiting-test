# T-141: Romania NGOs/SGOs landscape

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T20:54:52Z
Last-updated: 2025-12-20

---

## Goal

Map Romanian NGOs and SGOs that influence scholarships, mobility preparation, and counseling for students evaluating UNIC/UNIC Athens. Deliver an index and organization profiles inside `countries/romania/entities/ngos-sgos/` to direct partnership outreach.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` — repo map for country-first entity documentation.
  - `countries/romania/entities/ngos-sgos/README.md` — scope for NGO/SGO coverage in Romania.
- External constraints (if any): none noted.
- Assumptions (label them): include national and key regional organizations with demonstrated impact on outbound study funding or advising.

---

## Allowed write paths

- `countries/romania/entities/ngos-sgos/**`
- `countries/romania/data/entities/**`
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
- `countries/serbia/**`
- `UNIC/**`

---

## Required outputs

- `countries/romania/entities/ngos-sgos/index.md` summarizing priority NGOs/SGOs, thematic focus, geographies, and partnership status.
- `countries/romania/entities/ngos-sgos/profiles/*.md` (minimum 5 organizations) with a standard profile structure: overview, programs, target students, partnership fit, contacts/sources, and next steps.
- `countries/romania/entities/ngos-sgos/README.md` refreshed to link to the index and profile standards.
- `countries/romania/data/entities/ngos-sgos.csv` listing the same organizations with columns for name, scope, focus area, audience, partnership notes, status, and last-reviewed date.

---

## Acceptance criteria

- [x] Required files exist at the specified paths with Romania-specific content and functioning links to profiles.
- [x] At least five NGO/SGO profiles include mission, programs, reach, partnership fit, contacts/sources, and recommended next steps.
- [x] The index highlights prioritization and links to each profile file.
- [x] The CSV is populated, uses the specified columns, and rows align with the documented profiles.
- [x] No files were modified outside `Allowed write paths` and content follows repo writing conventions.

---

## Execution notes (optional)

- What changed (short): Added NGO/SGO index, six organization profiles, and populated data CSV aligned to profiles for Romania.
- Any open questions: None.
- Follow-up tickets suggested: Consider outreach-focused ticket to track responses and add contact outcomes.
