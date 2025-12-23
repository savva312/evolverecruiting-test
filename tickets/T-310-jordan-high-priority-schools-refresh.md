# T-310: Jordan high-priority school profiles refresh (index + CSV QA)

Status: done
Type: content
Priority: P0
Claimed-by: work
Claimed-at: 2025-12-21T17:23:19+00:00
Last-updated: 2025-12-21

---

## Goal

Review all existing **high-priority (Tier 1)** Jordan school profiles and ensure the country school README, index tables, and structured CSV reflect the latest data captured in the profiles. Fill any gaps between profiles and data and surface missing Tier 1 profiles via follow-on tickets.

## Context

- Multiple Tier 1 profiles were added recently without synchronized updates to the index and CSV.
- Use the global high-school template (`/skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`) and Jordan addendum (`/countries/jordan/skills/jordan-schools-and-feeders/SKILL.md`) as reference.

## Allowed write paths

- `tickets/T-278-jordan-high-priority-schools-refresh.md`
- `countries/jordan/entities/schools/**`
- `countries/jordan/data/entities/schools.csv`
- `tickets/T-23*-jordan-high-priority-school-profile-*.md` (new follow-on tickets for missing Tier 1 profiles)

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except paths listed in allowed write paths)
- Country directories other than `countries/jordan/**`

## Required outputs

- Updated `countries/jordan/entities/schools/README.md` with a clean, deduplicated tier table and notes aligned to refreshed profiles, including clear profile links/status.
- `countries/jordan/data/entities/schools.csv` refreshed to match the Tier 1 profiles (fee evidence, contact info, visit guidance, last verified dates) without duplicate rows.
- If any Tier 1 school lacks a profile, a new ticket is created for that profile under `tickets/T-23*-jordan-high-priority-school-profile-<slug>.md`.

## Acceptance criteria

- Ticket status/claim metadata reflects current execution.
- School README tier list aligns with refreshed CSV (no duplicates, consistent fees/curricula, profile link coverage noted).
- `schools.csv` is deduplicated and contains the latest contact/fee/visit info from profiles with populated `last_verified` dates.
- Follow-on tickets exist for any missing Tier 1 profiles (if none missing, state explicitly in README "All Tier 1 profiles present").
- No writes occur outside allowed paths.

## Execution notes

- Use profile files as the source of truth for each Tier 1 entry; update README and CSV accordingly.
- Normalize currencies/fees and evidence tags following the global skill.
- Synced Tier 1 table and `schools.csv` to the latest eight profiles (King’s, ACS, ICS, ABS, IAA, NES, MAS, Amman Academy); removed duplicates and aligned fee/visit/contact notes. ACS entry now carries USD→JOD conversion note and site-form contact flag; ABS/IAA/NES/Amman Academy notes reflect routing paths and scholarship/IB outcomes. All Tier 1 profiles already exist, so no follow-on profile tickets were required.
- 2025-12-21 refresh: re-validated Tier 1 data against profiles, set `last_verified` to 2025-12-21 across Tier 1, cleaned `schools.csv` column alignment (blank contact fields), and removed the legacy secondary dataset tail.
