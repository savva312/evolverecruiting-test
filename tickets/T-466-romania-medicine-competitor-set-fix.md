# T-466: Romania — fix Medicine/MD competitor set (remove Bulgaria drift; source-backed list)

Status: done
Type: content
Priority: P0
Dependencies: T-155, T-450
Claimed-by: CodexRun-20251222
Claimed-at: 2025-12-22T14:05Z
Completed-at: 2025-12-22T15:10Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Correct `countries/romania/program-clusters/medicine-md/competitors.md` so it becomes a Romania-relevant, source-backed competitor set:
- remove Bulgaria university sources currently referenced incorrectly
- ensure each competitor entry matches the institution named (no mismatched links)
- expand/refresh to at least 15 meaningful competitors Romanian applicants actually compare (Romania domestic + Greece/Cyprus + CEE where relevant)
- add a short “How to position UNIC vs each competitor category” section

---

## Context

Current file contains mismatched sources (e.g., Bulgarian medical university links under Romania headings), which makes it unusable for recruiting decisions and risks internal misinformation.

Related assets:
- Competitor entity profiles: `countries/romania/entities/competitors/profiles/`
- Competitor program dataset: `countries/romania/data/programs/competitor-programs.csv` (to be built in T-450)

---

## Allowed write paths

- `tickets/T-466-romania-medicine-competitor-set-fix.md`
- `countries/romania/program-clusters/medicine-md/competitors.md`
- `executions/**` (optional for notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`
- `tickets/**` (except this ticket file)
- `countries/**` (except `countries/romania/program-clusters/medicine-md/**`)

---

## Required outputs

- Updated `countries/romania/program-clusters/medicine-md/competitors.md`

---

## Acceptance criteria

- [x] No mismatched institution ↔ source links remain.
- [x] At least 15 competitors are listed with sources and (where possible) tuition/admissions signals.
- [x] Competitor set is explicitly Romania-relevant (not a generic regional list).
- [x] Adds a clear UNIC positioning section with compliant language around recognition/licensure.
- [x] No edits outside allowed paths.

## What changed
- Rebuilt `countries/romania/program-clusters/medicine-md/competitors.md` with 16 Romania-relevant MD competitors, refreshed tuition/admissions data, source links, and a UNIC positioning section.
