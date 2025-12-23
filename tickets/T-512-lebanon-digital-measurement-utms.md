# T-512: Lebanon — standardize UTMs + conversion events (digital measurement v1)

Status: open
Type: content
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

Replace the placeholder `countries/lebanon/go-to-market/digital-playbook/measurement-utms.md` with a Lebanon-ready measurement spec covering:
- UTM naming conventions (including campus split + language)
- required capture fields for CRM routing and agent attribution
- conversion event taxonomy (GA4 + ad platforms)
- QA checklist for campaign launches

---

## Context

- Placeholder file: `countries/lebanon/go-to-market/digital-playbook/measurement-utms.md`
- Related guidance:
  - `countries/lebanon/go-to-market/digital-playbook/channel-strategy.md`
  - `countries/lebanon/data/marketing/channel-benchmarks.csv`
- Lebanon realities to reflect:
  - Arabic/French/English creative variants
  - diaspora targeting alongside in-country Lebanon
  - strict consent expectations for messaging and retargeting (especially minors)

---

## Allowed write paths

- `tickets/T-452-lebanon-digital-measurement-utms.md`
- `countries/lebanon/go-to-market/digital-playbook/measurement-utms.md`

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

- `countries/lebanon/go-to-market/digital-playbook/measurement-utms.md` updated to include:
  - canonical UTM schema with examples (AR/FR/EN; Athens vs Nicosia; diaspora vs Lebanon)
  - required landing page parameters and form hidden fields to persist UTMs
  - conversion event names and definitions (lead submitted, call click, brochure download, booking)
  - go-live QA checklist (pixel firing, GA4 events, CRM field mapping)

---

## Acceptance criteria

- [ ] Includes a “minimum viable measurement” section that can be implemented without engineering work (UTMs + simple form fields).
- [ ] Explicitly prohibits tracking minors with extended retargeting windows and includes consent guidance for messaging apps.
- [ ] No files outside `Allowed write paths` were modified.

