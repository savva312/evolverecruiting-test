# T-137: Greece NGOs/SGOs landscape

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20 20:53 UTC
Last-updated: 2025-12-20

---

## Goal

Document the Greek NGO and SGO ecosystem that shapes scholarships, mobility support, and counseling for students considering UNIC/UNIC Athens. Deliver a country-specific index plus detailed organization profiles within `countries/greece/entities/ngos-sgos/` to guide partnership outreach.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` — repo map for country-first entity documentation.
  - `countries/greece/entities/ngos-sgos/README.md` — scope for NGO/SGO coverage in Greece.
- External constraints (if any): none noted.
- Assumptions (label them): prioritize organizations with national visibility or strong Athens/Thessaloniki presence influencing outbound study decisions.

---

## Allowed write paths

- `countries/greece/entities/ngos-sgos/**`
- `countries/greece/data/entities/**`
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
- `countries/nigeria/**`
- `countries/jordan/**`
- `countries/lebanon/**`
- `countries/romania/**`
- `countries/serbia/**`
- `UNIC/**`

---

## Required outputs

- `countries/greece/entities/ngos-sgos/index.md` summarizing priority NGOs/SGOs, thematic focus, geographies, and partnership status.
- `countries/greece/entities/ngos-sgos/profiles/*.md` (minimum 5 organizations) with a standard profile structure: overview, programs, target students, partnership fit, contacts/sources, and next steps.
- `countries/greece/entities/ngos-sgos/README.md` refreshed to link to the index and profile standards.
- `countries/greece/data/entities/ngos-sgos.csv` listing the same organizations with columns for name, scope, focus area, audience, partnership notes, status, and last-reviewed date.

---

## Acceptance criteria

- [x] Required files exist at the specified paths with Greece-specific content and functioning links to profiles.
- [x] At least five NGO/SGO profiles include mission, programs, reach, partnership fit, contacts/sources, and recommended next steps.
- [x] The index highlights prioritization and links to each profile file.
- [x] The CSV is populated, uses the specified columns, and rows align with the documented profiles.
- [x] No files were modified outside `Allowed write paths` and content follows repo writing conventions.

---

## Execution notes (optional)

- What changed (short): Added Greece NGO/SGO index, five detailed profiles, refreshed README, and populated NGO/SGO CSV for Greece.
- Any open questions: None; future additions can cover regional cultural associations and EU recovery calls.
- Follow-up tickets suggested: Add structured outreach tracker once initial contacts begin.
