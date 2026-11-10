"""Quickstart animations for the Sirenradar README.
Writes src/quickstart.html; render with:  node src/animate.cjs
Every line of terminal output and YAML is copied from the real tool (src/qs/), not written by hand."""
import html, json, os
from common import eye

HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.environ.get('RUN', 'uvx aisafe')   # today's command; change when the CLI is renamed

term = open(os.path.join(HERE, 'qs', 'terminal.txt')).read().splitlines()
head = term[:term.index('Findings')]                      # banner, disclaimer, summary
finds = [l for l in term if l.startswith('[')]           # one header line per finding
TRY = head + ['Findings', '--------'] + finds + ['', 'exit code: 1']
yml = [l for l in open(os.path.join(HERE, 'qs', 'workflow.yml')).read().splitlines() if not l.startswith('```')]

SCENES = {
    'try': dict(step=1, title='Try it in one minute',
                caption='From the root of any repository. No API key, no account, no model call.',
                cmd=f'{RUN} audit .', out=TRY,
                note="Real output on the project's test fixture persons_companion. Finding details folded."),
    'share': dict(step=2, title='Share a report',
                  caption='The same scan, as a document you can read and share.',
                  cmd=f'{RUN} audit . --format html -o aisafe-report.html', out=[],
                  note='Real report from the same fixture. Not legal advice; never a certificate.'),
    'ci': dict(step=3, title='Keep it running',
               caption='One step in GitHub Actions. With a committed baseline, only new findings count.',
               cmd='', out=yml, file='.github/workflows/aisafe.yml',
               note='From the README of v0.3.0. After the move, the action path follows the new repository name.'),
}

P = dict(plum='#3B1222', plumd='#22080F', pluml='#5A2A40', plumm='#C9A3D6', lilac='#E4B8F5', cream='#FDF6D8')

page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<link rel="stylesheet" href="./fonts/fonts.css">
<style>
html,body{{margin:0;background:{P['plum']}}}
*{{box-sizing:border-box}}
#f{{width:880px;height:520px;position:relative;overflow:hidden;background:{P['plum']};font-family:'Schibsted Grotesk',sans-serif;color:{P['cream']}}}
.m{{font-family:'JetBrains Mono',monospace}}
#steps span{{padding:5px 11px;border-radius:999px;color:{P['plumm']};border:1px solid {P['pluml']}}}
#steps span.on{{background:{P['lilac']};color:{P['plum']};border-color:{P['lilac']}}}
#term{{position:absolute;left:28px;right:28px;top:112px;bottom:44px;border-radius:20px;background:{P['plumd']};overflow:hidden}}
#bar{{height:38px;display:flex;align-items:center;gap:7px;padding:0 16px;border-bottom:1px solid {P['pluml']};font-size:12px;color:{P['plumm']}}}
#bar i{{width:9px;height:9px;border-radius:50%;background:{P['pluml']}}}
#body{{position:absolute;left:0;right:0;top:38px;bottom:0;padding:12px 18px;overflow:hidden}}
#lines{{position:absolute;left:18px;right:18px;top:12px;font-size:12.5px;line-height:19px;white-space:pre;color:{P['plumm']}}}
.c{{color:{P['cream']}}} .l{{color:{P['lilac']}}}
.cur{{display:inline-block;width:8px;height:15px;background:{P['lilac']};vertical-align:-3px}}
#doc{{position:absolute;left:44px;right:44px;top:128px;bottom:40px;border-radius:16px;overflow:hidden;background:#fff;transform:translateY(420px)}}
#doc .bar{{height:30px;background:{P['lilac']};color:{P['plum']};font-size:12px;display:flex;align-items:center;padding:0 14px}}
#doc iframe{{border:0;width:1100px;height:3200px;transform:scale(.72);transform-origin:0 0;position:absolute;top:30px;left:0}}
</style></head><body><div id="f">
  <div style="position:absolute;left:28px;top:24px;display:flex;align-items:center;gap:12px">
    <div style="width:36px;height:36px;border-radius:10px;background:{P['lilac']};display:flex;align-items:center;justify-content:center"><svg width="25" height="25" viewBox="0 0 120 120">{eye(P['plum'])}</svg></div>
    <div style="font-weight:800;font-size:22px;letter-spacing:-0.04em">Sirenradar</div>
    <div class="m" style="font-size:12px;color:{P['plumm']};margin-left:2px">quickstart</div></div>
  <div id="steps" class="m" style="position:absolute;right:28px;top:30px;display:flex;gap:6px;font-size:11.5px">
    <span data-s="1">1 · Try</span><span data-s="2">2 · Share</span><span data-s="3">3 · Keep it running</span></div>
  <div style="position:absolute;left:28px;top:72px;font-size:15px;color:{P['lilac']}"><b id="title" style="color:{P['cream']}"></b>&nbsp;&nbsp;<span id="cap"></span></div>
  <div id="term"><div id="bar" class="m"><i></i><i></i><i></i><span id="fname" style="margin-left:8px"></span></div>
    <div id="body"><div id="lines" class="m"></div></div></div>
  <div id="doc"><div class="bar m">aisafe-report.html</div><iframe id="ifr" src="./qs/aisafe-report.html" scrolling="no"></iframe></div>
  <div id="note" class="m" style="position:absolute;left:28px;right:28px;bottom:16px;font-size:10.5px;color:{P['plumm']}"></div>
</div>
<script>
const SCENES = {json.dumps(SCENES)};
const esc = s => s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const VISIBLE = 15;
function colour(l) {{
  if (/^\\[/.test(l)) {{ const m = l.match(/^(\\[[#.]+\\]) (\\S+) (\\S+)(.*)$/); if (m) return `<span class="l">${{m[1]}}</span> <span class="c">${{m[2]}}</span> <span class="c">${{m[3]}}</span>${{esc(m[4])}}`; }}
  if (/^\\d+ findings/.test(l) || /^exit code/.test(l)) return `<span class="c">${{esc(l)}}</span>`;
  return esc(l);
}}
function yamlColour(l) {{
  const m = l.match(/^(\\s*-?\\s*)([\\w-]+:)(.*)$/);
  if (!m) return esc(l);
  const [, rest, comment] = m[3].match(/^(.*?)(\\s+#.*)?$/);
  return esc(m[1]) + `<span class="l">${{esc(m[2])}}</span><span class="c">${{esc(rest||'')}}</span>` + (comment ? esc(comment) : '');
}}
window.DURATION = {{ try: 10, share: 9.5, ci: 10 }};
window.render = function (name, t) {{
  const S = SCENES[name];
  document.querySelectorAll('#steps span').forEach(s => s.classList.toggle('on', +s.dataset.s === S.step));
  document.getElementById('title').textContent = S.title + '.';
  document.getElementById('cap').textContent = S.caption;
  document.getElementById('note').textContent = S.note;
  document.getElementById('fname').textContent = S.file || 'persons_companion';
  const L = document.getElementById('lines');
  const blink = Math.floor(t * 2) % 2 === 0 ? '<span class="cur"></span>' : '';
  let out = [];
  if (name === 'ci') {{
    const n = Math.max(0, Math.min(S.out.length, Math.floor((t - 0.4) / 0.32) + 1));
    out = S.out.slice(0, n).map(yamlColour);
    if (n < S.out.length) out.push(blink);
    else if (t > 7.2) out.push('', `<span class="l">$</span> <span class="c">git add .github/workflows/aisafe.yml &amp;&amp; git push</span>`);
    out = out.slice(-VISIBLE);
  }} else {{
    const typed = Math.max(0, Math.min(S.cmd.length, Math.floor((t - 0.5) * 30)));
    const done = typed === S.cmd.length;
    out.push(`<span class="l">$</span> <span class="c">${{esc(S.cmd.slice(0, typed))}}</span>` + (done && t > (0.5 + S.cmd.length/30 + 0.4) ? '' : blink));
    const start = 0.5 + S.cmd.length / 30 + 0.4;
    if (t > start) {{
      const n = Math.min(S.out.length, Math.floor((t - start) / 0.11) + 1);
      out = out.concat(S.out.slice(0, n).map(colour));
      if (name === 'try' && n === S.out.length) out.push(`<span class="l">$</span> ${{blink}}`);
    }}
    if (name === 'share' && t > start + 0.6) out.push(`<span class="l">$</span> ${{blink}}`);
    out = out.slice(-VISIBLE);
  }}
  L.innerHTML = out.join('\\n');
  const doc = document.getElementById('doc');
  if (name === 'share') {{
    const s = t - 3.2, ease = x => x < 0 ? 0 : x > 1 ? 1 : 1 - Math.pow(1 - x, 3);
    doc.style.transform = `translateY(${{(1 - ease(s / 0.8)) * 420}}px)`;
    const sc = ease((t - 4.6) / 3.4) * 640;
    document.getElementById('ifr').style.transform = `scale(.72) translateY(${{-sc}}px)`;
  }} else doc.style.transform = 'translateY(420px)';
}};
const q = new URLSearchParams(location.search);
if (q.get('scene')) {{
  const name = q.get('scene');
  if (q.get('t')) render(name, +q.get('t'));
  else {{ const t0 = performance.now(); (function loop(){{ render(name, ((performance.now()-t0)/1000) % DURATION[name]); requestAnimationFrame(loop); }})(); }}
}}
</script></body></html>'''
open(os.path.join(HERE, 'quickstart.html'), 'w').write(page)
print('ok', len(TRY), 'terminal lines', len(yml), 'yaml lines')
