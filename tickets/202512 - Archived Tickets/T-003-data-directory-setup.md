# T-003: Add canonical data directory scaffolding

Status: archived
Type: structure
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-20T14:21:14Z
Last-updated: 2025-12-20

---

## Goal

Create the initial `data/` directory structure with placeholder CSVs and a README to house authoritative structured datasets for Bulgaria recruiting work.

---

## Context

We need a consistent home for datasets covering entities, programs, marketing, and operations to support recruiting plans for UNIC and UNIC Athens.

---

## Allowed write paths

- `data/**`
- `tickets/T-003-data-directory-setup.md`
- `research/**`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file)
- `.github/**`
- `scripts/**`

---

## Required outputs

- `data/README.md`
- `data/entities/schools.csv`
- `data/entities/agents.csv`
- `data/entities/government-regulators.csv`
- `data/entities/ngos-sgos.csv`
- `data/entities/fairs-events.csv`
- `data/entities/competitors.csv`
- `data/programs/<your-programs>.csv`
- `data/programs/competitor-programs.csv`
- `data/programs/scholarships-discounts.csv`
- `data/marketing/keywords.csv`
- `data/marketing/channel-benchmarks.csv`
- `data/marketing/creatives-inventory.csv`
- `data/operations/<topic-calendar>.csv`
- `data/operations/funnel-metrics.csv`
- `data/operations/budget-model.csv`

---

## Acceptance criteria

- The `data/` directory exists with the subfolders and files listed above, containing stub headers that reflect intended content.
- `data/README.md` explains the structure and intended use of each subfolder.
- No files are modified outside the allowed write paths.
- Ticket status and metadata are updated to reflect progress and completion.

---

## Execution notes (optional)

- What changed (short): Added `data/` scaffold with README and placeholder CSV headers across entities, programs, marketing, and operations datasets.
- Follow-ups suggested: Populate each CSV with sourced data and add data dictionaries where fields may be ambiguous.
