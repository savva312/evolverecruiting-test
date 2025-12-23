# T-041: Plovdiv priority school profile refresh

Status: archived
Type: content  
Priority: P1  
Dependencies: (none)  
Claimed-by: assistant  
Claimed-at: 2025-02-09T00:00:00Z  
Last-updated: 2025-02-09  
What changed: Added template-based profiles for Plovdiv priority schools (Tier 1 and Tier 2), refreshed Plovdiv index, and linked profiles from the Bulgaria schools index.

---

## Goal

Update and expand Plovdiv school profiles with evidence from the December 20, 2025 feeder report so recruiters can target realistic feeders for UNIC Nicosia and UNIC Athens.

---

## Allowed write paths

- `bulgaria/entities/schools/profiles/plovdiv/**`
- `bulgaria/entities/schools/README.md`
- `research/**`
- `tickets/T-030-plovdiv-profile-updates.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/README.md`
- `.github/**`
- `UNIC/**`
- Country directories other than `bulgaria/**`

---

## Required outputs

- Updated Plovdiv school profiles for existing targets (EG Plovdiv, MG “Acad. Kiril Popov”).
- New profiles for additional Plovdiv priority schools surfaced in the report (e.g., Classic, Druzhba, Stoyanstroi/Stoyan Sariev, French Language Gymnasium, EG “Ivan Vazov”, Talantite, GIKN, Humanities Gymnasium, Stage/Screen Arts, Tsanko Lavrenov).
- Plovdiv schools index reflecting the refreshed profile set.
- Cross-links added in `bulgaria/entities/schools/README.md` for the new Plovdiv profiles.

---

## Acceptance criteria

- Profiles follow the global high-school template structure and capture the new report signals (international orientation, ability-to-pay proxies, UNIC fit, missing info to validate).
- Facts drawn from the provided report are identified; uncertain items remain as `{ }` or in open questions.
- No edits outside allowed paths.
- Ticket status updated to `done` with a short change note after work is complete.

---

## Notes/Context

- Treat Athens Medicine as a micro-segment; mark it clearly in UNIC fit sections.
- Where tuition or placement data are unknown, keep them flagged for validation instead of inferring.
