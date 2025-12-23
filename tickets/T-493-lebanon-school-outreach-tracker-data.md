# T-493: Lebanon — add school outreach tracker dataset (no-PII ops table)

Status: done
Type: data
Priority: P1
Dependencies: (none)
Claimed-by: evoticketresolver_0l06hbta
Claimed-at: 2025-12-22T20:40:39Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Add a structured, no-PII outreach tracker so the Lebanon team can manage school engagement consistently across trips and staff turnover.

---

## Context

We already have:
- School profiles: `countries/lebanon/entities/schools/profiles/**`
- Schools dataset: `countries/lebanon/data/entities/schools.csv`
- Outreach playbook that currently references ad-hoc tracking in `/executions/`:
  - `countries/lebanon/go-to-market/schools-playbook/outreach.md`

What’s missing is an operational log that tracks outreach touches and next steps without storing sensitive personal data.

---

## Allowed write paths

- `tickets/T-493-lebanon-school-outreach-tracker-data.md`
- `countries/lebanon/data/operations/school-outreach-tracker.csv`
- `countries/lebanon/data/operations/school-outreach-tracker-dictionary.md`
- `countries/lebanon/go-to-market/schools-playbook/outreach.md` (optional: add a link to the tracker)

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

- `countries/lebanon/data/operations/school-outreach-tracker.csv` created with headers and (optionally) one example row.
- `countries/lebanon/data/operations/school-outreach-tracker-dictionary.md` created defining each field and explicitly stating “no personal phone numbers, no DOB/passport/ID”.

---

## Acceptance criteria

- [x] Tracker supports linking to `school_id` from `countries/lebanon/data/entities/schools.csv` without duplicating school master data.
- [x] Dictionary includes a “PII policy” section for this table.
- [x] No files outside `Allowed write paths` were modified.

---

## Execution notes

- What changed (short): Added a no-PII school outreach tracker CSV + data dictionary for Lebanon, and linked the tracker from the Lebanon schools outreach playbook.
