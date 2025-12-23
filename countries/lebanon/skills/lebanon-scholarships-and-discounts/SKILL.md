---
name: lebanon-scholarships-and-discounts
description: Lebanon addendum to the global scholarships and discounts skill; covers local sourcing, currency treatment, and messaging cautions.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: lebanon
---

# Lebanon addendum: scholarships and discounts

Use `/skills/scholarships-and-discounts/SKILL.md` for schema and approvals. Apply these Lebanon-specific notes.

## Sourcing and verification
- Rely on written sources: school scholarship bulletins, trusted counselor newsletters, and official government/NGO programs. Avoid verbal-only offers.
- Record amounts in EUR (or USD if provided). If quoting LBP, note the FX rate/date and clarify that amounts are indicative due to currency volatility.
- Save eligibility language in Arabic/French/English as provided; attach links or files with each record.

## Messaging guardrails
- Do not imply access to domestic financial aid unless an official source confirms outbound eligibility.
- Avoid promising bespoke discounts during fairs or visits; escalate through admissions for written approval.
- Specify whether benefits apply to UNIC, UNIC Athens, or both, and avoid stacking assumptions without confirmation.

## Data paths
- Store structured entries under `countries/lebanon/data/financial-aid/` following the global columns; add citations. If only notes exist, attach them to relevant school/agent profiles in `countries/lebanon/entities/`.
