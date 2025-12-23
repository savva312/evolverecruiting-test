# T-120: Bulgaria agent feeder discovery

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20 20:31:15Z
Last-updated: 2025-12-20

---

## Goal

Produce an extensive, prioritized roster of Bulgarian education agents and counseling firms that can reliably feed UNIC Nicosia and UNIC Athens, capturing country-specific compliance and commercial nuances.

---

## Context

- Follow the country-first layout in `AGENTS.md` and the repo map in `ROADMAP.md`.
- Build on `countries/bulgaria/entities/agents/README.md` and any existing profiles in `countries/bulgaria/entities/agents/profiles/`.
- Distinguish campus fit (UNIC vs UNIC Athens), popular outbound destinations for Bulgarian students, and EU vs non-EU placement experience.
- Note Bulgarian regulatory considerations (e.g., commission norms, sub-agent use, marketing practices) that affect partnership setup.

---

## Allowed write paths

- `countries/bulgaria/entities/agents/**`
- `countries/bulgaria/data/entities/agents/**`
- `countries/bulgaria/reports/**`
- `agent runs/**`
- `research/**`
- `tickets/T-097-bulgaria-agent-feeder-discovery.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- Any `countries/**` path outside `countries/bulgaria/**`

---

## Required outputs

- `countries/bulgaria/entities/agents/feeder-candidates.md` summarizing a tiered list (priority, watchlist) with campus fit, program strengths, office locations, and partnership risks.
- At least 12 updated or new agent profiles in `countries/bulgaria/entities/agents/profiles/*.md` with ownership/credibility signals, certifications, track record to EU/Cyprus/Greece, service mix, commission expectations, and compliance notes.
- `countries/bulgaria/entities/agents/README.md` refreshed with navigation to the roster and profiles.

---

## Acceptance criteria

- [ ] All required outputs exist with campus-specific notes for UNIC and UNIC Athens.
- [ ] Profiles cite sources or mark assumptions, and include contact placeholders and vetting flags (e.g., sub-agent chains, fee practices).
- [ ] At least 12 agents are covered, with clear rationale for inclusion and tiering.
- [ ] No files outside `Allowed write paths` are modified.
- [ ] Ticket status is updated when claimed/done with a brief “What changed” entry.

---

## Execution notes (optional)

- What changed (short): Added tiered feeder roster with campus-specific fit notes, refreshed existing profiles, and created seven new agent dossiers to reach 12 total candidates.
- Any open questions:
- Follow-up tickets suggested:
