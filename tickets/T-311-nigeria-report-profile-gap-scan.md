# T-311: Nigeria premium school report vs profile gap scan

Status: done  
Type: qa  
Priority: P1  
Dependencies: (none)  
Claimed-by: work  
Claimed-at: 2025-12-21T09:25:44Z  
Last-updated: 2025-12-21

---

## Goal

Identify any Nigerian premium secondary schools listed in the **20251220 Nigeria Premium Secondary School Pipeline** report that do **not** have profiles under `countries/nigeria/entities/schools/profiles/**`, and generate individual tickets to profile the missing schools.

## Context

- The Nigeria high-priority school set currently shows 61 profiled schools across 18 cities (see `countries/nigeria/entities/schools/index.md`).
- The pipeline report at `countries/nigeria/reports/20251220-Nigeria Premium Secondary School Pipeline.md` is the authoritative list of premium secondary schools as of 2025-12-20.
- This ticket ensures the profiled set matches the report and surfaces any gaps via new tickets.

## Allowed write paths

- `tickets/**`
- `executions/**`

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- Any `countries/**` path
- `.github/**`
- `scripts/**`

## Required outputs

- Execution note (or short summary in this ticket) that lists any schools found in the report without corresponding profiles, with city and evidence strength.
- New ticket(s) under `tickets/` for each missing school, each including:
  - Status set to `open`
  - Allowed/forbidden write paths scoped to Nigeria school profiles and data
  - Required outputs and acceptance criteria for creating the profile and updating the roster/index.
- Ticket updated to `done` with a brief “What changed” summary once the gap list and follow-up tickets are created.

## Acceptance criteria

- [x] Cross-check performed between the report’s school roster and existing profiles, with findings documented in `executions/**` or this ticket.
- [x] Every school present in the report but missing a profile has its own properly formatted ticket in `tickets/` with Nigeria-scoped allowed paths and clear outputs.
- [x] No modifications occur outside `Allowed write paths`.
- [x] This ticket status moved to `done` upon completion, with “What changed” noted.

## Execution notes (optional)

- Cross-checked 59 schools listed in `countries/nigeria/reports/20251220-Nigeria Premium Secondary School Pipeline.md` against the 61 profiled schools in `countries/nigeria/entities/schools/index.md` using a similarity check; every report school already has a profile (no gaps found), so no follow-up profile tickets were needed.
- Observed that the profiled set includes a couple of Ibadan schools (IIS and ISI) that were not in the report; they remain in place from prior work.
- What changed: Added this ticket to document the gap scan and confirmed no new Nigeria school-profile tickets are required from the Dec 20, 2025 report.
