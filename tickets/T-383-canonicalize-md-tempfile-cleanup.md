# T-383: Remove tracked md_files list from canonicalize workflow

Status: done  
Type: integration  
Priority: P0  
Dependencies: (none)  
Claimed-by: work  
Claimed-at: 2025-12-21T18:26:53Z  
Last-updated: 2025-12-21T18:27:22Z  

---

## Goal

Stop the canonicalize workflow from committing `md_files.txt`, switch to a run-scoped filename (ticket-prefixed) for changed Markdown lists, and ensure any scratch file is cleaned up after use.

---

## Context

`md_files.txt` is currently tracked and rewritten by the canonicalize workflow, creating constant merge conflicts across branches. We need to make the workflow self-contained by using an ephemeral file per run and cleaning it up once formatting completes.

---

## Allowed write paths

- `.github/workflows/canonicalize-md.yml`
- `md_files.txt`
- `tickets/T-367-canonicalize-md-tempfile-cleanup.md`
- `executions/**` (optional run notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**`
- Other `tickets/**` files
- Country directories (`countries/**`)
- `.github/**` files not listed in Allowed write paths

---

## Required outputs

- Canonicalize workflow uses a run-scoped, ticket-prefixed scratch file (not tracked) for Markdown path collection, deletes it after use, and still canonicalizes changed `.md` files.
- `md_files.txt` is removed from version control so it no longer causes merge conflicts.
- Ticket updated with completion status and brief execution notes.

---

## Acceptance criteria

- No steps in `.github/workflows/canonicalize-md.yml` read or write the tracked `md_files.txt`; the workflow writes the changed-file list to an ephemeral path named with the ticket prefix (e.g., `T-367-md-files-<...>.txt`) and cleans it up after formatting.
- Workflow still formats only the `.md` files changed in the PR and pushes `chore: canonicalize markdown` when it changes files.
- `md_files.txt` is deleted from the repo.
- Ticket marked `done` with concise execution notes; no files outside Allowed write paths are modified.

---

## Execution notes (optional)

- Canonicalize now writes changed Markdown paths to a T-367-prefixed temp file in `RUNNER_TEMP`, cleans it up after processing, and the tracked `md_files.txt` was removed to eliminate merge conflicts.
