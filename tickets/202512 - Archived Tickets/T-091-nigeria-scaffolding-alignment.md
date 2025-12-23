# T-091: Nigeria scaffolding alignment

Status: archived
Type: structure
Priority: P1
Dependencies: T-021
Claimed-by: assistant
Claimed-at: 2025-12-20T00:00:00Z
Last-updated: 2025-12-20

---

## Goal

Ensure the Nigeria country subtree matches the comprehensive scaffolding used for other markets (e.g., Bulgaria, Greece, Romania). Add the missing folder structure, READMEs, program-cluster stubs, go-to-market templates, and country-specific skills so operators can add Nigeria content without guessing locations.

---

## Context

- Nigeria currently only contains a README, a market outbound mobility note, reports, and a repo-routing skill.
- Other countries follow a standard layout: data dictionaries, entities subfolders, go-to-market playbooks, program-cluster stubs, and a full Nigeria-only skills set mirroring Bulgaria/Greece/Romania.
- No content changes are expected outside Nigeria; this ticket is a structure catch-up for parity.

---

## Allowed write paths

- `nigeria/**`
- `tickets/T-074-nigeria-scaffolding-alignment.md`
- `research/T-074-nigeria-scaffolding-alignment/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global skills)
- Other country directories (e.g., `/bulgaria/**`, `/greece/**`, `/romania/**`, `/serbia/**`, `/jordan/**`)
- Other tickets except status updates to this file

---

## Required outputs

- Nigeria subtree contains the standard directories and README templates for `data/`, `entities/`, `go-to-market/`, `market/`, `program-clusters/`, and `reports/` (reports already present).
- Program-cluster folders exist for all standard clusters with Nigeria-labeled playbook stubs.
- Go-to-market subfolders and template files exist (agents, schools, digital, offerholder/yield).
- Nigeria-specific skills set mirrors other countries (agents, program clusters, education system, recognition, data models, pricing, etc.).
- Ticket updated upon completion with a short “What changed” note.

---

## Acceptance criteria

- [x] Nigeria directory structure matches the standard country layout used by Bulgaria/Greece/Romania (data, entities, go-to-market, market, program-clusters, reports, skills).
- [x] Program clusters include Nigeria-specific playbook filenames and stubs across all standard clusters.
- [x] Go-to-market folder contains all standard subfolders/files with Nigeria framing.
- [x] Nigeria skills set includes the full list of country-specific skills aligned to other markets.
- [x] No files outside Allowed write paths are modified.

---

## Execution notes (optional)

- What changed (short): Added full Nigeria scaffolding (data dictionaries, entities READMEs, go-to-market templates, market stubs, program-cluster playbooks, and a complete Nigeria-only skills set) to match other countries.
- Any open questions: None.
- Follow-up tickets suggested: Populate Nigeria content using the new scaffolding (data, profiles, playbooks) via scoped tickets.
