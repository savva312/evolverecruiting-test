# T-525: Jordan — sync fairs/events CSV to calendar + profiles (confirmed dates only)

Status: open
Type: data
Priority: P2
Dependencies: (none)
Claimed-by:
Claimed-at:
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Bring `countries/jordan/data/entities/fairs-events.csv` into alignment with the (verified) Jordan events calendar and profiles by:
- Ensuring each CSV row represents a real event occurrence with **confirmed** dates.
- Ensuring `event_id` naming, `country`, and `format` conform to the data dictionary.

---

## Context

Reference files:
- Calendar: `countries/jordan/entities/fairs-events/calendar-2025-2026.md`
- Profiles: `countries/jordan/entities/fairs-events/profiles/**`
- Dictionary: `countries/jordan/data/entities/fairs-events-dictionary.md` (note: `start_date` is required)

Important constraint:
- Do **not** add “estimated” dates to the CSV. If dates are not confirmed, keep the event in the calendar/profiles only until the organizer publishes official dates.

---

## Allowed write paths

- `tickets/T-455-jordan-events-csv-sync.md`
- `countries/jordan/data/entities/fairs-events.csv`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/jordan/**`)

---

## Required outputs

- `countries/jordan/data/entities/fairs-events.csv` updated and dictionary-compliant.

---

## Acceptance criteria

- [ ] Every row has valid `start_date`/`end_date` in `YYYY-MM-DD` and includes `as_of`.
- [ ] `country` is `JO` and `format` is one of `in-person|virtual|hybrid`.
- [ ] CSV only includes events with confirmed dates; estimated-only events remain outside the CSV.

