# T-036: Serbia country scaffold and duplication

Status: archived
Type: structure
Priority: P1
Dependencies:
Claimed-by: work
Claimed-at: 2025-02-01
Last-updated: 2025-02-01

---

## Goal

Add a top-level `serbia/` directory that mirrors the Bulgaria country layout and content, with names, geography, and examples adjusted to Serbia. Update the control-plane roadmap to reflect Serbia as a supported market.

## Context

- Current country directories: `bulgaria/`, `nigeria/`, `greece/`.
- Serbia is a new market and requires its own subtree aligned to the country-first layout.
- Bulgarian materials provide the closest template; adapt references (country name, cities, entities) to Serbian context.

## Allowed write paths

- `serbia/**`
- `tickets/T-028-serbia-scaffold.md`
- `ROADMAP.md`
- `research/T-028-serbia-scaffold/**` (optional run notes)

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `skills/**` (global skills)
- Any existing country directories (`bulgaria/**`, `nigeria/**`, `greece/**`)
- Other tickets (except status updates to this ticket)

## Required outputs

- New `serbia/` directory with the same subfolders as `bulgaria/`, populated with Serbia-adjusted versions of each file (country name, city references, and contextual details updated).
- File and folder names updated to use "serbia" instead of "bulgaria" where applicable (e.g., playbooks, reports).
- `ROADMAP.md` updated to list Serbia in the country layout map.
- `tickets/T-028-serbia-scaffold.md` updated upon completion with status and summary of changes.

## Acceptance criteria

- [x] `serbia/` exists at the repo root with subdirectories for market, entities, go-to-market, program-clusters, data, reports, and skills.
- [x] Content inside `serbia/` references Serbia (and Serbian cities such as Belgrade, Novi Sad, Niš) rather than Bulgaria; no leftover Bulgarian-specific wording remains.
- [x] Serbia reports/playbooks are renamed accordingly (e.g., `Serbia Outbound Mobility Baseline`).
- [x] `ROADMAP.md` reflects Serbia in the country-first repo map.
- [x] No files outside Allowed write paths are modified.

## Execution notes (optional)

Use Bulgarian content as a template but localize names, examples, and geography to Serbia. If data gaps remain, mark them clearly for follow-up.

- Created new `serbia/` subtree mirroring Bulgaria with localized content, city coverage, agent/event profiles, data dictionaries, and reports reworked for Serbia.
- Updated ROADMAP country map to list Serbia.
