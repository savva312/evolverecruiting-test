# T-030: Bulgaria outbound mobility refresh (Eurostat 2023 extract)

Status: archived
Type: content
Priority: P1
Dependencies: T-006
Claimed-by: assistant
Claimed-at: 2025-12-20T16:52:11Z
Last-updated: 2025-12-20
What changed: Added Eurostat 2023 structured report under `bulgaria/reports/structured/` and refreshed `bulgaria/market/outbound-mobility.md` with the new baseline, implications, and caveats.

---

## Goal

Incorporate the new Bulgaria outbound mobility baseline (Eurostat `educ_uoe_mobs02`, reference year 2023) into the Bulgaria outbound mobility section and archive the full structured report under `bulgaria/reports/structured/`.

---

## Allowed write paths

- `bulgaria/market/outbound-mobility.md`
- `bulgaria/reports/structured/**`
- `research/**` (optional run notes)
- `tickets/T-027-bulgaria-outbound-mobility-refresh.md`

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`
- `data/**`
- `entities/**`
- `program-clusters/**`
- `go-to-market/**`
- `UNIC/**`
- Other tickets (except status updates to this file)

---

## Required outputs

- Updated `bulgaria/market/outbound-mobility.md` reflecting the Eurostat 2023 Bulgaria outbound baseline, destination structure, trends, and caveats relevant to UNIC and UNIC Athens.
- Structured report file added under `bulgaria/reports/structured/` containing the full provided baseline text.
- Ticket status updated when work is complete, with a short “what changed” note.

---

## Acceptance criteria

- Eurostat 2023 outbound volume and destination ranking for Bulgaria are captured, with explicit Bulgaria→Greece and Bulgaria→Cyprus counts and shares.
- Key caveats (Eurostat reporting-set scope, missing hosts, aggregate exclusion) are documented.
- Program/discipline guidance and implications for UNIC/UNIC Athens are updated using the provided report.
- All changes remain within Allowed write paths; control-plane files untouched.

---

## Notes/Context

- Builds on T-006 by refreshing the outbound baseline with the latest Eurostat host-country slice and aligning implications for UNIC and UNIC Athens.
- UNESCO UIS global flows are still a gap; treat Eurostat totals as reporting-set totals, not worldwide counts.
