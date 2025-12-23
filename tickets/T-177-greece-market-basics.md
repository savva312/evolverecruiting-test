# T-177: Greece affordability, outbound mobility, and recognition baselines

Status: done
Type: content
Priority: P1
Dependencies: 
Claimed-by: work
Claimed-at: 2025-12-20T22:03:45+00:00
Last-updated: 2025-12-20

---

## Goal

Add Greece market baseline notes for affordability/economics, outbound mobility, and recognition/licensure so country leads have parity with Bulgaria and Nigeria scaffolds.

---

## Allowed write paths

- `countries/greece/market/**`
- `countries/greece/data/**`
- `tickets/T-148-greece-market-basics.md`
- `research/T-148-greece-market-basics/**` (optional run notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- Any country directories outside `countries/greece/**`
- Any other tickets besides status updates to this file

---

## Required outputs

- `countries/greece/market/affordability-and-economics.md` aligned to Bulgaria/Nigeria structure with concise bullet points and sources.
- `countries/greece/market/outbound-mobility.md` summarizing outbound flows and destinations with sources.
- `countries/greece/market/recognition-and-licensure.md` capturing degree/credit recognition, NARIC/DOATAP cues, and licensure implications with sources.
- Cross-links in the above files to any structured tables in `countries/greece/data/entities` or `countries/greece/data/operations` when referenced.
- Ticket updated to `Status: done` with a short "What changed" note upon completion.

---

## Acceptance criteria

- New Greece market files exist with headings consistent with Bulgaria/Nigeria equivalents and contain sourced bullet points (no unsupported speculation).
- Where structured data tables are cited, the markdown files link to them in `countries/greece/data/entities` or `countries/greece/data/operations`.
- No files outside Allowed write paths are modified.
- Ticket reflects completion once work is done (status + what changed).

---

## Notes/Context

- Keep bullets concise and source-backed; prioritize 2023–2025 data.
- Avoid duplicating Bulgaria/Nigeria copy—make Greece-specific statements with citations.
- Cross-reference existing data tables instead of restating them; if missing, note gaps and proceed with sourced narrative.
- What changed: Added Greece market files for affordability/economics, outbound mobility, and recognition/licensure with sourced bullets and regulator cross-links; noted data follow-ups for UIS extracts and licensure pathways.
