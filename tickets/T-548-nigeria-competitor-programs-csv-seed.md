# T-548: Nigeria — Seed `competitor-programs.csv` (30+ rows, top clusters)

Status: open
Type: data
Priority: P1
Dependencies: T-459
Claimed-by:
Claimed-at:
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Populate `countries/nigeria/data/programs/competitor-programs.csv` with a practical baseline of competitor offerings and tuition cues that can be used for counseling and positioning (focus: Medicine, CS/Data, Business).

---

## Context

- File is currently header-only: `countries/nigeria/data/programs/competitor-programs.csv`
- Schema: `countries/nigeria/data/programs/competitor-programs-dictionary.md`
- The program-cluster pages will reference this data when completed:
  - `countries/nigeria/program-clusters/medicine-md/`
  - `countries/nigeria/program-clusters/cs-data-ai-cyber/`
  - `countries/nigeria/program-clusters/business-finance-accounting-marketing/`

---

## Allowed write paths

- `countries/nigeria/data/programs/competitor-programs.csv`
- `executions/T-461-nigeria-competitor-programs-csv-seed/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket for status updates)
- `countries/**` (except `countries/nigeria/**`)

---

## Required outputs

- `countries/nigeria/data/programs/competitor-programs.csv`

---

## Acceptance criteria

- [ ] CSV contains **≥ 30 rows** across at least 10 institutions
- [ ] Every row includes `program_id`, `institution`, `program_name`, `level`, `cluster`, `duration`, and `as_of`
- [ ] `tuition_eur` is only provided when a credible source exists; source link included in `notes`
- [ ] No invented numbers; unknown tuition is left blank with an explicit “tuition unknown” note + source attempt

