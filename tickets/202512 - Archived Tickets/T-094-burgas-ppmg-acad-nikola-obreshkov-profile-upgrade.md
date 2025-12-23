# T-094: PPMG ‘Acad. Nikola Obreshkov’ (Burgas) — upgrade to global high school profile standard

Status: archived
Type: content
Priority: P1
Dependencies: T-026-high-school-profile-template, T-032-bulgaria-school-upgrade-ticketization
Claimed-by: work
Claimed-at: 2025-12-20T19:19:14Z
Last-updated: 2025-12-20

---

## Goal

Upgrade the PPMG ‘Acad. Nikola Obreshkov’ (Burgas) profile to the global high school profile template in `skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`, preserving verified local insights while filling template sections with current, sourced data.

---

## Context

- Existing profile: `bulgaria/entities/schools/profiles/other/BG_Burgas_PPMG_Acad-Nikola-Obreshkov.md`
- City directory: `bulgaria/entities/schools/profiles/other/`
- Migrate into `bulgaria/entities/schools/profiles/other/BG_Burgas_PPMG_Acad-Nikola-Obreshkov/README.md` if needed, leaving a short redirect note at `bulgaria/entities/schools/profiles/other/BG_Burgas_PPMG_Acad-Nikola-Obreshkov.md` so existing links remain valid.
- Use `skills/high-school-profile-template/SKILL.md` and `skills/markdown-authoring` for structure, sourcing expectations, and style.

---

## Allowed write paths

- `bulgaria/entities/schools/profiles/other/BG_Burgas_PPMG_Acad-Nikola-Obreshkov.md`
- `bulgaria/entities/schools/profiles/other/BG_Burgas_PPMG_Acad-Nikola-Obreshkov/**`
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

- `bulgaria/entities/schools/profiles/other/BG_Burgas_PPMG_Acad-Nikola-Obreshkov.md` refreshed to match the global high school profile structure (or `bulgaria/entities/schools/profiles/other/BG_Burgas_PPMG_Acad-Nikola-Obreshkov/README.md` with `bulgaria/entities/schools/profiles/other/BG_Burgas_PPMG_Acad-Nikola-Obreshkov.md` kept as a redirect if migrated).

---

## Acceptance criteria

- [ ] Profile follows the sections and checklists from the global high school template with placeholders replaced or explicitly marked as open questions.
- [ ] Local facts are sourced or flagged for follow-up; no speculative claims.
- [ ] If the profile relocates to `bulgaria/entities/schools/profiles/other/BG_Burgas_PPMG_Acad-Nikola-Obreshkov/README.md`, the original file continues to resolve via a redirect note.
- [ ] No files modified outside `Allowed write paths`.

---

## Notes/Context

- Key sources to validate: recent admissions outcomes, tuition/fees, counselor contacts, outbound destinations, and language/exam tracks.
- Capture outstanding gaps in an **Open Questions** section within the profile.
- What changed: migrated profile to global template in subfolder, added redirect, preserved opportunities/risks, and logged remaining data gaps.
