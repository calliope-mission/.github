# Calliope · Brand and design reference

Brand Guidelines 1.0 · November 2026
Source canvas: *Calliope CMYK Directions* (claude.ai artifact, rows K, M0 and M). This folder holds the chosen boards and everything needed to build with them.

> **Calliope, born to free people from artificial influence.**
> Louder than the Sirens.

---

## 1. What is in this folder

```
calliope-brand/
├── README.md              ← this document (brand rules, naming, hierarchy)
├── CLAUDE.md              ← short rules for Claude Code when working in this folder
├── tokens/
│   ├── tokens.css         ← colours, type, radius, spacing, motion as CSS variables
│   └── tokens.json        ← the same tokens as data
├── fonts/                 ← Schibsted Grotesk + JetBrains Mono (woff2, SIL OFL) + fonts.css
├── logos/                 ← SVG marks and app icons (see §6)
├── mockups/
│   ├── manifest.json      ← list of boards, sizes, which ones move
│   ├── product/           ← reference screens for the site and products
│   ├── mission/           ← mission and explanation pages
│   └── elements/          ← marks and icon systems
│       (each board as .html source + .png at 2x; animated boards also as .mp4)
└── scripts/
    └── render.cjs         ← re-renders PNG/MP4 from the HTML after you edit it
```

The `.html` files are the editable source. The `.png` and `.mp4` files are exports of them.

---

## 2. Project hierarchy

```
Calliope ............................ the organisation (mission-driven)
│
├── 01 · Find   Sirenradar .......... audit tool for AI software        [Calliope brand]
├── 02 · Fix    Unsiren ............. remediation, reviewed by a person  [Calliope brand] · concept
├── 03 · Go out Orfeo apps .......... sirenless real-world apps         [own brand each]
│                ├── laiive ......... "Ask what is on tonight."  (laiive.com)
│                ├── VaiVia ......... "Ask for a trail the way you would ask a local." (vaivia.dev)
│                └── your app ....... open to any app that follows the Orfeo principles
│
└── Calliope community .............. not a product · members are called Argonauts
                 Resources: for teachers · developers · families · community leaders ·
                            small businesses · anyone
                 Links:     Work with us · Partners · Share what we do · Be updated
```

The three services read as one sequence: **find → fix → go out**.

### Brand scope (important)

| Part | Follows Calliope brand rules? |
|---|---|
| Calliope (site, docs, decks, print) | **Yes**, fully |
| Sirenradar | **Yes**, fully (plum role) |
| Unsiren | **Yes**, fully (cream/olive role) |
| Calliope community pages | **Yes**, fully (lilac role) |
| Orfeo apps (laiive, VaiVia, future apps) | **No.** Each app has its own name, look and style. |

Orfeo apps are style-independent products. What ties them to Calliope is behaviour, not design. Every Orfeo app:
- **ends**: no infinite feed;
- has **no streaks and no guilt notifications**;
- **points you out the door**, to people and places.

Inside Calliope pages, an Orfeo app appears on an aqua card with petrol text (see `M0i`). The icons in `logos/endorsement-*.svg` are optional and only for those Calliope pages. Apps never have to use them. An optional endorsement line for an app's own footer: *"An Orfeo app · by Calliope"*.

---

## 3. Naming

| Name | What it is | Write it | Never |
|---|---|---|---|
| **Calliope** | the organisation | Calliope | CALLIOPE in running text, Caliope |
| **Sirenradar** | the audit tool | Sirenradar (one word, one capital) · CLI: `sirenradar` | SirenRadar, Siren Radar, Sirenwatch (old name) |
| **Unsiren** | the fix / remediation | Unsiren | UnSiren, MutedSiren |
| **Orfeo apps** | family of real-world apps | Orfeo apps (Orfeo applications in long text) | Orfeo as a single app |
| **laiive** | Orfeo app | laiive (always lowercase) | Laiive, LAIIVE |
| **VaiVia** | Orfeo app (trails) | VaiVia | Vaivia, get-out-door (old name) |
| **Calliope community** | the community | Calliope community | Argonauts as the section name |
| **Argonauts** | what we call community members | "We call them Argonauts." | a product, a programme, a brand |
| **Sirenfree** | recognition for apps reviewed with Unsiren | Sirenfree recognition | certified, certificate, compliant |
| **AnyAISafe** | today's package and repo behind Sirenradar | "today: AnyAISafe v0.3.0" | hide it; the repo is the proof |
| **Sirens** | the hooks we fight: manipulative design and AI | the Sirens (capital S) | |

Rename plan: Sirenradar is the proposed public name. Today the CLI ships as `aisafe audit` (AnyAISafe). Mockups that show `sirenradar audit` say so in a footnote. Keep that footnote until the CLI is renamed.

---

## 4. Messaging

| Use | Text |
|---|---|
| Mission line | **Calliope, born to free people from artificial influence.** (after the wordmark: "born to free people from artificial influence.") |
| Why now | Now that AI is in the loop, digital influence puts people, communities, societies and democracies at risk. |
| Tagline | Louder than the Sirens. |
| Sequence | Find · Fix · Go out |
| Sirenradar | Locates the Sirens in AI software, and helps teams prepare for the EU AI Act and other AI rules. |
| Unsiren | Removes them. A named person reviews each fix, and the review is recorded. |
| Orfeo apps | Apps that sing louder than the Sirens, and bring you back to the real world. |
| Community | Everyone around Calliope. We call them Argonauts. |
| How we work | Spot · Strategy · Act |

**Terms.** "Artificial influence" is the headline term. "Digital influence" is the explanatory umbrella used in M1 and M2: feeds, alerts, recommendations, engagement design, tracking and reward loops, now amplified by AI. See §13 for the open decision.

---

## 5. Voice

Calm, steady, trustworthy: a long movement, not an emergency.

- **Say it plain.** Short words, active verbs.
- **Talk to one person.** "You", never "users".
- **No hooks.** No false urgency, no countdowns, no fear in copy either.
- Prefer *steadily, tend, care, carry, hand over* to *urgent, fight, hit, attack, before it's too late*.

Examples (from the voice board K14):

| Before (old README) | Calliope |
|---|---|
| We cannot wait for perfect research or perfect policy. | We don't wait for perfect research or perfect policy. We begin with what we have, and keep tending it. |
| SPOT · BUILD · HIT | Spot · Strategy · Act |
| Three fronts … one fight. | Three circles, one long work, shared. |
| …to turn evidence into pressure and awareness. | …to turn evidence into understanding, and understanding into care. |

Kept as is: *"We don't talk about the end of the world, we build a better one."*

---

## 6. Logo and marks

### Calliope mark: the Cheer (V1, chosen)
A person with arms raised. Files: `logos/calliope-mark-*.svg`, `calliope-app-icon*.svg`, `calliope-favicon.svg`.

Construction (viewBox 120 × 120, round caps and joins):
```
arms   M60 64 L28 36   M60 64 L92 36     stroke 12
body   M60 64 V82                         stroke 12
legs   M60 82 L42 106  M60 82 L78 106     stroke 12
head   circle cx 60 cy 24 r 13 (filled)
```
- **Tile**: the mark sits in a rounded square, radius = 29% of the tile size (`--icon-tile-ratio`). Default tile: aqua with a petrol mark. On aqua backgrounds use the petrol tile.
- **Small sizes**: below 32 px use the heavy cut (`calliope-favicon.svg`, stroke 17, head r16).
- **Clear space**: at least half the tile width on every side.
- **Lockup**: tile + "Calliope" in Schibsted Grotesk 800, tracking −0.05em, cap height ≈ 45% of the tile height, gap = 25% of the tile.
- **Don't**: rotate it, add outlines or shadows, recolour outside the palette, or put it on photos without a tile.
- **Trademark**: a raised-arms figure is a common pictogram, so it is weak as a trademark on its own. Register the mark together with the wordmark, and run an EUIPO/WIPO search first. Board K9 keeps the explorations (V2 to V8) for campaigns; K16 on the canvas has refinements of V1.

### Service and community marks (same stroke system)

| Mark | Meaning | File | Default colours |
|---|---|---|---|
| Eye | Sirenradar watches the code | `sirenradar-mark*.svg`, `sirenradar-app-icon.svg` | plum on lilac tile |
| Flat wave | Unsiren: the siren's wave goes flat | `unsiren-mark*.svg`, `unsiren-app-icon.svg` | cream on olive tile |
| Between | Orfeo: a person holding hands with another person and a tree | `orfeo-mark*.svg`, `orfeo-app-icon.svg` | aqua on petrol tile |
| Crew | Community: figures linking arms | `community-mark*.svg`, `community-app-icon.svg` | lilac on plum tile |
| Bubble + note / trail | laiive / VaiVia endorsement icons (optional) | `endorsement-*.svg` | aqua on petrol tile |

Every tool gets a face: same 120 grid, same round stroke (10 to 12), same tile radius.

---

## 7. Colour

| Token | Hex | Role |
|---|---|---|
| `--petrol` | `#10282E` | **Calliope**: high-level screens, the colour around everything |
| `--aqua` | `#A8F5EE` | accent on petrol · Orfeo apps cards |
| `--plum` | `#3B1222` | **Sirenradar** |
| `--lilac` | `#E4B8F5` | **Calliope community** · text on plum |
| `--cream` | `#FDF6D8` | data, communication, **Unsiren** · body text on dark |
| `--olive` | `#3A3200` | text on cream |

Supporting tints (surfaces, hairlines, muted text) are in `tokens/tokens.css`.

**Pairing rule.** Every colour has one partner it is always set with, so any tile is legible by default:
petrol ↔ cream/aqua · plum ↔ lilac/cream · cream ↔ olive · aqua ↔ petrol · lilac ↔ plum.

Contrast (WCAG): cream/petrol 14.2 · aqua/petrol 12.4 · lilac/plum 9.6 · olive/cream 11.8 · petrol/aqua 12.4 · plum/lilac 9.6. Muted text pairs are all ≥ 5.5:1.

- No gradients in the Calliope brand.
- Print: CMYK builds are set at press proof, not converted from hex.

---

## 8. Typography

| Use | Font | Weight | Notes |
|---|---|---|---|
| Display / headlines | Schibsted Grotesk | 800 | tracking −0.05em to −0.055em, line-height 0.95 |
| Body | Schibsted Grotesk | 400 (500 for emphasis) | 15 to 18 px, line-height 1.45 to 1.55 |
| Labels, code, data, sources | JetBrains Mono | 400 (700 for rule IDs) | 11 to 14 px |

One family for words, one for code. No italics in headlines. Both fonts are open source (SIL OFL) and bundled in `fonts/`.

---

## 9. Layout and components

- Boards are 1280 × 800 (organisation views 1280 × 900). Gutter 64 px, gap 16 px.
- **Cards**: radius 24 to 28 px, filled with a role colour, no shadows. Card anatomy: icon tile → mono label (`01 · Find`) → name (800) → one or two sentences → mono footnote (status or source).
- **Chips**: pill, radius 999. Filled = strong (critical, high); outline = medium; dashed = low.
- **Labels**: JetBrains Mono 12 px in the muted tone of the background.
- **Hairlines**: 1 px in the `*-line` tint.
- **Placeholders**: never invent names, venues or numbers. Use `[VENUE]`, `[ARTIST]`, `[TRAIL]`, `[N]`, `[NAME]`, `[REVIEWER]`, `[HASH]` until real content exists.

---

## 10. Motion

Motion explains how something works; it never decorates or hooks.
- Loops of 6 to 10 s, then rest. No autoplaying sound.
- Always respect `prefers-reduced-motion` (every board does; `tokens.css` includes a global rule).
- Reference animations:
  - **K5 Sirenradar**: a scan bar reads the code, flagged lines light up, findings print line by line.
  - **K6 Unsiren**: harmful lines are struck through and fade, the fix slides in, the decision changes, the review stamp appears.
  - **M4 How we work**: messages arrive in a room.
  - **M5 What we make**: dots travel from what we make, through Calliope, to who uses it.

---

## 11. Claims and accuracy (non-negotiable)

- **Sirenradar never says "compliant", "certified" or gives a score.** It "helps teams prepare for" the EU AI Act and other AI rules. Its output is evidence for a reviewer, not legal advice. (This matches the AnyAISafe README.)
- Regulations Sirenradar maps to (from the AnyAISafe README): EU AI Act (Art. 5 manipulation, Art. 50 AI disclosure), GDPR, Digital Services Act (Art. 25 manipulative design, Art. 28 minors), US companion-chatbot laws (California SB 243, SB 1119; New York), reference frameworks NIST AI RMF and OWASP LLM Top 10.
- **Unsiren is a concept** until it ships. Keep the "concept" label wherever it appears.
- **Sirenfree is a recognition, not a certificate**: public criteria, a named reviewer, a stated scope and an expiry date.
- Every statistic keeps its source line. No number without a source.

---

## 12. Evidence used in M2 (with sources)

| Figure | Claim | Source as cited |
|---|---|---|
| 6h 38m | average time online per day, worldwide | We Are Social & Meltwater, *Digital 2025* · [via Telefónica](https://www.telefonica.com/en/communication-room/blog/how-much-time-do-we-spend-on-our-digital-lives/) |
| ~70% | of YouTube watch time driven by its recommendations | Neal Mohan, CES 2018 · [Tubefilter](https://www.tubefilter.com/2018/01/11/youtube-most-watch-time-driven-by-recommendations/) |
| 97% | of popular EU websites/apps show at least one dark pattern | European Commission study, 2022 · [deceptive.design](https://deceptive.design/articles/behavioural-study-on-unfair-commercial-practices-in-the-digital-environment-dark-patterns-and-manipulative-personalisation) |
| 376× | times a day a European's data is broadcast in real-time bidding | [ICCL, May 2022](https://iccl.ie/news/iccl-report-on-the-scale-of-real-time-bidding-data-broadcasts-in-the-u-s-and-europe) |
| 2× | risk of depression/anxiety symptoms for teens on social media > 3 h/day | US Surgeon General advisory, 2023 · [GPB/NPR](https://www.gpb.org/news/2023/05/23/social-media-can-put-young-people-in-danger-us-surgeon-general-warns) |
| +81% | higher odds GPT-4 shifted views when it knew a few facts about the person, vs a human | Salvi et al., *Nature Human Behaviour*, 2025, n = 900 · [eWeek](https://www.eweek.com/news/ai-debates-persuasion/) |
| Rolled back | OpenAI withdrew a GPT-4o update (Apr 2025) "informed too much by short-term feedback" | [TechCrunch](https://techcrunch.com/2025/04/29/openai-explains-why-chatgpt-became-too-sycophantic) |

Several of these are secondary sources. Before publishing the site, link the primary documents (EC report, HHS advisory, the Nature Human Behaviour paper, OpenAI's post).

---

## 13. Mockups index

| File | Board | Use |
|---|---|---|
| `mockups/product/01-K1-guidelines-cover` | K1 | Brand guidelines cover; reference for type scale and the mark in a tile |
| `mockups/product/02-M0i-organisation` | M0i | **Primary** homepage / organisation view: mission first, three services, community as links |
| `mockups/product/03-M0h-organisation-alt` | M0h | **Second option**: four equal columns, community at the same level |
| `mockups/product/04-K5-sirenradar-in-motion` (+ .mp4) | K5 | Sirenradar product page hero; scan animation |
| `mockups/product/05-K6-unsiren-in-motion` (+ .mp4) | K6 | Unsiren product page hero; fix animation |
| `mockups/mission/01-M1-mission` | M1 | Mission: what digital influence is, six mechanisms |
| `mockups/mission/02-M2-evidence` | M2 | The evidence, in numbers (see §12) |
| `mockups/mission/03-M4-how-we-work` (+ .mp4) | M4 | How we work (Spot · Strategy · Act), joining steps, rooms |
| `mockups/mission/04-M5-what-we-make` (+ .mp4) | M5 | What we make and who carries it (flow) |
| `mockups/elements/01-K9-the-figure` | K9 | The mark and its explorations (V1 chosen) |
| `mockups/elements/02-K11-product-icons` | K11 | Product icon system and statuses |
| `mockups/elements/03-K15-orfeo-mark` | K15 | Orfeo mark options (Between used) |

Statuses shown in mockups (from the public repos, November 2026): laiive going to market · VaiVia in development · AnyAISafe v0.3.0 · Unsiren concept. Update them as they change.

---

## 14. Working with these files in Claude Code

- Open any `mockups/**/*.html` directly in a browser; fonts load from `fonts/` with no network.
- Build site components from `tokens/tokens.css` (`@import` it, or copy the variables). Do not hard-code new colours.
- After editing a board's HTML, re-export:
  ```bash
  npm i -D playwright && npx playwright install chromium
  node calliope-brand/scripts/render.cjs            # all PNGs (2x)
  node calliope-brand/scripts/render.cjs --video    # PNGs + MP4s (needs ffmpeg)
  node calliope-brand/scripts/render.cjs K5         # one board
  ```
- `mockups/manifest.json` lists each board's size, whether it moves, and the moment used for its still image.

---

## 15. Open decisions

1. **Artificial vs digital influence.** The mission line says "artificial influence"; M1 and M2 explain "digital influence". Current rule: artificial = headline, digital = explanation. Confirm, or align M1's headline ("To free people from digital influence.").
2. **Sirenradar name.** Public name chosen; the CLI still ships as `aisafe`. Decide when to rename the package.
3. **Unsiren scope.** Concept built on `aisafe review record`. Define what ships first.
4. **Sirenfree criteria.** Write the public criteria, scope and expiry before showing the badge outside mockups.
5. **Joining article title.** M4 uses "The existential risk of digital influence with AI technology", which is louder than the calm voice. Consider "Digital influence in the age of AI: the long risk".
6. **Rooms.** M4 shows rooms inside Calliope (no notifications, weekly digest). Building chat means moderation, safeguarding minors and GDPR work; an open protocol like Matrix under the Calliope skin is the lighter path.
