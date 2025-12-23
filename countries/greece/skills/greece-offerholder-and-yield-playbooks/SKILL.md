---
name: greece-offerholder-and-yield-playbooks
description: Greece addendum to the global offerholder and yield playbooks skill; adds local channel, timing, and compliance nuances.
metadata:
  owner: evobuilder
  version: "1.0"
  scope: greece
---

# Greece addendum: offerholder & yield playbooks

Use `/skills/offerholder-and-yield-playbooks/SKILL.md` for cadences and data capture. Apply these Greece-specific notes.

## Channel and language norms
- Lead with email and Viber/phone for parents and counselors; WhatsApp adoption varies, so confirm opt-in before using it for documents.
- Provide Greek-language templates by default; keep English variants for IB or international schools.

## Timing anchors
- Reduce volume during Panhellenic exam preparation and results weeks; shift to lighter check-ins or self-serve resources.
- For Athens campus messaging, highlight commuting/housing options early; for Nicosia, include travel/ID requirements for EU citizens and any timelines for residence registration.

## Compliance and documentation
- Log every touch with language and channel in the country data model; avoid storing national ID numbers—use application IDs instead.
- Capture explicit consent when adding students or parents to messaging groups; store source + timestamp.

## Objection handling to localize
- Cost: keep EUR pricing and avoid implying installment plans unless confirmed by admissions.
- Recognition: use the Greece recognition and licensure skill (`countries/greece/skills/greece-recognition-and-licensure/`) for sourced responses before promising licensure outcomes.
