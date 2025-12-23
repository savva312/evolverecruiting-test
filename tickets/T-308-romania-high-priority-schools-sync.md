# T-308: Romania — high-priority school readme/index/CSV sync

Status: done
Type: data
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-21T17:22:38Z
Last-updated: 2025-12-21
Completed-at: 2025-12-21T17:45:00Z

---

## Goal

Review all existing **high-priority Romanian school profiles** and make sure the schools README, the high-priority index, and the high-potential CSV reflect the latest information captured in those profiles. Document which high-priority schools still lack profiles and generate tickets for any gaps so the backlog is complete.

---

## Context

- Scope: high-priority secondary schools in Romania (Tier A/B/C from the feeder map and related profile tickets T-149–T-174).
- Existing sources: `countries/romania/entities/schools/profiles/**`, `countries/romania/entities/schools/high-potential-feeder-high-schools.md`, `countries/romania/data/entities/schools/romania-high-potential-feeder-high-schools.csv`, and `countries/romania/entities/schools/README.md`.
- Templates/skills: `/skills/schools-and-feeders/SKILL.md`, `/skills/high-school-profile-template/HIGH-SCHOOL-PROFILE-TEMPLATE.md`.

---

## Allowed write paths

- `tickets/T-276-romania-high-priority-schools-sync.md`
- `countries/romania/entities/schools/**`
- `countries/romania/data/entities/schools/**`
- `executions/**` (optional for run notes)
- `tickets/T-23*-*.md` (only if new tickets are needed for missing profiles)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`
- `tickets/**` (except this ticket file and any new tickets for missing profiles)
- Country directories other than `countries/romania/**`

---

## Required outputs

- Updated `countries/romania/entities/schools/README.md` summarizing high-priority coverage and linking to profiles/tickets.
- Updated `countries/romania/entities/schools/high-potential-feeder-high-schools.md` with an index of high-priority schools (profile status + ticket linkage).
- Clean, deduplicated `countries/romania/data/entities/schools/romania-high-potential-feeder-high-schools.csv` aligned to the latest profile facts (tiers, pathways, affordability signals, recruitment status).
- New tickets created for any high-priority schools lacking profiles and existing tickets.

---

## Acceptance criteria

- [x] README and index list all high-priority Romanian schools with clear links to profiles or tickets; notes flag any missing profiles.
- [x] CSV contains a single header row and one row per high-priority school with fields consistent with the index (school_id, city/region, tier, pathway, affordability signal, program-fit tags, recruitment status, sources, last_verified).
- [x] Any missing-profile schools have dedicated tickets created under `tickets/` (if not already present).
- [x] No files modified outside the allowed write paths; links and slugs match existing profile/ticket IDs.

---

## Execution notes (optional)

- What changed (short): Refreshed Romania schools README and coverage index to reflect 26/26 live high-priority profiles; cleaned the high-potential CSV to a single header with one row per school and dictionary-aligned fields/statuses; updated statuses to show no pending profile gaps.
- Open questions: Fee schedules and pathway validation remain pending for schools marked `verify_fees` or `verify_pathway` in the CSV/index.
- Follow-up tickets suggested: None; all high-priority profiles exist (focus on fee/pathway verification inside the current dataset).
