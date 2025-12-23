# T-470: EvoManager execution order JSON generator

Status: done
Type: integration
Priority: P1
Agent: EvoTicket Resolver
Claimed-by: work
Claimed-at: 2025-12-22T17:21:48Z

---

## Goal

Build a script that produces a JSON execution order for all tickets currently marked `on-deck`, to be invoked by **EvoManager** after it finalizes on-deck classification.

## Context

- EvoManager runs every 30 minutes; we need deterministic JSON naming using `YYYYMMDD` and the epoch number derived from 30-minute slots starting 00:00 UTC.
- JSON entries must include agent routing, ticket ID/title, status, full body, and explicit model selection (GPT 5.2 (H) for EvoResearcher manager/analyst; GPT 5.1 Codex for EvoTicket Resolver).
- Output should live in `tickets/executionorders/` for downstream automations.

## Allowed write paths

- `tickets/T-470-evomanager-execution-order-json.md`
- `scripts/**`
- `tickets/executionorders/**`
- `executions/**` (optional run notes)

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/README.md`
- `tickets/index.md`
- `countries/**`
- `UNIC/**`
- `reports/**`

## Required outputs

- `scripts/evomanager_execution_order.py` that reads all top-level tickets and emits a JSON file with on-deck entries using the required model mapping and naming convention.
- A generated sample JSON file under `tickets/executionorders/` following the `YYYYMMDD - Agent Execution Order - Epoch <n>.json` naming pattern to demonstrate the output path.
- Optional run notes in `executions/` if needed.

## Acceptance criteria

- Script scans top-level `tickets/T-*.md` files (excluding archived/template) and collects only those with `Status: on-deck`.
- Each JSON entry includes agent type, ticket ID, title, status, full body text, and model info (manager + analyst for EvoResearcher, GPT 5.1 Codex for EvoTicket Resolver).
- Output filename uses UTC date in `YYYYMMDD` format and the current epoch index based on 30-minute intervals from 00:00 UTC.
- Script creates `tickets/executionorders/` if missing and writes the JSON payload in UTF-8 with deterministic field names.
- Running the script succeeds without external dependencies beyond the standard library.

## What changed

- Added `scripts/evomanager_execution_order.py` to emit epoch-stamped JSON execution orders for on-deck tickets with required agent/model metadata.
- Generated a sample output file under `tickets/executionorders/` demonstrating the naming convention and payload structure (currently no on-deck tickets, so empty list).
