# T-101: PPMG ‘Geo Milev’ (Stara Zagora) — upgrade to global high school profile standard

Status: done
Type: content
Priority: P1
Dependencies: T-026-high-school-profile-template, T-032-bulgaria-school-upgrade-ticketization
Claimed-by: work
Claimed-at: 2025-12-20T19:20:32Z
Last-updated: 2025-12-20

---

## Goal

Upgrade the PPMG ‘Geo Milev’ (Stara Zagora) profile to the global high school profile template in `skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`, preserving verified local insights while filling template sections with current, sourced data.

---

## Context

- Existing profile: `bulgaria/entities/schools/profiles/other/BG_Stara-Zagora_PPMG_Geo-Milev.md`
- City directory: `bulgaria/entities/schools/profiles/other/`
- Migrate into `bulgaria/entities/schools/profiles/other/BG_Stara-Zagora_PPMG_Geo-Milev/README.md` if needed, leaving a short redirect note at `bulgaria/entities/schools/profiles/other/BG_Stara-Zagora_PPMG_Geo-Milev.md` so existing links remain valid.
- Use `skills/high-school-profile-template/SKILL.md` and `skills/markdown-authoring` for structure, sourcing expectations, and style.

---

## Allowed write paths

- `bulgaria/entities/schools/profiles/other/BG_Stara-Zagora_PPMG_Geo-Milev.md`
- `bulgaria/entities/schools/profiles/other/BG_Stara-Zagora_PPMG_Geo-Milev/**`
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

- `bulgaria/entities/schools/profiles/other/BG_Stara-Zagora_PPMG_Geo-Milev.md` refreshed to match the global high school profile structure (or `bulgaria/entities/schools/profiles/other/BG_Stara-Zagora_PPMG_Geo-Milev/README.md` with `bulgaria/entities/schools/profiles/other/BG_Stara-Zagora_PPMG_Geo-Milev.md` kept as a redirect if migrated).

---

## Acceptance criteria

- [ ] Profile follows the sections and checklists from the global high school template with placeholders replaced or explicitly marked as open questions.
- [ ] Local facts are sourced or flagged for follow-up; no speculative claims.
- [ ] If the profile relocates to `bulgaria/entities/schools/profiles/other/BG_Stara-Zagora_PPMG_Geo-Milev/README.md`, the original file continues to resolve via a redirect note.
- [ ] No files modified outside `Allowed write paths`.

---

## Notes/Context

- Key sources to validate: recent admissions outcomes, tuition/fees, counselor contacts, outbound destinations, and language/exam tracks.
- Capture outstanding gaps in an **Open Questions** section within the profile.
- What changed (2025-12-20): Updated profile to the global template with verified contacts, outreach plan, and open questions for missing data.
