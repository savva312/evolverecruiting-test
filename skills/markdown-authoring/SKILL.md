---
name: markdown-authoring
description: "Markdown style guide for EvoBuilder repos: structure, headings, link conventions, checklists, and how to write ticket-friendly, maintainable docs."
compatibility: Any markdown-based repo.
metadata:
  author: canonical
  version: "1.2"
---

## Writing principles
- Prefer short sections with clear headings.
- Avoid filler (“this document will…”). Start with substance.
- Make docs skimmable: bullets, tables (when appropriate), checklists.

## Headings
- Use one `#` per document for the document title.
- Use `##` for major sections, `###` for subsections.

## Links
- Use relative links whenever referencing repo files:
  - `../tickets/T-001.md`
  - `./index.md`
- Avoid raw URLs in the middle of paragraphs when a named link is clearer.

## Lists and checklists
- Use task checklists for procedural docs:
  - `- [ ] Step`
- Tickets should have a Definition of Done checklist.

## Stable formatting
- Do not reflow/reformat unrelated files in the same change.
- Avoid “format-only” PRs unless there is a ticket for it.

## Run the canonicalizer (Python CLI)
- Use the repo script to keep `.md` files aligned with the canonical rules: `python scripts/canonicalize_md.py`.
- Default mode fixes formatting in place; add `--check` to detect drift without writes.
- If you want to target specific files (especially new/untracked ones), pass them explicitly: `python scripts/canonicalize_md.py --fix path/to/file.md`.
- Without explicit paths, the script discovers staged and unstaged Markdown files via `git diff --name-only`.

## Canonical formatting checklist (manual; replaces the workflow)
- Strip trailing spaces/tabs at line ends.
- Headings: one space after the hashes, no trailing hashes (use `## Title`, not `##Title##`).
- Unordered lists: use `-` for markers, indent with spaces snapped to multiples of two (no tabs), and keep exactly one space after the marker (`- Item`).
- Blank lines: collapse runs of 2+ blank lines into a single blank line; avoid padding the end of the file with empties.
- EOF: ensure the file ends with exactly one newline (no missing or multiple trailing newlines).

## Quick self-check before commit
1) Run the canonicalizer: `python scripts/canonicalize_md.py --check` (or `--fix` to rewrite).
2) Scan headings for spacing/trailing hashes (`rg "^#"` is handy).
3) Glance at lists for mixed markers or tab indents; convert to spaced `-` bullets.
4) Remove double-blank runs (search for `^$\n^$`).
5) Trim trailing spaces and confirm a single newline at EOF (the canonicalizer enforces this).

## Source notes (lightweight)
When you make an externally-derived factual claim:
- add a short “Sources” section at the bottom of the file, or
- add sources in the ticket file if the doc shouldn’t carry citations
