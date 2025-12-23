---
name: romania-digital-measurement-and-benchmarks
description: Romania addendum to the global digital measurement and benchmarks skill; notes local naming, language, and privacy expectations.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: romania
---

# Romania addendum: digital measurement & benchmarks

Use `/skills/digital-measurement-and-benchmarks/SKILL.md` for KPI guardrails, UTMs, and diagnostics. Apply these Romania-specific conventions.

## Naming and UTMs
- Prefix campaigns and UTMs with `RO_`; add city tags (Bucharest, Cluj, Iași, Timișoara, Constanța, Regional) when relevant.
- Include language in `utm_content` (`ro` or `en`) for bilingual assets.

## Channel considerations
- Track Meta, Google Search, and TikTok separately; WhatsApp follow-ups should be logged as owned channels with opt-in recorded.
- For agent or school co-marketing, set `utm_source=partner_<slug>` and map to `countries/romania/entities/agents/` for attribution.

## Privacy and data handling
- Apply GDPR: store opt-in source/date for any first-party lists; avoid uploading contacts without explicit permission.
- Keep analytics/pixel disclosures visible in Romanian on landing pages; ensure cookie notices render before tracking.

## Reporting context
- Break out performance by city cluster and language to explain CPA/CPL variance. Annotate reports for periods affected by Baccalaureate exams or major holidays.
