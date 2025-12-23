# T-074: ХГ ‘Св. св. Кирил и Методий’ — upgrade to global high school profile standard

Status: archived
Claimed-by: execution-1
Claimed-at: 2025-12-20
Type: content
Priority: P1
Dependencies: T-026-high-school-profile-template, T-032-bulgaria-school-upgrade-ticketization
Last-updated: 2025-12-20

---

## Goal

Upgrade the ХГ ‘Св. св. Кирил и Методий’ profile to the global high school profile template in `skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`, preserving verified local insights while filling template sections with current, sourced data.

---

## Context

- Existing profile: `bulgaria/entities/schools/profiles/plovdiv/humanities-gymnasium-cyril-methodius/README.md`
- City directory: `bulgaria/entities/schools/profiles/plovdiv/`
- Keep the profile within this folder while aligning fully to the global template.
- Use `skills/high-school-profile-template/SKILL.md` and `skills/markdown-authoring` for structure, sourcing expectations, and style.

---

## Allowed write paths

- `bulgaria/entities/schools/profiles/plovdiv/humanities-gymnasium-cyril-methodius/README.md`
- `bulgaria/entities/schools/profiles/plovdiv/humanities-gymnasium-cyril-methodius/**`
- `research/**`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`

---

## Required outputs

- `bulgaria/entities/schools/profiles/plovdiv/humanities-gymnasium-cyril-methodius/README.md` updated to match the global high school profile template with current data and sources.

---

## Acceptance criteria

- [x] Profile follows the sections and checklists from the global high school template with placeholders replaced or explicitly marked as open questions.
- [x] Local facts are sourced or flagged for follow-up; no speculative claims.
- [x] Profile remains at the same path with any new assets contained within the school folder; no broken links introduced.
- [x] No files modified outside `Allowed write paths`.

## What changed

- Upgraded the Humanities Gymnasium profile to the global high school template with aligned sections.
- Captured identity, risks, outreach steps, and open questions; noted site access issues and pending contact verification.

---

## Notes/Context

- Key sources to validate: recent admissions outcomes, tuition/fees, counselor contacts, outbound destinations, and language/exam tracks.
- Capture outstanding gaps in an **Open Questions** section within the profile.
