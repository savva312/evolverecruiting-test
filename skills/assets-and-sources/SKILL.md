---
name: assets-and-sources
description: How to store assets (pdf/images/video) and how to record sources so agents can reliably use them; includes a text-first policy for binary artifacts.
compatibility: Any repo that may include non-text references.
metadata:
  author: canonical
  version: "1.0"
---

## Text-first policy
Assume some agents/models cannot directly interpret binary assets reliably.

If you add a binary asset (PDF/image/video), also add a **text companion**:
- a markdown summary
- key extracted text
- a link or citation to the original

## Suggested locations
- Small static assets: `/assets/`
- Source captures / excerpts: `/sources/` (markdown or text)
- Doc-embedded assets: `/docs/assets/` if the repo is docs-heavy

## Size and git friendliness
- Prefer small files.
- Use Git LFS for large binaries if this repo allows it.
- Never commit secrets inside documents (redact before storing).

## Source recording (minimum viable)
For each research-heavy ticket, record:
- what you looked at (links / doc names)
- when you accessed it (date)
- what you extracted (2–10 bullets)
Store this either:
- in the ticket file under a “Sources” section, or
- in a dedicated markdown file in `/sources/` referenced by the ticket
