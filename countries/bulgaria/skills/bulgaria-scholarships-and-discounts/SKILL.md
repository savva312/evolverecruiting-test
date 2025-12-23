---
name: bulgaria-scholarships-and-discounts
description: Bulgaria addendum to the global scholarships and discounts skill; records local sourcing channels, currency treatment, and compliance guardrails.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: bulgaria
---

# Bulgaria addendum: scholarships and discounts

Refer to `/skills/scholarships-and-discounts/SKILL.md` for schemas and vetting rules. Use this addendum to localize sourcing and messaging for Bulgaria.

## Sourcing and verification
- Check official sources first: Ministry of Education notices, school scholarship bulletins, and verified agent offers. Avoid relying on social posts without a primary source.
- Record all amounts in EUR and, if quoting BGN, note the FX rate/date in the notes column—do not imply fixed BGN pricing.
- Capture eligibility language verbatim in Bulgarian and English; attach links or file paths in the data model entry.

## Messaging guardrails
- Do not promise bespoke discounts at school visits; route any special requests through admissions with written approval.
- Clarify whether benefits apply to UNIC, UNIC Athens, or both, and whether they stack with existing merit aid.
- Avoid suggesting government-backed aid unless a public source confirms it for outbound study.

## Data paths
- Store structured records in `countries/bulgaria/data/programs/scholarships-discounts.csv` and align columns to the global schema (dictionary: `countries/bulgaria/data/programs/scholarships-discounts-dictionary.md`).
- If only notes are available, log them beside relevant school or agent profiles in `countries/bulgaria/entities/` with clear source citations.
