---
name: jordan-digital-measurement-and-benchmarks
description: Jordan addendum to the global digital measurement and benchmarks skill; notes local naming, language, and consent expectations.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: jordan
---

# Jordan addendum: digital measurement & benchmarks

Use `/skills/digital-measurement-and-benchmarks/SKILL.md` for KPI guardrails, UTMs, and diagnostics. Apply these Jordan-specific conventions.

## Naming and UTMs
- Prefix campaigns and UTMs with `JO_`; include city tags (`Amman`, `Irbid`, `Zarqa`, `Aqaba`, `Regional`) when applicable.
- Mark language in `utm_content` (`ar` for Arabic, `en` for English) for bilingual assets.

## Channel considerations
- Track Meta, Google Search, and TikTok separately; WhatsApp click-to-chat should be logged as owned follow-up with consent stored in the interaction record.
- For school/agent co-marketing, set `utm_source=partner_<slug>` and map slugs to entries in `countries/jordan/entities/agents/`.

## Privacy and consent
- Obtain explicit opt-in before uploading lists; log capture source/date and keep evidence in `countries/jordan/data/` where permitted.
- Ensure Arabic cookie/consent notices are present on landing pages when running tracking pixels.

## Reporting notes
- Break out performance by city cluster and note periods affected by Tawjihi exams or Ramadan where engagement patterns shift.
