# T-043: Jordan outbound mobility refresh

Status: archived
Type: content
Priority: P1
Dependencies: (none)
Claimed-by: evolverecruiting-run
Claimed-at: 2026-02-04T00:00:00Z
Last-updated: 2026-02-04
What changed: Refreshed `jordan/market/outbound-mobility.md` using the 2025-12-20 Jordan outbound mobility report as the anchor, keeping the source file untouched and clarifying Eurostat totals, gaps, and UNIC/UNIC Athens implications.

---

## Goal

Enhance the Jordan outbound mobility baseline using the December 20, 2025 report (`jordan/reports/20251220-Jordan Outbound Mobility Baseline.md`) without altering that source file. Refresh `jordan/market/outbound-mobility.md` with clearer sourcing, gaps, and UNIC/UNIC Athens implications; add any supporting markdown outputs needed to keep the baseline concise and evidence-backed.

---

## Allowed write paths

- `tickets/T-031-jordan-outbound-mobility-refresh.md`
- `jordan/market/outbound-mobility.md`
- `jordan/reports/**`
- `research/**` (optional for execution notes only)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `.github/**`
- `scripts/**`
- `tickets/**` (except this ticket file)
- Other country directories (`bulgaria/**`, `greece/**`, `nigeria/**`, `romania/**`, `serbia/**`, `UNIC/**`)

---

## Required outputs

- Updated `jordan/market/outbound-mobility.md` that incorporates the December 20, 2025 Jordan outbound mobility report as a primary source and clearly labels data recency, confidence, and gaps relevant to UNIC/UNIC Athens.
- (Optional) Supporting markdown in `jordan/reports/` if needed to keep the market baseline concise while preserving evidence fidelity.
- Ticket status updated on completion with a short “What changed” note.

---

## Acceptance criteria

- Content stays within `Allowed write paths` and does not alter the source report file.
- Updated outbound mobility baseline cites the 2025 report, clarifies methodology/definitions, and highlights implications for Greece/Cyprus.
- Data gaps and confidence levels are explicitly labeled (e.g., UIS vs Eurostat, missing field splits).
- Outputs remain markdown-only and easy to navigate.

---

## Notes/Context

Use the provided December 20, 2025 report as-is for evidence; do not edit that file. Keep UNIC/UNIC Athens positioning practical and tied to the cited data.
