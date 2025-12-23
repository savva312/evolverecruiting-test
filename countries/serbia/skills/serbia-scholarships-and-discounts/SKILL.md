---
name: serbia-scholarships-and-discounts
description: Serbia addendum to the global scholarships and discounts skill; outlines local sourcing, currency handling, and guardrails.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: serbia
---

# Serbia addendum: scholarships and discounts

Use `/skills/scholarships-and-discounts/SKILL.md` for schema and approvals. Apply these Serbia-specific notes.

## Sourcing and verification
- Rely on written sources: Ministry/municipality announcements, school scholarship bulletins, and documented agent offers. Avoid verbal-only promises.
- Record amounts in EUR; if RSD is requested, present as an estimate with FX rate/date and avoid implying fixed RSD pricing.
- Save eligibility language in Serbian (and English if provided) with links or files attached to each record.

## Messaging guardrails
- Do not imply access to domestic public funding for outbound study unless confirmed by an official source.
- Avoid promising bespoke discounts during fairs or visits; escalate requests to admissions for written approval.
- Clarify whether benefits apply to UNIC, UNIC Athens, or both and whether they stack with other aid.

## Data paths
- Store structured entries under `countries/serbia/data/financial-aid/` using the global columns and citations. If only notes exist, attach them to relevant school/agent profiles in `countries/serbia/entities/`.
