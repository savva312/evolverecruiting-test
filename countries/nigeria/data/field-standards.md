# Field standards

Shared standards for Nigeria datasets. Apply these to all CSVs unless a ticket defines stricter rules.

- **Encoding:** UTF-8. No BOM.
- **Dates:** `YYYY-MM-DD`.
- **Currency:** EUR unless otherwise specified; denote NGN explicitly if used.
- **Regions/cities:** Free text; follow Nigerian official spellings in English (e.g., `Lagos`, `Abuja`).
- **Enumerations:** Use lowercase with hyphens (e.g., `public`, `private`, `agency-generalist`).
- **Booleans:** `true` / `false`.
- **Multi-enum fields:** Semicolon-separated without spaces.
- **IDs:** Lowercase, ASCII, and globally unique within the file. Prefer prefixes like `ng-` for Nigeria-specific IDs.
