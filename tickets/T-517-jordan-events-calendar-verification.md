# T-517: Jordan — verify and correct fairs/events calendar (2025–2026)

Status: open
Type: content
Priority: P1
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

Make `countries/jordan/entities/fairs-events/calendar-2025-2026.md` accurate and safe to use by:
- Verifying that each “Must-do/Consider/Monitor” event actually operates in Jordan (and in which cities).
- Correcting any incorrect venue/city/organizer details (remove Bulgaria-only venues like “Inter Expo Center” unless a source confirms Jordan).
- Adding source links for dates/packages; marking estimates explicitly as estimates.

---

## Context

The calendar currently includes signals that some entries were copied from other markets (e.g., Bulgaria venues/contacts).

Related assets:
- Event profiles under `countries/jordan/entities/fairs-events/profiles/**`
- Data table: `countries/jordan/data/entities/fairs-events.csv` (note: this requires confirmed dates)

---

## Allowed write paths

- `tickets/T-453-jordan-events-calendar-verification.md`
- `countries/jordan/entities/fairs-events/calendar-2025-2026.md`

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

- `countries/jordan/entities/fairs-events/calendar-2025-2026.md` updated with verified Jordan event details and sources.

---

## Acceptance criteria

- [ ] Every “Must-do/Consider/Monitor” row has at least 1 relevant source link.
- [ ] Any dates not yet published are clearly labeled as estimates (and are not presented as confirmed).
- [ ] Obvious non-Jordan venue/city artifacts are removed or corrected with sources.

