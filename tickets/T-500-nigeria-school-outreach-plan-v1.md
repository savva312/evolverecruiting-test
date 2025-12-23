# T-500: Nigeria — School outreach plan (90-day) + operating cadence

Status: done
Type: content
Priority: P0
Dependencies: T-462
Claimed-by: run-2025-12-22T2042Z-codex-cli
Claimed-at: 2025-12-22T20:42Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Upgrade `countries/nigeria/go-to-market/schools-playbook/outreach.md` into a 90-day, city-by-city outreach plan (Lagos → Abuja → Port Harcourt) aligned to the Nigeria school calendar and the Tier1/Tier2 feeder roster.

---

## Context

- Current file is placeholder-level: `countries/nigeria/go-to-market/schools-playbook/outreach.md`
- Feeder roster lives in:
  - `countries/nigeria/entities/schools/index.md`
  - `countries/nigeria/data/entities/schools.csv`
- Calendar constraints: avoid WAEC/NECO exam months and end-of-term exam blocks (see `countries/nigeria/market/exams-and-calendar.md`).

---

## Allowed write paths

- `countries/nigeria/go-to-market/schools-playbook/outreach.md`
- `executions/T-449-nigeria-school-outreach-plan-v1/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket for status updates)
- `countries/**` (except `countries/nigeria/**`)

---

## Required outputs

- `countries/nigeria/go-to-market/schools-playbook/outreach.md`

---

## Acceptance criteria

- [x] Outreach plan includes: segmentation (Tier1/Tier2), city priorities, monthly cadence, and “who owns what” responsibilities
- [x] Includes at least 3 concrete outreach motions: counselor briefings, parent evenings, and student sessions (with clear CTAs + lead capture)
- [x] Includes a follow-up cadence (Day 0/2/7/14) and a “handoff to admissions” rule
- [x] Does not introduce PII; uses role-based contacts and references the CRM/trackers conceptually

## What changed

- Replaced the placeholder Nigeria school outreach doc with a calendar-aware 90-day plan sequenced **Lagos → Abuja → Port Harcourt**.
- Added Tier1/Tier2 segmentation, explicit ownership model, weekly operating cadence + SLAs, and standardized outreach motions with CTAs/lead capture.
- Defined follow-up rules (Day 0/2/7/14) and a clear handoff-to-admissions trigger to improve speed-to-lead and conversion.
