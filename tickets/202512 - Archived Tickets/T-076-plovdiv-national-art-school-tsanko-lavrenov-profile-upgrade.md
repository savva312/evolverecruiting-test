# T-076: Национална художествена гимназия ‘Цанко Лавренов’ — upgrade to global high school profile standard

Status: archived
Type: content
Priority: P1
Dependencies: T-026-high-school-profile-template, T-032-bulgaria-school-upgrade-ticketization
Claimed-by: work
Claimed-at: 2025-12-20T18:32:15Z
Last-updated: 2025-12-20

---

## Goal

Upgrade the Национална художествена гимназия ‘Цанко Лавренов’ profile to the global high school profile template in `skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`, preserving verified local insights while filling template sections with current, sourced data.

---

## Context

- Existing profile: `bulgaria/entities/schools/profiles/plovdiv/national-art-school-tsanko-lavrenov/README.md`
- City directory: `bulgaria/entities/schools/profiles/plovdiv/`
- Keep the profile within this folder while aligning fully to the global template.
- Use `skills/high-school-profile-template/SKILL.md` and `skills/markdown-authoring` for structure, sourcing expectations, and style.

---

## Allowed write paths

- `bulgaria/entities/schools/profiles/plovdiv/national-art-school-tsanko-lavrenov/README.md`
- `bulgaria/entities/schools/profiles/plovdiv/national-art-school-tsanko-lavrenov/**`
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

- `bulgaria/entities/schools/profiles/plovdiv/national-art-school-tsanko-lavrenov/README.md` updated to match the global high school profile template with current data and sources.

---

## Acceptance criteria

- [x] Profile follows the sections and checklists from the global high school template with placeholders replaced or explicitly marked as open questions.
- [x] Local facts are sourced or flagged for follow-up; no speculative claims.
- [x] Profile remains at the same path with any new assets contained within the school folder; no broken links introduced.
- [x] No files modified outside `Allowed write paths`.

**What changed (2025-12-20):** Updated the Tsanko Lavrenov profile to the global template, added academic calendar details, refreshed specialization summary, and documented sources/open questions.

---

## Notes/Context

- Key sources to validate: recent admissions outcomes, tuition/fees, counselor contacts, outbound destinations, and language/exam tracks.
- Capture outstanding gaps in an **Open Questions** section within the profile.
