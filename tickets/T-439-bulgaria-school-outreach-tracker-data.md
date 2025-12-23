# T-439: Bulgaria — add school outreach tracker dataset (no-PII ops table)

Status: done
Type: data
Priority: P1
Dependencies: (none)
Claimed-by: evoticketresolver_j605n8qs
Claimed-at: 2025-12-22T17:52:05Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Add a structured, no-PII outreach tracker so the Bulgaria team can manage school engagement consistently across trips and staff turnover.

---

## Context

We already have rich school profiles and a schools dataset:
- Profiles: `countries/bulgaria/entities/schools/profiles/**`
- Index + CSV: `countries/bulgaria/entities/schools/index.md`, `countries/bulgaria/data/entities/schools.csv`

What’s missing is an operational log that tracks interactions and next steps without storing sensitive personal data.

---

## Allowed write paths

- `tickets/T-439-bulgaria-school-outreach-tracker-data.md`
- `countries/bulgaria/data/operations/school-outreach-tracker.csv`
- `countries/bulgaria/data/operations/school-outreach-tracker-dictionary.md`
- `countries/bulgaria/go-to-market/schools-playbook/outreach.md` (optional: add a link to the tracker)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/bulgaria/**`)

---

## Required outputs

- `countries/bulgaria/data/operations/school-outreach-tracker.csv` created with headers only (no PII) and at least one example row (optional).
- `countries/bulgaria/data/operations/school-outreach-tracker-dictionary.md` created defining each field and explicitly stating “no personal phone numbers, no DOB/passport/ID”.

---

## Acceptance criteria

- [x] Tracker supports linking to `school_id` from `countries/bulgaria/data/entities/schools.csv` without duplicating school data.
- [x] Dictionary includes a “PII policy” section for this table.
- [x] No files outside `Allowed write paths` were modified.

## What changed (2025-12-22)

- Added the no-PII operational dataset: `countries/bulgaria/data/operations/school-outreach-tracker.csv`.
- Added the schema + PII policy: `countries/bulgaria/data/operations/school-outreach-tracker-dictionary.md`.
- Linked the tracker from the Bulgaria school outreach playbook: `countries/bulgaria/go-to-market/schools-playbook/outreach.md`.
