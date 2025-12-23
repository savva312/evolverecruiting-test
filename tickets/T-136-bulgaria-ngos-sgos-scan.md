# T-136: Bulgaria NGOs/SGOs landscape

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T20:53:36Z
Last-updated: 2025-12-20

---

## Goal

Map the Bulgarian NGO and SGO landscape that influences student mobility, scholarships, and counseling to prioritize partnership outreach for UNIC/UNIC Athens. Produce a country-specific index and a set of organization profiles inside the `countries/bulgaria/entities/ngos-sgos/` subtree.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` — repo map for country-first entity documentation.
  - `countries/bulgaria/entities/ngos-sgos/README.md` — scope and placement for NGO/SGO research.
- External constraints (if any): none noted.
- Assumptions (label them): focus on organizations with national or regional reach that impact Bulgarian students considering study abroad.

---

## Allowed write paths

- `countries/bulgaria/entities/ngos-sgos/**`
- `countries/bulgaria/data/entities/**`
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
- `countries/greece/**`
- `countries/nigeria/**`
- `countries/jordan/**`
- `countries/lebanon/**`
- `countries/romania/**`
- `countries/serbia/**`
- `UNIC/**`

---

## Required outputs

- `countries/bulgaria/entities/ngos-sgos/index.md` summarizing priority NGOs/SGOs, their focus areas, and partnership status.
- `countries/bulgaria/entities/ngos-sgos/profiles/*.md` (minimum 5 organizations) using a consistent profile structure: overview, programs, target students, partnership fit, contact/sources, next steps.
- `countries/bulgaria/entities/ngos-sgos/README.md` updated to reference the index and profile conventions.
- `countries/bulgaria/data/entities/ngos-sgos.csv` capturing the same organizations with columns for name, scope, focus area, audience, partnership notes, status, and last-reviewed date.

---

## Acceptance criteria

- [ ] All required files exist at the specified paths with Bulgaria-specific content and working internal links.
- [ ] At least five NGO/SGO profiles are completed with mission, programs, reach, partnership fit, contacts/sources, and recommended next steps.
- [ ] The index highlights prioritization and links to each profile file.
- [ ] The CSV is populated, uses the specified columns, and rows align with the documented profiles.
- [ ] No files were modified outside `Allowed write paths` and the content follows repo writing conventions.

---

## Execution notes (optional)

- What changed (short): Added Bulgaria NGO/SGO index, six organization profiles, and populated the NGOs/SGOs CSV aligned to the data dictionary; refreshed README to point to index and data.
- Any open questions: Confirm direct contact emails for each organization (profiles reference contact pages rather than individuals).
- Follow-up tickets suggested: Consider outreach log/CRM capture for NGO/SGO engagements once initial meetings are scheduled.
