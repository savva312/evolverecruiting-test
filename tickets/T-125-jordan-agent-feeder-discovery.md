# T-125: Jordan agent feeder discovery

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T20:32:31Z
Last-updated: 2025-12-20

---

## Goal

Assemble an extensive list of Jordanian education agents and counseling firms that can feed UNIC Nicosia and UNIC Athens, reflecting regional nuances, program demand, and compliance considerations.

---

## Context

- Follow the country-first layout in `AGENTS.md` and the repo map in `ROADMAP.md`.
- Use `countries/jordan/entities/agents/README.md` as the entry point; expand profiles in `countries/jordan/entities/agents/profiles/`.
- Prioritize agents with EU/Cyprus/Greece placement experience, strong medicine/healthcare and engineering pipelines, and coverage in Amman, Irbid, and international schools.
- Capture Jordan-specific considerations: MoE rules on advertising, scholarship expectations, reliance on sub-agents, and visa counseling practices for Cyprus/Greece.

---

## Allowed write paths

- `countries/jordan/entities/agents/**`
- `countries/jordan/data/entities/agents/**`
- `countries/jordan/reports/**`
- `agent runs/**`
- `research/**`
- `tickets/T-100-jordan-agent-feeder-discovery.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- Any `countries/**` path outside `countries/jordan/**`

---

## Required outputs

- `countries/jordan/entities/agents/feeder-candidates.md` providing a tiered roster with campus fit, program focus, city coverage, and risk/credibility notes.
- At least 10 updated or new profiles in `countries/jordan/entities/agents/profiles/*.md` covering ownership, credentials/associations, destination mix, conversion signals, commission terms, and compliance flags.
- `countries/jordan/entities/agents/README.md` refreshed to link the roster and profiles.

---

## Acceptance criteria

- [x] Required outputs exist and clearly differentiate UNIC vs UNIC Athens positioning.
- [x] Minimum 10 agents profiled with sources or marked assumptions and inclusion rationale.
- [x] Profiles include vetting notes (licensing/registration, sub-agent use, fee practices, scholarship expectations).
- [x] No files outside `Allowed write paths` are modified.
- [x] Ticket status is updated when claimed/done with a brief “What changed” entry.

---

## Execution notes (optional)

- What changed (short): Added tiered Jordan agent roster, refreshed agents index, and created/updated 12 agent profiles with UNIC Nicosia vs UNIC Athens fit, compliance, and fee notes.
- Any open questions: Verify current on-ground presence for IEC Abroad, Education Basket, Glinks, and StudyCo in Jordan; confirm MoE advertising approvals and fee disclosures before campaigns.
- Follow-up tickets suggested: If deeper due diligence is needed, create a compliance audit ticket for Jordan sub-agents and MoE approvals.
