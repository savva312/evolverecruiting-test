# T-260: Bulgaria high-priority school audit (README + index + CSV)

Status: done
Type: qa
Priority: P0
Dependencies: T-073-bulgaria-regional-school-profiles
Claimed-by: work
Claimed-at: 2025-12-21T09:18:51Z
Last-updated: 2025-12-21
What changed: Updated Bulgaria school navigation (Sofia, regional hubs) and regenerated `data/entities/schools.csv` to include all high-priority profiles; no missing schools identified, so no new tickets were required.

---

## Goal

Review all high-priority Bulgarian school profiles and ensure navigation (README + city/“other” indexes) and `data/entities/schools.csv` are in sync with the latest profiles. Identify any missing profiles that should exist and ticketize them.

---

## Allowed write paths

- `countries/bulgaria/entities/schools/**`
- `countries/bulgaria/data/entities/schools.csv`
- `tickets/T-227-bulgaria-high-priority-schools-audit.md`
- `tickets/T-228-*.md`
- `executions/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/README.md`
- `.github/**`
- `scripts/**`

---

## Required outputs

- Updated `countries/bulgaria/entities/schools/README.md` and relevant city/“other” index files to list all existing high-priority school profiles with correct links.
- Refreshed `countries/bulgaria/data/entities/schools.csv` containing one row per high-priority school profile with current IDs, names, city/region, type, ownership, contact email if available, concise notes, and `as_of` date.
- New follow-up ticket(s) under `tickets/T-228-*.md` for any missing high-priority school profiles discovered.

---

## Acceptance criteria

- Navigation pages list every existing high-priority profile (Sofia, Plovdiv, Varna, and regional cities) with working relative links; no duplicates or missing entries.
- `schools.csv` rows align one-to-one with the high-priority profiles, follow the dictionary in `countries/bulgaria/data/entities/schools-dictionary.md`, and use deterministic IDs and ISO `as_of` dates.
- Any gap (high-priority school lacking a profile) is documented via a newly created ticket in the allowed path.
- No changes occur outside allowed paths; ticket status fields are updated on completion.

---

## Notes/Context

- Use existing profile paths as the source of truth for names and emails; leave contact fields blank if not published.
- Keep IDs stable and deterministic (e.g., `sch-bg-<city>-<slug>`).
