# T-032: Greece folder alignment with Bulgaria

Status: archived
Type: structure  
Priority: P1  
Dependencies: T-022  
Claimed-by: work  
Claimed-at: 2025-12-20T16:59:29+00:00  
Last-updated: 2025-12-20

---

## Goal

Mirror the Bulgaria country subtree inside `/greece/`, creating the same folder scaffolding (data, market, entities, go-to-market, program clusters, reports, and skills) while keeping all content Greece-scoped. Add city folders for school profiles using the provided Greece city list.

---

## Allowed write paths

- `greece/**`
- `tickets/T-028-greece-folder-alignment.md`
- `research/T-028-greece-folder-alignment/**` (optional run notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- `skills/**` (global skills)
- Other country directories (e.g., `/bulgaria/**`, `/nigeria/**`)
- Any other tickets besides status updates to this file

---

## Required outputs

- `/greece/` subtree includes the same directory layout present in `/bulgaria/` (data, entities, go-to-market, market, program-clusters, reports/structured, skills subfolders).
- `/greece/entities/schools/profiles/` contains folders for the 20 named Greek cities (plus an `other` catch-all).
- Updated Greece README(s) as needed to reference the expanded structure.
- Ticket status updated on completion with a short “What changed” note.

---

## Acceptance criteria

- Greece directory tree matches Bulgaria’s structure (folders only; no Bulgarian data copied) under `greece/**`.
- City-level folders exist for Athens, Thessaloniki, Patras, Heraklion, Larissa, Volos, Ioannina, Chania, Rhodes, Kavala, Kalamata, Serres, Komotini, Xanthi, Alexandroupoli, Tripoli, Rethymno, Katerini, Corfu, Lamia, and `other`.
- No files outside the allowed write paths are modified.
- Greece README or index files reflect the new scaffolding so contributors know where to add content.

---

## Notes/Context

- Keep all new placeholders Greece-specific and text-first; do not migrate Bulgaria data or narratives.
- Use lightweight placeholders (`README.md` or `.gitkeep`) to ensure directories are tracked.
- What changed: Mirrored the Bulgaria folder scaffold into `greece/` (data, entities, go-to-market, market, program clusters, reports/structured, skills) and added city folders for school profiles using the provided 20-city list plus an `other` catch-all. Added Greece-scoped READMEs and skill stubs to guide future content.
