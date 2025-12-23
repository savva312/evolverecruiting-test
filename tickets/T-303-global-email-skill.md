# T-303: Global outbound email skill for AWS SES

Status: done
Type: structure
Priority: P2
Dependencies:
Claimed-by: work
Claimed-at: 2025-12-21T10:20:12Z
Last-updated: 2025-12-21

---

## Goal

Create a reusable global skill that instructs agents how to craft outbound emails that can be ingested by AWS SES, including both the raw `.eml` file and a companion Markdown file for human readability.

---

## Context

Agents occasionally need to deliver outbound email content via AWS SES. Providing a standard workflow and templates for producing RFC 822-compliant `.eml` files plus a human-friendly `.md` companion will reduce mistakes and speed delivery.

---

## Allowed write paths

- `skills/email-ses-outbound/**`
- `skills/README.md`
- `tickets/T-271-global-email-skill.md`
- `executions/**` (optional notes)

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- Any country directories (e.g., `/countries/**`)
- Other tickets in `/tickets/**` (except status updates to this file)
- `.github/**`
- `scripts/**`
- `skills/**` paths other than those explicitly allowed above

## Required outputs

- `skills/email-ses-outbound/SKILL.md` outlining the step-by-step process to generate a raw RFC 822 email file for SES and a companion `.md` file with context and previews.
- `skills/README.md` updated to list the new global skill.
- This ticket updated to `Status: done` with a short "What changed" note when complete.

## Acceptance criteria

- Skill includes YAML frontmatter, SES-specific guidance (sandbox vs production, verified senders/recipients), and clear steps to assemble headers, MIME boundaries, plain-text and HTML parts, and optional attachments.
- Provides minimal templates for `.eml` content and the companion `.md` context file, including placeholders for subject, sender/recipient, and body content.
- Instructs agents how to pass the `.eml` into `SendRawEmail` (raw bytes/Base64) and where to store files in the repo.
- No files outside `Allowed write paths` are modified.

## Execution notes (optional)

- What changed (short): Refreshed the global `email-ses-outbound` skill with detailed SES sandbox/production guardrails, multipart/attachment templates, companion `.md` brief guidance, and SendRawEmail usage; updated `skills/README.md`.
- Any open questions: None.
- Follow-up tickets suggested: None.
