# Calliope · GitHub artwork

Artwork for the Calliope organisation, the `sirenradar` and `unsiren` repositories, and the Orfeo apps family. Follows the Calliope brand (`calliope-brand/`).

Replace `[ORG]` in the Markdown files with the organisation's GitHub name once it is set.

## What is here

| Folder | Contents |
|---|---|
| `calliope-org/` | Avatar, share images (detailed and minimal), the `.github` profile README with its banners. |
| `sirenradar/` | Icon, share images, README banner, lockups, quickstart animations, README header. |
| `unsiren/` | Icon, share images, README banner, lockups, README header. Labelled concept everywhere. |
| `orfeo-apps/` | Icon, share images, README banner, lockups, README header, and the optional "An Orfeo app · by Calliope" badge. |
| `wordmarks/` | Every wordmark and lockup as SVG with text converted to outlines (no font needed), plus transparent PNGs at 4x in `wordmarks/png/`. |
| `src/` | Sources and scripts to regenerate everything. |

## Where each file goes

| File | Where | How |
|---|---|---|
| `calliope-org/avatar.png` (1024², aqua) | Organisation picture | Org → Settings → Profile → Profile picture. GitHub rounds the corners. `avatar-alt-petrol.png` is the alternative. |
| `calliope-org/profile/` | Repo `[ORG]/.github` | Commit as `profile/README.md` and `profile/assets/`. This is the org's public profile page. The README has the full banner on; the minimal banners and the lockup are in a comment, ready to swap in. |
| `*/social-preview.png` or `*/social-preview-minimal.png` (1280×640) | Each repo's share image | Repo → Settings → General → Social preview. Pick one per repo. For the org, set it on the `.github` repo. |
| `sirenradar/assets/` | Repo `sirenradar` | Commit at that path. `README-header.md` uses the banner and the three quickstart animations. |
| `unsiren/assets/` | Repo `unsiren` | Commit at that path. `README-header.md` uses the banner. |
| `orfeo-apps/` | A repo `orfeo-apps` (suggested name) | Commit `assets/` and `badge/`; `README-header.md` explains the family and lists the apps. |
| `orfeo-apps/badge/` | Each app's own README or footer | Optional. Apps never have to use Calliope's style. |
| `*/icon.png`, `*/icon.svg` | Docs, PyPI, slides | GitHub has no per-repo icon. |

Share images are 1280×640 and under 1 MB, as GitHub asks. Banners are 2x so they stay sharp on high-density screens.

## Wordmarks

- `*-wordmark-<colour>.svg`: the name only.
- `*-lockup-for-light.svg` / `*-for-dark.svg`: icon tile and name, transparent, for light or dark backgrounds.
- `*-lockup-endorsed-*`: with "by Calliope" (Unsiren: "concept · by Calliope").
- `calliope-lockup-tagline-*`: with "Louder than the Sirens."

To switch with GitHub's light or dark theme:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/brand/sirenradar-lockup-endorsed-for-dark.svg">
  <img src="./assets/brand/sirenradar-lockup-endorsed-for-light.svg" alt="Sirenradar, by Calliope" height="72">
</picture>
```

## Orfeo apps

The Orfeo apps artwork is for the family as it appears on Calliope pages: aqua, petrol text, the Between figure. It is not a style for the apps themselves; laiive and VaiVia keep their own name and look.

The laiive and VaiVia icons on the share image are the Calliope-page endorsement icons from `calliope-brand/logos/`, not the apps' own logos. If an app has its own logo, swap it in on Calliope pages.

The badge comes in four versions: petrol, aqua, and an outline for light or dark backgrounds. The outline is the quietest, for apps with their own look.

## Quickstart animations (Sirenradar)

`sirenradar/assets/quickstart/`, each as `.gif` (for READMEs), `.mp4` (for the site and slides) and `.png` (the last frame):

1. **Try**: `uvx aisafe audit .`, 10 s, 1.1 MB.
2. **Share**: the HTML report, 9.5 s, 2.4 MB.
3. **Keep it running**: the GitHub Actions workflow, 10 s, 0.2 MB.

Every line in them is real: the terminal output and the report come from running aisafe 0.3.0 on the project's test fixture `tests/fixtures/audit/persons_companion`, and the workflow is copied from the README. Finding details are folded in the terminal view; the animations say so.

The README header wraps each GIF in `<picture>` with `prefers-reduced-motion`, so people who turn motion off see the still PNG.

## Regenerating

```bash
python3 src/generate.py        # banners, share images, icons      -> src/*.html
python3 src/wordmarks.py       # wordmarks (needs: pip install fonttools brotli uharfbuzz)
python3 src/quickstart.py      # quickstart scenes                 -> src/quickstart.html
node src/render.cjs [filter]   # render PNGs
node src/animate.cjs [try|share|ci]   # render GIF, MP4 and still (needs ffmpeg)
```

**When the CLI is renamed** from `aisafe` to `sirenradar`, run `RUN="uvx sirenradar" python3 src/generate.py` and `RUN="uvx sirenradar" python3 src/quickstart.py`, then render again. Also re-run the tool on the fixture and replace `src/qs/terminal.txt` and `src/qs/aisafe-report.html`, so the output still matches the real tool. Update `src/qs/workflow.yml` when the action moves to the new repository.

## Moving the repos

- Transfer `ai-safe-earth/AnyAISafe` to the Calliope org, then rename it `sirenradar`. GitHub keeps issues, stars and history, and redirects the old URL, so `uses: ai-safe-earth/AnyAISafe@v0.3.0` keeps working. Never create a new repo with the old name, or the redirect breaks.
- Create `unsiren` as a new repo. Label it a concept in the description.
- Suggested descriptions:
  - sirenradar: "Locates the Sirens in AI software. Helps teams prepare for the EU AI Act and other AI rules. Not legal advice."
  - unsiren: "Concept. Proposes fixes for what Sirenradar finds; a named person reviews each one."
- Suggested topics: `ai-act`, `ai-safety`, `dark-patterns`, `static-analysis`, `gdpr`, `dsa`.
