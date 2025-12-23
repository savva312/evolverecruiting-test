# T-399: README parallelism and auto-merge philosophy

Status: done
Type: structure
Priority: P1
Dependencies: (none)
Claimed-by: work
Claimed-at: 2026-02-12T00:00:00Z
Last-updated: 2026-02-12
Completed-at: 2026-02-12T00:30:00Z

---

## Goal

Ensure the root `README.md` explicitly captures the repository's bias toward **massive parallelism**, **speed-first broad execution**, and the expectation of **auto-merging (including conflict auto-resolution when safe) to keep throughput high**, with cleanup/refactoring allowed to follow in later tickets.

---

## Context

- The operating rules emphasize ticket-driven, country-scoped work but the README does not yet foreground the speed/parallelism philosophy requested by stakeholders.
- Control-plane docs (`README.md`, `AGENTS.md`, `ROADMAP.md`) are protected; this ticket provides structure scope to update `README.md`.
- The message should make clear that minor text inconsistencies are acceptable trade-offs for velocity, with cleanup handled in subsequent tickets.

---

## Allowed write paths

- `README.md`
- `tickets/T-402-readme-parallelism-philosophy.md`
- `executions/work/**` (optional run notes)

---

## Forbidden write paths

- Any file or directory not listed in Allowed write paths

---

## Required outputs

- `README.md` updated to include:
  - Philosophy of massive parallelism and extreme speed.
  - Bias toward going vast/broad/parallel first, with cleanup/refactoring later.
  - Expectation of auto-merging (including conflict auto-resolution) to maintain velocity, with the note that text-only errors are fixable in follow-on tickets.
- `tickets/T-402-readme-parallelism-philosophy.md` updated with final status/notes when work is done.

---

## Acceptance criteria

- README contains a clearly labeled section or callout covering parallelism, speed-first execution, and auto-merge/auto-conflict-resolution philosophy, along with the follow-up cleanup expectation.
- Wording aligns with existing ticket-first and country-first guidance without contradicting protected-file or scope rules.
- No files outside Allowed write paths are modified.
- Ticket marked `Status: done` with brief execution notes after changes land.

---

## Execution notes (optional)

- What changed: Added an execution-philosophy section to `README.md` highlighting massive parallelism, broad-first execution with later cleanup, and the expectation of auto-merging/auto-resolving text conflicts to maintain speed.
- Open questions: None.
- Follow-up tickets suggested: None.
