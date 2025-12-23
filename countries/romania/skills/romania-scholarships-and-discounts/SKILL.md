---
name: romania-scholarships-and-discounts
description: Romania addendum to the global scholarships and discounts skill; outlines local sourcing, currency handling, and compliance.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: romania
---

# Romania addendum: scholarships and discounts

Refer to `/skills/scholarships-and-discounts/SKILL.md` for schema and approvals. Apply these Romania-specific notes.

## Sourcing and verification
- Use written sources: Ministry/Inspectorate announcements, school scholarship bulletins, and documented agent offers. Avoid verbal-only or social posts without primary evidence.
- Quote amounts in EUR; if RON is requested, provide an estimate with FX rate/date and avoid implying fixed RON pricing.
- Store eligibility language in Romanian (and English if available) with links or files attached to each record.

## Messaging guardrails
- Do not imply eligibility for domestic grant programs unless a government source confirms outbound coverage.
- Avoid promising bespoke discounts during fairs or visits; route requests to admissions for written approval.
- Clarify whether benefits apply to UNIC, UNIC Athens, or both, and whether they stack with other aid.

## Data paths
- Place structured entries under `countries/romania/data/financial-aid/` using the global columns and citations. If only qualitative notes exist, append them to relevant school/agent profiles in `countries/romania/entities/`.
