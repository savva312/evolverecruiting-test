# T-511: Lebanon — seed `creatives-inventory.csv` (concept inventory + statuses)

Status: open
Type: data
Priority: P2
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

Create a trackable creative inventory for Lebanon by populating `countries/lebanon/data/marketing/creatives-inventory.csv` with an initial set of creative concepts mapped to channels, with clear themes/hooks/CTAs and workflow status.

This inventory can start without asset links; `asset_link` may be blank until assets exist.

---

## Context

- Creative guidance exists: `countries/lebanon/go-to-market/digital-playbook/creative-library.md`
- Inventory table exists but is empty: `countries/lebanon/data/marketing/creatives-inventory.csv`
- Dictionary: `countries/lebanon/data/marketing/creatives-inventory-dictionary.md`

---

## Allowed write paths

- `tickets/T-451-lebanon-creatives-inventory-seed.md`
- `countries/lebanon/data/marketing/creatives-inventory.csv`
- `countries/lebanon/data/marketing/creatives-inventory-dictionary.md` (only if minor clarifications are needed)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/lebanon/**`)

---

## Required outputs

- `countries/lebanon/data/marketing/creatives-inventory.csv` populated with **≥25 rows** across Meta, Google Search/Display, YouTube, TikTok, and LinkedIn.

---

## Acceptance criteria

- [ ] Every row has `creative_id`, `channel`, `format`, `theme`, `hook`, `cta`, `status`, and `as_of`.
- [ ] `asset_link` is blank unless a durable URL exists; no placeholder links.
- [ ] Themes/hooks reflect Lebanon realities (Athens vs Nicosia choice, scholarships, recognition, proximity, exam timing, parent reassurance).
- [ ] No files outside `Allowed write paths` were modified.

