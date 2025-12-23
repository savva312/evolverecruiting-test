# T-269: PGKMKS ‘Acad. Blagovest Sendov’ — upgrade to global high school profile standard

Status: done
Type: content
Priority: P1
Dependencies: T-026-high-school-profile-template, T-032-bulgaria-school-upgrade-ticketization
Claimed-by: work
Claimed-at: 2025-12-21T10:14:52Z
Last-updated: 2025-12-21

---

## Goal

Upgrade the PGKMKS ‘Acad. Blagovest Sendov’ profile to the global high school profile template in `skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`, preserving verified local insights while filling template sections with current, sourced data.

---

## Context

- Existing profile: `countries/bulgaria/entities/schools/profiles/varna/pgkmks-akad-blagovest-sendov/README.md`
- City directory: `countries/bulgaria/entities/schools/profiles/varna/`
- Keep the profile within this folder while aligning fully to the global template.
- Use `skills/high-school-profile-template/SKILL.md` and `skills/markdown-authoring` for structure, sourcing expectations, and style.

---

## Allowed write paths

- `countries/bulgaria/entities/schools/profiles/varna/pgkmks-akad-blagovest-sendov/README.md`
- `countries/bulgaria/entities/schools/profiles/varna/pgkmks-akad-blagovest-sendov/**`
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

- `countries/bulgaria/entities/schools/profiles/varna/pgkmks-akad-blagovest-sendov/README.md` updated to match the global high school profile template with current data and sources.

---

## Acceptance criteria

- [x] Profile follows the sections and checklists from the global high school template with placeholders replaced or explicitly marked as open questions.
- [x] Local facts are sourced or flagged for follow-up; no speculative claims.
- [x] Profile remains at the same path with any new assets contained within the school folder; no broken links introduced.
- [x] No files modified outside `Allowed write paths`.

---

## Notes/Context

- Key sources to validate: recent admissions outcomes, tuition/fees, counselor contacts, outbound destinations, and language/exam tracks.
- Capture outstanding gaps in an **Open Questions** section within the profile.

## What changed

- Refreshed the Varna PGKMKS profile to the global high school template with 2024/2025 and 2025/2026 program details, grading system, outreach plan, and updated sourcing.
