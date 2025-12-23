# T-148: Romania fairs and events research pack

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T20:56:29Z
Last-updated: 2025-12-20

---

## Goal

Develop a prioritized calendar and event profiles for Romanian student recruitment fairs, counselor events, and community gatherings over the next 12–18 months. Capture organizer details, timing, pricing, expected reach, and engagement recommendations for UNIC and UNIC Athens.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` sections on country-first layout and entities
  - `countries/romania/entities/README.md`
  - `countries/romania/entities/fairs-events/README.md`
- External constraints: stay within Romania scope; do not change protected control-plane files.
- Assumptions: prioritize Bucharest, Cluj-Napoca, Iași, Timișoara, and virtual events with strong Romanian participation; focus on 2025 dates and recurring 2026 editions.

---

## Allowed write paths

- `tickets/T-124-romania-fairs-events-research.md`
- `countries/romania/entities/fairs-events/**`
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

- `countries/romania/entities/fairs-events/calendar-2025-2026.md` updated with organizer, city/format, timing, pricing, target audience, and prioritization for UNIC vs UNIC Athens.
- At least five event one-pagers in `countries/romania/entities/fairs-events/profiles/*.md` detailing organizer contact/URL, timing, city or virtual format, audience size, pricing, expected lead quality, and engagement plan.
- `research/T-124/notes.md` (optional) summarizing sources and assumptions.

---

## Acceptance criteria

- [ ] All required output files exist at the specified paths with clear headings and structured details.
- [ ] No files are modified outside `Allowed write paths`.
- [ ] Calendar spans multiple cities/virtual options with prioritization (e.g., must-do, consider, monitor) for UNIC vs UNIC Athens.
- [ ] Event profiles include organizer contact/URL, timing (month/year), city or virtual format, target audience size/segment, pricing or range, expected lead quality, and recommended engagement steps.
- [ ] Content is concise, actionable, and consistent with the Romania fairs/events folder format.

---

## Execution notes (optional)

- What changed (short): Claimed and completed Romania fairs/events pack; refreshed calendar with 2025/2026 timing and priorities, added RIUF one-pager and updated EducationUSA contact details, and logged research sources.
- Any open questions: Need to confirm final 2025/2026 pricing and seminar availability with each organizer once dates are published.
- Follow-up tickets suggested: none
