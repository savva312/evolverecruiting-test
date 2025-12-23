# T-410: Photo documentation skill (naming, descriptions, folder indices)

Status: done  
Type: structure  
Priority: P1  
Allowed write paths:
- skills/photo-documentation/**
- skills/README.md
- tickets/T-410-photo-documentation-skill.md
- executions/T-410-photo-documentation-skill/**
Forbidden write paths:
- README.md
- AGENTS.md
- ROADMAP.md
- skills/** (outside the path listed above)
- tickets/** (except this ticket file)
- .github/**
- scripts/**
- Any paths not listed in Allowed write paths
Required outputs:
- skills/photo-documentation/SKILL.md documenting conventions for renaming photo files, writing per-photo descriptions, and maintaining per-folder indices (with wishlist coverage) for facility/documentation shoots.
- skills/README.md updated to include the new photo documentation skill.
Acceptance criteria:
- Ticket is claimed with Claimed-by and Claimed-at fields set to the current branch and timestamp.
- SKILL file includes: (1) file naming pattern that captures date + location + view/angle; (2) step-by-step instructions to write concise descriptions; (3) per-folder index template covering filename, view/what’s visible, location/context, and wishlist gaps; (4) guidance on handling subfolders, formats, and source notes.
- skills/README.md lists the new skill with a concise label.
- No edits occur outside Allowed write paths.
Dependencies: none
Claimed-by: work
Claimed-at: 2025-12-22T06:14:27Z
Last-updated: 2025-12-22T06:15:37Z
Notes/Context:
- Request: add a reusable global skill for photo handling so facility shoots have consistent naming, descriptions, and indices per folder.
- Scope: global; avoid duplicating country-specific guidance.
- What changed (short): Added global photo-documentation skill covering naming, per-photo descriptions, and folder indices with wishlist coverage; indexed it in `skills/README.md`.
