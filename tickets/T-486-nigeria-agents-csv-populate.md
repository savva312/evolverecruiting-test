# T-486: Nigeria — Populate `agents.csv` from existing profiles

Status: done
Type: data
Priority: P1
Dependencies: (none)
Claimed-by: evoticketresolver_vpkwx02e
Claimed-at: 2025-12-22T20:37:59Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Turn `countries/nigeria/data/entities/agents.csv` from header-only into a usable, **non-PII** structured roster that aligns to the existing Nigeria agent profiles and the tiered roster.

---

## Context

- `countries/nigeria/data/entities/agents.csv` is currently header-only.
- Existing Nigeria agent assets:
  - Tiered roster: `countries/nigeria/entities/agents/feeder-candidates.md`
  - Profiles folder: `countries/nigeria/entities/agents/profiles/`
  - Data dictionary: `countries/nigeria/data/entities/agents-dictionary.md`
- Repo constraint: avoid storing personal data (use role-based inboxes only; no personal mobiles; leave contact fields blank if only personal contacts are available).

---

## Allowed write paths

- `countries/nigeria/data/entities/agents.csv`
- `countries/nigeria/data/entities/agents-dictionary.md` (only if needed to clarify non-PII expectations)
- `executions/T-445-nigeria-agents-csv-populate/**` (optional notes)

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

- `countries/nigeria/data/entities/agents.csv`

---

## Acceptance criteria

- [x] `countries/nigeria/data/entities/agents.csv` contains **≥ 12 agent rows** covering the currently-profiled Nigeria agents in `countries/nigeria/entities/agents/profiles/`
- [x] All rows include: `agent_id`, `name`, `region`, `services`, `primary_markets`, `as_of`
- [x] `services` and `primary_markets` follow the dictionary conventions (semicolon-separated; ISO country codes for markets)
- [x] No personal emails/phone numbers are added; `contact_name`/`contact_email` are blank or role-based only (e.g., `info@`, `admissions@`)
- [x] CSV remains valid UTF-8 with a single header row; no stray commas/newlines inside fields

## What changed

- Populated `countries/nigeria/data/entities/agents.csv` with 12 non-PII agent rows sourced from existing Nigeria agent profiles.
- Clarified non-PII expectations in `countries/nigeria/data/entities/agents-dictionary.md` for `contact_name` / `contact_email`.
