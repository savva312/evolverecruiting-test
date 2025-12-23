# T-147: Lebanon fairs and events research pack

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20 20:56:47Z
Last-updated: 2025-12-20

---

## Goal

Build a prioritized 12–18 month calendar and event profiles for Lebanese student recruitment fairs, counselor events, and community gatherings. Capture organizer details, timing, pricing, expected reach, and engagement recommendations for UNIC and UNIC Athens.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` sections on country-first layout and entities
  - `countries/lebanon/entities/README.md`
  - `countries/lebanon/entities/fairs-events/README.md`
- External constraints: keep edits within Lebanon scope; avoid protected control-plane files.
- Assumptions: prioritize Beirut and major regional/virtual events with strong Lebanese participation; emphasize 2025 dates with recurring 2026 editions.

---

## Allowed write paths

- `tickets/T-122-lebanon-fairs-events-research.md`
- `countries/lebanon/entities/fairs-events/**`
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

- `countries/lebanon/entities/fairs-events/calendar-2025-2026.md` updated with organizer, city/format, timing, pricing, target audience, and prioritization for UNIC vs UNIC Athens.
- At least five event one-pagers in `countries/lebanon/entities/fairs-events/profiles/*.md` with organizer contact/URL, timing, city or virtual format, audience size, pricing, expected lead quality, and engagement plan.
- `research/T-122/notes.md` (optional) summarizing sources and assumptions.

---

## Acceptance criteria

- [ ] All required output files exist at the specified paths with clear headings and structured details.
- [ ] No files are modified outside `Allowed write paths`.
- [ ] Calendar spans multiple cities/virtual options with prioritization (e.g., must-do, consider, monitor) for UNIC vs UNIC Athens.
- [ ] Event profiles include organizer contact/URL, timing (month/year), city or virtual format, target audience size/segment, pricing or range, expected lead quality, and recommended engagement steps.
- [ ] Content is concise, actionable, and consistent with the Lebanon fairs/events folder format.

---

## Execution notes (optional)

- What changed (short): Calendar refreshed with 2025–2026 Lebanon priorities and 7 detailed event one-pagers (EducationUSA, Campus France, Access MBA/Masters, EBB, agent/partner roadshows, counselor/virtual fairs); research notes captured under `research/T-122/notes.md`.
- Any open questions: Await 2025/2026 date confirmations from EducationUSA, Campus France, Advent Group, and agent partners; pricing to be revalidated once prospectuses publish.
- Follow-up tickets suggested: Add ticket to log confirmed dates and booth bookings once organizer calendars release.
