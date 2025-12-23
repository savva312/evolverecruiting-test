---
name: nigeria-repo-routing
description: "Place Nigeria-specific outputs inside /countries/nigeria while keeping global paths and skills country-agnostic."
compatibility: Any agent writing Nigeria content in this repo.
metadata:
  author: EvoBuilder
  version: "1.0"
---

## Goal
Keep Nigeria research, reports, and playbooks contained in the `countries/nigeria/` subtree with correct linking and separation from other country work.

## When to use
- Preparing or migrating Nigeria-focused docs, data tables, or playbooks.
- Publishing Nigeria reports or syntheses.
- Adding Nigeria-only procedures that should not affect global skills.

## Prerequisites
- Read the ticket governing the change to confirm `countries/nigeria/**` is in the allowed write paths.
- Skim `countries/nigeria/README.md` for the latest Nigeria layout guidance.
- Keep `skills/README.md` conventions in mind: one skill per folder, with `SKILL.md`.

## Steps
1) **Choose the destination**
   - Reports → `countries/nigeria/reports/`.
   - Other Nigeria workstreams → create or use subfolders inside `countries/nigeria/` that mirror the repo map (e.g., `countries/nigeria/market/`, `countries/nigeria/entities/`, `countries/nigeria/go-to-market/`, `countries/nigeria/program-clusters/`; keep shared campus materials in `/UNIC/`).
2) **Create files with relative links**
   - Link between Nigeria files using relative paths (e.g., `./reports/<file>.md` or `../market/<file>.md`).
   - Avoid linking into Bulgaria or Greece folders unless cross-country comparisons are explicitly required.
3) **Keep run logs separate**
   - Use `/executions/` for global run logging when a ticket explicitly calls for it.
4) **Add Nigeria-only skills here**
   - If you create a Nigeria-specific procedure, place it under `countries/nigeria/skills/<skill-name>/SKILL.md` and keep global skills generic.
5) **Self-check before commit**
   - Confirm no Nigeria content lives outside `countries/nigeria/**`.
   - Ensure reports are under `countries/nigeria/reports/`.
   - Verify links resolve within the Nigeria subtree or to globally approved locations.

## Outputs
- Nigeria materials stored under `countries/nigeria/**` with reports in `countries/nigeria/reports/`.
- Nigeria-only procedures documented in `countries/nigeria/skills/**` instead of global skill folders.

## Quality bar
- Respect ticket write boundaries and avoid touching Bulgaria or Greece scopes.
- Prefer concise markdown with clear headings and stable filenames.
- Do not relocate `/executions/`; only add Nigeria content where the country-first layout expects it.
