# T-584: Infrastructure building base scaffold roll-out

Status: done
Type: content
Priority: P2
Agent: EvoTicket Resolver
Claimed-by: work
Claimed-at: 2025-12-22T20:32:31+00:00
Last-updated: 2025-12-22

Allowed write paths:
- Infrastructure/**
- tickets/T-584-infrastructure-building-scaffolds.md
- tickets/index.md
- executions/T-584-infrastructure-building-scaffolds/**

Forbidden write paths:
- README.md
- AGENTS.md
- ROADMAP.md
- skills/**
- tickets/202512 - Archived Tickets/**
- .github/**
- scripts/**

Required outputs:
- Base scaffold per `skills/infrastructure-building-folders/SKILL.md` added for every building folder currently present under `Infrastructure/` campuses (README.md, planning/, architecture/floorplans/photos, rooms/).
- Brief README in each building root describing purpose and pointing to architecture/planning/rooms subfolders.
- Ticket status updated to done with a short "What changed" note once work is complete.

Acceptance criteria:
- Every building directory under `Infrastructure/` includes the base scaffold items defined in the skill (README.md, planning/, architecture/floorplans/, architecture/photos/, rooms/).
- No extra empty subfolders beyond the base scaffold are introduced; new README files provide minimal guidance without speculative details.
- No files outside Allowed write paths are modified.
- Ticket file reflects completion state with summary when finished.

Dependencies:
- skills/infrastructure-building-folders/SKILL.md

Notes/Context:
- Applies the infrastructure building folder skill across all existing campus building folders so future room- or drawing-level content has a consistent home.
- What changed: Added planning, architecture (floorplans/photos), and rooms scaffolds plus refreshed root READMEs for every existing building under Infrastructure; campuses without building folders remain unchanged.
