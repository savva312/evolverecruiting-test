Status: done
Type: content
Priority: P3
Agent: EvoTicket Resolver
Claimed-by: local/evoticketresolver
Claimed-at: 2025-12-23T07:28:11Z

## Summary
Document how to use the schedule JSON + `create_eventbridge_rule.py` script in `scripts/schedules/README.md`.

## Allowed write paths
- scripts/schedules/**
- tickets/T-590-schedules-readme.md

## Forbidden write paths
- README.md
- AGENTS.md
- ROADMAP.md
- skills/**
- tickets/README.md
- countries/**
- UNIC/**
- Infrastructure/**
- executions/**
- reports/**
- scripts/** (except `scripts/schedules/**`)
- tickets/** (except this ticket file)

## Required outputs
- scripts/schedules/README.md

## Acceptance criteria
- README explains config structure, how to edit it, and how to run the script (including `--update`, `--region`, `--profile`, `--dry-run`).

## What changed
- Added `scripts/schedules/README.md` documenting schedule config format and how to run `create_eventbridge_rule.py`.


