# T-004: Establish program clusters folder structure

Status: archived
Type: structure
Priority: P1
Dependencies: (none)
Claimed-by: chatgpt
Claimed-at: 2025-12-20T14:34:49Z
Last-updated: 2025-12-20

---

## Goal

Create the `program-clusters/` directory hierarchy with cluster, competitor, and playbook placeholders for key program types serving UNIC and UNIC Athens recruiting.

---

## Context

The repository needs structured folders to capture program-specific competitor sets and Bulgaria playbooks. This work should add the requested directories and markdown placeholders so future contributors can populate the content.

---

## Allowed write paths

- `program-clusters/**`
- `tickets/T-003-program-clusters-structure.md`
- `research/**`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/README.md`

---

## Required outputs

- `program-clusters/README.md`
- `program-clusters/medicine-md/cluster.md`
- `program-clusters/medicine-md/competitors.md`
- `program-clusters/medicine-md/bulgaria-playbook.md`
- `program-clusters/health-pharmacy-allied-health/cluster.md`
- `program-clusters/health-pharmacy-allied-health/competitors.md`
- `program-clusters/health-pharmacy-allied-health/bulgaria-playbook.md`
- `program-clusters/cs-data-ai-cyber/cluster.md`
- `program-clusters/cs-data-ai-cyber/competitors.md`
- `program-clusters/cs-data-ai-cyber/bulgaria-playbook.md`
- `program-clusters/business-finance-accounting-marketing/cluster.md`
- `program-clusters/business-finance-accounting-marketing/competitors.md`
- `program-clusters/business-finance-accounting-marketing/bulgaria-playbook.md`
- `program-clusters/psychology-counselling-behavioral/cluster.md`
- `program-clusters/psychology-counselling-behavioral/competitors.md`
- `program-clusters/psychology-counselling-behavioral/bulgaria-playbook.md`
- `program-clusters/law-governance-international/cluster.md`
- `program-clusters/law-governance-international/competitors.md`
- `program-clusters/law-governance-international/bulgaria-playbook.md`
- `program-clusters/design-creative-media/cluster.md`
- `program-clusters/design-creative-media/competitors.md`
- `program-clusters/design-creative-media/bulgaria-playbook.md`

---

## Acceptance criteria

- All required directories and files exist under `program-clusters/` with stub markdown content and clear headings for cluster, competitors, and Bulgaria playbook sections.
- No files outside the allowed write paths are modified.
- Ticket status reflects completion when work is finished, with a brief note on what changed.

---

## Execution notes (optional)

- What changed: Added `program-clusters/` directory with cluster, competitor, and Bulgaria playbook stubs for medicine, health/pharmacy/allied health, CS/data/AI/cyber, business/finance/accounting/marketing, psychology/counselling/behavioral, law/governance/international, and design/creative media. Documented directory map in README.
- Follow-ups suggested: None.
