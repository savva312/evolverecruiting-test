# T-122: Country addenda for new global skills (T-091 to T-095)

Status: done
Type: content
Priority: P1
Dependencies: T-091, T-092, T-093, T-094, T-095
Claimed-by: work
Claimed-at: 2025-12-20T20:54:44+00:00
Last-updated: 2025-12-20T20:56:36+00:00

---

## Goal

Extend the new global skills from T-091 through T-095 with country-specific addenda (Bulgaria, Greece, Nigeria, Jordan, Lebanon, Romania, Serbia) so market teams have localized etiquette, routing, measurement baselines, and compliance notes without duplicating the global workflow.

---

## Allowed write paths

- `countries/bulgaria/skills/**`
- `countries/greece/skills/**`
- `countries/nigeria/skills/**`
- `countries/jordan/skills/**`
- `countries/lebanon/skills/**`
- `countries/romania/skills/**`
- `countries/serbia/skills/**`
- `tickets/T-097-country-addenda-for-new-global-skills.md`
- `research/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file)
- `.github/**`
- `scripts/**`
- `UNIC/**`
- `agent runs/**`
- Any other paths not explicitly listed in Allowed write paths

---

## Required outputs

Addenda SKILL files that reference the new global skills and capture country-specific guidance:
- `countries/<country>/skills/<country>-school-outreach-and-counselor-engagement/SKILL.md`
- `countries/<country>/skills/<country>-events-and-fairs/SKILL.md`
- `countries/<country>/skills/<country>-scholarships-and-discounts/SKILL.md`
- `countries/<country>/skills/<country>-digital-measurement-and-benchmarks/SKILL.md`
- `countries/<country>/skills/<country>-offerholder-and-yield-playbooks/SKILL.md`

Update each country skills README to reference the new addenda.

---

## Acceptance criteria

- Country addenda exist for Bulgaria, Greece, Nigeria, Jordan, Lebanon, Romania, and Serbia for all five skills noted above.
- Each addendum clearly points to the corresponding global skill and only layers country-specific routing/compliance/calendar notes.
- No files outside Allowed write paths are modified.

---

## Execution notes (optional)

- What changed (short): Aligned the events-and-fairs addenda across Bulgaria, Greece, Nigeria, Jordan, Lebanon, Romania, and Serbia to enforce campus clarity (UNIC vs UNIC Athens) and consistent post-event data-model logging (event, city, campus interest).
- Any open questions: None.
- Follow-up tickets suggested: Add localized artifacts (templates/CSVs) per country when ticket scopes require concrete outputs beyond guidance.
