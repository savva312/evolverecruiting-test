# T-450: Romania — populate `countries/romania/data/programs/competitor-programs.csv` (v1)

Status: done
Type: data
Priority: P1
Dependencies: T-447, T-466
Claimed-by: codex-run-20251222
Claimed-at: 2025-12-22T00:00Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Populate `countries/romania/data/programs/competitor-programs.csv` with a first, Romania-relevant competitor program list for:
- Medicine/MD (priority)
- CS/Data/AI/Cyber (priority)
- Business/Finance/Accounting/Marketing (priority)

Focus on **programs Romanian applicants actually compare** against UNIC/UNIC Athens, with tuition + language + intake + admissions signal fields and sources.

---

## Context

Related Romania content:
- Cluster folders under `countries/romania/program-clusters/` (competitor sets are currently incomplete and in some cases incorrect).
- Entity competitor dataset to be built in T-447.
- CSV scaffold: `countries/romania/data/programs/competitor-programs.csv`
- Dictionary scaffold: `countries/romania/data/programs/competitor-programs-dictionary.md`

---

## Allowed write paths

- `tickets/T-450-romania-competitor-programs-csv-v1.md`
- `countries/romania/data/programs/competitor-programs.csv`
- `countries/romania/data/programs/competitor-programs-dictionary.md`
- `executions/**` (optional for notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`
- `tickets/**` (except this ticket file)
- `countries/**` (except `countries/romania/data/programs/**`)

---

## Required outputs

- Updated `countries/romania/data/programs/competitor-programs.csv` (minimum: 20 meaningful rows across the three priority clusters)
- Updated `countries/romania/data/programs/competitor-programs-dictionary.md`

---

## Acceptance criteria

- [x] Dataset has at least 20 rows across Medicine, CS, and Business clusters, each with a source and `as_of` date.
- [x] Tuition fields are numeric where declared numeric; currencies are explicit where needed.
- [x] Dictionary matches dataset exactly.
- [x] No edits outside allowed paths.

**What changed:** Populated `countries/romania/data/programs/competitor-programs.csv` with 20 sourced entries (Medicine/CS/Business) and synchronized `competitor-programs-dictionary.md` with the notes format.
