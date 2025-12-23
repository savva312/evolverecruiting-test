# T-549: Jordan — build counselor toolkit pack (checklist + scholarships + net price)

Status: open
Type: integration
Priority: P0
Dependencies: (none)
Claimed-by:
Claimed-at:
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Replace placeholders in the Jordan counselor toolkit by producing a small, complete toolkit pack that can actually be used in school outreach:
- application checklist (AR/EN)
- scholarships/discounts summary (Jordan-facing, campus-aware)
- net price + cost of attendance (COA) mini-calculator (table-based, not a spreadsheet)

---

## Context

Current toolkit contains placeholders:
- `countries/jordan/go-to-market/schools-playbook/counselor-toolkit.md`

Useful supporting references:
- `countries/jordan/market/exams-and-calendar.md`
- `countries/jordan/market/recognition-and-licensure.md` (placeholder today; should link carefully / add disclaimers)
- `countries/jordan/data/programs/scholarships-discounts.csv`
- `UNIC/unicathens/scholarships/README.md` and `UNIC/unicnicosia/scholarships/README.md` (global hubs; may be placeholders)

---

## Allowed write paths

- `tickets/T-461-jordan-counselor-toolkit-pack.md`
- `countries/jordan/go-to-market/schools-playbook/counselor-toolkit.md`
- `countries/jordan/go-to-market/schools-playbook/application-checklist-ar-en.md`
- `countries/jordan/go-to-market/schools-playbook/scholarships-and-discounts-jordan.md`
- `countries/jordan/go-to-market/schools-playbook/net-price-and-coa-calculator.md`

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

- `countries/jordan/go-to-market/schools-playbook/application-checklist-ar-en.md` (new)
- `countries/jordan/go-to-market/schools-playbook/scholarships-and-discounts-jordan.md` (new)
- `countries/jordan/go-to-market/schools-playbook/net-price-and-coa-calculator.md` (new)
- `countries/jordan/go-to-market/schools-playbook/counselor-toolkit.md` updated to replace placeholder bullets with links to the new assets and to the recognition brief (with disclaimers if still incomplete).

---

## Acceptance criteria

- [ ] Toolkit assets avoid legal promises and include clear “verify with authority” language for recognition/licensure topics.
- [ ] Scholarship summary clearly distinguishes “confirmed policy” vs “Jordan-recommended positioning” (if any), and labels assumptions.
- [ ] Calculator uses EUR, includes at least 2 living-cost scenarios, and does not invent tuition figures (use ranges or leave blanks with notes if not sourced).
- [ ] No files outside `Allowed write paths` were modified.

