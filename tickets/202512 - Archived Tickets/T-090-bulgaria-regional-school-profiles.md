# T-090: Bulgaria regional school profiles (outside Sofia/Plovdiv/Varna)

Status: archived
Type: content
Priority: P1
Dependencies: T-026-high-school-profile-template
Claimed-by: work
Claimed-at: 2025-12-20T18:29:44+00:00
Last-updated: 2025-12-20

---

## Goal

Add recruiter-ready profiles for priority regional Bulgarian schools (outside Sofia, Plovdiv, and Varna) using the provided Bulgaria Regional Feeders report as the primary source. Profiles should follow the global high school profile template structure as closely as possible given available data.

---

## Context

- Work is limited to the `other/` catch-all under Bulgarian school profiles.
- Use the December 20, 2025 Bulgaria Regional Feeders report as the source for identity, affordability signals, and outreach playbooks.
- Align sections to the global `skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md` where possible; mark gaps clearly when data is missing.

---

## Allowed write paths

- `bulgaria/entities/schools/profiles/other/**`
- `tickets/T-073-bulgaria-regional-school-profiles.md`
- `research/**` (optional run notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/` files other than this ticket
- `.github/**`
- `scripts/**`

---

## Required outputs

Profiles created/updated under `bulgaria/entities/schools/profiles/other/`:
- `BG_Ruse_Leonardo-da-Vinci.md`
- `BG_Ruse_SOUEE_European-Languages.md`
- `BG_Blagoevgrad_EG_Acad-Lyudmil-Stoyanov.md`
- `BG_Burgas_AEG_Geo-Milev.md`
- `BG_Burgas_NEG_Goethe.md`
- `BG_Burgas_PPMG_Acad-Nikola-Obreshkov.md`
- `BG_Stara-Zagora_GPCE_Romain-Rolland.md`
- `BG_Stara-Zagora_PPMG_Geo-Milev.md`
- `BG_Veliko-Tarnovo_PMG_Vasil-Drumev.md`
- `BG_Haskovo_EG_Asen-Zlatarov.md`
- `BG_Kyustendil_EG_Dr-Petar-Beron.md`
- `BG_Pernik_GPCE_Simeon-Radev.md`

---

## Acceptance criteria

- Each required profile file exists under `bulgaria/entities/schools/profiles/other/` and follows a consistent section structure inspired by the global high school profile template (snapshot, identity/access, academic/international profile, affordability signals, outreach plan, validation questions, sources/gaps).
- Content is sourced from the Bulgaria Regional Feeders report dated December 20, 2025; any assumptions or gaps are explicitly labeled.
- No edits occur outside `Allowed write paths`.
- This ticket is updated to reflect completion status when work is done.

---

## Execution notes (optional)

- What changed: Added 12 regional Bulgarian school profiles (outside Sofia/Plovdiv/Varna) under `bulgaria/entities/schools/profiles/other/`, aligning to the global high school profile structure using the Bulgaria Regional Feeders report.
- Follow-ups: None; future steps are validation of contacts and placement data per profile questions.
