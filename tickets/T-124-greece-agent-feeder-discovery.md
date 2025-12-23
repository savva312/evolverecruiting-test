# T-124: Greece agent feeder discovery

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-05-27
Last-updated: 2025-05-27

---

## Goal

Develop a comprehensive roster of Greek education agents and counseling firms that can drive enrollments to UNIC Nicosia and UNIC Athens, including Athens-specific feeder logic and cross-border placement patterns.

---

## Context

- Follow the country-first layout in `AGENTS.md` and the repo map in `ROADMAP.md`.
- Use `countries/greece/entities/agents/README.md` as the entry point; expand with detailed profiles under `countries/greece/entities/agents/profiles/`.
- Account for domestic vs outbound counseling, relationships with Greek private schools, and pathways to Cyprus and wider EU destinations.
- Capture Athens-campus positioning (proximity, Greek-language support, cost) versus Nicosia and note any licensing/advertising requirements for Greek agents.

---

## Allowed write paths

- `countries/greece/entities/agents/**`
- `countries/greece/data/entities/agents/**`
- `countries/greece/reports/**`
- `agent runs/**`
- `research/**`
- `tickets/T-099-greece-agent-feeder-discovery.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- Any `countries/**` path outside `countries/greece/**`

---

## Required outputs

- `countries/greece/entities/agents/feeder-candidates.md` with a tiered roster showing campus fit, program strengths, target student profiles, and relationship status.
- At least 10 updated or new profiles in `countries/greece/entities/agents/profiles/*.md` covering ownership, credentials, destination mix, conversion history, commission norms, and compliance notes (licensing/advertising).
- `countries/greece/entities/agents/README.md` refreshed to link the roster and profiles.

---

## Acceptance criteria

- [x] Required outputs exist with clear UNIC vs UNIC Athens positioning.
- [x] Minimum 10 agents profiled with sources or marked assumptions and rationale for inclusion/tiering.
- [x] Profiles include vetting notes (licensing status, sub-agents, fee structures) and campus-specific fit.
- [x] No files outside `Allowed write paths` are modified.
- [x] Ticket status is updated when claimed/done with a brief “What changed” entry.

---

## Execution notes (optional)

- What changed (short): Rebuilt Greece agent roster from December 2025 shortlist, added/updated 12+ profiles with campus-specific fit and compliance notes, and captured Cyprus-intent vs Athens conversion priorities.
- Any open questions: Validate licensing/fee transparency for the new Cyprus-intent partners and multi-destination engines before contracting; confirm commission schedules per intake.
- Follow-up tickets suggested: (none)
