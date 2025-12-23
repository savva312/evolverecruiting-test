# Bulgaria offerholder comms sequence (BG/EN)

- **Last updated:** 2025-12-22  
- **Owners:** Country Recruiter Bulgaria (execution); Admissions Ops (Nicosia/Athens) (templates + CRM hygiene); Housing Lead (campus) (housing steps)

## Purpose

Move admitted Bulgarian-market students from **offer → deposit → arrival** with:
- clear campus separation (UNIC **Nicosia** vs UNIC **Athens**)
- segmentation by **Medicine vs non-Medicine** and **EU passport vs non-EU resident in Bulgaria**
- exam-safe pacing during **May–June** Bulgarian exams

## Compliance and data-handling rules (non-negotiable)

- **Messaging apps (WhatsApp/Viber):** only message if the student has given explicit consent (portal checkbox, signed form, or explicit written “YES” reply). Always include an opt-out (“STOP” or “Отписване”) and record consent/opt-out in CRM.
- **Do not collect/store sensitive documents in chat:** passports, residence permits, bank statements, medical documents, visas, and full IDs must go through the portal or official email upload, not WhatsApp/Viber.
- **Minimize personal data:** in chat use first name + application ID; avoid DOB, passport numbers, and home address.
- **Campus separation:** separate WhatsApp/Viber groups per campus; never mix Athens and Nicosia students in the same group.

## Segmentation logic (apply to every touch)

### A) Program track
- **Medicine/limited-seats (MED):** Medicine (and any other limited-seat programs you classify as scarcity-based).
- **Non-Medicine (GEN):** all other programs.

### B) Travel/visa track (Bulgaria market)
- **EU:** EU passport holder (includes BG citizens).
- **Non-EU in BG:** non-EU resident living in Bulgaria (often requires earlier visa/residence planning).

> If you can’t confidently classify a student, default to **EU** messaging until verified, then switch to the correct track.

## Exam-safe pacing (May–June)

Bulgarian state exams typically run **May–June**; avoid high-pressure messaging during this window.

- If a student is flagged **“BG Grade 12 / exams ongoing”**, then:
  - send **only supportive** touches (wellbeing, resources, Q&A) until **48h after their last exam**
  - start the “deposit clock” based on your admissions policy for the cohort (typically after results/diploma release, often mid–July), not the day the conditional offer email was sent
  - operational default for Grade 12: set `{DEPOSIT_DEADLINE_DATE}` to **10–14 days after diploma/results release** (or after an unconditional offer is issued, whichever is later)

## Subject line convention (required)

Every email subject must start with the campus tag:

- `[NICOSIA] …` for UNIC Nicosia
- `[ATHENS] …` for UNIC Athens

Recommended pattern:

`[CAMPUS] [STAGE] — [Program/Track] — [Single CTA]`

Examples:
- `[NICOSIA] Offer received — Medicine — Confirm your seat (deposit)`
- `[ATHENS] Next steps — Business/CS — Book a 10‑minute call`

## Sequence overview (10 touches)

**How to use:** start at Touch 1 on Day 0. Apply the timing rules and suppressions below.

| Touch | Trigger / timing | Primary channel | Secondary | Purpose |
| --- | --- | --- | --- | --- |
| 1. Offer + next steps | Day 0 (offer sent) | Email | — | Clarity on campus, timeline, what happens next |
| 2. Consent + warm welcome | Day 1–2 (if consent captured) | WhatsApp/Viber | Email (if no consent) | Move to 2-way channel; book call |
| 3. Welcome webinar invite | Day 3–5 (or post-exams) | Email | WhatsApp/Viber reminder | Group Q&A, reduce anxiety, clarify deposit |
| 4. Exam-safe check-in / deposit nudge | Day 7 (or post-exams) | Email | WhatsApp/Viber | Gentle intent check; help unblock |
| 5. Deposit due / seat confirmation | Day 10 MED / Day 14 GEN (or policy date) | Email | WhatsApp/Viber | Clear deadline + payment rails + consequences |
| 6. At-risk escalation | Day 18 (or 4 days after missed deadline) | Call | Email + WhatsApp/Viber | Save at-risk applicants with human contact |
| 7. Deposit received + next steps | T+24h after deposit | Email | WhatsApp/Viber | Confirm seat; route to visa/housing workflow |
| 8. Visa/housing/doc kit | T+3–7d after deposit | Email | WhatsApp/Viber | Checklist + webinar + upload links |
| 9. Pre-departure readiness | 6–8 weeks pre-start (or upon unconditional) | Email | WhatsApp/Viber | Travel window, insurance, housing, arrival form |
| 10. Arrival week welcome | Day 0–2 after arrival / 10–14 days pre-start | WhatsApp/Viber | Email | Orientation, first-week tasks, reduce no-shows |

---

## Track-specific adjustments (MED/GEN + EU/non‑EU in BG)

Use these rules to keep templates consistent without rewriting everything:

- **MED vs GEN**
  - Touch 1/4/5: always include `{PROGRAM}` and use the correct deposit SLA (MED typically faster than GEN per `countries/bulgaria/go-to-market/offerholder-and-yield/deposit-deadlines.md`).
  - Touch 3: run Medicine breakout Q&A (faculty + student ambassador) when possible; keep messaging factual (seat caps + process), not fear-based.
- **EU vs Non‑EU in BG**
  - Touch 7: for non‑EU, trigger the visa support workflow immediately after deposit (document kit + appointment planning).
  - Touch 8/9: for non‑EU, emphasize lead times and “do this now” tasks; for EU, emphasize insurance + post-arrival registration steps.
  - Touch 10: keep arrival steps campus-specific; do not give legal advice—point to the official campus checklist/appointments.

## Touch templates (BG + EN)

### Common placeholders

- `{FIRST_NAME}`, `{LAST_NAME}`
- `{CAMPUS_TAG}` = `[NICOSIA]` or `[ATHENS]`
- `{CAMPUS_NAME}` = UNIC Nicosia or UNIC Athens
- `{PROGRAM}` / `{TRACK}` = Medicine / Non‑Medicine
- `{APP_ID}`, `{OFFER_PORTAL_LINK}`, `{DEPOSIT_LINK}`, `{CALL_BOOKING_LINK}`
- `{WHATSAPP_OPTIN_LINK}` (or consent language)
- `{DEPOSIT_DEADLINE_DATE}` (use local date format)
- `{CONTACT_EMAIL}`, `{CONTACT_PHONE}`

### Touch 1 — Offer + next steps (Day 0)

**Email subject (EN):** `{CAMPUS_TAG} Offer received — {PROGRAM} — Next steps`  
**Email subject (BG):** `{CAMPUS_TAG} Получена оферта — {PROGRAM} — Следващи стъпки`

**Email (EN)**
Hi {FIRST_NAME},  
Congratulations — your offer for **{PROGRAM}** at **{CAMPUS_NAME}** is ready.

**Next steps (2 minutes):**
1) Review your offer and upload any pending documents: {OFFER_PORTAL_LINK}  
2) Reserve your seat with the deposit by **{DEPOSIT_DEADLINE_DATE}**: {DEPOSIT_LINK}  
3) Book a quick call if you want us to walk you through everything: {CALL_BOOKING_LINK}

If you’re currently in Bulgarian exams (May–June), we’ll keep messages low-pressure and focus on support; we can align your timeline after exams.

Best,  
{SIGNATURE}

**Email (BG)**
Здравей, {FIRST_NAME},  
Поздравления — вашата оферта за **{PROGRAM}** в **{CAMPUS_NAME}** е готова.

**Следващи стъпки (2 минути):**
1) Прегледайте офертата и качете липсващи документи: {OFFER_PORTAL_LINK}  
2) Резервирайте мястото си с депозит до **{DEPOSIT_DEADLINE_DATE}**: {DEPOSIT_LINK}  
3) Запазете кратък разговор, ако искате да минем през всичко заедно: {CALL_BOOKING_LINK}

Ако сте в матури/изпити (май–юни), ще поддържаме комуникацията спокойна и насочена към помощ; ще синхронизираме сроковете след изпитите.

Поздрави,  
{SIGNATURE}

---

### Touch 2 — Consent + warm welcome (Day 1–2; only if consent)

**WhatsApp/Viber (EN)**  
Hi {FIRST_NAME} — it’s {RECRUITER_NAME} from UNIC. With your permission, I’ll message here about your offer for **{CAMPUS_NAME}**.  
Reply **YES** to confirm (or **STOP** to opt out). Quick call booking: {CALL_BOOKING_LINK}

**WhatsApp/Viber (BG)**  
Здравей, {FIRST_NAME} — аз съм {RECRUITER_NAME} от UNIC. С ваше съгласие ще пиша тук за офертата ви за **{CAMPUS_NAME}**.  
Отговорете **ДА** за потвърждение (или **СТОП** за отказ). Кратък разговор: {CALL_BOOKING_LINK}

**Fallback email (if no consent yet) — EN**  
Subject: `{CAMPUS_TAG} Quick question — can we message you on WhatsApp/Viber?`  
Can we contact you on WhatsApp/Viber for quick reminders and Q&A? If yes, please reply “YES” and share your preferred number, or opt in here: {WHATSAPP_OPTIN_LINK}.

**Fallback email (if no consent yet) — BG**  
Subject: `{CAMPUS_TAG} Кратък въпрос — може ли да пишем в WhatsApp/Viber?`  
Може ли да ви пишем в WhatsApp/Viber за кратки напомняния и въпроси? Ако да, отговорете „ДА“ и изпратете предпочитан номер, или се запишете тук: {WHATSAPP_OPTIN_LINK}.

---

### Touch 3 — Welcome webinar invite (Day 3–5; suppress during exams if needed)

**Email subject (EN):** `{CAMPUS_TAG} Live Q&A — your offer + deposit + next steps`  
**Email subject (BG):** `{CAMPUS_TAG} Онлайн среща (Q&A) — оферта + депозит + следващи стъпки`

**Email (EN)**  
Hi {FIRST_NAME},  
Join our short live Q&A for Bulgarian offerholders. We’ll cover the deposit process, timelines, and campus-specific next steps for **{CAMPUS_NAME}**.

Register here: {WEBINAR_REG_LINK}  
If you can’t attend, we’ll send the recording.

**CTA:** bring one question you want answered before you decide.

**Email (BG)**  
Здравей, {FIRST_NAME},  
Каним ви на кратка онлайн среща (Q&A) за български кандидати с оферта. Ще обясним депозита, сроковете и стъпките за **{CAMPUS_NAME}**.

Регистрация: {WEBINAR_REG_LINK}  
Ако не можете да присъствате, ще изпратим запис.

**CTA:** донесете 1 въпрос, който искате да изясните преди решението си.

**WhatsApp/Viber reminder (EN):** Reminder: today’s UNIC Q&A at {TIME_BG}. Link: {WEBINAR_JOIN_LINK}.  
**WhatsApp/Viber reminder (BG):** Напомняне: днес Q&A срещата е в {TIME_BG}. Линк: {WEBINAR_JOIN_LINK}.

---

### Touch 4 — Exam-safe check-in / deposit nudge (Day 7; adjust for exams)

**Email subject (EN):** `{CAMPUS_TAG} Checking in — what’s your plan?`  
**Email subject (BG):** `{CAMPUS_TAG} Проверка — какъв е вашият план?`

**Email (EN)**  
Hi {FIRST_NAME},  
Quick check-in: are you planning to reserve your seat at **{CAMPUS_NAME}**?

Reply with one option (just one word is fine):  
1) **YES** — I’ll deposit by {DEPOSIT_DEADLINE_DATE}  
2) **MAYBE** — I need a call  
3) **NO** — I’m choosing another option

If you’re in exams right now, no pressure — tell me your last exam date and we’ll align your timeline.

**Email (BG)**  
Здравей, {FIRST_NAME},  
Кратка проверка: планирате ли да резервирате място в **{CAMPUS_NAME}**?

Отговорете с един вариант (може само с една дума):  
1) **ДА** — ще платя депозит до {DEPOSIT_DEADLINE_DATE}  
2) **МОЖЕ БИ** — имам нужда от разговор  
3) **НЕ** — избирам друга опция

Ако сте в изпити, без напрежение — кажете кога е последният ви изпит и ще съобразим сроковете.

**WhatsApp/Viber (EN):** Quick check-in: are you planning to deposit for {CAMPUS_NAME}? Reply YES / MAYBE / NO.  
**WhatsApp/Viber (BG):** Кратко питане: планирате ли депозит за {CAMPUS_NAME}? Отговорете ДА / МОЖЕ БИ / НЕ.

---

### Touch 5 — Deposit due / seat confirmation (Day 10 MED / Day 14 GEN)

**Email subject (EN):** `{CAMPUS_TAG} Deposit due — confirm your seat by {DEPOSIT_DEADLINE_DATE}`  
**Email subject (BG):** `{CAMPUS_TAG} Срок за депозит — потвърдете мястото до {DEPOSIT_DEADLINE_DATE}`

**Email (EN)**  
Hi {FIRST_NAME},  
This is your seat‑confirmation reminder for **{PROGRAM}** at **{CAMPUS_NAME}**.

**Deposit deadline:** {DEPOSIT_DEADLINE_DATE}  
Pay here: {DEPOSIT_LINK}  
If you’ve already paid, reply with the receipt confirmation number (don’t send sensitive bank documents in chat).

If you need a 10‑minute call to unblock payment, book here: {CALL_BOOKING_LINK}

**Email (BG)**  
Здравей, {FIRST_NAME},  
Напомняне за потвърждение на мястото ви за **{PROGRAM}** в **{CAMPUS_NAME}**.

**Срок за депозит:** {DEPOSIT_DEADLINE_DATE}  
Плащане: {DEPOSIT_LINK}  
Ако вече сте платили, отговорете с номер/потвърждение (не изпращайте чувствителни банкови документи в чат).

Ако искате кратък разговор (10 мин) за да помогнем с плащането: {CALL_BOOKING_LINK}

**WhatsApp/Viber (EN):** Deposit deadline {DEPOSIT_DEADLINE_DATE} to confirm your seat at {CAMPUS_NAME}. Link: {DEPOSIT_LINK}.  
**WhatsApp/Viber (BG):** Срокът за депозит е {DEPOSIT_DEADLINE_DATE} за потвърждение на място в {CAMPUS_NAME}. Линк: {DEPOSIT_LINK}.

---

### Touch 6 — At-risk escalation (Day 18 or 4 days after missed deadline)

**Call opener (EN)**  
Hi {FIRST_NAME}, it’s {RECRUITER_NAME} from UNIC. I’m calling to help you keep your seat for **{CAMPUS_NAME}** — do you have 2 minutes?

**Call opener (BG)**  
Здравей, {FIRST_NAME}, {RECRUITER_NAME} от UNIC. Обаждам се да помогна да запазите мястото си за **{CAMPUS_NAME}** — имате ли 2 минути?

**WhatsApp/Viber follow-up (EN)**  
Thanks for your time. Can you confirm your plan?  
1) Paying today / tomorrow  
2) Need help with payment method  
3) Not proceeding  
Reply 1/2/3.

**WhatsApp/Viber follow-up (BG)**  
Благодаря! Може ли да потвърдите план?  
1) Плащам днес/утре  
2) Нуждая се от помощ с плащането  
3) Няма да продължа  
Отговорете 1/2/3.

---

### Touch 7 — Deposit received + next steps (T+24h after deposit)

**Email subject (EN):** `{CAMPUS_TAG} Deposit received — next steps for {CAMPUS_NAME}`  
**Email subject (BG):** `{CAMPUS_TAG} Получен депозит — следващи стъпки за {CAMPUS_NAME}`

**Email (EN)**  
Hi {FIRST_NAME},  
We’ve received your deposit — your seat for **{PROGRAM}** at **{CAMPUS_NAME}** is confirmed.

Next steps (please complete in the portal):  
1) Upload remaining docs: {OFFER_PORTAL_LINK}  
2) Housing preferences (if needed): {HOUSING_FORM_LINK}  
3) Visa/residence track confirmation (EU vs non‑EU): {VISA_TRACK_FORM_LINK}

We’ll send your visa/housing checklist next.

**Email (BG)**  
Здравей, {FIRST_NAME},  
Потвърждаваме получения депозит — мястото ви за **{PROGRAM}** в **{CAMPUS_NAME}** е запазено.

Следващи стъпки (в портала):  
1) Качете оставащите документи: {OFFER_PORTAL_LINK}  
2) Предпочитания за настаняване (ако е нужно): {HOUSING_FORM_LINK}  
3) Потвърдете вашия статут (ЕС / не‑ЕС): {VISA_TRACK_FORM_LINK}

Следващото писмо ще е с чеклист за виза/настаняване.

**WhatsApp/Viber (EN)**  
Great news — your deposit is received and your seat at {CAMPUS_NAME} is confirmed. Next, please complete the portal steps: {OFFER_PORTAL_LINK}

**WhatsApp/Viber (BG)**  
Чудесна новина — депозитът е получен и мястото ви в {CAMPUS_NAME} е потвърдено. Следващо: довършете стъпките в портала: {OFFER_PORTAL_LINK}

---

### Touch 8 — Visa/housing/doc kit (T+3–7d after deposit)

**Email subject (EN):** `{CAMPUS_TAG} Your checklist — visa/residence + housing + arrival`  
**Email subject (BG):** `{CAMPUS_TAG} Вашият чеклист — виза/регистрация + настаняване + пристигане`

**Email (EN)**  
Hi {FIRST_NAME},  
Here’s your checklist for **{CAMPUS_NAME}**. Choose your track:

- **EU passport:** focus on insurance + residence registration steps after arrival.  
- **Non‑EU resident in Bulgaria:** start visa documentation now (processing can take weeks).

Checklist + upload links: {CHECKLIST_LINK}  
Optional clinic/webinar: {WEBINAR_REG_LINK}

**Email (BG)**  
Здравей, {FIRST_NAME},  
Ето чеклист за **{CAMPUS_NAME}**. Изберете вашия вариант:

- **Паспорт от ЕС:** фокус върху застраховка + регистрация след пристигане.  
- **Не‑ЕС (живеещ в България):** започнете документите за виза навреме (може да отнеме седмици).

Чеклист + линкове за качване: {CHECKLIST_LINK}  
По желание среща/уебинар: {WEBINAR_REG_LINK}

**WhatsApp/Viber (EN):** Sent your visa/housing checklist for {CAMPUS_NAME}: {CHECKLIST_LINK}.  
**WhatsApp/Viber (BG):** Изпратихме чеклиста за виза/настаняване за {CAMPUS_NAME}: {CHECKLIST_LINK}.

---

### Touch 9 — Pre-departure readiness (6–8 weeks pre-start or upon unconditional)

**Email subject (EN):** `{CAMPUS_TAG} Pre‑departure checklist — ready for {CAMPUS_NAME}`  
**Email subject (BG):** `{CAMPUS_TAG} Подготовка за заминаване — готови ли сте за {CAMPUS_NAME}`

**Email (EN)**  
Hi {FIRST_NAME},  
Let’s make sure you’re ready to arrive smoothly:

- Housing confirmed (contract signed)  
- Insurance ready (EHIC or approved private policy)  
- Arrival form submitted with flight details: {ARRIVAL_FORM_LINK}  
- Originals packed (diploma/transcripts as needed)

Recommended arrival window: {ARRIVAL_WINDOW}  
Questions? Reply here or book a call: {CALL_BOOKING_LINK}

**Email (BG)**  
Здравей, {FIRST_NAME},  
Нека проверим, че сте подготвени за спокойно пристигане:

- Потвърдено настаняване (подписан договор)  
- Готова застраховка (ЕЗОК/EHIC или одобрена частна)  
- Попълнен формуляр за пристигане с полет: {ARRIVAL_FORM_LINK}  
- Оригинали в багажа (диплома/приложение при нужда)

Препоръчителен период за пристигане: {ARRIVAL_WINDOW}  
Въпроси? Пишете или запазете разговор: {CALL_BOOKING_LINK}

**WhatsApp/Viber (EN):** Pre‑departure checklist for {CAMPUS_NAME}: {CHECKLIST_LINK}. Any questions?  
**WhatsApp/Viber (BG):** Чеклист за подготовка за {CAMPUS_NAME}: {CHECKLIST_LINK}. Ако имате въпроси — пишете.

---

### Touch 10 — Arrival week welcome (10–14 days pre-start + Day 0–2 after arrival)

**WhatsApp/Viber (EN)**  
Welcome to {CAMPUS_NAME}, {FIRST_NAME}!  
Today: check‑in + SIM/Wi‑Fi. Tomorrow: campus ID + orientation info. If you need help, message here.

**WhatsApp/Viber (BG)**  
Добре дошли в {CAMPUS_NAME}, {FIRST_NAME}!  
Днес: настаняване + SIM/Wi‑Fi. Утре: студентска карта + информация за ориентация. Ако имате нужда от помощ — пишете тук.

**Email subject (EN):** `{CAMPUS_TAG} Arrival week — your first 72 hours at {CAMPUS_NAME}`  
**Email subject (BG):** `{CAMPUS_TAG} Първа седмица — първите 72 часа в {CAMPUS_NAME}`

**Email (EN)**  
Hi {FIRST_NAME},  
Here’s your quick 72‑hour plan:
1) Housing check‑in and local SIM  
2) Campus ID + orientation schedule  
3) Tuition/payment confirmation (if needed)  
4) Residence/registration steps (EU / non‑EU) via the campus team

We’re happy you’re here — welcome.

**Email (BG)**  
Здравей, {FIRST_NAME},  
Ето кратък план за първите 72 часа:
1) Настаняване и местна SIM карта  
2) Студентска карта + график за ориентация  
3) Потвърждение на такси/плащания (ако е нужно)  
4) Регистрация/разрешителни (ЕС / не‑ЕС) с помощ от кампуса

Радваме се, че сте тук — добре дошли!

---

## Operational notes (so this runs cleanly)

- Log every touch in CRM with: `touch_name`, `date/time`, `campus`, `track (MED/GEN)`, `visa_track (EU/non‑EU in BG)`, and `next_action_date`.
- If a student is in the **exam window**, tag them and shift Touches 3–5 to post-exam timing.
- Any exceptions to deposit deadlines must be approved per `countries/bulgaria/go-to-market/offerholder-and-yield/deposit-deadlines.md`.
- Keep housing and arrival language aligned with `countries/bulgaria/go-to-market/offerholder-and-yield/housing-and-arrival.md`.
- Keep webinar cadence aligned with `countries/bulgaria/go-to-market/offerholder-and-yield/webinars.md`.
