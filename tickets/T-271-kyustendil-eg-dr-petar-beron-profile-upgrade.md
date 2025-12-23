# T-271: EG ‘Dr. Petar Beron’ (Kyustendil) — upgrade to global high school profile standard

Status: done
Type: content
Priority: P1
Dependencies: T-026-high-school-profile-template, T-032-bulgaria-school-upgrade-ticketization
Claimed-by: work
Claimed-at: 2025-12-21T10:14:41+00:00
Last-updated: 2025-12-21

---

## Goal

Upgrade the EG ‘Dr. Petar Beron’ (Kyustendil) profile to the global high school profile template in `skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`, preserving verified local insights while filling template sections with current, sourced data.

---

## Context

- Existing profile: `bulgaria/entities/schools/profiles/other/BG_Kyustendil_EG_Dr-Petar-Beron.md`
- City directory: `bulgaria/entities/schools/profiles/other/`
- Migrate into `bulgaria/entities/schools/profiles/other/BG_Kyustendil_EG_Dr-Petar-Beron/README.md` if needed, leaving a short redirect note at `bulgaria/entities/schools/profiles/other/BG_Kyustendil_EG_Dr-Petar-Beron.md` so existing links remain valid.
- Use `skills/high-school-profile-template/SKILL.md` and `skills/markdown-authoring` for structure, sourcing expectations, and style.

---

## Allowed write paths

- `bulgaria/entities/schools/profiles/other/BG_Kyustendil_EG_Dr-Petar-Beron.md`
- `bulgaria/entities/schools/profiles/other/BG_Kyustendil_EG_Dr-Petar-Beron/**`
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

- `bulgaria/entities/schools/profiles/other/BG_Kyustendil_EG_Dr-Petar-Beron.md` refreshed to match the global high school profile structure (or `bulgaria/entities/schools/profiles/other/BG_Kyustendil_EG_Dr-Petar-Beron/README.md` with `bulgaria/entities/schools/profiles/other/BG_Kyustendil_EG_Dr-Petar-Beron.md` kept as a redirect if migrated).

---

## Acceptance criteria

- [x] Profile follows the sections and checklists from the global high school template with placeholders replaced or explicitly marked as open questions.
- [x] Local facts are sourced or flagged for follow-up; no speculative claims.
- [x] If the profile relocates to `bulgaria/entities/schools/profiles/other/BG_Kyustendil_EG_Dr-Petar-Beron/README.md`, the original file continues to resolve via a redirect note.
- [x] No files modified outside `Allowed write paths`.

---

## Notes/Context

- Key sources to validate: recent admissions outcomes, tuition/fees, counselor contacts, outbound destinations, and language/exam tracks.
- Capture outstanding gaps in an **Open Questions** section within the profile.

## What changed

- Updated the Kyustendil EG “Dr. Petar Beron” profile to the global template with leadership contacts, address, exam schedule dates, social links, and refreshed outreach questions. Redirect stub preserved.
