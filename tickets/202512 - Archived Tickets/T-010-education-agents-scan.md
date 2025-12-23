# T-010: Bulgaria education agents scan

Status: archived
Type: content
Priority: P0
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T15:29:58+00:00
Last-updated: 2025-12-20

What changed: Added five agent profiles (Integral, Darbi, UNIFY, StudyAbroad.bg, Edlanta), updated agents README with links, and logged research notes.

---

## Goal

Identify and profile leading education agents/counseling firms in Bulgaria that could recruit for UNIC and UNIC Athens.

---

## Allowed write paths

- `entities/agents/profiles/**`
- `entities/agents/README.md` (if adding navigation links)
- `research/**`
- `tickets/T-008-education-agents-scan.md`

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

- At least five agent profile files (e.g., `entities/agents/profiles/<slug>.md`) capturing:
  - Services offered, geographies, and target destinations.
  - Ownership/credibility signals, certifications (ICEF, British Council, etc.).
  - Historical placement data if available; focus on EU/Cyprus/Greece relevance.
  - Contact placeholders and compliance risks (e.g., subagents, fee structures).
- Optional summary bullets appended to `entities/agents/README.md` with links.

---

## Acceptance criteria

- Profiles use concise bullets with sources/links or explicit assumptions.
- Slugs are readable and consistent (lowercase, hyphen-separated).
- No files outside allowed paths are modified.
- Ticket status updated when claimed/done with a short “what changed” note.

---

## Notes/Context

Prioritize agents visible in Sofia/Plovdiv/Varna/Burgas and those marketing healthcare, business, and tech programs. Include any Greece/Cyprus specialization.
