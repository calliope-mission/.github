// Renders every entry in manifest.json to PNG.  Usage: node src/render.cjs [name-filter]
const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');
const root = path.resolve(__dirname, '..');
const list = fs.readdirSync(__dirname).filter(f => /^manifest.*\.json$/.test(f))
  .flatMap(f => JSON.parse(fs.readFileSync(path.join(__dirname, f), 'utf8')))
  .filter(e => !process.argv[2] || e.src.includes(process.argv[2]));
(async () => {
  const browser = await chromium.launch();
  for (const e of list) {
    const page = await browser.newPage({ viewport: { width: e.width, height: e.height }, deviceScaleFactor: e.scale });
    await page.goto('file://' + path.join(root, e.src));
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(150);
    const out = path.join(root, e.png);
    fs.mkdirSync(path.dirname(out), { recursive: true });
    await page.screenshot({ path: out, clip: { x: 0, y: 0, width: e.width, height: e.height }, omitBackground: !!e.transparent });
    console.log(e.png, e.width * e.scale + 'x' + e.height * e.scale, Math.round(fs.statSync(out).size / 1024) + ' KB');
    await page.close();
  }
  await browser.close();
})();
