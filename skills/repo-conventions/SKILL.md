---
name: repo-conventions
description: "Canonical file/folder conventions for EvoBuilder-managed topic repos: required root files, optional common folders, naming rules, and how to safely change structure."
compatibility: Any repo that wants stable agent behavior and predictable navigation.
metadata:
  author: canonical
  version: "1.0"
---

## Canonical root files (expected in every repo)
- `README.md` — What this repo is, how to navigate it, what "done" looks like
- `AGENTS.md` — Persistent instructions/guardrails for any agent operating in the repo
- `ROADMAP.md` — Milestones, current state, and a map of workstreams → tickets
- `/tickets/` — One markdown file per discrete unit of work
- `/skills/` — Agent Skills format (this folder)

## Common optional folders (use only if helpful for the repo)
- `/docs/` — human-facing documentation
- `/data/` — structured data files and schemas (YAML/JSON/CSV)
- `/templates/` — reusable templates (letters, checklists, SOPs)
- `/scripts/` — small auditable utilities
- `/dist/` — generated artifacts (only commit if the repo policy says so)
- `/assets/` — small static assets; use Git LFS for large binaries

## Naming conventions
- Use kebab-case for directories and files where possible.
- Prefer short, descriptive names. Avoid spaces unless necessary.
- Tickets should be stable identifiers (e.g., `T-001-short-title.md`).

## Changing folder structure (allowed but controlled)
Folder structure may evolve per repo, but **structure changes must be deliberate**:
1. Update `ROADMAP.md` to reflect the new structure.
2. Update any affected ticket `allowed_write_paths`.
3. Prefer additive migration:
   - create new paths
   - move content in a dedicated “migration” ticket
4. Avoid big bang renames without a ticket.

## “Keep files” for empty directories
If a ticket asks you to create a directory tree and git must detect it:
- add a `.keep` file (or `README.md`) inside otherwise-empty directories.
