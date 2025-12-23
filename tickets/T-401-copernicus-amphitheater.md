# T-401: UNIC Nicosia Europa Building — Copernicus Amphitheater subfolder

Status: done
Type: content
Priority: P2
Dependencies: (none)
Claimed-by: work
Claimed-at: 2025-12-21T23:01:33+00:00
Last-updated: 2025-12-21

---

## Goal

Add a dedicated subfolder for the **Copernicus Amphitheater** under `Infrastructure/UNIC Nicosia/Europa Building/` to capture venue-specific layout, capacity, and scheduling notes.

---

## Context

- Request: scaffold documentation space for the Copernicus Amphitheater within the Europa Building.
- Scope: limited to adding the new subfolder and a clear placeholder README so future facility details have a home.
- Governance: no other campus folders or control-plane files should be touched.

---

## Allowed write paths

- `Infrastructure/UNIC Nicosia/Europa Building/**`
- `tickets/T-404-copernicus-amphitheater.md`
- `executions/T-404-copernicus-amphitheater/**` (optional notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- `tickets/**` (except this ticket file)
- `.github/**`
- `scripts/**`
- Any paths not listed in Allowed write paths

---

## Required outputs

- `Infrastructure/UNIC Nicosia/Europa Building/Copernicus Amphitheater/README.md` created with a concise placeholder describing intended content (layout, capacity, AV, scheduling/logistics).
- Parent `Infrastructure/UNIC Nicosia/Europa Building/README.md` references the Copernicus Amphitheater location so it is discoverable.

---

## Acceptance criteria

- Copernicus Amphitheater subfolder exists at `Infrastructure/UNIC Nicosia/Europa Building/Copernicus Amphitheater/`.
- README in the new subfolder states purpose and expected details without speculative claims.
- Europa Building README links or lists the Copernicus Amphitheater so navigation is clear.
- No files outside Allowed write paths are modified.

---

## Execution notes (optional)

- What changed (short): Relocated the Copernicus Amphitheater image set into a `photos/` subfolder and updated local documentation to reference the new location alongside the photo-based description.
- Open questions: None.
- Follow-up tickets suggested: Populate verified dimensions, MEP/suppression specs, AV hardware details, and official capacity when onsite data is available.
