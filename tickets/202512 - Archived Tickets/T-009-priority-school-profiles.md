# T-009: Priority Sofia and Plovdiv school profiles

Status: archived
Type: content
Priority: P0
Dependencies: (none)
Claimed-by: assistant-2025-12-20
Claimed-at: 2025-12-20T15:28:40+00:00
Last-updated: 2025-12-20
What changed: Added ACS and NPMG (Sofia) plus EG Plovdiv and Math HS Kiril Popov (Plovdiv) profiles; linked from entities/schools README.

---

## Goal

Create focused profiles for top secondary schools in Sofia and Plovdiv to target early counselor outreach for UNIC and UNIC Athens.

---

## Allowed write paths

- `entities/schools/profiles/sofia-*/**`
- `entities/schools/profiles/plovdiv-*/**`
- `entities/schools/README.md` (if adding navigation links)
- `research/**`
- `tickets/T-007-priority-school-profiles.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`
- `market/**`
- `program-clusters/**`
- `go-to-market/**`
- `data/**`
- `UNIC/**`

---

## Required outputs

- At least four school profile files (e.g., `entities/schools/profiles/sofia-<slug>.md` and `plovdiv-<slug>.md`) containing:
  - School type (language/IB/science), enrollment size, key programs.
  - Counselor contact placeholders and any known recruiting history.
  - Notes on mobility destinations and fit for UNIC vs UNIC Athens.
- Updated `entities/schools/README.md` linking to the new profiles (optional but preferred).

---

## Acceptance criteria

- Profiles are concise, bullet-based, and cite sources or note assumptions.
- Slugs are readable (e.g., `sofia-american-college.md`) and reflect city in filename.
- No files outside allowed paths are modified.
- Ticket status updated when claimed/done with a short “what changed” note.

---

## Notes/Context

Favor international/English-medium or high-performing state schools with university counseling presence. Capture any historical engagement with Cyprus/Greece institutions if available.
