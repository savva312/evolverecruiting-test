# T-145: Greece fairs and events research pack

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T20:55:36Z
Last-updated: 2025-12-20

---

## Goal

Compile a prioritized calendar and event profiles for Greek student recruitment fairs, counselor events, and community gatherings over the next 12–18 months. Document organizer details, timing, pricing, expected reach, and engagement recommendations for UNIC and UNIC Athens.

---

## Context

- Links to relevant repo files:
  - `ROADMAP.md` sections on country-first layout and entities
  - `countries/greece/entities/README.md`
  - `countries/greece/entities/fairs-events/README.md`
- External constraints: stay within Greece scope; do not touch protected control-plane files.
- Assumptions: prioritize Athens, Thessaloniki, Patras, and virtual events with high Greek participation for 2025–2026.

---

## Allowed write paths

- `tickets/T-120-greece-fairs-events-research.md`
- `countries/greece/entities/fairs-events/**`
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

- `countries/greece/entities/fairs-events/calendar-2025-2026.md` updated with organizer, city/format, timing, pricing, target audience, and prioritization for UNIC vs UNIC Athens.
- At least five event one-pagers in `countries/greece/entities/fairs-events/profiles/*.md` with organizer contact/URL, timing, city or virtual format, audience size, pricing, expected lead quality, and engagement plan.
- `research/T-120/notes.md` (optional) summarizing sources and assumptions.

---

## Acceptance criteria

- [ ] All required output files exist at the specified paths with clear headings and structured details.
- [ ] No files are modified outside `Allowed write paths`.
- [ ] Calendar covers multiple cities/virtual options with prioritization (e.g., must-do, consider, monitor) for UNIC vs UNIC Athens.
- [ ] Event profiles include organizer contact/URL, timing (month/year), city or virtual format, target audience size/segment, pricing or range, expected lead quality, and recommended engagement steps.
- [ ] Content is concise, actionable, and consistent with the Greece fairs/events folder format.

---

## Execution notes (optional)

- What changed (short): Added 2025–2026 Greece fairs/events calendar, created five event profiles (QS Discover Athens, Study UK, Fulbright/EducationUSA, CIS University Exploration Day, Study in Greece virtual fair), and logged research notes under `research/T-120/`.
- Any open questions: Need to confirm final 2025/26 dates and pricing when organizers publish schedules; verify if Fulbright adds Thessaloniki stop.
- Follow-up tickets suggested: Ticket for on-the-ground outreach to Athens/Thessaloniki schools during CIS/Study UK weeks and to set up Greek-language landing/CRM flows for fairs.
