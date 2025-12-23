---
name: email-ses-outbound
description: "Workflow for creating RFC 822 emails plus a companion Markdown brief that AWS SES can ingest via SendRawEmail."
compatibility: AWS SES SendRawEmail; RFC 822 MIME messages.
metadata:
  author: evobuilder
  version: "1.1"
---

## When to use this
Use this skill when you need an outbound email that SES can send directly from a raw RFC 822 (`.eml`) file, while keeping a human-friendly `.md` brief in the repo.

## SES prerequisites and guardrails
- Sandbox vs production: sandbox requires **verified** sender *and* recipient addresses; production still requires verified senders. Always work in the correct region/account and respect sending limits.
- Use only SES-verified identities for `From` and `Reply-To`. If using a custom MAIL FROM domain, ensure DKIM/SPF/DMARC are valid outside the repo.
- Keep secrets and credentials out of the repo. Store only content and metadata.
- Author files in UTF-8. SES normalizes line endings, but prefer `\n` (Unix); keep header lines under ~78 chars and fold if needed.
- Choose a unique boundary string that will not appear in the body (e.g., `SES-2025-01-A`).

## Where to place files in the repo
- Store the `.eml` in a stable, reviewable path allowed by the ticket, e.g., `templates/email/<campaign>/message.eml` or `templates/email/<country>/<campaign>/message.eml`.
- Save the companion Markdown brief alongside it (e.g., `message.md`) so reviewers do not need to parse MIME boundaries.
- Keep both files under the same folder for easy linking in tickets and PRs. Example:
  ```
  templates/email/offerholder-welcome/
    message.eml
    message.md
  ```

## Build the raw RFC 822 email (step-by-step)
1. Gather metadata: `From`, `To` (comma-separated), optional `Cc`/`Bcc`, `Reply-To`, and `Subject`. Set `Date` in RFC 2822 format and generate a `Message-ID` (e.g., `<welcome-2025-01-21@example.com>`).
2. Draft both bodies: plain-text is mandatory; HTML is recommended. Keep content consistent between them.
3. Pick a boundary token (e.g., `SES-2025-01-A`).
4. Compose headers, then add a blank line, then the multipart body. Minimum headers: `From`, `To`, `Subject`, `Date`, `Message-ID`, `MIME-Version`, and `Content-Type`.
5. For attachments (only if allowed by the ticket), switch the outer content type to `multipart/mixed`, nest a `multipart/alternative` part for text+HTML, and add attachment parts with Base64 content.
6. Save as UTF-8 text with the `.eml` extension; ensure the final boundary ends with `--`.

### Minimal templates (copy and replace placeholders)
**Multipart alternative (text + HTML)**
```
From: Sender Name <sender@example.com>
To: Recipient One <one@example.com>, Recipient Two <two@example.com>
Subject: {{SUBJECT_GOES_HERE}}
Date: Tue, 21 Jan 2025 10:00:00 +0000
Message-ID: <{{STABLE_ID}}@example.com>
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="SES-2025-01-A"

--SES-2025-01-A
Content-Type: text/plain; charset="UTF-8"

{{PLAIN_TEXT_BODY}}

--SES-2025-01-A
Content-Type: text/html; charset="UTF-8"

{{HTML_BODY}}

--SES-2025-01-A--
```

**Text-only (no HTML)**
```
From: Sender Name <sender@example.com>
To: Recipient One <one@example.com>
Subject: {{SUBJECT_GOES_HERE}}
Date: Tue, 21 Jan 2025 10:00:00 +0000
Message-ID: <{{STABLE_ID}}@example.com>
MIME-Version: 1.0
Content-Type: text/plain; charset="UTF-8"

{{PLAIN_TEXT_BODY}}
```

**Multipart mixed with attachment**
```
From: Sender Name <sender@example.com>
To: Recipient One <one@example.com>
Subject: {{SUBJECT_GOES_HERE}}
Date: Tue, 21 Jan 2025 10:00:00 +0000
Message-ID: <{{STABLE_ID}}@example.com>
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="SES-2025-01-MIXED"

--SES-2025-01-MIXED
Content-Type: multipart/alternative; boundary="SES-2025-01-A"

--SES-2025-01-A
Content-Type: text/plain; charset="UTF-8"

{{PLAIN_TEXT_BODY}}

--SES-2025-01-A
Content-Type: text/html; charset="UTF-8"

{{HTML_BODY}}

--SES-2025-01-A--

--SES-2025-01-MIXED
Content-Type: application/pdf; name="attachment.pdf"
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="attachment.pdf"

{{BASE64_CONTENT}}

--SES-2025-01-MIXED--
```

## Companion `.md` brief template (keep beside the `.eml`)
```
# Email: {{CAMPAIGN_OR_SUBJECT}}

- Channel: AWS SES (SendRawEmail)
- EML file: {{relative/path/to/message.eml}}
- Sender: {{From}}
- Recipients: {{To/Cc/Bcc placeholder list}}
- Audience: {{who receives this}}
- Purpose: {{goal of the send}}
- Variables/placeholders: {{list handlebars or placeholder keys and meanings}}
- Links/UTM: {{list key links and tracking parameters}}

## Plain-text preview
{{paste the plain-text body}}

## HTML preview (optional)
{{paste or describe key HTML blocks; keep inline styles minimal}}

## QA checklist
- [ ] Sender and reply-to are verified/allowed in the SES account and region
- [ ] Recipient list matches the ticket scope and (if sandbox) is verified
- [ ] Subject matches both bodies; placeholders resolved or documented
- [ ] Plain-text and HTML content are consistent
- [ ] Boundary strings do not appear in the bodies
- [ ] Attachments (if any) are Base64-encoded, sized under SES limits, and allowed by policy
- [ ] File saved as UTF-8 `.eml` and stored in the allowed repo path
```

## Sending with SES
- Use `SendRawEmail` with the `.eml` bytes. Most SDKs accept Base64 in `RawMessage.Data`; the AWS CLI accepts binary via `fileb://`.
- AWS CLI example:
  ```
  aws ses send-raw-email \
    --from "sender@example.com" \
    --destinations "one@example.com" "two@example.com" \
    --raw-message Data=fileb://templates/email/offerholder-welcome/message.eml \
    --region <ses-region>
  ```
- SDK pseudocode:
  - Read `message.eml` as bytes.
  - If required by the SDK, Base64-encode the bytes; otherwise pass them directly.
  - Call `SendRawEmail` with `Source` (From), `Destinations` (To/Cc/Bcc), and `RawMessage`.
- Keep the `.eml` and `.md` together for review; do **not** store credentials or SES configuration in the repo.

## Quick QA before committing
- Open the `.eml` in a mail client or parser to confirm text and HTML render and boundaries close properly.
- Double-check headers for typos, missing commas, or mismatched counts (e.g., `Destinations` vs `To/Cc/Bcc`).
- Validate date/time zone, subject line, and any dynamic variables against the ticket requirements.
- Confirm the ticket scope allows the storage path you chose and that no real PII is embedded unless explicitly permitted.
