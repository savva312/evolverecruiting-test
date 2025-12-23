# T-111: Global skills index refresh

Status: done
Type: structure
Priority: P2
Dependencies: T-020, T-026
Claimed-by: work
Claimed-at: 2025-12-20T19:52:16+00:00
Last-updated: 2025-12-20

---

## Goal

Ensure `skills/README.md` lists every global skill folder with concise labels so contributors can quickly locate the right procedures.

## Context

- New global skills have been added under `/skills/` and the index needs to stay complete.
- Root control-plane rules require a structure ticket to modify `skills/**`.

## Allowed write paths

- `skills/README.md`
- `tickets/T-090-global-skills-index-refresh.md`
- `research/**` (optional execution notes)

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- Country directories (e.g., `/bulgaria/**`, `/greece/**`, `/nigeria/**`, `/lebanon/**`, `/romania/**`, `/serbia/**`, `/jordan/**`)
- Other tickets in `/tickets/**` (except status updates to this file)
- `.github/**`
- `scripts/**`
- `research/runs/**`

## Required outputs

- `skills/README.md` updated with a complete, labeled index of all global skills.

## Acceptance criteria

- Global skill index enumerates every skill directory under `/skills/` (excluding the README) with names matching folder names and brief descriptions.
- No files outside the Allowed write paths are modified.
- Ticket status updated to `done` with a short “What changed” note.

## Execution notes (optional)

- What changed (short): Updated `skills/README.md` global index to enumerate every current global skill folder with concise labels.
