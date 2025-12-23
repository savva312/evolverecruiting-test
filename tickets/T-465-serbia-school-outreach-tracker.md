# T-465: Serbia — Add a school outreach tracker dataset and wire it into the outreach playbook

Status: done
Type: data
Priority: P1
Dependencies: (none)
Claimed-by: codex-run-20251222
Claimed-at: 2025-12-22
Completed-at: 2025-12-22
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Add a lightweight, non-PII outreach tracker CSV for Serbia schools and update the outreach playbook to use it (so the team can track outreach status without relying on ad-hoc notes).

---

## Context

- Playbook that currently references a “shared tracker”:
  - `countries/serbia/go-to-market/schools-playbook/outreach.md`
- Schools list exists and should be used as the baseline entity list:
  - `countries/serbia/data/entities/schools.csv`
  - `countries/serbia/entities/schools/README.md`
- Constraints:
  - No PII beyond professional emails already in the repo; do not add student-level data.

---

## Allowed write paths

- `countries/serbia/data/operations/school-outreach-tracker.csv`
- `countries/serbia/data/operations/school-outreach-tracker-dictionary.md`
- `countries/serbia/go-to-market/schools-playbook/outreach.md`
- `executions/**` (optional; notes only)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)

---

## Required outputs

- `countries/serbia/data/operations/school-outreach-tracker.csv`
- `countries/serbia/data/operations/school-outreach-tracker-dictionary.md`
- `countries/serbia/go-to-market/schools-playbook/outreach.md`

---

## Acceptance criteria

- [x] Tracker CSV exists and is populated with one row per high-priority school in `countries/serbia/data/entities/schools.csv`.
- [x] Tracker schema is documented in the dictionary file (columns include: `school_id`, `stage`, `last_touch_date`, `next_touch_date`, `owner`, `notes`, `as_of`).
- [x] Outreach playbook links to the tracker and defines the rule: “update tracker after every touch”.
- [x] No PII beyond school-level professional contacts; no student names/emails/phones.
- [x] No edits outside allowed write paths.

---

## What changed
- Added operational tracker + dictionary + wired playbook to enforce usage cadence per acceptance criteria.
