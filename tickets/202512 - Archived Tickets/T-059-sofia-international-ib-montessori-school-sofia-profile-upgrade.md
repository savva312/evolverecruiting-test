# T-059: International IB Montessori School (Sofia) — upgrade to global high school profile standard

Status: archived
Type: content
Priority: P1
Dependencies: T-026-high-school-profile-template, T-032-bulgaria-school-upgrade-ticketization
Claimed-by: work
Claimed-at: 2025-12-20T18:30:32Z
Last-updated: 2025-12-20

---

## Goal

Upgrade the International IB Montessori School (Sofia) profile to the global high school profile template in `skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`, preserving verified local insights while filling template sections with current, sourced data.

---

## Context

- Existing profile: `bulgaria/entities/schools/profiles/sofia/international-ib-montessori-school-sofia.md`
- City directory: `bulgaria/entities/schools/profiles/sofia/`
- Migrate into `bulgaria/entities/schools/profiles/sofia/international-ib-montessori-school-sofia/README.md` if needed, leaving a short redirect note at `bulgaria/entities/schools/profiles/sofia/international-ib-montessori-school-sofia.md` so existing links remain valid.
- Use `skills/high-school-profile-template/SKILL.md` and `skills/markdown-authoring` for structure, sourcing expectations, and style.

---

## Allowed write paths

- `bulgaria/entities/schools/profiles/sofia/international-ib-montessori-school-sofia.md`
- `bulgaria/entities/schools/profiles/sofia/international-ib-montessori-school-sofia/**`
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

- `bulgaria/entities/schools/profiles/sofia/international-ib-montessori-school-sofia.md` refreshed to match the global high school profile structure (or `bulgaria/entities/schools/profiles/sofia/international-ib-montessori-school-sofia/README.md` with `bulgaria/entities/schools/profiles/sofia/international-ib-montessori-school-sofia.md` kept as a redirect if migrated).

---

## Acceptance criteria

- [ ] Profile follows the sections and checklists from the global high school template with placeholders replaced or explicitly marked as open questions.
- [ ] Local facts are sourced or flagged for follow-up; no speculative claims.
- [ ] If the profile relocates to `bulgaria/entities/schools/profiles/sofia/international-ib-montessori-school-sofia/README.md`, `bulgaria/entities/schools/profiles/sofia/international-ib-montessori-school-sofia.md` continues to resolve via a redirect note.
- [ ] No files modified outside `Allowed write paths`.

---

## Notes/Context

- Key sources to validate: recent admissions outcomes, tuition/fees, counselor contacts, outbound destinations, and language/exam tracks.
- Capture outstanding gaps in an **Open Questions** section within the profile.
- Completion (2025-12-20): Migrated profile to global template, emphasized affordability positioning, and logged data gaps/open questions for follow-up.
