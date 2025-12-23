# T-044: Nigeria outbound mobility upgrade and report ingest

Status: archived
Type: content  
Priority: P1  
Dependencies: (none)  
Claimed-by: work  
Claimed-at: 2025-12-20T17:39:50Z  
Last-updated: 2025-12-20  
What changed: Ingested the Nigeria outbound mobility baseline into `nigeria/reports/` and published an upgraded outbound mobility summary under `nigeria/market/`.

---

## Goal

Ingest the provided “Nigeria Outbound Mobility Baseline” report into `nigeria/reports/` and upgrade the Nigeria outbound mobility market page with decision-ready summaries for UNIC (RoC Cyprus) and UNIC Athens (Greece).

---

## Allowed write paths

- `nigeria/market/**`
- `nigeria/reports/**`
- `tickets/T-031-nigeria-outbound-mobility.md`
- `research/T-031-nigeria-outbound-mobility/**` (optional run notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- Other country directories (e.g., `/bulgaria/**`, `/greece/**`, `/romania/**`, `/serbia/**`, `/jordan/**`)
- `.github/**`
- `scripts/**`
- `data/**`
- `entities/**`
- `program-clusters/**`
- `go-to-market/**`
- `UNIC/**`

---

## Required outputs

- New markdown report under `nigeria/reports/` containing the provided baseline.
- Updated Nigeria outbound mobility page under `nigeria/market/` with:
  - Current Eurostat stock and permit flow signals for Nigeria → RoC Cyprus and Greece.
  - Destination/program preference highlights (U.S., Canada, UK anchors; graduate orientation; STEM/business context).
  - Explicit data caveats (UIS extract pending, stock vs flow distinctions, TRNC separation).
  - Actionable implications for UNIC (RoC) and UNIC Athens.

---

## Acceptance criteria

- Report text is captured verbatim (or near-verbatim) in `nigeria/reports/`, clearly dated and sourced.
- `nigeria/market/outbound-mobility.md` is concise, bullet-heavy, and clearly labeled with “last updated”.
- Eurostat and host-country indicators are correctly reflected with stock vs flow clarity and TRNC caveat.
- Implications distinguish UNIC (RoC) vs UNIC Athens (Greece) and emphasize graduate/ employability positioning.
- No files outside Allowed write paths are modified.
- Ticket status updated to `done` with a brief “what changed” note when complete.

---

## Notes/Context

- Treat UNESCO UIS outbound totals and destination rankings as provisional until a direct UIS extract is added.
- Keep country-first boundaries: Nigeria content must remain under `nigeria/**` only.
