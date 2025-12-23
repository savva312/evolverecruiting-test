# T-469: Romania — replace UNIC Athens Romania recruitment plan template with an actionable 2026 plan

Status: done
Type: content
Priority: P0
Dependencies: T-452, T-453, T-449, T-463
Claimed-by: codex-20251222
Claimed-at: 2025-12-22
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Replace the placeholder plan at `countries/romania/reports/2025-12-20 - UNIC Athens Romania Recruitment Plan.md` with an actionable Romania plan for the next intake cycle (2026), including:
- target segments and priority cities (tied to the feeder school tiers + diaspora where relevant)
- program focus and positioning vs Romania shortlists and the cluster competitor sets
- channel mix plan (schools, agents, fairs, digital) with owners and cadences
- offerholder/yield workflow that references Romania timing (Bac + results + deposit windows)
- a measurable KPI dashboard section aligned to `countries/romania/data/operations/funnel-metrics.csv`

---

## Context

This repo already contains many Romania components (schools list, agent roster, fair calendar, draft playbooks), but the recruitment plan report is still a template and is not usable as the “single plan” for the team.

Key Romania inputs to link:
- Schools: `countries/romania/entities/schools/high-potential-feeder-high-schools.md`
- Agents: `countries/romania/entities/agents/feeder-candidates.md`
- Events: `countries/romania/entities/fairs-events/calendar-2025-2026.md`
- Digital: `countries/romania/go-to-market/digital-playbook/channel-strategy.md`
- Yield: `countries/romania/go-to-market/offerholder-and-yield/*`

---

## Allowed write paths

- `tickets/T-469-romania-unic-athens-recruitment-plan-2026.md`
- `countries/romania/reports/2025-12-20 - UNIC Athens Romania Recruitment Plan.md`
- `executions/**` (optional for notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`
- `tickets/**` (except this ticket file)
- `countries/**` (except `countries/romania/reports/**`)

---

## Required outputs

- Updated `countries/romania/reports/2025-12-20 - UNIC Athens Romania Recruitment Plan.md` (no longer a template; contains Romania-specific plan content)

---

## Acceptance criteria

- [x] Plan contains a 12-month calendar with channel actions by month (high-level is fine, but must be explicit).
- [x] Includes a “Single owner per channel” accountability table (schools / agents / events / digital / offerholder).
- [x] Includes measurable KPIs and definitions, and references the funnel metrics CSV as the canonical metric glossary.
- [x] No copy/paste drift remains (no Bulgaria examples or placeholders).
- [x] No edits outside allowed paths.

---

What changed: Replaced the placeholder with a Romania-specific 2026 UNIC Athens plan covering segments, program positioning, 12-month channel calendar, accountability table, yield workflow, and KPI dashboard tying back to the funnel metrics CSV.
