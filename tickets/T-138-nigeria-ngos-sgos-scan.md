# T-138: Nigeria NGOs/SGOs landscape

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T20:54:41Z
Last-updated: 2025-12-20

---

## Goal

Capture the Nigerian NGO and SGO ecosystem that drives scholarships, mobility, and career readiness for students who may consider UNIC/UNIC Athens. Build an index and detailed organization profiles under `countries/nigeria/entities/ngos-sgos/` to steer partnership outreach.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` — repo map for country-first entity documentation.
  - `countries/nigeria/entities/ngos-sgos/README.md` — scope for NGO/SGO coverage in Nigeria.
- External constraints (if any): none noted.
- Assumptions (label them): include national and regional organizations with measurable impact on outbound student decisions or funding.

---

## Allowed write paths

- `countries/nigeria/entities/ngos-sgos/**`
- `countries/nigeria/data/entities/**`
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
- `countries/jordan/**`
- `countries/lebanon/**`
- `countries/romania/**`
- `countries/serbia/**`
- `UNIC/**`

---

## Required outputs

- `countries/nigeria/entities/ngos-sgos/index.md` summarizing priority NGOs/SGOs, thematic focus, geographic reach, and partnership status.
- `countries/nigeria/entities/ngos-sgos/profiles/*.md` (minimum 5 organizations) using a consistent profile structure: overview, programs, target students, partnership fit, contacts/sources, and next steps.
- `countries/nigeria/entities/ngos-sgos/README.md` refreshed to link to the index and profile conventions.
- `countries/nigeria/data/entities/ngos-sgos.csv` listing the same organizations with columns for name, scope, focus area, audience, partnership notes, status, and last-reviewed date.

---

## Acceptance criteria

- [x] Required files exist at the specified paths with Nigeria-specific content and functioning links to profiles.
- [x] At least five NGO/SGO profiles include mission, programs, reach, partnership fit, contacts/sources, and recommended next steps.
- [x] The index highlights prioritization and links to each profile file.
- [x] The CSV is populated, uses the specified columns, and rows align with the documented profiles.
- [x] No files were modified outside `Allowed write paths` and content follows repo writing conventions.

---

## Execution notes (optional)

- What changed (short): Added prioritized index, five detailed NGO/SGO profiles, and populated `ngos-sgos.csv` with aligned statuses and focus areas for Nigeria.
- Any open questions: None.
- Follow-up tickets suggested: Add additional regional NGOs and women-in-STEM accelerators after initial outreach feedback.
