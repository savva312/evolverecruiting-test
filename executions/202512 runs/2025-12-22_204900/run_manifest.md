# Run manifest — 2025-12-22_204900

- Run id: `2025-12-22_204900`
- Date/time (UTC): `2025-12-22 20:49:00`
- Request: Execute `T-492` (Romania — competitors CSV v1 + dictionary)
- Tickets executed: `T-492`
- Status: `success`
- PR: `none`

## Outputs

- Updated `countries/romania/data/entities/competitors.csv` with a Romania-relevant schema (cluster tags, country/city, tuition signals) and rows for all existing Romania competitor profiles.
- Updated `countries/romania/data/entities/competitors-dictionary.md` to match the final CSV columns exactly.

## Notes / issues

- `competitor_id` uses deterministic `comp-ro-<city>-<profile-slug>` to stay stable and joinable to future program-level tables (e.g., `competitor-programs.csv`).
- Ticket metadata appears inconsistent (`Allowed write paths` references `tickets/T-447-...` and `Forbidden write paths` blocks `tickets/**`); this run did not update the ticket file status fields.
