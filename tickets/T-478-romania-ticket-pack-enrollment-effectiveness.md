# T-478: Romania — enrollment effectiveness ticket pack (25 tickets)

Status: done
Type: qa
Priority: P1
Dependencies: (none)
Claimed-by: evoticketresolver_sd8ny6m8
Claimed-at: 2025-12-22T17:11:45+00:00
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Review `countries/romania/**` in detail and produce a set of **25 narrowly-scoped, execution-ready tickets** that improve Romania recruiting operations for UNIC and UNIC Athens.

---

## Context

Key gaps/opportunities identified in `countries/romania/**`:
- **Data hygiene risk:** `countries/romania/data/entities/schools.csv` contains multiple schemas and repeated headers, which makes it unreliable for ops.
- **Empty datasets:** key CSVs exist but are mostly empty (`agents.csv`, `competitors.csv`, `fairs-events.csv`, marketing/ops/programs CSVs).
- **Copy/paste drift:** `countries/romania/go-to-market/schools-playbook/outreach.md` references Bulgaria city folders; `digital-playbook/creative-library.md` contains Bulgarian copy; `program-clusters/medicine-md/competitors.md` contains Bulgaria sources.
- **Placeholders:** outbound mobility report and some strategic docs are still templates; `market/recognition-and-licensure.md` is empty.

This ticket is complete when the 25 tickets below exist and follow the canonical ticket format with tight scopes.

---

## Allowed write paths

- `tickets/T-444-romania-ticket-pack-enrollment-effectiveness.md`
- `tickets/T-445-romania-schools-csv-normalization.md`
- `tickets/T-446-romania-agents-csv-v1.md`
- `tickets/T-447-romania-competitors-csv-v1.md`
- `tickets/T-448-romania-fairs-events-csv-v1.md`
- `tickets/T-449-romania-scholarships-discounts-csv-v1.md`
- `tickets/T-450-romania-competitor-programs-csv-v1.md`
- `tickets/T-451-romania-channel-benchmarks-csv-v1.md`
- `tickets/T-452-romania-funnel-metrics-targets.md`
- `tickets/T-453-romania-schools-outreach-playbook-fix.md`
- `tickets/T-454-romania-counselor-toolkit-pack.md`
- `tickets/T-455-romania-school-visit-templates-pack.md`
- `tickets/T-456-romania-agents-onboarding-playbook.md`
- `tickets/T-457-romania-agents-partner-slas.md`
- `tickets/T-458-romania-agents-compliance-gdpr.md`
- `tickets/T-459-romania-offerholder-comms-templates.md`
- `tickets/T-460-romania-school-profiles-cleanup-navigation.md`
- `tickets/T-461-romania-digital-measurement-utms-and-landing-pages.md`
- `tickets/T-462-romania-creative-library-romanian-localization.md`
- `tickets/T-463-romania-outbound-mobility-baseline-report.md`
- `tickets/T-464-romania-recognition-and-licensure-deep-dive.md`
- `tickets/T-465-romania-exams-calendar-2026-refresh.md`
- `tickets/T-466-romania-medicine-competitor-set-fix.md`
- `tickets/T-467-romania-cs-competitor-set-and-partners.md`
- `tickets/T-468-romania-business-competitor-set-and-partners.md`
- `tickets/T-469-romania-unic-athens-recruitment-plan-2026.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except the files listed in Allowed write paths)
- `.github/**`
- `scripts/**`
- `countries/**` (this ticket does not modify country content; it only creates ticket files)

---

## Required outputs

- The 25 ticket files listed in Allowed write paths (T-445 through T-469), all with:
  - Canonical ticket fields (Status/Type/Priority/Allowed/Forbidden/Outputs/Acceptance)
  - Narrow, non-ambiguous scope
  - Romania-only write boundaries (unless explicitly justified)

---

## Acceptance criteria

- [x] 25 Romania improvement tickets exist (`tickets/T-445` … `tickets/T-469`).
- [x] Each ticket has narrowly scoped `Allowed write paths` and explicit `Required outputs`.
- [x] EvoResearcher tickets include `Research output path`, `Research rounds`, and `Research sections`, and contain the prompt in the ticket body.
- [x] No files outside `tickets/` were modified by this run.

---

## Execution notes (optional)

- What changed (short): Created 25 Romania-focused execution tickets covering data hygiene, playbooks, digital ops, market baselines, and program-cluster competitor sets; prioritized to remove copy/paste drift and make Romania ops measurable.

