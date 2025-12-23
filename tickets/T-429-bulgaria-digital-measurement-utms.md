# T-429: Bulgaria — standardize UTMs + conversion events (digital measurement v1)

Status: done
Type: content
Priority: P0
Dependencies: T-421 (recommended)
Claimed-by: exec-20251222-1750-evoticketresolver_ues9ykoq
Claimed-at: 2025-12-22T17:50:20Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Replace the placeholder `countries/bulgaria/go-to-market/digital-playbook/measurement-utms.md` with a Bulgaria-ready measurement spec covering:
- UTM naming conventions (including campus split)
- required capture fields for CRM routing
- conversion event taxonomy (GA4 + ad platforms)
- QA checklist for campaign launches

---

## Context

- Placeholder file: `countries/bulgaria/go-to-market/digital-playbook/measurement-utms.md`
- Related guidance:
  - `countries/bulgaria/go-to-market/digital-playbook/channel-strategy.md`
  - `countries/bulgaria/data/marketing/channel-benchmarks.csv`

---

## Allowed write paths

- `tickets/T-429-bulgaria-digital-measurement-utms.md`
- `countries/bulgaria/go-to-market/digital-playbook/measurement-utms.md`

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

- `countries/bulgaria/go-to-market/digital-playbook/measurement-utms.md` updated to include:
  - canonical UTM schema with examples (BG language vs EN language; Athens vs Nicosia)
  - required landing page parameters and form hidden fields to persist UTMs
  - conversion event names and definitions (lead submitted, call click, brochure download, booking)
  - go-live QA checklist (pixel firing, GA4 events, CRM field mapping)

---

## Acceptance criteria

- [x] Includes a “minimum viable measurement” section that can be implemented without engineering work (UTMs + simple form fields).
- [x] Explicitly prohibits tracking minors with extended retargeting windows; includes compliance notes.
- [x] No files outside `Allowed write paths` were modified.

---

## What changed (2025-12-22)

- Replaced the placeholder measurement doc with a Bulgaria-ready v1 spec: canonical UTMs (campus + language split), required CRM capture fields, GA4/ad-platform conversion event taxonomy, and a go-live QA checklist.
