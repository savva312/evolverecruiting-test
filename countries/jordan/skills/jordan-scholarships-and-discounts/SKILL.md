---
name: jordan-scholarships-and-discounts
description: Jordan addendum to the global scholarships and discounts skill; captures local sourcing, currency treatment, and guardrails.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: jordan
---

# Jordan addendum: scholarships and discounts

Use `/skills/scholarships-and-discounts/SKILL.md` for schema, vetting, and messaging rules. Apply these Jordan-specific notes.

## Sourcing and verification
- Rely on written sources: Ministry/Directorate announcements, school scholarship circulars, and documented agent offers. Avoid verbal-only promises.
- Quote amounts in EUR; if mentioning JOD, state the FX rate/date and avoid implying fixed JOD pricing.
- Save eligibility language in Arabic and English, with links or files stored alongside the record.

## Messaging guardrails
- Do not imply access to government-backed funding for outbound study unless an official source confirms it.
- Avoid promising bespoke discounts during fairs or visits; escalate requests to admissions for written approval.
- Clarify whether awards apply to UNIC, UNIC Athens, or both and whether they can stack with existing merit aid.

## Data paths
- Store structured entries in `countries/jordan/data/financial-aid/` using the global columns. If notes are unstructured, append them to related school or agent profiles in `countries/jordan/entities/` with citations.
