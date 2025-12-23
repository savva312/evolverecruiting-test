# T-438: Bulgaria — upgrade competitor profiles to primary sources + add tuition snapshots

Status: done
Type: qa
Priority: P2
Dependencies: T-416 (optional)
Claimed-by: evoticketresolver_pgb_aw5a
Claimed-at: 2025-12-22T19:59:24Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Improve credibility and usability of the existing Bulgaria competitor profiles by replacing Wikipedia-only sourcing with primary sources (official websites, tuition pages, admissions pages) and adding a concise, recruiter-usable tuition/admissions snapshot.

Scope is intentionally limited to the existing three profiles.

---

## Context

Competitor profiles currently rely heavily on Wikipedia extracts:
- `countries/bulgaria/entities/competitors/profiles/american-university-in-bulgaria.md`
- `countries/bulgaria/entities/competitors/profiles/new-bulgarian-university.md`
- `countries/bulgaria/entities/competitors/profiles/technical-university-of-sofia.md`

---

## Allowed write paths

- `tickets/T-438-bulgaria-competitor-profiles-primary-sources.md`
- `countries/bulgaria/entities/competitors/profiles/american-university-in-bulgaria.md`
- `countries/bulgaria/entities/competitors/profiles/new-bulgarian-university.md`
- `countries/bulgaria/entities/competitors/profiles/technical-university-of-sofia.md`
- `countries/bulgaria/entities/competitors/README.md` (only if minor navigation/source guidance needs updating)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/bulgaria/**`)

---

## Required outputs

- The three competitor profiles updated to include:
  - primary source links for tuition/admissions/program pages
  - `last_verified: YYYY-MM-DD` updated to reflect the new check date
  - removal (or de-emphasis) of Wikipedia API extract links as the main source

---

## Acceptance criteria

- [x] Each profile cites ≥2 primary sources (official domains) and any remaining Wikipedia content is clearly secondary/background.
- [x] No files outside `Allowed write paths` were modified.

---

## What changed

- Upgraded the three Bulgaria competitor profiles to cite primary sources (official admissions/fees/program pages) and moved Wikipedia to secondary/background only.
- Added a concise “Tuition & admissions snapshot” section to each profile and updated `last_verified` to 2025-12-22.
