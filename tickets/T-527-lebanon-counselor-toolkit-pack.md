# T-527: Lebanon — build counselor toolkit pack (checklist + scholarships + net price)

Status: open
Type: integration
Priority: P0
Dependencies: T-458 (recommended), T-460 (recommended)
Claimed-by:
Claimed-at:
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Replace placeholders in the Lebanon counselor toolkit by producing a small, complete “toolkit pack” that can actually be used in school outreach:
- application checklist (EN + Arabic/French placeholders)
- scholarships/discounts summary (Lebanon-facing, campus-aware)
- net price + cost of attendance (COA) mini-calculator (table-based, not a spreadsheet)

---

## Context

Current counselor toolkit contains placeholders:
- `countries/lebanon/go-to-market/schools-playbook/counselor-toolkit.md`

Useful supporting references:
- `countries/lebanon/market/exams-and-calendar.md`
- `countries/lebanon/market/education-system.md`
- `countries/lebanon/market/recognition-and-licensure.md` (to be completed in T-458)
- `countries/lebanon/data/programs/scholarships-discounts.csv`
- `countries/lebanon/reports/2025-12-20 - UNIC Athens Lebanon Recruitment Plan.md` (to be expanded in T-460)
- Shared campus materials: `UNIC/unicnicosia/**`, `UNIC/unicathens/**` (link, do not duplicate large content)

---

## Allowed write paths

- `tickets/T-455-lebanon-counselor-toolkit-pack.md`
- `countries/lebanon/go-to-market/schools-playbook/counselor-toolkit.md`
- `countries/lebanon/go-to-market/schools-playbook/application-checklist-ar-fr-en.md`
- `countries/lebanon/go-to-market/schools-playbook/scholarships-and-discounts-lebanon.md`
- `countries/lebanon/go-to-market/schools-playbook/net-price-and-coa-calculator.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/lebanon/**`)

---

## Required outputs

- `countries/lebanon/go-to-market/schools-playbook/application-checklist-ar-fr-en.md` (new)
- `countries/lebanon/go-to-market/schools-playbook/scholarships-and-discounts-lebanon.md` (new)
- `countries/lebanon/go-to-market/schools-playbook/net-price-and-coa-calculator.md` (new)
- `countries/lebanon/go-to-market/schools-playbook/counselor-toolkit.md` updated to replace placeholder bullets with links to the new assets and to the recognition brief.

---

## Acceptance criteria

- [ ] Toolkit assets avoid legal promises and include clear “verify with authority” language for recognition/licensure topics.
- [ ] Scholarship summary clearly distinguishes “confirmed policy” vs “Lebanon-recommended positioning” (if any), and labels assumptions.
- [ ] Calculator uses EUR, shows at least 2 living cost scenarios, and does not invent tuition figures (use ranges or blanks with notes if not sourced).
- [ ] No files outside `Allowed write paths` were modified.

