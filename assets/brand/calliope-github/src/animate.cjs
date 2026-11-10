// Renders the quickstart scenes to GIF, MP4 and a still PNG.
// Usage: node src/animate.cjs [try|share|ci]      (needs ffmpeg on PATH)
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const path = require('path'), fs = require('fs'), os = require('os');
const root = path.resolve(__dirname, '..');
const outDir = path.join(root, 'sirenradar', 'assets', 'quickstart');
const FPS = 12, SCALE = 1.5, W = 880, H = 520;
const names = process.argv[2] ? [process.argv[2]] : ['try', 'share', 'ci'];
const order = { try: '1-try', share: '2-share', ci: '3-keep-running' };
(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  for (const name of names) {
    const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: SCALE });
    await page.goto('file://' + path.join(__dirname, 'quickstart.html'));
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(1000);   // let the report iframe load
    const dur = await page.evaluate(n => window.DURATION[n], name);
    const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'qs-'));
    const frames = Math.round(dur * FPS);
    for (let i = 0; i < frames; i++) {
      await page.evaluate(([n, t]) => window.render(n, t), [name, i / FPS]);
      await page.screenshot({ path: path.join(tmp, `f${String(i).padStart(4, '0')}.png`), clip: { x: 0, y: 0, width: W, height: H } });
    }
    const base = path.join(outDir, `sirenradar-quickstart-${order[name]}`);
    const inp = ['-y', '-loglevel', 'error', '-framerate', String(FPS), '-i', path.join(tmp, 'f%04d.png')];
    execFileSync('ffmpeg', [...inp, '-vf', 'scale=1100:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=64:stats_mode=full[p];[b][p]paletteuse=dither=none:diff_mode=rectangle', '-loop', '0', base + '.gif']);
    execFileSync('ffmpeg', [...inp, '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', base + '.mp4']);
    fs.copyFileSync(path.join(tmp, `f${String(frames - 1).padStart(4, '0')}.png`), base + '.png');   // last frame = still for reduced motion
    fs.rmSync(tmp, { recursive: true });
    for (const ext of ['gif', 'mp4', 'png']) console.log(path.relative(root, base + '.' + ext), Math.round(fs.statSync(base + '.' + ext).size / 1024) + ' KB');
    await page.close();
  }
  await browser.close();
})();
