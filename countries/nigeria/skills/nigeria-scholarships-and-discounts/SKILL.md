---
name: nigeria-scholarships-and-discounts
description: Nigeria addendum to the global scholarships and discounts skill; captures local sourcing channels, currency handling, and guardrails.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: nigeria
---

# Nigeria addendum: scholarships and discounts

Use `/skills/scholarships-and-discounts/SKILL.md` for schema, approvals, and messaging rules. Apply these Nigeria-specific notes when collecting or communicating offers.

## Sourcing and verification
- Prioritize written sources: school scholarship circulars, trusted counselor newsletters, and official government/NGO programs. Avoid unverified social posts or verbal agent promises.
- Record amounts in EUR (or USD if provided) and, when quoting NGN, capture the FX rate/date; avoid implying fixed NGN pricing.
- Note whether awards are need-based, merit, or agent-funded; attach proof in the data record stored under `countries/nigeria/data/financial-aid/` when available.

## Messaging guardrails
- Do not promise fee waivers or bespoke discounts at fairs or visits; route requests through admissions with written approval.
- Clarify whether benefits apply to UNIC, UNIC Athens, or both, and whether they are stackable; avoid commitments on installment plans unless confirmed.
- Be explicit about limited seats or deadlines, but only if sourced.

## Compliance and logging
- Keep contact details tied to scholarship inquiries minimal and consented (NDPR); store opt-in source/time with each record.
- If a scholarship is linked to a school or agent partner, tag the corresponding profile in `countries/nigeria/entities/` for auditability.
