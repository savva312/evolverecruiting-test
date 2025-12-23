# T-123: Nigeria agent feeder discovery

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20
Last-updated: 2025-12-20

---

## Goal

Create an extensive, prioritized roster of Nigerian education agents and counseling firms that can reliably feed UNIC Nicosia and UNIC Athens, with explicit handling of compliance, payment, and visa-support nuances.

---

## Context

- Follow the country-first layout in `AGENTS.md` and the repo map in `ROADMAP.md`.
- Use `countries/nigeria/entities/agents/README.md` as the entry point; expand with detailed profiles under `countries/nigeria/entities/agents/profiles/`.
- Capture campus fit (UNIC vs UNIC Athens), program strengths (e.g., medicine, tech, business), and regional coverage across Lagos, Abuja, Port Harcourt, and diaspora pathways.
- Surface Nigerian-specific considerations: CAC registration, credibility signals, embassy/visa coaching practices, fee collection, and sub-agent models.

---

## Allowed write paths

- `countries/nigeria/entities/agents/**`
- `countries/nigeria/data/entities/agents/**`
- `countries/nigeria/reports/**`
- `agent runs/**`
- `research/**`
- `tickets/T-098-nigeria-agent-feeder-discovery.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- Any `countries/**` path outside `countries/nigeria/**`

---

## Required outputs

- `countries/nigeria/entities/agents/feeder-candidates.md` with a tiered list covering campus fit, specialization, region served, scholarship/discount expectations, and risk flags.
- At least 12 updated or new profiles in `countries/nigeria/entities/agents/profiles/*.md` detailing ownership, certifications/associations, destination mix, visa success signals, commission/payment terms, and compliance risks.
- `countries/nigeria/entities/agents/README.md` updated to link the roster and profiles.

---

## Acceptance criteria

- [ ] All required outputs exist and distinguish UNIC vs UNIC Athens positioning where relevant.
- [ ] Minimum 12 agents documented with sources or stated assumptions and clear inclusion rationale.
- [ ] Profiles include vetting notes (CAC registration, sub-agent chains, visa coaching approach, student fee policies).
- [ ] No files outside `Allowed write paths` are modified.
- [ ] Ticket status is updated when claimed/done with a brief “What changed” entry.

---

## Execution notes (optional)

- What changed (short): Added tiered feeder roster, created 12 Nigerian agent profiles with compliance/visa/commission details, and updated agents README links.
- Any open questions:
- Follow-up tickets suggested:
