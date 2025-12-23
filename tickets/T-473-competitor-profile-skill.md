# T-473: Global competitor profile + presence skill

Status: done
Type: structure
Priority: P1
Dependencies: T-020, T-026, T-121
Claimed-by: work
Claimed-at: 2025-12-22T06:32:23+00:00
Last-updated: 2025-12-22T06:33:42+00:00

---

## Goal

Create a global skill for documenting competitor institutions so agents treat each competitor holistically: the home-country base profile, cross-country presence/competition lists, and a reusable profile template.

---

## Context

- Competitor content currently lives inside country folders without a unified skill describing how to structure base profiles and cross-country competition.
- The program-clusters skill covers cluster-level competitor sets, but we need a skill focused on the **institution-level** competitor profile and how to capture its presence in multiple markets.
- This skill should standardize how we capture the home/branch location, the countries where the competitor actively recruits, and the profile structure for the competitor itself.

---

## Allowed write paths

- `skills/competitors/**`
- `skills/README.md`
- `tickets/T-411-competitor-profile-skill.md`
- `executions/**` (optional run notes)

---

## Forbidden write paths

- `README.md`
- `AGENTS.md`
- `ROADMAP.md`
- Other tickets in `/tickets/**`
- Country directories (e.g., `/countries/**`)
- `.github/**`
- `scripts/**`

---

## Required outputs

- New global skill at `skills/competitors/SKILL.md` covering base profiles, cross-country competitor presence lists, and the competitor profile template/fields.
- `skills/README.md` updated to index the new skill.
- This ticket updated to reflect completion status and a short execution note.

---

## Acceptance criteria

- Skill defines the relationship between a competitor’s **home/base profile**, **cross-country competitive presence lists**, and the **competitor profile structure** itself.
- Guidance includes workflows, required data fields, and storage locations (country folders, data files, and profile paths) consistent with the country-first repo layout and program-cluster guidance.
- Skill provides QA checks and deliverables/templates agents should use when creating or updating competitor profiles.
- Only files in Allowed write paths are modified.
- Ticket marked `done` with a concise summary when complete.

---

## Execution notes (optional)

- What changed (short): Added a global competitors skill covering home/base profiles, cross-country competitive presence, and a reusable profile template; indexed it in `skills/README.md`.
- Open questions: None.
