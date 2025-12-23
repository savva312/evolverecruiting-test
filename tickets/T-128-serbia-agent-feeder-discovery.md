# T-128: Serbia agent feeder discovery

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T20:31:56Z
Last-updated: 2025-12-20

---

## Goal

Build an extensive roster of Serbian education agents and counseling firms that can feed UNIC Nicosia and UNIC Athens, including regional coverage and compliance nuances.

---

## Context

- Follow the country-first layout in `AGENTS.md` and the repo map in `ROADMAP.md`.
- Use `countries/serbia/entities/agents/README.md` as the entry point; expand with detailed profiles under `countries/serbia/entities/agents/profiles/`.
- Prioritize agents with EU/Cyprus/Greece placement experience and pipelines in Belgrade, Novi Sad, Niš, and international schools.
- Capture Serbia-specific considerations: commission/fee norms, sub-agent networks, recognition/licensure guidance for medicine/health, and marketing/advertising rules.

---

## Allowed write paths

- `countries/serbia/entities/agents/**`
- `countries/serbia/data/entities/agents/**`
- `countries/serbia/reports/**`
- `agent runs/**`
- `research/**`
- `tickets/T-103-serbia-agent-feeder-discovery.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- Any `countries/**` path outside `countries/serbia/**`

---

## Required outputs

- `countries/serbia/entities/agents/feeder-candidates.md` detailing a tiered roster with campus fit, program strengths, city coverage, and risk/credibility notes.
- At least 10 updated or new profiles in `countries/serbia/entities/agents/profiles/*.md` covering ownership, credentials/associations, destination mix, conversion signals, commission/payment terms, and compliance flags.
- `countries/serbia/entities/agents/README.md` refreshed to link the roster and profiles.

---

## Acceptance criteria

- [x] Required outputs exist with explicit UNIC vs UNIC Athens positioning where relevant.
- [x] Minimum 10 agents documented with sources or stated assumptions and rationale for inclusion/tiering.
- [x] Profiles include vetting notes (licensing/registration, sub-agent use, fee practices, recognition/licensure guidance needs).
- [x] No files outside `Allowed write paths` are modified.
- [x] Ticket status is updated when claimed/done with a brief “What changed” entry.

---

## Execution notes (optional)

- What changed (short): Added tiered roster and 10 agent profiles with UNIC Athens/Nicosia positioning, compliance notes, and city coverage; refreshed agents README.
- Any open questions: Need to validate application/start volumes, current accreditations, and confirmed URLs for Global Education Consultants Serbia and SAT Agency before contracting.
- Follow-up tickets suggested: Add Serbian-language one-pagers/webinar decks for Athens (business/CS/hospitality) and Nicosia (medicine/health/cybersecurity); create compliance checklist for vetting Serbia-based sub-agents/portals.
