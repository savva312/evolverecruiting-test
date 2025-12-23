# T-018: Bulgaria fairs and counselor events pack

Status: archived
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T15:30:54+00:00
Last-updated: 2025-12-20

---

## Goal

Create a prioritized calendar and profiles of Bulgarian recruitment fairs, counselor gatherings, and community events relevant to UNIC and UNIC Athens for the next 12–18 months. Deliver actionable details (organizers, dates, pricing, audience size, fit for Nicosia vs Athens, and follow-up actions) so the team can decide attendance, budget, and lead capture workflows.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` sections on repo scope and go-to-market folders
  - `entities/fairs-events/README.md` and `entities/fairs-events/profiles/README.md`
- External constraints: avoid modifying protected control-plane files unless a structure ticket authorizes it.
- Assumptions: focus on Bulgaria-hosted events or virtual events with strong Bulgarian attendance; prioritize 2025 dates with any known recurring 2026 editions.

---

## Allowed write paths

- `tickets/T-016-fairs-and-events-calendar.md`
- `entities/fairs-events/**`
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

- `entities/fairs-events/calendar-2025-2026.md` — calendar-style overview with timing, city, organizer, target audience, pricing, format, and recommendation.
- At least five event profiles in `entities/fairs-events/profiles/*.md` capturing organizer, timing, city, target audience, estimated leads, pricing, and recommended engagement plan for UNIC/UNIC Athens.
- `research/T-016/notes.md` (optional but recommended) if additional sources or assumptions need recording.

---

## Acceptance criteria

- [ ] All required output files exist at the specified paths with clear headings and structured details.
- [ ] No files are modified outside `Allowed write paths`.
- [ ] Event profiles include organizer contact/URL, timing (month/year), city or virtual format, target audience, estimated reach, cost (or price range), and UNIC vs UNIC Athens relevance with follow-up actions.
- [ ] Calendar includes at least five events spanning multiple cities/virtual, with prioritization (e.g., must-do, consider, monitor).
- [ ] Content is actionable, concise, and consistent with repo writing conventions.

---

## Execution notes (optional)

- What changed (short): Added 2025–2026 calendar, five prioritized event profiles, and research notes for pricing/lead assumptions.
- Any open questions: Confirm final 2025 dates and pricing with organizers; validate lead estimates with prior UNIC participation data.
- Follow-up tickets suggested: Add post-event reporting template and CRM mapping for fairs (new ticket needed).
