# T-406: Old Teaching Kitchen photo folder reorganization

Status: done
Type: structure
Priority: P1
Allowed write paths:
- Infrastructure/UNIC Nicosia/Main Building/Old Teaching Kitchen/**
- tickets/T-406-old-teaching-kitchen-photos-subfolder.md
- executions/T-406-old-teaching-kitchen-photos-subfolder/**
Forbidden write paths:
- README.md
- AGENTS.md
- ROADMAP.md
- skills/**
- tickets/** (except this ticket file)
- .github/**
- scripts/**
- Any paths not listed in Allowed write paths
Required outputs:
- Infrastructure/UNIC Nicosia/Main Building/Old Teaching Kitchen/photos/ (new subfolder containing the photo assets and index)
- Infrastructure/UNIC Nicosia/Main Building/Old Teaching Kitchen/README.md updated to point to the relocated photo index
- tickets/T-406-old-teaching-kitchen-photos-subfolder.md updated to reflect claim and completion
Acceptance criteria:
- Ticket is claimed (Status: in-progress) with Claimed-by and Claimed-at populated before work begins.
- All photo assets and the photo index currently in the Old Teaching Kitchen directory are moved into the new `photos/` subfolder with filenames preserved.
- README links correctly to the relocated index; no broken references remain.
- Original directory no longer contains loose photo files or the index file outside `photos/`.
- No edits occur outside the Allowed write paths.
Dependencies: none
Claimed-by: work
Claimed-at: 2025-12-21T23:04:39+00:00
Last-updated: 2025-12-21T23:04:39+00:00
Notes/Context:
- Requestor wants the existing Old Teaching Kitchen photo set and index organized under a dedicated `photos/` subfolder for cleaner navigation.
- Completed: created `photos/` subfolder, moved all existing images and the 2025-12-20 photo index into it, and updated README link.
