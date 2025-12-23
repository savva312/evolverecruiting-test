# T-487: Jordan — fix schools outreach playbook (remove non-Jordan artifacts)

Status: done
Type: content
Priority: P0
Dependencies: (none)
Claimed-by: evoticketresolver_3i9931k0
Claimed-at: 2025-12-22T20:40:01Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Make `countries/jordan/go-to-market/schools-playbook/outreach.md` operationally correct for Jordan by:
- Removing Bulgaria/copy-paste artifacts (Sofia/Plovdiv/Varna/Ruse/Veliko Tarnovo references).
- Replacing them with Jordan geography and working links to Jordan school indices/profiles.
- Aligning outreach timing and channels to Jordan realities (Tawjihi/IB/A-Level calendar; WhatsApp norms).

---

## Context

Current file has clear non-Jordan artifacts, e.g. links like `entities/schools/profiles/sofia/README.md` and city references that do not exist in `countries/jordan/**`.

Relevant Jordan sources already in-repo:
- Priority schools index: `countries/jordan/entities/schools/README.md`
- Exams/calendar: `countries/jordan/market/exams-and-calendar.md`
- School profiles: `countries/jordan/entities/schools/profiles/**`

---

## Allowed write paths

- `tickets/T-487-jordan-schools-outreach-playbook-fix.md`
- `countries/jordan/go-to-market/schools-playbook/outreach.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/jordan/**`)

---

## Required outputs

- `countries/jordan/go-to-market/schools-playbook/outreach.md` updated with Jordan-correct targeting, links, and cadence.

---

## Acceptance criteria

- [x] `countries/jordan/go-to-market/schools-playbook/outreach.md` contains **no** references to Bulgaria cities/folders (at minimum: `sofia`, `plovdiv`, `varna`, `ruse`, `tarnovo`).
- [x] All internal links in the file resolve to existing paths under `countries/jordan/**`.
- [x] Targeting priorities reference Jordan hubs (at minimum: Amman, Irbid, Zarqa, Aqaba, Madaba/King’s Academy as relevant).
- [x] Outreach cadence explicitly calls out Jordan exam windows (Tawjihi + IB/A-Level) using `countries/jordan/market/exams-and-calendar.md` as the anchor.

---

## What changed
- Rewrote the Jordan school outreach playbook to remove non-Jordan (Bulgaria) artifacts and replace them with Jordan geography, links to Jordan school indices/profiles, and a Jordan-specific cadence anchored to the Tawjihi/IB/A-Level calendar.
