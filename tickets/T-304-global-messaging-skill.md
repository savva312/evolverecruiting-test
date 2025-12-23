# T-304: Global multi-channel messaging skill

Status: done
Type: content
Priority: P1
Dependencies: T-017, T-020, T-026, T-095
Claimed-by: work
Claimed-at: 2025-12-21T10:20:03Z
Last-updated: 2025-12-21

---

## Goal

Create a **global, API-ready messaging skill** that standardizes how to compose, log, and send compliant outbound messages across SMS, Signal, WhatsApp, Telegram, and email. The skill must define a portable message schema, channel-specific formatting rules, consent/opt-out handling, and delivery QA steps that countries can extend via local addenda.

---

## Context

- Agents need a single, text-first template system that can be rendered per channel while keeping consent, opt-out, and logging requirements consistent.
- The skill should define: (1) a canonical message payload schema (JSON/YAML), (2) formatting/feature deltas by channel, (3) rendering rules and examples, (4) QA and logging requirements (ids, timestamps, outcomes), and (5) safety guardrails (no promises, respect local consent).
- Country etiquette, language, or legal nuances should be added later via country-scoped addenda, not by editing the global skill.

---

## Allowed write paths

- `skills/multi-channel-messaging/**`
- `skills/README.md`
- `tickets/T-272-global-messaging-skill.md`
- `research/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- Any country directories (e.g., `/countries/**`)
- Other tickets in `/tickets/**` (except this ticket file for status updates)
- `.github/**`
- `scripts/**`

---

## Required outputs

- `skills/multi-channel-messaging/SKILL.md` capturing the schema, rendering rules, channel nuances, consent/opt-out requirements, and delivery QA.
- `skills/README.md` updated to list the new skill.
- `tickets/T-272-global-messaging-skill.md` updated to `done` with a short “What changed” note after completion.

---

## Acceptance criteria

- [x] Skill defines a channel-agnostic message schema (fields for audience, content variants, consent, metadata, attachments, and delivery preferences) with JSON/YAML examples suitable for APIs.
- [x] Channel rendering section covers SMS, Signal, WhatsApp, Telegram, and email: supported formatting, length limits, buttons/links handling, and downgrade rules (plain text fallback).
- [x] QA and logging steps detail ids/timestamps, provider responses, retries/escalations, and opt-out handling.
- [x] Guidance is global; country nuances are explicitly deferred to addenda.
- [x] No files outside `Allowed write paths` are modified.

---

## Execution notes (optional)

- What changed (short): Refreshed the global multi-channel messaging skill with richer API schema (JSON/YAML), channel guardrails and opt-out copy, QA/logging upgrades, and updated skills index entry.
- Any open questions: None.
- Follow-up tickets suggested: Create country addenda for channel etiquette, quiet hours, template approvals, and mandatory keywords where required.
