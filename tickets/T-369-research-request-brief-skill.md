# T-369: Global research request brief skill

Status: done
Type: structure
Priority: P1
Dependencies: T-017, T-020
Claimed-by: work
Claimed-at: 2025-12-21T10:07:00+00:00
Last-updated: 2025-12-21T10:20:00+00:00

---

## Goal

Create a global skill that teaches agents how to produce a compact research brief file for EvoResearcher runs, capturing the report title, selected manager model (default GPT-5.2 (H)), number of sections, and number of research rounds. The skill must also show how to package the same prompt as an email-ready `.eml` with a Markdown sidecar, using the subject pattern `title, <sections>, <rounds>` and the prompt text in the email body.

## Context

- EvoResearcher runs require consistent, human-supplied inputs (title, model choice, section count, research rounds) before the pipeline executes.
- Agents sometimes need to hand off the same prompt via email; providing an `.eml` template plus a Markdown companion avoids mistakes and keeps artifacts reviewable.
- Secrets (JWT/access tokens) are handled by the system; the skill should focus solely on human-authored inputs and formatting.

## Allowed write paths

- `skills/research-request-briefs/**`
- `skills/README.md`
- `tickets/T-357-research-request-brief-skill.md`
- `executions/**` (optional notes)

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- Any country directories (e.g., `/countries/**`)
- Other tickets in `/tickets/**` (except status updates to this file)
- `.github/**`
- `scripts/**`

## Required outputs

- `skills/research-request-briefs/SKILL.md` detailing how to draft the Markdown brief and the optional `.eml` + Markdown sidecar.
- `skills/README.md` updated to list the new global skill.
- This ticket updated to `Status: done` with a brief "What changed" note when complete.

## Acceptance criteria

- Skill includes YAML frontmatter and is text-first.
- Provides a Markdown template that captures: report title, manager model selection (default GPT-5.2 (H) unless overridden), section count, research round count, and the prompt text.
- Shows how to generate an `.eml` with subject formatted as `title, <sections>, <rounds>`, body equal to the prompt text, and a Markdown sidecar carrying the same information.
- Notes that JWT/access tokens are handled by the system and do not belong in the brief.
- Respects Allowed/Forbidden write paths; no unrelated files changed.

## Execution notes (optional)

- What changed (short): Added global research-request-briefs skill with Markdown and `.eml` workflows, updated skills index.
- Any open questions: None.
- Follow-up tickets suggested: None.
