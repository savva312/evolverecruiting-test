---
name: greece-scholarships-and-discounts
description: Greece addendum to the global scholarships and discounts skill; covers local sourcing, messaging, and data storage.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: greece
---

# Greece addendum: scholarships and discounts

Use the global standard at `/skills/scholarships-and-discounts/SKILL.md` for schema and approvals. Apply these Greece-specific practices.

## Sourcing and verification
- Prioritize official sources: Ministry or school scholarship announcements, verified counselor bulletins, and written agent offers.
- Quote amounts in EUR; if families ask for cost in EUR plus local payment schedules, clarify that pricing is EUR-denominated and subject to intake policies.
- Keep eligibility language in Greek and English; store source links or files with each record.

## Messaging guardrails
- Avoid implying access to domestic public grants unless a government source explicitly allows outbound study support.
- Do not promise bespoke discounts during fairs or school visits; route requests through admissions for written approval.
- State whether benefits apply to UNIC, UNIC Athens, or both; avoid stacking assumptions without confirmation.

## Data paths
- Store structured entries under `countries/greece/data/financial-aid/` using the global columns (eligibility, amount, proof of source, deadlines).
- If only qualitative notes are available, append them to related school/agent profiles in `countries/greece/entities/` with citations.
