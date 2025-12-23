# T-434: Bulgaria — build out Health/Pharmacy/Allied Health cluster pack

Status: done
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: evoticketresolver_3m9nhw1a
Claimed-at: 2025-12-22 17:54:06Z
Last-updated: 2025-12-22
Agent: EvoTicket Resolver
Research rounds: N/A
Research sections: N/A
Research output path: N/A

---

## Goal

Upgrade the Health/Pharmacy/Allied Health cluster from placeholders to an actionable Bulgaria recruiting pack that correctly handles recognition/licensure sensitivity for return-to-Bulgaria pathways.

---

## Context

Current cluster files are placeholders:
- `countries/bulgaria/program-clusters/health-pharmacy-allied-health/cluster.md`
- `countries/bulgaria/program-clusters/health-pharmacy-allied-health/competitors.md`
- `countries/bulgaria/program-clusters/health-pharmacy-allied-health/bulgaria-playbook.md`

Recognition reference:
- `countries/bulgaria/market/recognition-and-licensure.md`

---

## Allowed write paths

- `tickets/T-434-bulgaria-health-pharmacy-cluster-build.md`
- `countries/bulgaria/program-clusters/health-pharmacy-allied-health/cluster.md`
- `countries/bulgaria/program-clusters/health-pharmacy-allied-health/competitors.md`
- `countries/bulgaria/program-clusters/health-pharmacy-allied-health/bulgaria-playbook.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global)
- `tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`
- `countries/**` (except `countries/bulgaria/**`)

---

## Required outputs

- Updated cluster pack (all three files) including:
  - ≥3 Bulgaria-relevant segments (nursing, pharmacy, allied health)
  - ≥8 competitor entries with sources and `last_updated`/`last_verified` notes
  - a Bulgaria outreach playbook that includes a “recognition/licensure caveats” section and a counselor-ready FAQ outline

---

## Acceptance criteria

- [x] No promises of licensure; all regulated-profession language is framed as “process + competent authority” and linked to the Bulgaria recognition brief.
- [x] Competitor list uses primary sources where possible (official program/tuition/admissions pages).
- [x] No files outside `Allowed write paths` were modified.

---

## What changed (2025-12-22)
- Replaced placeholder cluster content with a Bulgaria-specific, counselor-safe pack (segments, triage script, UNIC programme map, and non-negotiable recognition/licensure guardrails).
- Added an 8-institution competitor set with primary sources plus per-entry `last_verified` / `last_updated` metadata.
- Shipped a Bulgaria outreach playbook with a standard qualification workflow, channel plan (schools/agents/digital/events), a do-not-say list, and a counselor-ready FAQ outline.

## Verification notes
- Scope check: `git status` shows changes only in the ticket + the three cluster files under the allowed path list.
