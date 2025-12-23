# T-178: Greece program cluster content build

Status: done  
Type: content  
Priority: P1  
Dependencies: T-022, T-028  
Claimed-by: work  
Claimed-at: 2025-12-20T22:04:45+00:00  
Last-updated: 2025-12-20T22:07:06+00:00

---

## Goal

Populate the Greece program cluster folders with country-specific cluster summaries, competitor lists, and go-to-market playbooks that mirror the structure used in the Nigeria and Bulgaria program clusters.

## Allowed write paths

- `countries/greece/program-clusters/**`
- `tickets/T-148-greece-program-clusters.md`
- `research/T-148-greece-program-clusters/**` (optional run notes)

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- Other country directories
- `.github/**`
- `scripts/**`

## Required outputs

- `countries/greece/program-clusters/*/cluster.md` drafted for all existing Greece clusters.
- `countries/greece/program-clusters/*/competitors.md` with local and regional competitor lists and positioning notes against UNIC and UNIC Athens.
- `countries/greece/program-clusters/*/greece-playbook.md` outlining next-step actions and Greece-specific outreach ideas per cluster.
- Ticket updated to `Status: done` with a short “What changed” note when complete.

## Acceptance criteria

- Only allowed paths are modified.
- Each Greece cluster directory contains the three markdown files with Greece-specific content (not empty stubs).
- Competitor sections include at least 5 named institutions or providers across local/EU/online where relevant plus positioning notes vs UNIC/UNIC Athens.
- Playbooks include concrete next steps and partner/channel ideas tailored to Greece.
- Ticket status updated to `done` on completion with changes summarized.

## Notes/Context

- Use existing Nigeria/Bulgaria cluster files as models for headings and brevity.
- Keep tuition and positioning statements concise; include sources only if readily available and text-first.
- What changed: Added Greece-specific cluster, competitor, and playbook files for all program clusters with local competitor lists, positioning notes vs. UNIC/UNIC Athens, and next-step actions.
