---
name: serbia-digital-measurement-and-benchmarks
description: Serbia addendum to the global digital measurement and benchmarks skill; notes local naming, language, and privacy expectations.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: serbia
---

# Serbia addendum: digital measurement & benchmarks

Use `/skills/digital-measurement-and-benchmarks/SKILL.md` for KPI guardrails, UTMs, and diagnostics. Apply these Serbia-specific conventions.

## Naming and UTMs
- Prefix campaigns and UTMs with `RS_`; include city tags (Belgrade, NoviSad, Niš, Kragujevac, Regional) when relevant.
- Include language in `utm_content` (`sr` or `en`) when running bilingual assets.

## Channel considerations
- Track Meta, Google Search, and TikTok separately; log Viber/WhatsApp follow-ups as owned channels with consent stored in the interaction record.
- For partner campaigns, set `utm_source=partner_<slug>` and map slugs to entries in `countries/serbia/entities/agents/` for attribution.

## Privacy and data handling
- Apply Serbia’s GDPR-aligned rules: store opt-in source/date for any first-party lists; avoid uploading contacts without explicit permission.
- Ensure cookie/consent notices render in Serbian on landing pages before tracking.

## Reporting context
- Break out performance by city cluster and language to explain CPA/CPL differences. Annotate reports for periods affected by Matura/exam windows or holidays.
