---
name: greece-digital-measurement-and-benchmarks
description: Greece addendum to the global digital measurement and benchmarks skill; notes local naming, channel mix, and privacy expectations.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: greece
---

# Greece addendum: digital measurement & benchmarks

Rely on `/skills/digital-measurement-and-benchmarks/SKILL.md` for KPI guardrails, UTM standards, and diagnostics. Use this addendum for Greece-specific conventions.

## Naming and UTMs
- Prefix campaigns and UTMs with `GR_`; include metro tags (`Athens`, `Thessaloniki`, `Patras`, `Crete`, `Regional`) when relevant.
- Note language in `utm_content` (`el` for Greek, `en` for English) when running bilingual assets.

## Channel considerations
- Track Meta, Google Search, and TikTok separately; log Viber/SMS outreach as owned channels with proof of consent.
- For school or agent co-marketing, map `utm_source=partner_<slug>` to entries in `countries/greece/entities/agents/`.

## Privacy and data handling
- Apply GDPR: store opt-in source and date for any first-party lists; avoid uploading contacts without explicit permission.
- Keep pixel/analytics implementations transparent in Greek on landing pages; ensure cookie notices are present before measuring.

## Reporting cadence
- Weekly reporting should break out Athens vs Thessaloniki vs other regions to spot performance deltas.
- Annotate reports when performance is affected by Panhellenic exams or August holidays to contextualize deviations from global benchmarks.
