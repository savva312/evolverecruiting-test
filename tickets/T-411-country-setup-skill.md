# T-411: Country setup skill (layered ticket playbook)

Status: done
Type: structure
Priority: P1
Dependencies: none
Claimed-by: work
Claimed-at: 2025-12-22T06:26:48+00:00
Last-updated: 2025-12-22

---

## Goal

Create a global skill that standardizes how to onboard a new country into the repo using layered, parallel-safe tickets (scaffolding, discovery, profiling across stakeholders). Add it to the global skills index.

## Context

- Country-first layout requires consistent scaffolding and ticket boundaries when introducing new markets.
- The skill should act as a reusable playbook for breaking down country launches into atomic tickets (directories, indices, entities, stakeholders, data models) while keeping country scopes isolated.
- Control-plane rules treat `skills/**` as protected; changes must be driven via a structure ticket.

## Allowed write paths

- skills/country-setup/**
- skills/README.md
- tickets/T-411-country-setup-skill.md
- executions/T-411-country-setup-skill/** (optional notes)

## Forbidden write paths

- README.md
- AGENTS.md
- ROADMAP.md
- tickets/** (except this ticket file)
- .github/**
- scripts/**
- Any country directories (e.g., /countries/**)
- skills/** (outside the allowed folder and README entry)
- Any paths not listed in Allowed write paths

## Required outputs

- skills/country-setup/SKILL.md with layered-ticket guidance to stand up a new country: preflight checks, scaffolding steps, discovery tasks across stakeholder groups, ticketization plan, and QA/closure checklist.
- skills/README.md updated to index the new skill with a concise label.
- Ticket updated to `Status: done` with a short execution note once outputs are complete.

## Acceptance criteria

- Skill covers: (1) preflight inputs (control-plane docs, country code, naming), (2) scaffolding directories/README setup, (3) layered ticket breakdown for schools, agents, regulators, NGOs/SGOs, fairs/events, digital benchmarks, program clusters, and competitor profiling, (4) data/ID governance hooks, (5) execution/QA checkpoints before closing a country launch.
- Ticketization guidance is explicit about allowed/forbidden paths and parallel-safe slicing.
- Skills index lists the new skill with an accurate description.
- No edits occur outside Allowed write paths.

## Execution notes (optional)

- What changed (short): Added global country-setup skill covering layered tickets for scaffolding, stakeholder discovery, profiling, and QA; indexed it in the global skills README.
- Follow-up tickets suggested: None.
