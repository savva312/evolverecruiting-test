# T-482: Jordan — audit + improvement ticket pack (25 tickets total)

Status: done
Type: qa
Priority: P1
Dependencies: (none)
Claimed-by: evoticketresolver_ca5sg03e
Claimed-at: 2025-12-22T17:13:26Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Produce a set of **Jordan-scoped**, narrowly scoped tickets that upgrade the usefulness and correctness of `countries/jordan/**` for UNIC + UNIC Athens enrollment work.

---

## Context

This run reviewed `countries/jordan/**` in detail and found several high-impact issues that make the Jordan subtree risky to use operationally:
- Bulgaria/copy-paste artifacts in key Jordan playbooks and a Jordan recruitment report (Bulgarian language, Bulgaria cities, and +359 phone numbers).
- Incorrect Medicine competitor content (Jordan cities paired with Bulgarian medical university sources).
- Offerholder materials containing inaccurate visa/residence assumptions for Jordanian applicants.
- A broken CSV (`countries/jordan/data/programs/competitor-programs.csv`) due to unquoted comma-containing locations.

This ticket creates remediation and build-out tickets focused on Jordan.

---

## Allowed write paths

- `tickets/T-444-jordan-ticket-pack.md`
- `tickets/T-445-jordan-schools-outreach-playbook-fix.md`
- `tickets/T-446-jordan-digital-creative-library-localization.md`
- `tickets/T-447-jordan-medicine-competitor-set-rebuild.md`
- `tickets/T-448-jordan-competitor-programs-csv-schema-fix.md`
- `tickets/T-449-jordan-offerholder-visa-residence-corrections.md`
- `tickets/T-450-jordan-visa-documents-checklist.md`
- `tickets/T-451-jordan-recognition-and-licensure-overview.md`
- `tickets/T-452-jordan-professional-bodies-regulators-pack.md`
- `tickets/T-453-jordan-events-calendar-verification.md`
- `tickets/T-454-jordan-events-profiles-verification.md`
- `tickets/T-455-jordan-events-csv-sync.md`
- `tickets/T-456-jordan-agent-onboarding-playbook.md`
- `tickets/T-457-jordan-agent-compliance-playbook.md`
- `tickets/T-458-jordan-agent-partner-slas-playbook.md`
- `tickets/T-459-jordan-digital-measurement-utms.md`
- `tickets/T-460-jordan-digital-landing-pages-plan.md`
- `tickets/T-461-jordan-counselor-toolkit-pack.md`
- `tickets/T-462-jordan-report-fix-school-pipeline.md`
- `tickets/T-463-jordan-report-fix-adcopy-keywords.md`
- `tickets/T-464-jordan-report-fix-calendar-assumptions.md`
- `tickets/T-465-jordan-program-cluster-cs-data-playbook.md`
- `tickets/T-466-jordan-program-cluster-business-playbook.md`
- `tickets/T-467-jordan-tier1-school-contact-verification.md`
- `tickets/T-468-jordan-agents-csv-roster-expansion.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except the ticket files listed in Allowed write paths)
- `.github/**`
- `scripts/**`

---

## Required outputs

- `tickets/T-445-jordan-schools-outreach-playbook-fix.md`
- `tickets/T-446-jordan-digital-creative-library-localization.md`
- `tickets/T-447-jordan-medicine-competitor-set-rebuild.md`
- `tickets/T-448-jordan-competitor-programs-csv-schema-fix.md`
- `tickets/T-449-jordan-offerholder-visa-residence-corrections.md`
- `tickets/T-450-jordan-visa-documents-checklist.md`
- `tickets/T-451-jordan-recognition-and-licensure-overview.md`
- `tickets/T-452-jordan-professional-bodies-regulators-pack.md`
- `tickets/T-453-jordan-events-calendar-verification.md`
- `tickets/T-454-jordan-events-profiles-verification.md`
- `tickets/T-455-jordan-events-csv-sync.md`
- `tickets/T-456-jordan-agent-onboarding-playbook.md`
- `tickets/T-457-jordan-agent-compliance-playbook.md`
- `tickets/T-458-jordan-agent-partner-slas-playbook.md`
- `tickets/T-459-jordan-digital-measurement-utms.md`
- `tickets/T-460-jordan-digital-landing-pages-plan.md`
- `tickets/T-461-jordan-counselor-toolkit-pack.md`
- `tickets/T-462-jordan-report-fix-school-pipeline.md`
- `tickets/T-463-jordan-report-fix-adcopy-keywords.md`
- `tickets/T-464-jordan-report-fix-calendar-assumptions.md`
- `tickets/T-465-jordan-program-cluster-cs-data-playbook.md`
- `tickets/T-466-jordan-program-cluster-business-playbook.md`
- `tickets/T-467-jordan-tier1-school-contact-verification.md`
- `tickets/T-468-jordan-agents-csv-roster-expansion.md`

---

## Acceptance criteria

- [x] 24 Jordan improvement tickets exist at the Required outputs paths
- [x] Each ticket is narrowly scoped with explicit `Allowed write paths` under `countries/jordan/**` (plus its own ticket file)
- [x] Highest-risk items are prioritized (copy/paste artifacts, visa assumptions, broken CSV, Medicine competitor set)

---

## Execution notes (optional)

- What changed (short): Created a Jordan-focused remediation + build-out ticket pack (T-445 to T-468).
- Top risks identified: Bulgaria artifacts in Jordan docs; incorrect Medicine competitor content; visa/residence inaccuracies; invalid competitor-programs CSV.

