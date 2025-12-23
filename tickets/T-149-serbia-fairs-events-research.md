# T-149: Serbia fairs and events research pack

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T20:56:09+00:00
Last-updated: 2025-12-20

---

## Goal

Create a prioritized 12–18 month calendar and event profiles for Serbian student recruitment fairs, counselor events, and community gatherings. Capture organizer details, timing, pricing, expected reach, and engagement recommendations for UNIC and UNIC Athens.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` sections on country-first layout and entities
  - `countries/serbia/entities/README.md`
  - `countries/serbia/entities/fairs-events/README.md`
- External constraints: keep edits within Serbia scope; do not modify protected control-plane files.
- Assumptions: prioritize Belgrade, Novi Sad, Niš, and virtual events with strong Serbian participation; focus on 2025 dates and recurring 2026 editions.

---

## Allowed write paths

- `tickets/T-125-serbia-fairs-events-research.md`
- `countries/serbia/entities/fairs-events/**`
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

- `countries/serbia/entities/fairs-events/calendar-2025-2026.md` updated with organizer, city/format, timing, pricing, target audience, and prioritization for UNIC vs UNIC Athens.
- At least five event one-pagers in `countries/serbia/entities/fairs-events/profiles/*.md` covering organizer contact/URL, timing, city or virtual format, audience size, pricing, expected lead quality, and engagement plan.
- `research/T-125/notes.md` (optional) summarizing sources and assumptions.

---

## Acceptance criteria

- [x] All required output files exist at the specified paths with clear headings and structured details.
- [x] No files are modified outside `Allowed write paths`.
- [x] Calendar spans multiple cities/virtual options with prioritization (e.g., must-do, consider, monitor) for UNIC vs UNIC Athens.
- [x] Event profiles include organizer contact/URL, timing (month/year), city or virtual format, target audience size/segment, pricing or range, expected lead quality, and recommended engagement steps.
- [x] Content is concise, actionable, and consistent with the Serbia fairs/events folder format.

---

## Execution notes (optional)

- What changed (short): Added 2025–2026 prioritized calendar with actions, refreshed six event profiles with timing/pricing/lead quality and engagement steps, and logged research notes in `research/T-125/notes.md`.
- Any open questions: Need confirmed 2025/2026 rate cards and final city lists from Integral, EBB, and Unify once published.
- Follow-up tickets suggested: Add confirmed dates/pricing once organizers release final calendars; capture post-event performance data to refine lead quality assumptions.
