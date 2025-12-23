---
name: multi-channel-messaging
description: Global, API-ready messaging playbook for SMS, Signal, WhatsApp, Telegram, and email with portable schema, rendering rules, consent, and QA.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: global
license: Proprietary (UNIC Evolve internal)
---

# Multi-channel messaging (global skill)

## Purpose
Provide a **single, portable messaging standard** that can be rendered per channel (SMS, Signal, WhatsApp, Telegram, email) without rewriting copy. This skill defines the canonical payload schema, channel rendering/downgrade rules, consent and opt-out handling, QA, and logging so messages can be sent safely via APIs and reused across countries.

## When to use
- Tickets that require outbound notifications, nudges, or follow-ups across more than one channel.
- Building message templates for automations (CRM, marketing automation, bot handoffs) that must degrade gracefully to plain text.
- Situations where compliance and auditability (consent, opt-outs, delivery receipts) are mandatory.

## Hard constraints
1) **Consent and channel gating first.** Only use channels explicitly consented for the audience; store `consent.channel`, `source`, and `timestamp`.
2) **Opt-out honored everywhere.** Always provide and enforce an opt-out (SMS: `Reply STOP`, WhatsApp/Telegram: “Reply STOP to pause”; email: unsubscribe link). Suppress future sends once an opt-out is logged.
3) **No unverified claims.** Do not promise admissions, scholarships, or visa outcomes. Link only to vetted UNIC/UNIC Athens pages and approved short links.
4) **Text-first, downgradeable.** Keep the base copy plain text; apply minimal styling per channel. Always be able to ship a plain-text fallback.
5) **Audit-friendly.** Every send must log ids, timestamps, payload hash, provider response, and any retries or failures.

## Inputs
- Campaign/event: objective, CTA, deadline, link/asset, audience segment.
- Consent log per recipient: allowed channels, language preference, opt-out status, time window (do-not-disturb).
- Personalization fields: name, program, intake/term, campus (UNIC or UNIC Athens), time zone.
- Compliance constraints: local do-not-contact rules, template approvals (WhatsApp Business), data handling limits.
- Fallback preferences: primary/secondary channel order and retry interval.

## Outputs
- Channel-agnostic message payload (JSON/YAML) using the schema below.
- Rendered channel variants (SMS-safe, WhatsApp template with parameters, email subject/body).
- QA log entry covering test sends, provider responses, and opt-out validation.
- Delivery record per recipient with status and next action (retry/failover/success).

## Workflow
1) **Define objective + CTA.** One primary action. Keep a single link and a clear deadline when relevant.
2) **Check consent + window.** Confirm the recipient opted in for the intended channel and that the send window respects time zone/quiet hours.
3) **Draft the base text (plain).** Structure: greeting → purpose → key detail(s) → CTA → opt-out. Aim for ≤480 chars before channel rendering; include one short link max.
4) **Map to the schema.** Populate `audience`, `content.base_text`, `content.variants`, `channel_preferences`, `metadata`, `consent`, `attachments` (if any).
5) **Render per channel.** Apply channel rules below (formatting, length, buttons), generate fallbacks, and strip unsupported markup.
6) **QA before send.** Test on an internal seed list; verify opt-out works, links resolve, and personalization fills. Log provider payloads/hashes.
7) **Send + monitor.** Trigger via API with idempotency keys; capture provider message ids, delivery receipts, and error codes. Apply retry/failover rules.
8) **Close the loop.** Update CRM/DB with delivery + opt-out state; suppress future sends on opt-out or hard bounce; surface failures for manual follow-up.

## Canonical message schema (API-ready)

Field | Description
--- | ---
`id` | Unique message id (UUID); reuse on retries to stay idempotent.
`audience` | Array of recipients `{recipient_id, name, phone, email, locale, timezone, consent: [{channel, timestamp, source, terms_version}], opt_out: bool, attributes: {program, campus, intake}}`.
`objective` | Short label (`offer-reminder`, `event-invite`, `document-chase`) for analytics and throttling.
`content.base_text` | Plain-text master copy (no markup). Holds all required information including the opt-out line.
`content.variants` | Optional per-channel overrides `{sms, whatsapp, signal, telegram, email: {subject, body}}`. Keep aligned to base text.
`cta` | `{label, url, button_allowed (bool), tracking_params}`. Only one CTA per message.
`channel_preferences` | Ordered list `{channel, max_attempts, retry_minutes, send_window, provider_hint, fallback_to}` controlling retries/failover.
`attachments` | Array `{type, url, filename, description, inline (bool)}`; never for SMS; ensure consent and virus scanning.
`metadata` | `{campaign_id, template_id (WA), locale, tags: [], source_system, quiet_hours}`.
`logging` | `{webhook_url, payload_hash, redact: [fields], log_fields: [message_id, provider_status, delivery_ts, error_code, attempt, channel_used]}`.
`audit` | `{consent_verified_at, opt_out_checked_at, approvals: {template, legal}, operator}` for compliance-grade traces.

### JSON example (API payload)

### JSON example
```json
{
  "id": "msg-20260321-001",
  "audience": [
    {
      "recipient_id": "student-123",
      "name": "Alex",
      "phone": "+3570000000",
      "email": "alex@example.com",
      "locale": "en",
      "timezone": "Europe/Athens",
      "consent": [{"channel": "whatsapp", "timestamp": "2026-03-01T10:00:00Z", "source": "form"}],
      "opt_out": false
    }
  ],
  "objective": "offer-reminder",
  "content": {
    "base_text": "Hi {{name}}, this is UNIC Admissions. Your offer for {{program}} is waiting—can you confirm by {{deadline}}? Reply with questions or tap the link to confirm.",
    "variants": {
      "email": {
        "subject": "Confirm your UNIC offer for {{program}}",
        "body": "Hi {{name}},\n\nYour offer for {{program}} is ready. Please confirm by {{deadline}}. Questions? Reply here or schedule a call.\n\nConfirm: {{cta.url}}\n\nIf you prefer not to get these reminders, reply STOP."
      }
    }
  },
  "cta": {"label": "Confirm offer", "url": "https://unic.example/confirm?offer=123", "button_allowed": true},
  "channel_preferences": [
    {"channel": "whatsapp", "max_attempts": 1, "retry_minutes": 0},
    {"channel": "email", "max_attempts": 1, "retry_minutes": 60}
  ],
  "attachments": [],
  "metadata": {"campaign_id": "offer-spring", "template_id": "wa_offer_confirm_v1", "locale": "en", "tags": ["offer", "reminder"], "source_system": "crm"},
  "logging": {"webhook_url": "https://logs.example/webhook", "log_fields": ["payload_hash", "message_id", "provider_status", "delivery_ts", "error_code"]}
}
```

### YAML example (same payload)
```yaml
id: msg-20260321-001
audience:
  - recipient_id: student-123
    name: Alex
    phone: "+3570000000"
    email: alex@example.com
    locale: en
    timezone: Europe/Athens
    consent:
      - channel: whatsapp
        timestamp: 2026-03-01T10:00:00Z
        source: form
        terms_version: v1
    opt_out: false
objective: offer-reminder
content:
  base_text: >
    Hi {{name}}, this is UNIC Admissions. Your offer for {{program}} is
    waiting—can you confirm by {{deadline}}? Reply with questions or tap the link to confirm.
  variants:
    email:
      subject: "Confirm your UNIC offer for {{program}}"
      body: |
        Hi {{name}},

        Your offer for {{program}} is ready. Please confirm by {{deadline}}. Questions? Reply here or schedule a call.

        Confirm: {{cta.url}}

        If you prefer not to get these reminders, reply STOP.
cta:
  label: Confirm offer
  url: https://unic.example/confirm?offer=123
  button_allowed: true
channel_preferences:
  - channel: whatsapp
    max_attempts: 1
    retry_minutes: 0
  - channel: email
    max_attempts: 1
    retry_minutes: 60
attachments: []
metadata:
  campaign_id: offer-spring
  template_id: wa_offer_confirm_v1
  locale: en
  tags: [offer, reminder]
  source_system: crm
logging:
  webhook_url: https://logs.example/webhook
  log_fields: [payload_hash, message_id, provider_status, delivery_ts, error_code]
audit:
  consent_verified_at: 2026-03-21T09:55:00Z
  opt_out_checked_at: 2026-03-21T09:55:00Z
  approvals:
    template: wa_offer_confirm_v1
    legal: true
  operator: messaging-bot
```

## Channel rendering rules and downgrade matrix

Channel | Formatting | Length/limits | Buttons/links | Downgrade path
--- | --- | --- | --- | ---
SMS | Plain text only; avoid Unicode heavy chars | ~160 chars per segment; aim ≤320 | Single short link; no buttons | If >320 chars, trim to essentials and keep one link; split into two concise messages only if needed
Signal | Supports basic bold/italic/mono; attachments allowed | Generous length; still keep concise | One link; avoid heavy images by default | Strip styling if provider fallback required; remove attachments if not permitted
WhatsApp | Markdown-like `*bold*`, `_italics_`; templates may require approval | Template-dependent; stay concise | Buttons allowed in approved templates; single link recommended | If template/button unsupported, send plain-text variant without buttons
Telegram | Markdown/HTML permitted; inline links OK | Higher limits; prefer ≤700 chars | Inline URL or single link; buttons via bots | Fallback to plain text if Markdown rejected; avoid multi-link spam
Email | Full subject/body; basic Markdown/text | Subject ≤78 chars; body concise | Multiple links allowed but prefer one CTA | If HTML blocked, ensure text body carries CTA and opt-out

**General downgrade rules:** If a channel disallows styling or buttons, send the `content.base_text` with a single CTA link and explicit opt-out. Never drop the opt-out line when downgrading.

### Channel guardrails and opt-out copy
- **SMS:** Opt-out line: `Reply STOP to opt out.` Strip emoji; avoid >1 link. Do not send attachments.
- **Signal:** Opt-out line: `Reply STOP to pause messages.` Keep attachments <2MB unless user expects media.
- **WhatsApp:** Use approved templates with parameters; include `Reply STOP to opt out.` Buttons only if approved; otherwise share the URL in-line.
- **Telegram:** Opt-out line: `Reply STOP to pause updates.` Avoid sending multiple links; bots should throttle to avoid spam flags.
- **Email:** Include unsubscribe link + plain-text opt-out line in the footer. Subject ≤78 chars; preheader optional but recommended.

## Content building blocks (portable template)
```
Hi {{name}}, this is {{sender}} (UNIC/UNIC Athens).
Purpose: {{one-line reason}}.
Detail: {{deadline or key fact}}.
CTA: {{action}} → {{link}}.
If you’d like to stop these updates, reply STOP.
```
- Keep personalization lightweight; avoid branching logic in copy. Apply locale and timezone to deadlines.
- One CTA only. If two actions are needed, send separate messages.
- Avoid attachments unless necessary; prefer links to hosted assets with tracking.

## QA and logging checklist
- Validate consent + opt-out state before enqueueing; log `consent_verified_at` and `terms_version`.
- Render each channel variant and visually spot-check (including emoji/Unicode stripping for SMS). Keep pre-send snapshots with payload hash.
- Test send to an internal device per channel; confirm link works, UTM params preserved, and opt-out behaves as expected.
- Capture and store: `message_id`, provider response code, delivery/seen timestamps (if available), payload hash, attempt count, channel used, error details, and retries executed.
- Retries: exponential backoff; fail over to next consented channel only after documenting failure reason (throttle/quiet-hour aware).
- Suppression: on STOP/opt-out/hard bounce, mark `opt_out=true`, log source/time, sync to CRM suppression lists, and halt further sends.
- Reporting: aggregate delivery rate, click-through (if tracked), opt-out rate, and error codes per campaign_id.

## API integration guardrails
- Use idempotency keys per `id` to prevent double-sends.
- Respect rate limits; throttle bursts and obey quiet hours per timezone.
- Shorten links via approved domains; avoid rotating domains that trigger spam filters.
- Keep PII minimal in logs; hash payloads when exporting to observability tools.
- For WhatsApp templates, store `template_id` and language code; reject sends if not approved.

## Implementation quickstart
1) Build the payload using the schema (JSON/YAML) and store the payload hash.
2) Confirm consent + opt-out, then select the primary channel and backup channel from `channel_preferences`.
3) Render per channel, apply downgrade rules, and enqueue with idempotency keys.
4) Log provider responses to `logging.webhook_url`; persist delivery status and retries.
5) On completion, sync suppression flags and delivery outcomes back to CRM; archive payload + hash for audits.

## Country addenda (future tickets)
Do not add country specifics here. For local etiquette, language, or compliance (e.g., DND hours, mandatory keywords), create `countries/<country>/skills/multi-channel-messaging-addendum/SKILL.md` via a country-scoped ticket and link back to this global skill.
