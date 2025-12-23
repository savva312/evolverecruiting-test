# T-117: Digital measurement and benchmarks (global)

Status: done
Type: content
Priority: P2
Dependencies: T-017, T-020, T-026
Claimed-by: work
Claimed-at: 2025-12-20T20:12:23Z
Last-updated: 2025-12-20

---

## Goal

Create a global measurement and benchmarking skill (or module) that defines KPI guardrails, UTM governance, tracking requirements, diagnostics, and reporting cadences for paid media and digital channels.

---

## Context

- The global paid media skill exists but lacks a dedicated measurement/benchmarking framework.
- This skill should provide baseline targets, health checks, and troubleshooting steps; it should also clarify how to log results and share benchmarks across countries.
- If preferred, it may be implemented as a dedicated SKILL or as a clearly linked measurement module inside `paid-media-and-channel-playbooks`.

---

## Allowed write paths

- `skills/digital-measurement-and-benchmarks/**`
- `skills/paid-media-and-channel-playbooks/**` (only if adding a measurement module rather than a separate SKILL)
- `tickets/T-094-digital-measurement-and-benchmarks.md`
- `research/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (except the paths above)
- `tickets/**` (except this ticket file)
- `.github/**`
- `scripts/**`
- Any country directories (e.g., `/bulgaria/**`, `/nigeria/**`, `/greece/**`)

---

## Required outputs

- Either:
  - `skills/digital-measurement-and-benchmarks/SKILL.md`, **or**
  - A new “Measurement & Benchmarks” section inside `skills/paid-media-and-channel-playbooks/SKILL.md` with clear anchors.

---

## Acceptance criteria

- [ ] Measurement framework covers KPI targets, UTM standards, tracking requirements, and diagnostic steps for underperformance.
- [ ] Guidance is country-agnostic and references the paid media skill for channel context.
- [ ] No files outside `Allowed write paths` are modified.

---

## Execution notes (optional)

- What changed (short): Added global digital measurement skill with KPI guardrails, UTM governance, tracking requirements, diagnostics, and reporting/logging guidance aligned to the updated `/countries/<country>/` path.
- Any open questions: None.
- Follow-up tickets suggested: Country-level measurement addenda once local baselines are available.
