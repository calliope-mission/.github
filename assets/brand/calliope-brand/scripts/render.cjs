// Render the Calliope mockups to PNG (2x) and, for animated boards, to MP4.
// Usage:  node scripts/render.cjs            -> all PNGs
//         node scripts/render.cjs --video    -> PNGs + MP4s for boards with motion (needs ffmpeg)
//         node scripts/render.cjs K5         -> only boards whose name contains "K5"
// Needs:  npm i -D playwright && npx playwright install chromium
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const { execFileSync } = require('child_process');

const root = path.resolve(__dirname, '..');
const manifest = JSON.parse(fs.readFileSync(path.join(root, 'mockups/manifest.json'), 'utf8'));
const args = process.argv.slice(2);
const wantVideo = args.includes('--video');
const filter = args.find(a => !a.startsWith('--'));

(async () => {
  const browser = await chromium.launch();
  for (const b of manifest) {
    if (filter && !b.name.includes(filter)) continue;
    const html = path.join(root, 'mockups', b.section, b.name + '.html');
    const url = 'file://' + html;
    const size = { width: b.width, height: b.height };

    const ctx = await browser.newContext({ viewport: size, deviceScaleFactor: 2 });
    const page = await ctx.newPage();
    await page.goto(url);
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(Math.max(300, (b.still_at_seconds || 0) * 1000));
    const png = html.replace(/\.html$/, '.png');
    await page.screenshot({ path: png });
    await ctx.close();
    console.log('png ', path.relative(root, png));

    if (wantVideo && b.motion) {
      const tmp = fs.mkdtempSync(path.join(require('os').tmpdir(), 'calliope-'));
      const vctx = await browser.newContext({ viewport: size, recordVideo: { dir: tmp, size } });
      const vpage = await vctx.newPage();
      await vpage.goto(url);
      await vpage.waitForTimeout(10500);
      const webm = await vpage.video().path();
      await vctx.close();
      const mp4 = html.replace(/\.html$/, '.mp4');
      execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-ss', '0.4', '-i', webm, '-t', '10',
        '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', mp4]);
      fs.rmSync(tmp, { recursive: true, force: true });
      console.log('mp4 ', path.relative(root, mp4));
    }
  }
  await browser.close();
})();
