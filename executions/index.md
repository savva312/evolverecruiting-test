# /executions/ index

This file is a lightweight registry of /executions/.

Current staging window: add new runs under `/executions/202512 runs/` using timestamped folder names.

Each run should have:
- a folder under `executions/<run_id>/`
- a `run_manifest.md` inside the folder
- an entry below

---

## Runs

### 2025-12-22_204900 — T-492 Romania competitors CSV v1
- Run folder: `executions/202512 runs/2025-12-22_204900/`
- Status: `success`
- Date: `2025-12-22`
- PR: `none`
- Tickets: `T-492`
- Summary:
  - Populated `countries/romania/data/entities/competitors.csv` (2 rows) and aligned `competitors-dictionary.md` to the final schema
- Notes / Issues:
  - Ticket metadata appears inconsistent (`Allowed write paths` references `tickets/T-447-...`); ticket status was not updated in-file in this run

### <run_id> — <short title / intent>
- Run folder: `executions/<run_id>/`
- Status: `<success | partial | failed>`
- Date: `<YYYY-MM-DD>`
- PR: `<link or "none">`
- Tickets: `<T-001, T-002, ...>`
- Summary:
  - <1–3 bullets about what happened / key outputs>
- Notes / Issues:
  - <1–3 bullets about problems, blockers, boundary issues, or follow-ups>

---

### (example) 2025-12-20_141530 — Bulgaria school list bootstrap
- Run folder: `executions/2025-12-20_141530/`
- Status: `partial`
- Date: `2025-12-20`
- PR: `https://github.com/<org>/<repo>/pull/<id>`
- Tickets: `T-001, T-003`
- Summary:
  - Created initial `data/entities/schools.csv` with 25 rows
  - Added draft playbook section for counselor outreach
- Notes / Issues:
  - Needs verification pass for 10 rows (missing official URLs)
  - Ticket T-003 blocked on acceptance criteria clarification
