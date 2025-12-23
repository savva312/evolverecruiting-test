# Bulgaria digital measurement v1 (UTMs + conversion events)

Audience: UNIC enrollment + performance marketing teams supporting **Bulgaria** for both campuses:
- **UNIC Nicosia**
- **UNIC Athens**

This spec standardizes:
- **UTM naming** (including campus split + language split)
- **Fields we must capture** to route leads correctly in the CRM
- **Conversion event taxonomy** (GA4 + ad platforms)
- **Launch QA** so campaigns don’t “run blind”

---

## Minimum viable measurement (no engineering required)

If you can do only one thing this week, do this:

1) **All paid/partner/offline links use UTMs + `campus` + `lang`.**  
2) **All inquiry forms store the UTM parameters into CRM fields** (many form tools support “hidden fields” and “capture URL parameters” without custom code).  
3) **Define and verify one primary conversion event:** `generate_lead` (form successfully submitted).

Everything else in this doc improves attribution, routing, and optimization, but the above is the minimum to stop wasting budget and time.

---

## UTM + parameter standard (canonical schema)

### Required parameters (all trackable links)

These must exist on every paid, email, influencer/creator, QR, partner, and fair/event link:

- `utm_source` — platform/vendor (e.g., `meta`, `google`, `tiktok`)
- `utm_medium` — channel type (e.g., `paid_social`, `cpc`, `email`)
- `utm_campaign` — structured campaign name (see format below)
- `utm_content` — creative/link variant (ad, placement, CTA)
- `utm_term` — keyword (search) or audience (social) or left blank (`na`)
- `campus` — **required**: `nicosia` or `athens`
- `lang` — **required**: `bg` or `en` (use page language, not user browser language)

Recommended (use when available):
- `utm_id` — stable campaign id (useful when ad platforms rewrite names)
- Click IDs (auto-appended by platforms): `gclid`, `gbraid`, `wbraid`, `fbclid`, `ttclid`, `li_fat_id`, `msclkid`
- `lp` — landing page short code (e.g., `bg-medicine`, `bg-cs`, `bg-scholarships`)
- `intake` — `2026-09`, `2026-02` (pick a consistent intake notation)

### Controlled vocabulary (keep reports clean)

Use lowercase, no spaces, only `a-z 0-9 - _`. Prefer hyphens inside values.

**`utm_source`**
- Paid platforms: `meta`, `google`, `tiktok`, `linkedin`, `youtube`, `bing`
- Owned: `email`, `sms`, `whatsapp`, `website`
- Earned/referrals: `organic_social`, `referral`
- Offline bridge: `qr`, `print`, `fair`
- Partners (only when links are controlled): `agent`, `school`, `ngo`

**`utm_medium`**
- Paid social: `paid_social`
- Paid search: `cpc`
- Display: `display`
- Paid video: `video`
- Email: `email`
- SMS/WhatsApp: `sms`, `whatsapp`
- Organic social: `organic_social`
- Referral: `referral`
- Offline-to-online: `offline`

Rule: **do not invent new mediums** unless the enrollment ops owner approves; otherwise reporting fragments.

---

## UTM campaign naming (Bulgaria + campus split)

### Format (recommended)

`utm_campaign = bg-{campus}-{level}-{intake}-{program}-{objective}-{audience}-{lang}`

Where:
- `{campus}`: `nicosia` | `athens`
- `{level}`: `ug` | `pg` | `foundation` | `professional`
- `{intake}`: `2026-09` (or your next intake)
- `{program}`: `medicine` | `cs` | `business` | `psychology` | `general` (use clusters if you don’t have a single program LP)
- `{objective}`: `lead` | `book` | `visit` | `apply`
- `{audience}`: `prospecting` | `retargeting` | `parents` | `counselors` | `diaspora`
- `{lang}`: `bg` | `en` (duplicate of the `lang` parameter; include it here for quick scans in ad platforms)

### `utm_content` conventions (creative + placement)

`utm_content = {channel}-{format}-{angle}-{variant}`

Examples:
- `reels-ugc-tuition-v1`
- `feed-carousel-campuscompare-v2`
- `search-rsa-brand-v1`

### `utm_term` conventions

- Paid search: the **keyword** (or `kw-{adgroup}` if you can’t pass keywords). Example: `medicine-cyprus`, `study-in-athens`.
- Paid social: the **audience** or targeting logic. Example: `broad-17-24`, `lookalike-leads-1p`, `interest-erasmus`.
- If unknown/not applicable: use `na` (never leave it blank; blanks become “(not set)” and break filters).

---

## Examples (copy/paste)

### Meta paid social → Bulgaria → UNIC Nicosia → Bulgarian page

```
?utm_source=meta
&utm_medium=paid_social
&utm_campaign=bg-nicosia-ug-2026-09-medicine-lead-prospecting-bg
&utm_content=reels-ugc-medicineoutcomes-v1
&utm_term=broad-17-24
&campus=nicosia
&lang=bg
&lp=bg-medicine
```

### Google Search (CPC) → Bulgaria → UNIC Athens → English page

```
?utm_source=google
&utm_medium=cpc
&utm_campaign=bg-athens-ug-2026-09-business-lead-prospecting-en
&utm_content=search-rsa-studyabroad-v1
&utm_term=study%20business%20athens
&campus=athens
&lang=en
&lp=bg-business
```

### QR code (offline) → education fair → Bulgarian page (campus-neutral)

```
?utm_source=fair
&utm_medium=offline
&utm_campaign=bg-nicosia-ug-2026-09-general-lead-fair-bg
&utm_content=qr-rollup-stand-a
&utm_term=na
&campus=nicosia
&lang=bg
```

Note: for fairs where both campuses are promoted, use two separate QR codes (one per campus).

---

## CRM capture fields (required for routing + reporting)

### Must-capture (store both first-touch and last-touch)

Store **first-touch** and **last-touch** values for:
- `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`
- `campus`, `lang`
- Landing page URL (full): `landing_page_url`
- Referrer (if available): `referrer_url`
- Click IDs (if present): `gclid`, `gbraid`, `wbraid`, `fbclid`, `ttclid`, `li_fat_id`, `msclkid`
- Timestamp: `first_touch_at`, `last_touch_at`

### CRM routing fields (minimum)

These fields must exist on the lead record (or be derived from form answers):
- `campus_preference` (values: `nicosia`, `athens`, `undecided`)
- `program_interest` (free text is acceptable short-term; controlled list is better)
- `level_interest` (`ug`, `pg`, etc.)
- `country_of_residence` (pre-fill `Bulgaria` when applicable)
- `preferred_language` (`bg`, `en`)
- Consent fields: `consent_marketing` (true/false), `consent_at` (timestamp), `consent_source` (form/platform)

Routing rule of thumb:
- If `campus` parameter exists → default route to that campus team.
- If `campus` missing → route to a shared “Bulgaria triage” queue and require outreach to confirm campus.

---

## Form + landing page implementation (persist UTMs)

### Landing page requirements

- Every LP must accept query parameters (UTMs + `campus` + `lang`) without redirecting/stripping them.
- Avoid redirect chains that drop UTMs (especially on mobile).
- If using a short-link tool, ensure the destination preserves the full query string.

### Form hidden fields (recommended set)

Add hidden fields to all inquiry/booking forms:
- `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`
- `campus`, `lang`, `lp`, `intake`
- `page_url` (current page), `referrer_url`
- Click IDs: `gclid`, `gbraid`, `wbraid`, `fbclid`, `ttclid`, `li_fat_id`, `msclkid`

### Persistence (what “good” looks like)

Goal: if a prospect clicks an ad today and submits a form next week, we still capture attribution.

- Persist UTM + click id values for **30–90 days** (choose one duration and apply consistently).
- Prefer **first-party** storage (first-party cookie or local storage).
- When users consent only to essential cookies, store UTMs only when your privacy policy and consent banner allow it.

If your form tool supports it, enable:
- “Capture URL parameters into hidden fields”
- “Store first attribution + last attribution”

---

## Conversion event taxonomy (GA4 + ad platforms)

### Naming rules

- Use lowercase `snake_case`
- Max 40 characters (GA4 guidance)
- One event name = one clear definition

### Primary conversion events (must exist)

1) `generate_lead` — **inquiry form successfully submitted**  
2) `book_consultation` — booking confirmed (Calendly/booking tool “confirmed” step)  
3) `click_call` — click on a phone link (`tel:`)  
4) `download_brochure` — brochure PDF download (or brochure page “download” click)

### Supporting events (recommended)

- `form_start` — user focuses first form field
- `view_program` — program page view (if program pages are distinct)
- `click_apply` — click to application portal / application form start
- `chat_start` — live chat started
- `click_whatsapp` — click on WhatsApp link (if used)

### Event parameters (recommended)

Attach these parameters where relevant:
- `campus` (`nicosia`/`athens`)
- `lang` (`bg`/`en`)
- `program` (short code)
- `intake`
- `form_id` / `form_name`

### Platform mapping (implementation checklist)

- **GA4**: mark `generate_lead` and `book_consultation` as conversions.
- **Google Ads**: import GA4 conversions *or* fire Google Ads conversion tags directly; ensure deduping if both are used.
- **Meta**: map `generate_lead` to Pixel **Lead** event (or use Conversions API if available).
- **TikTok**: map `generate_lead` to Pixel **SubmitForm** or **Lead** equivalent; verify it appears in Events Manager.
- **LinkedIn**: track lead gen via Insight Tag (site) and Lead Gen Forms reporting (in-platform); don’t mix definitions.

---

## Launch QA checklist (Bulgaria campaigns)

### Before launch (must pass)

- UTM links tested on mobile + desktop; query string remains on final LP.
- `campus` and `lang` present and correct on every ad/link variant.
- Form submission writes UTM fields into CRM (spot-check 3 test leads per campus).
- GA4 receives events: `page_view` + `generate_lead` (verify in GA4 DebugView or real-time).
- Ad platform pixels/tags fire on the correct triggers (not on page load).
- Consent banner present; marketing tags respect consent mode where applicable.

### First 24 hours (must monitor)

- Leads arrive in CRM with non-empty `utm_source/medium/campaign` and `campus`.
- No spike in `(not set)` / `(direct)` for paid traffic.
- Duplicate lead handling is working (same email/phone not creating multiple “new leads” without linking).

### Weekly hygiene (keep attribution usable)

- Review top campaigns by **qualified lead rate** (not CPL alone).
- Audit naming drift: reject any campaign that doesn’t follow the schema.
- Confirm retargeting audiences are within policy limits (see compliance).

---

## Compliance and minors (non-negotiable)

This repo supports Bulgaria recruiting; many prospects are **17** (minors). Treat compliance as a performance lever: bad consent practices destroy long-term channel access and brand trust.

Minimum requirements:
- Follow **GDPR** and local ePrivacy/cookie rules for tracking/remarketing.
- **Do not build or use extended retargeting windows for minors.** Practical rule:
  - Keep retargeting membership to **≤30 days** where age is unknown or likely under 18.
  - If you can reliably segment adults (e.g., based on declared age), you may run longer windows for adults only (still keep them reasonable; avoid “always-on” year-long audiences).
- Avoid sensitive targeting categories and do not infer sensitive attributes from behavior.
- Store consent timestamp + source in CRM; honor opt-outs promptly.

If any channel partner proposes “aggressive” tracking (fingerprinting, cross-site identifiers, hidden pixels), reject it.
