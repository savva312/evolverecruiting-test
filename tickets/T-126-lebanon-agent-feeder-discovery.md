# T-126: Lebanon agent feeder discovery

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T20:31:31Z
Last-updated: 2025-12-20

---

## Goal

Compile a deep roster of Lebanese education agents and counseling firms that can feed UNIC Nicosia and UNIC Athens, capturing Beirut and regional coverage plus compliance and financial nuances.

---

## Context

- Follow the country-first layout in `AGENTS.md` and the repo map in `ROADMAP.md`.
- Use `countries/lebanon/entities/agents/README.md` as the entry point; expand with detailed profiles under `countries/lebanon/entities/agents/profiles/`.
- Map agents serving Beirut, Tripoli, Saida, and francophone/Anglophone school networks; emphasize healthcare, business, and tech pipelines.
- Capture Lebanon-specific considerations: currency/payment handling, scholarship/discount sensitivity, visa guidance for Cyprus/Greece, and advertising/representation norms.

---

## Allowed write paths

- `countries/lebanon/entities/agents/**`
- `countries/lebanon/data/entities/agents/**`
- `countries/lebanon/reports/**`
- `agent runs/**`
- `research/**`
- `tickets/T-101-lebanon-agent-feeder-discovery.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- Any `countries/**` path outside `countries/lebanon/**`

---

## Required outputs

- `countries/lebanon/entities/agents/feeder-candidates.md` outlining a tiered roster with campus fit, program focus, city coverage, and risk/credibility notes.
- At least 10 updated or new profiles in `countries/lebanon/entities/agents/profiles/*.md` detailing ownership, credentials/associations, destination mix, conversion indicators, commission/payment terms (including FX handling), and compliance flags.
- `countries/lebanon/entities/agents/README.md` refreshed to link the roster and profiles.

---

## Acceptance criteria

- [ ] Required outputs exist with explicit UNIC vs UNIC Athens positioning where relevant.
- [ ] Minimum 10 agents documented with sources or stated assumptions and rationale for inclusion/tiering.
- [ ] Profiles include vetting notes (licensing, sub-agent chains, fee and FX practices, visa guidance approach).
- [ ] No files outside `Allowed write paths` are modified.
- [ ] Ticket status is updated when claimed/done with a brief “What changed” entry.

---

## Execution notes (optional)

- What changed (short): Created tiered Lebanon agent roster, added/updated 15 agent profiles with UNIC vs UNIC Athens positioning, FX/commission notes, and compliance vetting flags.
- Any open questions: Validate licenses and counselor credentials for Tier C prospects before engagement.
- Follow-up tickets suggested: Add intake tracking template and data model for agent performance (applications→offers→enrolments) under `countries/lebanon/data/entities/agents/`.
