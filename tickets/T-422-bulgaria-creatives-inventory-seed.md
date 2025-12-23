# T-422: Bulgaria — seed `creatives-inventory.csv` (concept inventory + statuses)

Status: done
Type: data
Priority: P2
Dependencies: (none)
Claimed-by: exec-20251222T174832Z
Claimed-at: 2025-12-22T17:48:32Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Create a trackable creative inventory for Bulgaria by populating `countries/bulgaria/data/marketing/creatives-inventory.csv` with an initial set of creative concepts mapped to channels, with clear themes/hooks/CTAs and workflow status.

This inventory can start without asset links; `asset_link` may be blank until assets exist.

---

## Context

- Creative guidance exists: `countries/bulgaria/go-to-market/digital-playbook/creative-library.md`
- Inventory table exists but is empty: `countries/bulgaria/data/marketing/creatives-inventory.csv`
- Dictionary: `countries/bulgaria/data/marketing/creatives-inventory-dictionary.md`

---

## Allowed write paths

- `tickets/T-422-bulgaria-creatives-inventory-seed.md`
- `countries/bulgaria/data/marketing/creatives-inventory.csv`
- `countries/bulgaria/data/marketing/creatives-inventory-dictionary.md` (only if minor clarifications are needed)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/bulgaria/**`)

---

## Required outputs

- `countries/bulgaria/data/marketing/creatives-inventory.csv` populated with **≥25 rows** across Meta, Google Search/Display, YouTube, TikTok, and LinkedIn.

---

## Acceptance criteria

- [x] Every row has `creative_id`, `channel`, `format`, `theme`, `hook`, `cta`, `status`, and `as_of`.
- [x] `asset_link` is blank unless a durable URL exists; no placeholder links.
- [x] Themes/hooks reflect Bulgaria realities (Athens vs Nicosia choice, scholarships, recognition, proximity, exam timing).
- [x] No files outside `Allowed write paths` were modified.

## What changed

- Seeded `countries/bulgaria/data/marketing/creatives-inventory.csv` with 30 cross-channel creative concepts and workflow statuses.
- Clarified `channel` allowed values in `countries/bulgaria/data/marketing/creatives-inventory-dictionary.md` for Bulgaria (includes LinkedIn).
