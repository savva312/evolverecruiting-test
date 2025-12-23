# T-127: Romania agent feeder discovery

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T20:34:47Z
Last-updated: 2025-12-20

---

## Goal

Develop an extensive list of Romanian education agents and counseling firms that can feed UNIC Nicosia and UNIC Athens, with attention to regional coverage, program demand, and regulatory nuances.

---

## Context

- Follow the country-first layout in `AGENTS.md` and the repo map in `ROADMAP.md`.
- Use `countries/romania/entities/agents/README.md` as the entry point; add detailed profiles under `countries/romania/entities/agents/profiles/`.
- Map agents serving Bucharest, Cluj, Iași, Timișoara, and international school networks; emphasize medicine, business, IT, and design pipelines.
- Capture Romania-specific considerations: EU vs non-EU placement balance, commission expectations, advertising rules, and any sub-agent or franchise models.

---

## Allowed write paths

- `countries/romania/entities/agents/**`
- `countries/romania/data/entities/agents/**`
- `countries/romania/reports/**`
- `agent runs/**`
- `research/**`
- `tickets/T-102-romania-agent-feeder-discovery.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- Any `countries/**` path outside `countries/romania/**`

---

## Required outputs

- `countries/romania/entities/agents/feeder-candidates.md` summarizing a tiered roster with campus fit, program focus, city coverage, and risk/credibility notes.
- At least 10 updated or new profiles in `countries/romania/entities/agents/profiles/*.md` covering ownership, credentials/associations, destination mix, conversion history, commission/payment terms, and compliance flags.
- `countries/romania/entities/agents/README.md` refreshed to link the roster and profiles.

---

## Acceptance criteria

- [x] Required outputs exist with explicit UNIC vs UNIC Athens positioning where relevant.
- [x] Minimum 10 agents documented with sources or stated assumptions and rationale for inclusion/tiering.
- [x] Profiles include vetting notes (licensing/registration, sub-agent use, advertising constraints, fee structures).
- [x] No files outside `Allowed write paths` are modified.
- [x] Ticket status is updated when claimed/done with a brief “What changed” entry.

---

## Execution notes (optional)

- What changed (short): Added tiered roster, refreshed agents README, and documented 10 agent profiles with ownership, commissions, compliance notes, and UNIC Nicosia vs UNIC Athens positioning.
- Any open questions: Verify each partner’s latest accreditations and commission terms before co-branded marketing.
- Follow-up tickets suggested: None; proceed to partner outreach and data validation via country team.
