---
name: nigeria-digital-measurement-and-benchmarks
description: Nigeria addendum to the global digital measurement and benchmarks skill; notes local naming, channel mix, and consent requirements.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: nigeria
---

# Nigeria addendum: digital measurement & benchmarks

Follow `/skills/digital-measurement-and-benchmarks/SKILL.md` for KPI targets, UTMs, and diagnostics. Apply these Nigeria-specific conventions.

## Naming and UTMs
- Prefix campaigns and UTMs with `NG_`; include city tags when targeting Lagos/Abuja/Port Harcourt/other regions.
- Capture channel in `utm_medium` and mark WhatsApp follow-ups as owned (`utm_medium=owned_whatsapp`) with consent stored in the log.

## Channel considerations
- Track Meta, Google Search, and TikTok separately; WhatsApp click-to-chat should be measured with server-side events where available and reconciled with chat transcripts.
- For agent or school co-marketing, set `utm_source=partner_<slug>` and map slugs to `countries/nigeria/entities/agents/` to keep attribution clean.

## Privacy and data handling
- Apply NDPR principles: store opt-in source and timestamp for any first-party lists; avoid uploading contacts without explicit permission.
- When connectivity is unreliable, export platform data promptly and back it up in `countries/nigeria/data/` to prevent loss.

## Reporting and context
- Break out performance by city cluster and by curriculum type where possible (WAEC/NECO vs international) to explain CPA/CPL variance.
- Annotate reports for major disruptions (power/network outages, currency shifts) and exam windows to contextualize deviations from global guardrails.
