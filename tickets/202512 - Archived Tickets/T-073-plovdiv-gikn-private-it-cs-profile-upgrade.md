# T-073: ЧПГ по информатика и КН ‘Акад. Благовест Сендов’ — upgrade to global high school profile standard

Status: archived
Type: content
Priority: P1
Dependencies: T-026-high-school-profile-template, T-032-bulgaria-school-upgrade-ticketization
Claimed-by: assistant-2025-12-20
Claimed-at: 2025-12-20T18:32:07+00:00
Last-updated: 2025-12-20
What changed: Profile aligned to global template with current tuition, admissions grade, contact lines, and next 90-day plan (2025-12-20).

---

## Goal

Upgrade the ЧПГ по информатика и КН ‘Акад. Благовест Сендов’ profile to the global high school profile template in `skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`, preserving verified local insights while filling template sections with current, sourced data.

---

## Context

- Existing profile: `bulgaria/entities/schools/profiles/plovdiv/gikn-private-it-cs/README.md`
- City directory: `bulgaria/entities/schools/profiles/plovdiv/`
- Keep the profile within this folder while aligning fully to the global template.
- Use `skills/high-school-profile-template/SKILL.md` and `skills/markdown-authoring` for structure, sourcing expectations, and style.

---

## Allowed write paths

- `bulgaria/entities/schools/profiles/plovdiv/gikn-private-it-cs/README.md`
- `bulgaria/entities/schools/profiles/plovdiv/gikn-private-it-cs/**`
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

- `bulgaria/entities/schools/profiles/plovdiv/gikn-private-it-cs/README.md` updated to match the global high school profile template with current data and sources.

---

## Acceptance criteria

- [ ] Profile follows the sections and checklists from the global high school template with placeholders replaced or explicitly marked as open questions.
- [ ] Local facts are sourced or flagged for follow-up; no speculative claims.
- [ ] Profile remains at the same path with any new assets contained within the school folder; no broken links introduced.
- [ ] No files modified outside `Allowed write paths`.

---

## Notes/Context

- Key sources to validate: recent admissions outcomes, tuition/fees, counselor contacts, outbound destinations, and language/exam tracks.
- Capture outstanding gaps in an **Open Questions** section within the profile.
