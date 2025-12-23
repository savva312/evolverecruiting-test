# T-518: Romania — fix schools outreach playbook (remove Bulgaria drift; Romania-specific cadence)

Status: open
Type: content
Priority: P0
Dependencies: T-308
Claimed-by:
Claimed-at:
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Make `countries/romania/go-to-market/schools-playbook/outreach.md` accurate and Romania-usable by:
- removing Bulgaria city/path references (e.g., Sofia/Plovdiv/Varna folders)
- aligning targeting priorities to Romania’s actual feeder list and geographies
- adding practical scripts (email + phone + WhatsApp/Viber) and required CRM fields for school outreach

---

## Context

`countries/romania/go-to-market/schools-playbook/outreach.md` currently contains copy/paste drift and wrong file references, which is a direct operational risk.

Romania school targeting sources:
- `countries/romania/entities/schools/high-potential-feeder-high-schools.md`
- `countries/romania/data/entities/schools/romania-high-potential-feeder-high-schools.csv`
- Per-school profiles under `countries/romania/entities/schools/profiles/`

---

## Allowed write paths

- `tickets/T-453-romania-schools-outreach-playbook-fix.md`
- `countries/romania/go-to-market/schools-playbook/outreach.md`
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
- `countries/**` (except `countries/romania/go-to-market/**`)

---

## Required outputs

- Updated `countries/romania/go-to-market/schools-playbook/outreach.md`

---

## Acceptance criteria

- [ ] No references remain to Bulgaria city folders or Bulgaria tickets/templates.
- [ ] Outreach “targeting priorities” section references Romania Tier A/B/C structure and links to the Romania feeder CSV/profile paths.
- [ ] Includes at least: intro email script, follow-up call script, and WhatsApp/Viber consent-safe message.
- [ ] Defines minimum CRM fields to capture per school interaction (date, contact role, outcome, next step, preferred channel).
- [ ] No edits outside allowed paths.

