# T-393: Doukas School EvoResearcher prompt

Status: done
Type: content
Priority: P1
Dependencies: T-307
Claimed-by: work
Claimed-at: 2025-12-21T19:25:29+00:00
Last-updated: 2025-12-21T19:25:57+00:00

---

## Goal

Author a deep-dive EvoResearcher prompt for **Doukas School (Marousi, Athens)** that requests a comprehensive report returned as Markdown file(s) and focuses on unresolved intelligence gaps.

## Context

- Use existing profile at `countries/greece/entities/schools/profiles/athens/sch-gr-marousi-doukas-001/README.md` as baseline; open questions include tuition, contacts, academic calendar, and outcomes.
- Follow the global research brief standard in `skills/research-request-briefs/SKILL.md` (Markdown only; no `.eml` needed for this run).
- Report outputs should be Markdown and scoped to the Doukas school dossier.

## Allowed write paths

- `tickets/T-373-doukas-evoresearcher-prompt.md`
- `countries/greece/entities/schools/profiles/athens/sch-gr-marousi-doukas-001/research/**`
- `executions/T-373-doukas-evoresearcher-prompt/**` (optional run notes)

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/README.md`
- Other country directories (e.g., `countries/bulgaria/**`, `countries/nigeria/**`)
- `countries/greece/data/entities/schools.csv`
- `countries/greece/entities/schools/index.md`
- `countries/greece/entities/schools/README.md`

## Required outputs

- `countries/greece/entities/schools/profiles/athens/sch-gr-marousi-doukas-001/research/doukas-evoresearcher-prompt.md` containing the Markdown brief (title, manager_model, sections, research_rounds, prompt body) instructing EvoResearcher to return its report as Markdown file(s) and address current gaps (tuition, contacts, outcomes, calendar, risks, partnerships).

## Acceptance criteria

- Brief follows the Markdown format from `skills/research-request-briefs/SKILL.md` with metadata fields and prompt heading.
- Prompt requests EvoResearcher to deliver findings in one or more Markdown report files and suggests a storage path under the Doukas research folder.
- Prompt explicitly calls out unresolved issues (fees, cohort sizes, contacts, outcomes, calendar, risks) and asks for source citations and validation steps.
- Work stays within allowed paths; no edits to CSV/index/README control files.

## What changed

- Created and stored a Markdown EvoResearcher brief for Doukas, requesting deep-dive outputs as Markdown and highlighting tuition, contact, calendar, cohort, and outcomes gaps.
