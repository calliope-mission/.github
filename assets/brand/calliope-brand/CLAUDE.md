# Calliope brand · rules for Claude Code

Full reference: `README.md` in this folder. Read it before designing or writing anything user-facing.

## Scope
- Calliope, **Sirenradar**, **Unsiren** and the **Calliope community** follow the Calliope brand: `tokens/tokens.css`, `fonts/`, `logos/`.
- **Orfeo apps** (laiive, VaiVia, future apps) are style-independent products. Do not impose Calliope colours, fonts or marks on them. Only their behaviour is shared: lists end, no streaks or guilt notifications, every screen points out the door.

## Must
- Use the tokens. No new colours, no gradients, no shadows on cards.
- Roles: petrol = Calliope · plum = Sirenradar · cream/olive = Unsiren and data · aqua = Orfeo cards on Calliope pages · lilac = community.
- Type: Schibsted Grotesk (400/500/800) for words, JetBrains Mono (400/700) for labels, code, data and sources.
- Spelling: Calliope · Sirenradar · Unsiren · Orfeo apps · laiive (lowercase) · VaiVia · Calliope community · "We call them Argonauts."
- Mission line: "Calliope, born to free people from artificial influence." Tagline: "Louder than the Sirens."
- Voice: calm and steady. No urgency, no fear, no "fight". Talk to one person ("you").
- Respect `prefers-reduced-motion`. Motion loops 6 to 10 s and only explains how something works.

## Never
- Never write that Sirenradar makes software "compliant", "certified", or gives a "score". Say it "helps teams prepare for" the EU AI Act and other AI rules; it is not legal advice.
- Never present Unsiren as shipped while it is a concept; keep the "concept" label.
- Never call Sirenfree a certificate.
- Never invent statistics, names, venues or reviews. Use `[VENUE]`, `[N]`, `[NAME]` placeholders, and keep the source line on every figure.
- Never use the old names: Sirenwatch, get-out-door, Argonauts as a section or product.

## Files
- Mockups: `mockups/{product,mission,elements}/*.html` (source) with `.png` (2x) and `.mp4` exports.
- Re-export after editing: `node scripts/render.cjs` (add `--video` for animated boards).
