# T-381: Jordan country README scaffold

Status: done
Type: content
Priority: P1
Dependencies:
Claimed-by: work
Claimed-at: 2025-02-07
Last-updated: 2025-02-07

---

## Goal

Create a Jordan country README that mirrors the structure used for other markets (e.g., Serbia and Romania), so collaborators can quickly navigate the Jordan subtree and jump to key reports.

## Context

Jordan already has country subdirectories and initial reports, but lacks a top-level README that explains the layout and points to priority deliverables. Adding this index will keep work aligned to the country-first model and surface the most relevant Jordan reports.

## Allowed write paths

- `countries/jordan/README.md`
- `tickets/T-366-jordan-readme.md`
- `executions/work/**` (optional run notes)

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- Any country directory except `countries/jordan/README.md`
- Other tickets (besides status updates to this ticket)

## Required outputs

- `countries/jordan/README.md` with directory overview, working guidelines, and quick-start links to key Jordan reports.
- Updated ticket status and a "What changed" note linking to the new README once work is done.

## Acceptance criteria

- Jordan README follows the layout used by Serbia/Romania (intro, directory layout, working guidelines) with Jordan-specific wording.
- Quick-start section includes relative links to `reports/2025-12-20 - UNIC Athens Jordan Recruitment Plan.md` and `reports/20251220-Jordan Premium High-School Feeders.md`.
- Links stay inside the Jordan subtree; no cross-country references are introduced.
- Only files within Allowed write paths are modified.

## What changed

- Added [`countries/jordan/README.md`](../countries/jordan/README.md) with a Serbia/Romania-style layout, Jordan-specific working guidelines, and quick-start links to the priority reports above.
