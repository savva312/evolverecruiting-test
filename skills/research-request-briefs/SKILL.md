---
name: research-request-briefs
description: "Ticket-first EvoResearcher prompt guidance with defaults for research rounds and report-as-artifact outputs (model fixed to GPT-5.2 (H))."
compatibility: EvoResearcher and similar manager/analyst research pipelines.
metadata:
  author: evo
  version: "1.2"
---

## Purpose
- Capture the human-provided inputs an EvoResearcher run needs: report title, report destination folder, number of report sections, and number of research rounds (model is fixed to **GPT-5.2 (H)**).
- Ensure EvoResearcher tickets include the prompt text itself; the ticket doubles as the prompt beyond parameter fields.
- Default to **5** research rounds (1–3 for easy topics, 10–15 for hard topics; rarely more than that).
- Treat the “report” as a detailed **artifact**; extract/curate the important information into the repo’s primary deliverables (profiles, playbooks, tables) when appropriate.
- Secrets (JWT/access tokens, API keys) are handled by the system; **do not place them in tickets**.

## Inputs to collect
- **Report title**: concise, ≤40–60 characters if possible.
- **Agent**: `EvoResearcher`.
- **Research output path**: folder in the repo where the final report should be saved (or the target dossier folder if the report will update files in-place).
- **Sections**: integer 1–100 (code enforces ≤100). Treat this as an organization/scaffolding hint, not a length limit.
- **Research rounds**: integer 1–99 (default **5**; easy 1–3; hard 10–15; rarely above that).
- **Prompt text/request**: the actual research ask, including constraints, sources, or formatting expectations.
- **Ticket scope**: allowed write paths, required outputs, and any forbidden paths the prompt should explicitly respect (e.g., “do not touch CSVs / indexes”).


## Format (required): EvoResearcher ticket prompt
Use this when you want EvoResearcher to execute work and write outputs directly to the repo (the normal path).

1. Create a ticket from `tickets/T-000-template.md`.
2. Set:
   - `Agent: EvoResearcher`
   - `Research rounds: 5` (default; change  when needed)
   - `Research sections: <integer>`(2 to 15 is a reasonable range)
   - `Research output path: <folder>`
3. Define `Allowed write paths`, `Forbidden write paths`, `Required outputs`, and `Acceptance criteria` normally.
4. Put the prompt under a section like `## Research prompt (EvoResearcher)` and make it explicitly compatible with the write boundary.

**Ticket prompt skeleton**
```markdown
## Research prompt (EvoResearcher)

You are EvoResearcher. Write results directly to the repo under the allowed paths for this ticket.

### Deliverables
- Primary deliverable): <exact file paths>

### Report length
- The report can be as long as needed. Do not compress or omit important details to “hit a length”.

**End Ticket prompt skeleton**

## Prompt templates (copy/paste starting points)
- Use: `skills/research-request-briefs/prompt-templates/`if there is a relevant template.  If not, start from scratch
- Pick the closest template, replace placeholders, and delete any sections you don’t need.
- Keep templates generic; country- or entity-specific nuance belongs in the filled ticket.


