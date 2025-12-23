# T-442: Bulgaria — build counselor toolkit pack (checklist + scholarships + net price)

Status: done
Type: integration
Priority: P0
Dependencies: (none)
Claimed-by: evoticketresolver_g11d64da
Claimed-at: 2025-12-22T17:53:06Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Replace placeholders in the Bulgaria counselor toolkit by producing a small, complete “toolkit pack” that can actually be used in school outreach:
- application checklist (BG/EN)
- scholarships/discounts summary (Bulgaria-facing, campus-aware)
- net price + cost of attendance (COA) mini-calculator (table-based, not a spreadsheet)

---

## Context

Current counselor toolkit contains placeholders:
- `countries/bulgaria/go-to-market/schools-playbook/counselor-toolkit.md`

Useful supporting references:
- `countries/bulgaria/market/exams-and-calendar.md`
- `countries/bulgaria/market/recognition-and-licensure.md`
- `countries/bulgaria/data/programs/scholarships-discounts.csv`
- `countries/bulgaria/reports/2025-12-20 - UNIC Athens Bulgaria Recruitment Plan.md` (COA framing and scholarship tier concepts)

---

## Allowed write paths

- `tickets/T-442-bulgaria-counselor-toolkit-pack.md`
- `countries/bulgaria/go-to-market/schools-playbook/counselor-toolkit.md`
- `countries/bulgaria/go-to-market/schools-playbook/application-checklist-bg-en.md`
- `countries/bulgaria/go-to-market/schools-playbook/scholarships-and-discounts-bg.md`
- `countries/bulgaria/go-to-market/schools-playbook/net-price-and-coa-calculator.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/bulgaria/**`)

---

## Required outputs

- `countries/bulgaria/go-to-market/schools-playbook/application-checklist-bg-en.md` (new)
- `countries/bulgaria/go-to-market/schools-playbook/scholarships-and-discounts-bg.md` (new)
- `countries/bulgaria/go-to-market/schools-playbook/net-price-and-coa-calculator.md` (new)
- `countries/bulgaria/go-to-market/schools-playbook/counselor-toolkit.md` updated to replace placeholder bullets with links to the new assets and to the recognition brief.

---

## Acceptance criteria

- [x] Toolkit assets avoid legal promises and include clear “verify with authority” language for recognition/licensure topics.
- [x] Scholarship summary clearly distinguishes “confirmed policy” vs “Bulgaria-recommended positioning” (if any), and labels assumptions.
- [x] Calculator uses EUR, shows at least 2 living cost scenarios, and does not invent tuition figures (use ranges or leave blanks with notes if not sourced).
- [x] No files outside `Allowed write paths` were modified.

---

## What changed

- Added counselor-ready assets:
  - `countries/bulgaria/go-to-market/schools-playbook/application-checklist-bg-en.md`
  - `countries/bulgaria/go-to-market/schools-playbook/scholarships-and-discounts-bg.md`
  - `countries/bulgaria/go-to-market/schools-playbook/net-price-and-coa-calculator.md`
- Updated `countries/bulgaria/go-to-market/schools-playbook/counselor-toolkit.md` to replace placeholders with links to the assets above and to the Bulgaria recognition brief.
