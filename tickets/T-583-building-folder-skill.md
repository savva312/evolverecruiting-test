# T-583: Infrastructure building folder skill

Status: done
Type: content
Priority: P2
Agent: EvoTicket Resolver
Claimed-by: work
Claimed-at: 2025-12-22T20:26:41Z

Allowed write paths:
- /skills/**
- /tickets/T-583-building-folder-skill.md

Forbidden write paths:
- /AGENTS.md
- /ROADMAP.md
- /tickets/202512 - Archived Tickets/**

Required outputs:
- /skills/infrastructure-building-folder-skill.md

Acceptance criteria:
- Skill captures a world-class folder structure for UNIC campus buildings consistent with Infrastructure conventions.
- Base setup defaults to creating only README.md, planning/, architecture/ (with floorplans/ and photos/), and rooms/ to avoid empty directories.
- Skill instructs how to expand incrementally (e.g., engineering, operations, compliance, room/equipment subfolders) without creating empty folders by default.
- Includes guidance on metadata, naming, and how to store drawings/photos responsibly.

Notes/Context:
- User asked for a skill covering building folder setup with a minimal default scaffold to avoid empty folders.

What changed:
- Added global skill `skills/infrastructure-building-folders/SKILL.md` outlining minimal base scaffold and incremental expansion rules.
- Updated `skills/README.md` to index the new skill.
