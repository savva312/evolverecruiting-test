# T-392: UNIC Nicosia housing options content

Status: done
Type: content
Priority: P1
Dependencies: none
Claimed-by: work
Claimed-at: 2025-12-21T21:25:00+00:00
Claimed-at: 2025-12-21T21:13:53Z
Claimed-at: 2025-12-21T21:20:14Z
Claimed-by: branch
Claimed-at: 2025-12-21T21:21:00+00:00
Claimed-at: 2025-12-21T21:13:55Z

---

## Goal

Populate the UNIC Nicosia housing section with concrete, recruiter-ready guidance covering university-managed residences and vetted private accommodation options.

## Context

Recruiters need a single page they can share with prospects and parents that summarizes on-campus/managed residences (UNIC Residences SIX, TRIANGLE, U) plus trusted third-party options like Unihalls and nearby dorm/apartment providers, with prices, room types, booking steps, and location notes.

## Allowed write paths

- UNIC/unicnicosia/housing/**
- tickets/T-372-unic-nicosia-housing.md
- executions/T-372-unic-nicosia-housing/**

## Forbidden write paths

- README.md
- AGENTS.md
- ROADMAP.md
- skills/**
- tickets/** (except this ticket)
- .github/**
- scripts/**
- Any paths not listed in Allowed write paths

## Required outputs

- Updated `UNIC/unicnicosia/housing/README.md` with structured housing guidance that covers UNIC Residences (SIX, TRIANGLE, U) and other organized dorm/apartment options (e.g., Unihalls, Nicosia student apartments), including pricing ranges, room types, booking steps, and proximity/transport notes.

## Acceptance criteria

- Housing page lists at least: SIX, TRIANGLE, U (UNIC Residences), Unihalls, and additional organized dorm/apartment options with short descriptions and practical details (room types, amenities, distance to campus, estimated monthly cost ranges, lease/booking notes).
- Provides clear booking workflow (who to contact, required documents/deposits, timing) for UNIC Residences and third-party options.
- Highlights safety/maintenance/support and any notable restrictions (e.g., lease terms, utilities, meal plans, parking).
- Content stays within allowed paths and is self-contained (links relative where possible).

## Notes/Context

If more providers emerge during research, include up to two additional vetted options with concise fact-based notes and mark assumptions if data is estimated.

## What changed

- Added a detailed Unihome Student Residence profile (room specs, annual rates, amenities, booking steps, contacts) and linked it from the housing overview with updated pricing/booking guidance for third-party options.
- Added a detailed Triangle Residence profile with floor-by-floor weekly pricing, amenities, booking and contact info, and linked it from the housing README, keeping existing SIX/U and third-party options intact.
- Added a detailed SIX Residence profile with room-by-room rates, sizes, equipment, deposits, and booking steps, and refreshed the housing README pricing/booking guidance to point recruiters to the new detail while keeping Unihalls/private rental notes intact.
- Added recruiter-facing housing summary for UNIC Nicosia covering UNIC Residences (SIX, TRIANGLE, U) with current weekly rates, amenities, booking flow, and contacts, plus third-party/market options (Unihalls, private apartments) with cost guidance and safety/lease notes.
- Added NYM Student Residence profile and integrated it into the housing quick view with estimated pricing and a verification-focused booking workflow (website unavailable at time of research).
- Created a detailed U Student Residence profile with room-by-room pricing, amenities, and booking guidance, and refreshed the housing overview to link to it.
