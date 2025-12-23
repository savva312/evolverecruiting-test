# T-140: Lebanon NGOs/SGOs landscape

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T21:32:24Z
Last-updated: 2025-12-20

---

## Goal

Capture the Lebanese NGO and SGO landscape that shapes scholarships, mobility support, and counseling for prospective UNIC/UNIC Athens students. Build an index and detailed organization profiles within `countries/lebanon/entities/ngos-sgos/` to steer partnership outreach and sponsorship opportunities.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` — repo map for country-first entity documentation.
  - `countries/lebanon/entities/ngos-sgos/README.md` — scope for NGO/SGO coverage in Lebanon.
- External constraints (if any): none noted.
- Assumptions (label them): include national organizations plus diaspora/aid groups materially affecting outbound study funding or advising.

---

## Allowed write paths

- `countries/lebanon/entities/ngos-sgos/**`
- `countries/lebanon/data/entities/**`
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
- `countries/romania/**`
- `countries/serbia/**`
- `UNIC/**`

---

## Required outputs

- `countries/lebanon/entities/ngos-sgos/index.md` summarizing priority NGOs/SGOs, thematic focus, geographies, and partnership status.
- `countries/lebanon/entities/ngos-sgos/profiles/*.md` (minimum 5 organizations) with a standard profile structure: overview, programs, target students, partnership fit, contacts/sources, and next steps.
- `countries/lebanon/entities/ngos-sgos/README.md` refreshed to link to the index and profile standards.
- `countries/lebanon/data/entities/ngos-sgos.csv` listing the same organizations with columns for name, scope, focus area, audience, partnership notes, status, and last-reviewed date.

---

## Acceptance criteria

- [x] Required files exist at the specified paths with Lebanon-specific content and functioning links to profiles.
- [x] At least five NGO/SGO profiles include mission, programs, reach, partnership fit, contacts/sources, and recommended next steps.
- [x] The index highlights prioritization and links to each profile file.
- [x] The CSV is populated, uses the specified columns, and rows align with the documented profiles.
- [x] No files were modified outside `Allowed write paths` and content follows repo writing conventions.

---

## Execution notes (optional)

- What changed (short): Refreshed Lebanon NGO/SGO README and index with scoped priorities, confirmed five detailed profiles, updated the data dictionary, and rebuilt ngos-sgos.csv with scope/focus/audience/status columns aligned to the profiles.
- Any open questions: None noted.
- Follow-up tickets suggested: Extend coverage to regional NGOs (Bekaa/Baalbek, Mount Lebanon) and embassy cultural centers once outbound advising roles are confirmed.
