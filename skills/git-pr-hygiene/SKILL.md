---
name: git-pr-hygiene
description: "Git/PR hygiene for EvoBuilder repos: small diffs, ticket-referenced commits, safe structure changes, and predictable PR summaries."
compatibility: Any git-based workflow (GitHub, GitLab, etc.).
metadata:
  author: canonical
  version: "1.0"
---

## Goals
- Make changes reviewable.
- Make history searchable by ticket id.
- Avoid accidental cross-scope edits.

## Commit guidance
- Prefer commit messages that reference the ticket id:
  - `T-012: add initial country index`
  - `T-021: scaffold folder tree`
- Keep commits focused. Don’t mix unrelated tickets.

## PR description guidance
Include:
- What the ticket asked for
- What was changed (file list)
- Any follow-ups / known gaps
- How to verify (if applicable)

## Safe changes
- Avoid deleting content unless a ticket explicitly authorizes it.
- For folder refactors, prefer:
  1) add new structure
  2) move content
  3) update links
  4) only then delete old paths (in a later ticket)
