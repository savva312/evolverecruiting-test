---
name: bulgaria-digital-measurement-and-benchmarks
description: Bulgaria addendum to the global digital measurement and benchmarks skill; documents local platform mix, naming, and compliance notes.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: bulgaria
---

# Bulgaria addendum: digital measurement & benchmarks

Use the global spec at `/skills/digital-measurement-and-benchmarks/SKILL.md` for KPIs, UTMs, diagnostics, and reporting cadence. Apply these Bulgaria-specific conventions.

## Naming and UTM conventions
- Prefix campaigns and UTMs with `BG_` and include city cluster when relevant (e.g., `Sofia`, `Plovdiv`, `Varna/Burgas`, `Regional`).
- Note language in the content parameter (`utm_content=bg` or `utm_content=en`) when running parallel Bulgarian/English creatives.

## Platform nuances
- Benchmark Meta, Google Search, and TikTok separately; Viber/SMS retargeting should be logged as owned channels with consent proof.
- For agent co-marketing, track partner attribution via `utm_source=partner_<slug>` and ensure the partner slug maps to `countries/bulgaria/entities/agents/` entries.

## Data capture and privacy
- Follow GDPR requirements; store only consented first-party lists with capture source and date.
- If schools share counselor or student emails, log consent in the interaction record before uploading to any ad platform.

## Reporting cadence and baselines
- Weekly reporting should separate Sofia/Plovdiv/Varna/Burgas vs regional results to spot city-level outliers.
- When comparing to global guardrails, annotate any deviations caused by exam blackouts (Matura) or summer slowdowns.
