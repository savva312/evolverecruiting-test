# Research Reports

This folder contains **polished, stakeholder-ready narrative outputs**.

For now, these will be manually uploaded by humans and so agents should never write to this folder unless specifically requested to do so

These files should be:
- readable end-to-end without extra context
- internally consistent
- easy to cite, share, and review
- linked to the underlying tickets and data


If you’re looking for run logs and per-run artifacts, use:
- `../../executions/` (archived runs)

---

## Folder layout

Keep this folder flat: store each report markdown directly under `reports/`. Add any annexes alongside the parent report instead of nesting inside additional subfolders.

---

## File naming

Use:

- `YYYY-MM-DD-<slug>.md`

Examples:
- `2025-12-18-unic-athens-bulgaria-recruitment-plan.md`
- `2026-01-05-competitor-snapshot-medicine-md.md`

---

## Recommended report structure

Most reports should include:

1) **Title**
2) **Context / purpose**
3) **Scope** (what is included / excluded)
4) **Key findings**
5) **Recommendations / actions**
6) **Risks & open questions**
7) **Appendix** (optional)
8) **Sources** (URLs)

When relevant, include pointers to:
- the ticket(s) this report fulfills
- the datasets used/updated under `../data/`
- relevant entity profiles under `../entities/`
- relevant playbooks under `../go-to-market/`

---

## Stability and updates

Reports are “polished,” but not immutable. If updating:
- add a short **Changelog** section near the top (optional)
- preserve key decisions and make changes explicit
- if a report becomes outdated, consider writing a new one and linking them

---

## What does NOT belong here

Do not put:
- raw research dumps
- big unordered lists of links without commentary
- partial tables or intermediate calculations
- run-by-run artifacts (those belong in `/executions/`)

Those belong in `/executions/`.
