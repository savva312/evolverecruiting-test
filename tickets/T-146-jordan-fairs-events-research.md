# T-146: Jordan fairs and events research pack

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T20:55:40Z
Last-updated: 2025-12-20

---

## Goal

Deliver a prioritized calendar and event profiles for Jordanian student recruitment fairs, counselor events, and community gatherings for the next 12–18 months. Capture organizer details, timing, pricing, expected reach, and engagement recommendations for UNIC and UNIC Athens.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` sections on country-first layout and entities
  - `countries/jordan/entities/README.md`
  - `countries/jordan/entities/fairs-events/README.md`
- External constraints: limit changes to Jordan scope; avoid protected control-plane files.
- Assumptions: focus on Amman and regional/virtual events with strong Jordanian participation; emphasize 2025 dates with recurring 2026 editions.

---

## Allowed write paths

- `tickets/T-121-jordan-fairs-events-research.md`
- `countries/jordan/entities/fairs-events/**`
- `research/**`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`

---

## Required outputs

- `countries/jordan/entities/fairs-events/calendar-2025-2026.md` updated with organizer, city/format, timing, pricing, target audience, and prioritization for UNIC vs UNIC Athens.
- At least five event one-pagers in `countries/jordan/entities/fairs-events/profiles/*.md` covering organizer contact/URL, timing, city or virtual format, audience size, pricing, expected lead quality, and engagement plan.
- `research/T-121/notes.md` (optional) summarizing sources and assumptions.

---

## Acceptance criteria

- [x] All required output files exist at the specified paths with clear headings and structured details.
- [x] No files are modified outside `Allowed write paths`.
- [x] Calendar spans multiple cities/virtual options with prioritization (e.g., must-do, consider, monitor) for UNIC vs UNIC Athens.
- [x] Event profiles include organizer contact/URL, timing (month/year), city or virtual format, target audience size/segment, pricing or range, expected lead quality, and recommended engagement steps.
- [x] Content is concise, actionable, and consistent with the Jordan fairs/events folder format.

---

## Execution notes (optional)

- What changed (short): Updated Jordan 2025–2026 fairs calendar, added QS and IDP event profiles, refreshed action plans, and captured research notes.
- Any open questions: Confirm final 2025/2026 dates and rate cards with Integral, EBB, QS, IDP, and Unify once released.
- Follow-up tickets suggested: None (monitor for new counselor forums or emerging fairs).
