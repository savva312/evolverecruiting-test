# /executions/ (Archive)

This folder contains **archived run outputs** from /executions/.

A “run” is a single EvoBuilder execution against this repo that produces:
- a run plan
- analyst research rounds
- a workplan
- per-block outputs
- ticket deliverables elsewhere in the repo
- often a PR link

Current staging area for new runs: `/executions/202512 runs/`. Create timestamped folders there until a new window is designated.

During the run, EvoBuilder writes to:
- `executions/<run_id>/`

…and then records the run in:
- `executions/index.md`

---

## Run folder naming

Use:

- `YYYY-MM-DD_HHMMSS/`

Example:
- `2025-12-20_141530/`

---

## What a run folder should contain

Minimum recommended contents:
- `run_manifest.md`  
  A short summary including:
  - run id
  - date/time
  - request / intent
  - tickets executed
  - PR link (if any)
  - status
  - notes / known issues

And the run artifacts:
- `evobuilder_run_plan.md`
- `evobuilder_workplan.md`
- `round_1_research.md`, `round_2_research.md`, ...
- `section_1.md`, `section_2.md`, ...

Optional:
- `assembled.md` if you produce a single assembled narrative from the block outputs
- any additional run-scoped diagnostics



## Boundary reminder

`executions/` is for run artifacts only.

Ticket deliverables should live in their “real” locations, defined by each ticket’s `allowed_write_paths`.
