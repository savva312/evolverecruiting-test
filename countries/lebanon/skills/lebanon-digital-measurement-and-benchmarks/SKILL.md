---
name: lebanon-digital-measurement-and-benchmarks
description: Lebanon addendum to the global digital measurement and benchmarks skill; notes local naming, language, and data-handling practices.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: lebanon
---

# Lebanon addendum: digital measurement & benchmarks

Use `/skills/digital-measurement-and-benchmarks/SKILL.md` for KPI guardrails, UTMs, and diagnostics. Apply these Lebanon-specific conventions.

## Naming and UTMs
- Prefix campaigns and UTMs with `LB_`; add city tags when relevant (Beirut, MountLebanon, Tripoli, Bekaa, South).
- Mark language in `utm_content` (`ar`, `fr`, or `en`) to separate Arabic/French/English assets.

## Channel considerations
- Track Meta, Google Search, and TikTok separately; WhatsApp click-to-chat should be logged as owned follow-up with consent stored in the interaction record.
- For partner campaigns, set `utm_source=partner_<slug>` and map slugs to entries in `countries/lebanon/entities/agents/` for attribution.

## Privacy and data handling
- Obtain explicit opt-in before uploading first-party lists; store capture source/date. Avoid storing sensitive personal data in measurement exports.
- When connectivity is unstable, export platform data frequently and back it up in `countries/lebanon/data/`.

## Reporting context
- Break out performance by city cluster and language to spot CPAs/CTR shifts. Annotate reports for periods affected by exam seasons or major power outages that impact response rates.
