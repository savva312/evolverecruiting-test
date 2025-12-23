# T-143: Bulgaria fairs and events research pack

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: assistant-2025-12-20
Claimed-at: 2025-12-20
Last-updated: 2025-12-20

---

## Goal

Produce an actionable 12–18 month calendar and prioritized event profiles for Bulgarian student recruitment fairs, counselor gatherings, and community events relevant to UNIC and UNIC Athens. Capture organizer details, timing, pricing, expected reach, and recommended engagement so the team can decide attendance and follow-up plans.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` sections on country-first layout and entities
  - `countries/bulgaria/entities/README.md`
  - `countries/bulgaria/entities/fairs-events/README.md`
- External constraints: keep changes within Bulgaria scope; do not modify protected control-plane files.
- Assumptions: focus on Bulgaria-hosted or virtual events with strong Bulgarian attendance; prioritize 2025 dates and recurring 2026 editions.

---

## Allowed write paths

- `tickets/T-118-bulgaria-fairs-events-research.md`
- `countries/bulgaria/entities/fairs-events/**`
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

- `countries/bulgaria/entities/fairs-events/calendar-2025-2026.md` updated with organizer, city/format, timing, pricing, target audience, and recommended priority for UNIC vs UNIC Athens.
- At least five event one-pagers in `countries/bulgaria/entities/fairs-events/profiles/*.md` with organizer contact/URL, timing, city or virtual format, audience size, pricing, and engagement plan.
- `research/T-118/notes.md` (optional) summarizing sources and assumptions.

---

## Acceptance criteria

- [x] All required output files exist at the specified paths with clear headings and structured event details.
- [x] No files are modified outside `Allowed write paths`.
- [x] Calendar spans multiple cities/virtual options and includes prioritization (e.g., must-do, consider, monitor) for UNIC vs UNIC Athens.
- [x] Event profiles include organizer contact/URL, timing (month/year), city or virtual format, target audience size/segment, pricing or range, expected lead quality, and recommended engagement steps.
- [x] Content is concise, actionable, and consistent with existing fairs/events format in the Bulgaria tree.

---

## Execution notes (optional)

- What changed (short): Updated 2025–2026 Bulgaria fairs calendar with added QS Discover, SRT Fairs, and Begin Group; created new one-pagers and research notes; confirmed priorities and actions for UNIC vs UNIC Athens.
- Any open questions: Confirm final organizer rate cards and 2026 dates once published.
- Follow-up tickets suggested: None.
