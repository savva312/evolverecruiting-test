# T-144: Nigeria fairs and events research pack

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-03-09
Last-updated: 2025-03-09

---

## Goal

Assemble a prioritized 12–18 month view of Nigerian student recruitment fairs, counselor gatherings, and community events relevant to UNIC and UNIC Athens. Provide organizer details, timing, pricing, expected reach, and engagement guidance to inform attendance and follow-up plans.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` sections on country-first layout and entities
  - `countries/nigeria/entities/README.md`
  - `countries/nigeria/entities/fairs-events/README.md`
- External constraints: keep edits within Nigeria scope; avoid protected control-plane files.
- Assumptions: prioritize Lagos, Abuja, Port Harcourt, and virtual events with strong Nigerian participation for 2025–2026 cycles.

---

## Allowed write paths

- `tickets/T-119-nigeria-fairs-events-research.md`
- `countries/nigeria/entities/fairs-events/**`
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

- `countries/nigeria/entities/fairs-events/calendar-2025-2026.md` updated with organizer, city/format, timing, pricing, target audience, and prioritization for UNIC vs UNIC Athens.
- At least five event one-pagers in `countries/nigeria/entities/fairs-events/profiles/*.md` capturing organizer contact/URL, timing, city or virtual format, audience size, pricing, expected lead quality, and engagement plan.
- `research/T-119/notes.md` (optional) summarizing sources and assumptions.

---

## Acceptance criteria

- [ ] All required output files exist at the specified paths with clear headings and structured details.
- [ ] No files are modified outside `Allowed write paths`.
- [ ] Calendar spans multiple cities/virtual options with prioritization (e.g., must-do, consider, monitor) for UNIC vs UNIC Athens.
- [ ] Event profiles include organizer contact/URL, timing (month/year), city or virtual format, target audience size/segment, pricing or range, expected lead quality, and recommended engagement steps.
- [ ] Content is concise, actionable, and consistent with the Nigeria fairs/events folder format.

---

## Execution notes (optional)

- What changed (short): Added a 2025–2026 Nigeria fairs/events calendar with priorities and pricing notes, plus five event one-pagers (IDP Expo, EducationUSA fairs, QS Discovery Lagos, Intake Study World, Maple Canada Fair). Logged sources/assumptions in `research/T-119/notes.md`.
- Any open questions: Confirm latest pricing and date releases with each organizer; Intake partner status impacts fees.
- Follow-up tickets suggested: None.
