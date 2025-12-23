# T-523: Jordan — verify and correct fairs/events profiles (Jordan relevance + contacts)

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

Audit and correct Jordan fairs/events profiles under `countries/jordan/entities/fairs-events/profiles/**` so each profile:
- Clearly states whether the event has Jordan editions (and which cities).
- Uses correct venue/organizer info for Jordan (no unverified venue claims).
- Includes `last_verified` and sources.

---

## Context

Several Jordan event profile files appear to contain non-Jordan venue/phone details.

Profile folder:
- `countries/jordan/entities/fairs-events/profiles/`

---

## Allowed write paths

- `tickets/T-454-jordan-events-profiles-verification.md`
- `countries/jordan/entities/fairs-events/profiles/**`
- `countries/jordan/entities/fairs-events/profiles/README.md`

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

- Updated event profiles under `countries/jordan/entities/fairs-events/profiles/**` with corrected Jordan relevance, contacts, and sources.

---

## Acceptance criteria

- [ ] Every profile includes a `last_verified` date and at least 1 source link.
- [ ] Venue/city claims are sourced; remove/qualify any unsourced venue names.
- [ ] Jordan relevance is explicit (Jordan edition vs “regional/virtual only”).

