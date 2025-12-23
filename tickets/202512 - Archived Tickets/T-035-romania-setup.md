# T-035: Romania country setup

Status: archived
Type: structure
Priority: P1
Dependencies: 
Claimed-by: work
Claimed-at: 2025-12-20T17:01:37+00:00
Last-updated: 2025-12-20

---

## Goal

Add Romania as a new country namespace aligned to the country-first layout by duplicating the Bulgaria structure and tailoring the content to Romania where relevant (e.g., geography, major cities, and labels).

---

## Context

- The repo currently includes Bulgaria, Nigeria, and Greece country trees. Romania needs to be added as a new market.
- The Romania namespace should mirror the existing Bulgaria layout so shared processes stay consistent across markets.

---

## Allowed write paths

- `romania/**`
- `tickets/T-028-romania-setup.md`
- `ROADMAP.md`
- `research/T-028-romania-setup/**` (optional run notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `skills/**` (outside any Romania-specific skills added under `/romania/skills`)
- Other country directories (e.g., `/bulgaria/**`, `/nigeria/**`, `/greece/**`)
- Other tickets except status updates to this file

---

## Required outputs

- New `/romania` top-level directory mirroring the Bulgaria folder structure (market, entities, go-to-market, program-clusters, data, reports, skills) with Romania-specific naming and geography where applicable.
- Content within the Romania namespace adjusted from Bulgaria references to Romania equivalents (e.g., major cities, country labels) while preserving templates/playbooks.
- `ROADMAP.md` updated to include Romania in the country-first map and mission description.
- `tickets/T-028-romania-setup.md` updated to `done` upon completion with a brief summary of changes.

---

## Acceptance criteria

- Romania has its own country directory `/romania/**` following the canonical layout with the same subfolders as Bulgaria.
- Files within `/romania/**` reference Romania (not Bulgaria) in names and descriptive text where applicable; placeholders or TODOs are clearly marked where data is unknown.
- `ROADMAP.md` reflects Romania as an included country in the repo map/mission.
- No files outside Allowed write paths are modified.

---

## Execution notes (optional)

- What changed (short): Added `/romania` country subtree mirroring Bulgaria’s layout, localized city/agent/school placeholders, templated reports and market baselines, and updated ROADMAP to include Romania.
- Follow-ups: Populate Romania-specific data (Eurostat/UIS extracts, entity datasets) and replace placeholder school/agent details with sourced entries.
