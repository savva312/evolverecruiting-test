# T-420: Markdown canonicalizer guidance uplift

Status: done
Type: structure
Priority: P1
Agent: EvoTicket Resolver
Dependencies: (none)
Claimed-by: work
Claimed-at: 2026-02-28T00:00:00Z
Last-updated: 2026-02-28T00:30:00Z

---

## Goal

Update the Markdown authoring skill so it explicitly instructs contributors to use the Python-based Markdown canonicalizer CLI when creating or editing `.md` files, keeping manual guidance aligned with the script’s behavior.

## Context

- The repo now ships a Markdown canonicalization script (`scripts/canonicalize_md.py`) that mirrors the retired workflow.
- The existing Markdown authoring skill documents manual rules but doesn’t remind contributors to run the CLI for enforcement.
- Aligning the skill with the tool will reduce drift and keep formatting consistent across tickets.

## Allowed write paths

- `tickets/T-420-markdown-canonicalizer-skill-alignment.md`
- `skills/markdown-authoring/**`
- `executions/**` (optional notes)

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- Country directories (e.g., `/countries/**`)
- Other tickets in `/tickets/**`
- `.github/**`
- `scripts/**`
- `skills/**` paths not listed above

## Required outputs

- Updated `skills/markdown-authoring/SKILL.md` that references the Python canonicalizer CLI and clarifies when/how to run it.
- This ticket updated with execution notes and marked done.

## Acceptance criteria

- Markdown authoring skill explicitly references `scripts/canonicalize_md.py`, covering both check and fix usage.
- Guidance ties the canonical formatting checklist to the CLI, reinforcing alignment with automated rules.
- No files outside Allowed write paths are modified.
- Ticket marked `done` with a short summary of changes.

## Execution notes (optional)

- Added canonicalizer usage guidance (default fix mode, `--check`, explicit paths for new files) to `skills/markdown-authoring/SKILL.md`.
