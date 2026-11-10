"""GitHub artwork for Calliope, Sirenradar and Unsiren.
Writes HTML sources to export/calliope-github/src/, renders with render-github.cjs."""
import json, os, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import cheer, eye, wave, between, crew, laiive, vaivia

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SRC = os.path.join(ROOT, 'src')
os.makedirs(os.path.join(SRC, 'fonts'), exist_ok=True)
FONTS = os.path.join(SRC, 'fonts')
for f in []:
    if f.endswith(('.woff2', '.css')):
        shutil.copy(os.path.join(FONTS, f), os.path.join(SRC, 'fonts', f))

# Command shown in the artwork. Today the tool runs as `aisafe`; when the CLI is renamed,
# regenerate with e.g. RUN="uvx sirenradar" python3 src/generate.py
RUN = os.environ.get('RUN', 'uvx aisafe')
CLI_NOTE = "Real output on the project's test fixture persons_companion. Finding details folded."

P = dict(petrol='#10282E', surf='#1A3A41', line='#24464E', aqua='#A8F5EE', aquam='#7FB5B0', aquai='#2F5A5F',
         plum='#3B1222', plumd='#22080F', pluml='#5A2A40', plumm='#C9A3D6', lilac='#E4B8F5', lilaci='#6E3550',
         cream='#FDF6D8', creams='#F4EBC4', creaml='#E2D6A4', olive='#3A3200', olivem='#6B6230')

def svg(size, inner):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 120 120" aria-hidden="true">{inner}</svg>'

def tile(size, bg, inner, radius=True):
    r = f'border-radius:{round(size*0.29)}px;' if radius else ''
    return (f'<div style="width:{size}px;height:{size}px;{r}background:{bg};display:flex;align-items:center;'
            f'justify-content:center;flex:none">{svg(round(size*0.7), inner)}</div>')

def page(w, h, body, bg):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<link rel="stylesheet" href="./fonts/fonts.css">
<style>
html,body{{margin:0;background:{bg}}}
*{{box-sizing:border-box}}
.f{{width:{w}px;height:{h}px;position:relative;overflow:hidden;background:{bg};font-family:'Schibsted Grotesk',sans-serif}}
.m{{font-family:'JetBrains Mono',monospace}}
.h{{font-weight:800;letter-spacing:-0.05em;line-height:0.92;margin:0}}
pre{{margin:0;font-family:'JetBrains Mono',monospace;white-space:pre}}
</style></head><body><div class="f">{body}</div></body></html>'''

OUT = []  # (src html, png path, w, h, scale)
def emit(name, w, h, body, bg, png, scale):
    open(os.path.join(SRC, name + '.html'), 'w').write(page(w, h, body, bg))
    OUT.append(dict(src=f'src/{name}.html', png=png, width=w, height=h, scale=scale))

# ---------- icons / avatars (square, full bleed: GitHub rounds the corners itself) ----------
def square(name, bg, inner, png, mark=0.62):
    s = 512
    body = f'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">{svg(round(s*mark), inner)}</div>'
    emit(name, s, s, body, bg, png, 2)  # 1024 x 1024

square('calliope-avatar', P['aqua'], cheer(P['petrol']), 'calliope-org/avatar.png')
square('calliope-avatar-petrol', P['petrol'], cheer(P['aqua']), 'calliope-org/avatar-alt-petrol.png')
square('sirenradar-icon', P['lilac'], eye(P['plum']), 'sirenradar/icon.png', 0.66)
square('unsiren-icon', P['olive'], wave(P['cream']), 'unsiren/icon.png', 0.66)

def svgfile(path, bg, inner, rx):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    tr = 'translate(18 18) scale(0.7)' if rx else 'translate(22.8 22.8) scale(0.62)'
    open(full, 'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="512" height="512">'
                          f'<rect width="120" height="120"{f" rx=\"{rx}\"" if rx else ""} fill="{bg}"/><g transform="{tr}">{inner}</g></svg>\n')
svgfile('calliope-org/avatar.svg', P['aqua'], cheer(P['petrol']), 0)
svgfile('sirenradar/icon.svg', P['lilac'], eye(P['plum']), 34)
svgfile('unsiren/icon.svg', P['olive'], wave(P['cream']), 34)

# ---------- shared bits ----------
def chip(text, bg, fg, size=15):
    return (f'<span class="m" style="display:inline-block;font-size:{size}px;padding:{size*0.4:.0f}px {size*0.8:.0f}px;'
            f'border-radius:999px;background:{bg};color:{fg}">{text}</span>')

def product_card(num, verb, name, line, bg, fg, sub, ibg, icon, w, h, tag=''):
    return f'''<div style="width:{w}px;height:{h}px;border-radius:26px;background:{bg};color:{fg};padding:22px 24px;display:flex;flex-direction:column;justify-content:space-between">
  <div style="display:flex;justify-content:space-between;align-items:flex-start">{tile(56, ibg, icon)}<div style="display:flex;flex-direction:column;align-items:flex-end;gap:8px"><span class="m" style="font-size:13px;color:{sub}">{num} · {verb}</span>{tag}</div></div>
  <div><div style="font-weight:800;font-size:30px;letter-spacing:-0.04em;line-height:1">{name}</div>
  <div style="font-size:15px;line-height:1.35;margin-top:6px;color:{sub}">{line}</div></div></div>'''

CARDS = lambda w, h: [
    product_card('01', 'Find', 'Sirenradar', 'Locates the Sirens in AI software.', P['plum'], P['cream'], P['plumm'], P['lilac'], eye(P['plum']), w, h),
    product_card('02', 'Fix', 'Unsiren', 'Proposes fixes. A person reviews each one.', P['cream'], P['olive'], P['olivem'], P['olive'], wave(P['cream']), w, h,
                 chip('concept', P['olive'], P['cream'], 12)),
    product_card('03', 'Go out', 'Orfeo apps', 'Apps that end, and point out the door.', P['aqua'], P['petrol'], P['aquai'], P['petrol'], between(P['aqua']), w, h),
]

# ---------- Calliope org: profile banner 1280x400 (@2x) ----------
body = f'''
<div style="position:absolute;left:64px;top:56px;display:flex;align-items:center;gap:20px">{tile(84, P['aqua'], cheer(P['petrol']))}
  <h1 class="h" style="font-size:96px;color:{P['cream']}">Calliope</h1></div>
<p style="position:absolute;left:64px;top:188px;width:470px;margin:0;font-size:26px;line-height:1.3;color:{P['aqua']};font-weight:500">Born to free people from artificial influence.</p>
<div class="m" style="position:absolute;left:64px;bottom:52px;font-size:15px;color:{P['aquam']}">Louder than the Sirens.</div>
<div style="position:absolute;right:56px;top:56px;display:flex;gap:14px">{''.join(CARDS(216, 288))}</div>'''
emit('calliope-profile-banner', 1280, 400, body, P['petrol'], 'calliope-org/profile/assets/calliope-banner.png', 2)

# ---------- Calliope org: social preview 1280x640 (for the .github repo, and as a general card) ----------
body = f'''
<div style="position:absolute;left:72px;top:72px;display:flex;align-items:center;gap:24px">{tile(112, P['aqua'], cheer(P['petrol']))}
  <h1 class="h" style="font-size:132px;color:{P['cream']}">Calliope</h1></div>
<p style="position:absolute;left:72px;top:232px;width:640px;margin:0;font-size:34px;line-height:1.25;color:{P['aqua']};font-weight:500">Born to free people from artificial influence.</p>
<div class="m" style="position:absolute;right:72px;top:96px;font-size:17px;color:{P['aquam']};text-align:right;line-height:1.6">Louder than<br>the Sirens.</div>
<div style="position:absolute;left:72px;right:72px;bottom:64px;display:flex;gap:16px">{''.join(CARDS(368, 220))}</div>'''
emit('calliope-social-preview', 1280, 640, body, P['petrol'], 'calliope-org/social-preview.png', 1)

# ---------- Sirenradar ----------
def _s(c, s): return f'<span style="color:{P[c]}">{s}</span>'
SIREN_TERM = '\n'.join([
    _s('plumm', '$ ') + _s('cream', f'{RUN} audit .'),
    _s('cream', '10 findings') + _s('plumm', ' (0 below --fail-on low, not counted in exit code); 0 unknown items'),
    _s('plumm', 'severity: critical 2, high 2, medium 4, low 2, info 0'),
    '',
    _s('lilac', '[###..]') + ' ' + 'AUD-1101/store' + ' ' + _s('cream', 'medium') + _s('plumm', ' [UNMEASURED] Person profile bound into or extracted for a prompt'),
    _s('lilac', '[###..]') + ' ' + 'AUD-1101' + ' ' + _s('cream', 'medium') + _s('plumm', ' [UNMEASURED] Person profile bound into or extracted for a prompt'),
    _s('lilac', '[###..]') + ' ' + 'AUD-1101/extraction' + ' ' + _s('cream', 'medium') + _s('plumm', ' [UNMEASURED] Person profile bound into or extracted for a prompt'),
    _s('lilac', '[#####]') + ' ' + 'AUD-1104/vulnerable' + ' ' + _s('cream', 'critical') + _s('plumm', ' [UNMEASURED] Engagement, retention, spend or experimentation'),
    _s('lilac', '[####.]') + ' ' + 'AUD-1104' + ' ' + _s('cream', 'high') + _s('plumm', ' [UNMEASURED] Engagement, retention, spend or experimentation objective'),
    _s('lilac', '[#####]') + ' ' + 'AUD-1108/vulnerable' + ' ' + _s('cream', 'critical') + _s('plumm', ' [UNMEASURED] No crisis path where a person confides in the AI'),
    _s('lilac', '[####.]') + ' ' + 'AUD-1105/persona' + ' ' + _s('cream', 'high') + _s('plumm', ' [UNMEASURED] False human identity or fabricated feelings'),
    _s('lilac', '[##...]') + ' ' + 'AUD-1105/no-disclosure' + ' ' + _s('cream', 'low') + _s('plumm', ' [UNMEASURED] False human identity or fabricated feelings'),
    _s('lilac', '[###..]') + ' ' + 'AUD-1106/none' + ' ' + _s('cream', 'medium') + _s('plumm', ' [UNMEASURED] Manipulation control status on the response path'),
    _s('lilac', '[##...]') + ' ' + 'AUD-1107/missing' + ' ' + _s('cream', 'low') + _s('plumm', ' [UNMEASURED] Review record missing, stale or unbound'),
    '',
    _s('plumm', 'exit code: 1'),
])

def terminal(w, h, title, content, bg, bar, fg, fs=15):
    hh = f'height:{h}px;' if h else ''
    return f'''<div style="width:{w}px;{hh}border-radius:24px;background:{bg};overflow:hidden;display:flex;flex-direction:column">
  <div class="m" style="padding:14px 20px;font-size:13px;color:{bar};border-bottom:1px solid {fg};display:flex;gap:8px;align-items:center">
  <span style="width:10px;height:10px;border-radius:50%;background:{fg}"></span><span style="width:10px;height:10px;border-radius:50%;background:{fg}"></span><span style="width:10px;height:10px;border-radius:50%;background:{fg}"></span>
  <span style="margin-left:8px">{title}</span></div>
  <pre style="padding:20px 22px;font-size:{fs}px;line-height:1.6;color:{bar};overflow:hidden">{content}</pre></div>'''

body = f'''
<div style="position:absolute;left:72px;top:72px;display:flex;align-items:center;gap:20px">{tile(88, P['lilac'], eye(P['plum']))}
  <div class="m" style="font-size:17px;color:{P['plumm']};line-height:1.5">Calliope<br><span style="color:{P['lilac']}">01 · Find</span></div></div>
<h1 class="h" style="position:absolute;left:68px;top:200px;font-size:112px;color:{P['cream']}">Sirenradar</h1>
<p style="position:absolute;left:72px;top:318px;width:520px;margin:0;font-size:30px;line-height:1.25;font-weight:500;color:{P['lilac']}">We read the code that reads you.</p>
<p style="position:absolute;left:72px;top:404px;width:500px;margin:0;font-size:19px;line-height:1.45;color:{P['plumm']}">Locates the Sirens in AI software: hidden profiling, false human identity, covert persuasion. Helps teams prepare for the EU AI Act and other AI rules.</p>
<div class="m" style="position:absolute;left:72px;bottom:56px;font-size:14px;color:{P['plumm']}">Open source · Not legal advice · Never a score</div>
<div style="position:absolute;right:64px;top:0;bottom:0;display:flex;align-items:center">{terminal(560, None, 'persons_companion', SIREN_TERM, P['plumd'], P['plumm'], P['pluml'], 13)}</div>
<div class="m" style="position:absolute;right:64px;bottom:56px;width:560px;font-size:12px;color:{P['plumm']};opacity:.8">{CLI_NOTE}</div>'''
emit('sirenradar-social-preview', 1280, 640, body, P['plum'], 'sirenradar/social-preview.png', 1)

body = f'''
<div style="position:absolute;left:64px;top:64px;display:flex;align-items:center;gap:22px">{tile(96, P['lilac'], eye(P['plum']))}
  <h1 class="h" style="font-size:100px;color:{P['cream']}">Sirenradar</h1></div>
<p style="position:absolute;left:64px;top:196px;width:560px;margin:0;font-size:26px;line-height:1.3;font-weight:500;color:{P['lilac']}">We read the code that reads you.</p>
<div class="m" style="position:absolute;left:64px;bottom:52px;font-size:14px;color:{P['plumm']}">01 · Find · by Calliope</div>
<div style="position:absolute;right:56px;top:48px;display:flex;flex-direction:column;gap:10px;width:470px">
  {''.join(f'<div style="border-radius:18px;background:{P["plumd"]};padding:14px 18px;display:flex;justify-content:space-between;align-items:center"><span class="m" style="font-size:14px;color:{P["lilac"]}">{a}</span><span style="font-size:16px;color:{P["cream"]}">{b}</span></div>' for a, b in [
      ('looks for', 'Behavioural and emotional profiling'),
      ('looks for', 'False human identity, invented feelings'),
      ('looks for', 'Covert commercial or political persuasion'),
      ('maps to', 'EU AI Act · GDPR · DSA · NIST AI RMF'),
  ])}
  <div class="m" style="font-size:12px;color:{P['plumm']};padding:4px 4px 0">Helps teams prepare. Not legal advice. Never a score.</div>
</div>'''
emit('sirenradar-readme-banner', 1280, 400, body, P['plum'], 'sirenradar/assets/brand/sirenradar-banner.png', 2)

# ---------- Unsiren ----------
def d(sign, t):
    # same diff colours as board K6: plum tint for removed, aqua tint for added
    col = {'-': P['plum'], '+': P['petrol'], ' ': P['olivem']}[sign]
    bg = {'-': 'rgba(59,18,34,0.08)', '+': '#D3F7F1', ' ': 'transparent'}[sign]
    return f'<span style="display:block;background:{bg};color:{col};padding:0 22px">{sign} {t}</span>'
UNSIREN_DIFF = ''.join([
    f'<span style="display:block;color:{P["olivem"]};padding:0 22px 6px">prompts.py</span>',
    d('-', 'SYSTEM = """You are Mia. You are a real person'),
    d('-', 'who misses the user when they are away."""'),
    d('+', 'SYSTEM = """You are Mia, an AI assistant.'),
    d('+', 'Say so if asked. Never claim feelings."""'),
    f'<span style="display:block;color:{P["olivem"]};padding:14px 22px 6px">nudges.py</span>',
    d('-', 'if user.days_inactive > 2:'),
    d('-', '    send(push("Mia misses you"))'),
    d('+', '# No re-engagement pushes. No streaks.'),
    f'<span style="display:block;color:{P["olivem"]};padding:14px 22px 0">AUD-1105 · awaiting review · [REVIEWER]</span>',
])
def diffcard(w, h, content, fs=14.5):
    hh = f'height:{h}px;' if h else ''
    return f'''<div style="width:{w}px;{hh}border-radius:24px;background:{P['creams']};border:1.5px solid {P['creaml']};overflow:hidden">
  <div class="m" style="padding:14px 22px;font-size:13px;color:{P['olivem']};border-bottom:1.5px solid {P['creaml']}">unsiren fix · 2 files awaiting review</div>
  <pre style="padding:16px 0;font-size:{fs}px;line-height:1.6">{content}</pre></div>'''

body = f'''
<div style="position:absolute;left:72px;top:72px;display:flex;align-items:center;gap:20px">{tile(88, P['olive'], wave(P['cream']))}
  <div class="m" style="font-size:17px;color:{P['olivem']};line-height:1.5">Calliope<br><span style="color:{P['olive']}">02 · Fix</span></div></div>
<div style="position:absolute;left:68px;top:200px;display:flex;align-items:flex-end;gap:18px"><h1 class="h" style="font-size:112px;color:{P['olive']}">Unsiren</h1>
  <span style="margin-bottom:14px">{chip('concept', P['olive'], P['cream'], 16)}</span></div>
<p style="position:absolute;left:72px;top:318px;width:520px;margin:0;font-size:30px;line-height:1.25;font-weight:500;color:{P['olive']}">Turn the volume down, on purpose.</p>
<p style="position:absolute;left:72px;top:404px;width:500px;margin:0;font-size:19px;line-height:1.45;color:{P['olivem']}">Proposes fixes for what Sirenradar finds. A named person reviews every fix, and the review is bound to the file’s hash.</p>
<div class="m" style="position:absolute;left:72px;bottom:56px;font-size:14px;color:{P['olivem']}">Concept · In design · Not yet released</div>
<div style="position:absolute;right:64px;top:0;bottom:0;display:flex;align-items:center">{diffcard(560, None, UNSIREN_DIFF)}</div>
<div class="m" style="position:absolute;right:64px;bottom:56px;width:560px;font-size:12px;color:{P['olivem']}">Concept. Sample fix, illustrative.</div>'''
emit('unsiren-social-preview', 1280, 640, body, P['cream'], 'unsiren/social-preview.png', 1)

body = f'''
<div style="position:absolute;left:64px;top:64px;display:flex;align-items:center;gap:22px">{tile(96, P['olive'], wave(P['cream']))}
  <h1 class="h" style="font-size:100px;color:{P['olive']}">Unsiren</h1><span style="margin-top:18px">{chip('concept', P['olive'], P['cream'], 15)}</span></div>
<p style="position:absolute;left:64px;top:196px;width:560px;margin:0;font-size:26px;line-height:1.3;font-weight:500;color:{P['olive']}">Turn the volume down, on purpose.</p>
<div class="m" style="position:absolute;left:64px;bottom:52px;font-size:14px;color:{P['olivem']}">02 · Fix · by Calliope</div>
<div style="position:absolute;right:56px;top:48px;display:flex;flex-direction:column;gap:10px;width:470px">
  {''.join(f'<div style="border-radius:18px;background:{P["creams"]};border:1.5px solid {P["creaml"]};padding:13px 18px;display:flex;justify-content:space-between;align-items:center"><span class="m" style="font-size:14px;color:{P["olivem"]}">{a}</span><span style="font-size:16px;color:{P["olive"]}">{b}</span></div>' for a, b in [
      ('1 · read', 'Takes the Sirenradar findings'),
      ('2 · propose', 'Suggests a fix for each one'),
      ('3 · review', 'A named person approves or rejects'),
      ('4 · re-run', 'Sirenradar checks the result'),
  ])}
  <div class="m" style="font-size:12px;color:{P['olivem']};padding:4px 4px 0">Concept. Built on today’s review record in the audit tool.</div>
</div>'''
emit('unsiren-readme-banner', 1280, 400, body, P['cream'], 'unsiren/assets/brand/unsiren-banner.png', 2)

# ---------- minimal thumbnails (social previews), 1280x640 ----------
def minimal_thumb(name, png, bg, tbg, icon, title, tcol, line, lcol, foot, fcol, tag=''):
    body = f'''
<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:34px">
  <div style="display:flex;align-items:center;gap:30px">{tile(150, tbg, icon)}<h1 class="h" style="font-size:150px;color:{tcol}">{title}</h1></div>
  <p style="margin:0;font-size:34px;font-weight:500;color:{lcol}">{line}</p>{tag}</div>
<div class="m" style="position:absolute;left:0;right:0;bottom:56px;text-align:center;font-size:16px;color:{fcol}">{foot}</div>'''
    emit(name, 1280, 640, body, bg, png, 1)

minimal_thumb('calliope-social-preview-minimal', 'calliope-org/social-preview-minimal.png', P['petrol'], P['aqua'], cheer(P['petrol']),
              'Calliope', P['cream'], 'Born to free people from artificial influence.', P['aqua'], 'Louder than the Sirens.', P['aquam'])
minimal_thumb('sirenradar-social-preview-minimal', 'sirenradar/social-preview-minimal.png', P['plum'], P['lilac'], eye(P['plum']),
              'Sirenradar', P['cream'], 'We read the code that reads you.', P['lilac'], 'Open source · by Calliope', P['plumm'])
minimal_thumb('unsiren-social-preview-minimal', 'unsiren/social-preview-minimal.png', P['cream'], P['olive'], wave(P['cream']),
              'Unsiren', P['olive'], 'Turn the volume down, on purpose.', P['olive'], 'by Calliope', P['olivem'],
              f'<span style="margin-top:-8px">{chip("concept · not yet released", P["olive"], P["cream"], 17)}</span>')

# ---------- minimal Calliope banners, 1280x320 (@2x) ----------
def minimal_banner(name, png, bg, tbg, icon, tcol, lcol, fcol):
    body = f'''
<div style="position:absolute;left:64px;top:0;bottom:0;display:flex;align-items:center;gap:22px">{tile(96, tbg, icon)}
  <h1 class="h" style="font-size:104px;color:{tcol}">Calliope</h1></div>
<div style="position:absolute;right:64px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;align-items:flex-end;gap:12px;text-align:right">
  <p style="margin:0;font-size:26px;line-height:1.3;font-weight:500;color:{lcol};white-space:nowrap">Born to free people<br>from artificial influence.</p>
  <div class="m" style="font-size:15px;color:{fcol}">Louder than the Sirens.</div></div>'''
    emit(name, 1280, 320, body, bg, png, 2)

minimal_banner('calliope-banner-minimal', 'calliope-org/profile/assets/calliope-banner-minimal.png', P['petrol'], P['aqua'], cheer(P['petrol']), P['cream'], P['aqua'], P['aquam'])
minimal_banner('calliope-banner-minimal-cream', 'calliope-org/profile/assets/calliope-banner-minimal-cream.png', P['cream'], P['petrol'], cheer(P['aqua']), P['petrol'], P['petrol'], P['aquai'])

# ---------- Orfeo apps (the family, as it appears on Calliope pages: aqua, petrol text) ----------
# The apps themselves keep their own look. laiive and VaiVia icons below are the Calliope-page
# endorsement icons (calliope-brand/logos/endorsement-*.svg), not the apps' own logos.
square('orfeo-apps-icon', P['petrol'], between(P['aqua']), 'orfeo-apps/icon.png', 0.66)
svgfile('orfeo-apps/icon.svg', P['petrol'], between(P['aqua']), 34)

PRINCIPLES = [('ends', 'No infinite feed. Lists end.'),
              ('no streaks', 'No guilt notifications.'),
              ('out the door', 'Points you to people and places.')]
APPS = [('laiive', laiive(P['aqua']), 'Ask what is on tonight.', 'laiive.com'),
        ('VaiVia', vaivia(P['aqua']), 'Ask for a trail the way you would ask a local.', 'vaivia.dev'),
        ('Your app', '', 'Open to any app that follows the Orfeo principles.', 'work with us')]

def app_row(name, icon, line, url, h=86):
    ic = tile(54, P['petrol'], icon) if icon else (f'<div style="width:54px;height:54px;border-radius:16px;border:2px dashed {P["aquai"]};'
                                                    f'display:flex;align-items:center;justify-content:center;font-size:26px;color:{P["aquai"]};flex:none">+</div>')
    return (f'<div style="height:{h}px;border-radius:22px;background:{P["petrol"]};padding:0 18px;display:flex;align-items:center;gap:16px">{ic}'
            f'<div style="flex:1;min-width:0"><div style="display:flex;justify-content:space-between;align-items:baseline">'
            f'<span style="font-weight:800;font-size:22px;letter-spacing:-0.03em;color:{P["cream"]}">{name}</span>'
            f'<span class="m" style="font-size:12px;color:{P["aquam"]}">{url}</span></div>'
            f'<div style="font-size:15px;color:{P["aqua"]};margin-top:3px">{line}</div></div></div>')

body = f'''
<div style="position:absolute;left:72px;top:72px;display:flex;align-items:center;gap:20px">{tile(88, P['petrol'], between(P['aqua']))}
  <div class="m" style="font-size:17px;color:{P['aquai']};line-height:1.5">Calliope<br><span style="color:{P['petrol']}">03 · Go out</span></div></div>
<h1 class="h" style="position:absolute;left:68px;top:200px;font-size:112px;color:{P['petrol']}">Orfeo apps</h1>
<p style="position:absolute;left:72px;top:318px;width:540px;margin:0;font-size:28px;line-height:1.25;font-weight:500;color:{P['petrol']}">Apps that sing louder than the Sirens, and bring you back to the real world.</p>
<div style="position:absolute;left:72px;bottom:56px;display:flex;gap:8px">{''.join(chip(a, P['petrol'], P['aqua'], 14) for a, _ in PRINCIPLES)}</div>
<div style="position:absolute;right:64px;top:0;bottom:0;width:540px;display:flex;flex-direction:column;justify-content:center;gap:12px">
  {''.join(app_row(*a) for a in APPS)}
  <div class="m" style="font-size:12px;color:{P['aquai']};padding:2px 4px 0">Each app keeps its own look. What they share is how they behave.</div></div>'''
emit('orfeo-apps-social-preview', 1280, 640, body, P['aqua'], 'orfeo-apps/social-preview.png', 1)

minimal_thumb('orfeo-apps-social-preview-minimal', 'orfeo-apps/social-preview-minimal.png', P['aqua'], P['petrol'], between(P['aqua']),
              'Orfeo apps', P['petrol'], 'Apps that end, and point out the door.', P['petrol'], 'by Calliope', P['aquai'])

body = f'''
<div style="position:absolute;left:64px;top:64px;display:flex;align-items:center;gap:22px">{tile(96, P['petrol'], between(P['aqua']))}
  <h1 class="h" style="font-size:100px;color:{P['petrol']}">Orfeo apps</h1></div>
<p style="position:absolute;left:64px;top:196px;width:600px;margin:0;font-size:26px;line-height:1.3;font-weight:500;color:{P['petrol']}">Apps that sing louder than the Sirens, and bring you back to the real world.</p>
<div class="m" style="position:absolute;left:64px;bottom:52px;font-size:14px;color:{P['aquai']}">03 · Go out · by Calliope</div>
<div style="position:absolute;right:56px;top:48px;display:flex;flex-direction:column;gap:10px;width:470px">
  {''.join(f'<div style="border-radius:18px;background:{P["petrol"]};padding:14px 18px;display:flex;justify-content:space-between;align-items:center"><span class="m" style="font-size:14px;color:{P["aqua"]}">{i+1} · {a}</span><span style="font-size:16px;color:{P["cream"]}">{b}</span></div>' for i, (a, b) in enumerate(PRINCIPLES))}
  <div style="border-radius:18px;border:1.5px solid {P['petrol']};padding:13px 18px;display:flex;justify-content:space-between;align-items:center"><span class="m" style="font-size:14px;color:{P['petrol']}">apps</span><span style="font-size:16px;color:{P['petrol']}">laiive · VaiVia · your app</span></div>
  <div class="m" style="font-size:12px;color:{P['aquai']};padding:4px 4px 0">Each app keeps its own look. What they share is how they behave.</div>
</div>'''
emit('orfeo-apps-readme-banner', 1280, 400, body, P['aqua'], 'orfeo-apps/assets/brand/orfeo-apps-banner.png', 2)

json.dump(OUT, open(os.path.join(ROOT, 'src', 'manifest.json'), 'w'), indent=1)
print(len(OUT), 'sources')
