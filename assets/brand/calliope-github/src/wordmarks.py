"""Wordmarks and lockups with text converted to outlines (no font needed to display them).
Run with a Python that has fonttools, brotli and uharfbuzz:  python3 src/wordmarks.py
Writes ../wordmarks/*.svg and src/wordmarks-sheet.html (rendered to PNG by render.cjs)."""
import io, json, os
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from common import cheer, eye, wave, between

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, 'wordmarks')
os.makedirs(OUT, exist_ok=True)
FONTS = os.path.join(HERE, 'fonts')

class Face:
    def __init__(self, file):
        self.tt = TTFont(os.path.join(FONTS, file))
        buf = io.BytesIO(); self.tt.flavor = None; self.tt.save(buf)   # woff2 -> sfnt for HarfBuzz
        self.hbfont = hb.Font(hb.Face(buf.getvalue()))
        self.upm = self.tt['head'].unitsPerEm
        self.cap = self.tt['OS/2'].sCapHeight
        self.gs = self.tt.getGlyphSet()
        self.order = self.tt.getGlyphOrder()

    def path(self, text, size, x0=0.0, baseline=0.0, tracking_em=0.0):
        """SVG path data for `text` at `size` px, baseline at y=baseline. Returns (d, width)."""
        buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
        hb.shape(self.hbfont, buf, {'kern': True, 'liga': False})
        s = size / self.upm
        pen = SVGPathPen(self.gs)
        x = 0
        n = len(buf.glyph_infos)
        for i, (info, pos) in enumerate(zip(buf.glyph_infos, buf.glyph_positions)):
            name = self.order[info.codepoint]
            tp = TransformPen(pen, (s, 0, 0, -s, x0 + (x + pos.x_offset) * s, baseline - pos.y_offset * s))
            self.gs[name].draw(tp)
            x += pos.x_advance + (tracking_em * self.upm if i < n - 1 else 0)
        return pen.getCommands(), x * s

GROT = Face('schibsted-grotesk-latin-800-normal.woff2')
MONO = Face('jetbrains-mono-latin-400-normal.woff2')

P = dict(petrol='#10282E', aqua='#A8F5EE', aquam='#7FB5B0', plum='#3B1222', lilac='#E4B8F5', plumm='#C9A3D6',
         lilaci='#6E3550', aquai='#2F5A5F', cream='#FDF6D8', olive='#3A3200', olivem='#6B6230')

def num(v): return f'{v:.2f}'.rstrip('0').rstrip('.')

def write(name, w, h, body, title):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {num(w)} {num(h)}" width="{num(w)}" height="{num(h)}" role="img" aria-label="{title}">'
           f'<title>{title}</title>{body}</svg>\n')
    open(os.path.join(OUT, name + '.svg'), 'w').write(svg)
    SHEET.append((name, w, h))

SHEET = []
TRACK = -0.05

def wordmark(name, text, color, size=100):
    pad = size * 0.06
    d, tw = GROT.path(text, size, pad, pad + size * GROT.cap / GROT.upm, TRACK)
    # height covers cap height plus descenders (p in Calliope)
    h = pad * 2 + size * GROT.cap / GROT.upm + size * 0.22
    write(name, tw + pad * 2, h, f'<path fill="{color}" d="{d}"/>', text)

def lockup(name, text, tile_bg, icon, text_color, sub=None, sub_color=None, tile=120, stacked=False):
    """Tile + wordmark. Text cap height = 0.6 of the tile, centred on it. `sub` is a mono line under the name."""
    size = tile * 0.6 / (GROT.cap / GROT.upm)
    capH = size * GROT.cap / GROT.upm
    gap = tile * 0.22
    r = tile * 0.29
    tile_svg = (f'<rect width="{num(tile)}" height="{num(tile)}" rx="{num(r)}" fill="{tile_bg}"/>'
                f'<g transform="translate({num(tile*0.15)} {num(tile*0.15)}) scale({num(tile*0.7/120)})">{icon}</g>')
    x = tile + gap
    if sub:
        size = tile * 0.5 / (GROT.cap / GROT.upm)
        msize = tile * 0.19
        base = tile * 0.56
        d, tw = GROT.path(text, size, x, base, TRACK)
        md, mw = MONO.path(sub, msize, x + size * 0.02, tile * 0.92)
        body = tile_svg + f'<path fill="{text_color}" d="{d}"/><path fill="{sub_color}" d="{md}"/>'
        w = x + max(tw, mw) + 4
    else:
        base = tile * 0.5 + capH * 0.5
        d, tw = GROT.path(text, size, x, base, TRACK)
        body = tile_svg + f'<path fill="{text_color}" d="{d}"/>'
        w = x + tw + 4
    write(name, w, tile, body, text + (f'. {sub}' if sub else ''))

# ---- wordmarks only ----
for col in ('petrol', 'cream', 'aqua'):
    wordmark(f'calliope-wordmark-{col}', 'Calliope', P[col])
for col in ('plum', 'lilac', 'cream'):
    wordmark(f'sirenradar-wordmark-{col}', 'Sirenradar', P[col])
for col in ('olive', 'cream'):
    wordmark(f'unsiren-wordmark-{col}', 'Unsiren', P[col])

# ---- lockups: for-light = on white / light backgrounds, for-dark = on dark backgrounds ----
lockup('calliope-lockup-for-light', 'Calliope', P['petrol'], cheer(P['aqua']), P['petrol'])
lockup('calliope-lockup-for-dark', 'Calliope', P['aqua'], cheer(P['petrol']), P['cream'])
lockup('calliope-lockup-tagline-for-light', 'Calliope', P['petrol'], cheer(P['aqua']), P['petrol'], 'Louder than the Sirens.', P['aquai'])
lockup('calliope-lockup-tagline-for-dark', 'Calliope', P['aqua'], cheer(P['petrol']), P['cream'], 'Louder than the Sirens.', P['aquam'])

lockup('sirenradar-lockup-for-light', 'Sirenradar', P['plum'], eye(P['lilac']), P['plum'])
lockup('sirenradar-lockup-for-dark', 'Sirenradar', P['lilac'], eye(P['plum']), P['cream'])
lockup('sirenradar-lockup-endorsed-for-light', 'Sirenradar', P['plum'], eye(P['lilac']), P['plum'], 'by Calliope', P['lilaci'])
lockup('sirenradar-lockup-endorsed-for-dark', 'Sirenradar', P['lilac'], eye(P['plum']), P['cream'], 'by Calliope', P['plumm'])

lockup('unsiren-lockup-for-light', 'Unsiren', P['olive'], wave(P['cream']), P['olive'])
lockup('unsiren-lockup-for-dark', 'Unsiren', P['cream'], wave(P['olive']), P['cream'])
lockup('unsiren-lockup-endorsed-for-light', 'Unsiren', P['olive'], wave(P['cream']), P['olive'], 'concept · by Calliope', P['olivem'])
lockup('unsiren-lockup-endorsed-for-dark', 'Unsiren', P['cream'], wave(P['olive']), P['cream'], 'concept · by Calliope', '#E2D6A4')

# ---- Orfeo apps (the family, as it appears on Calliope pages) ----
for col in ('petrol', 'aqua', 'cream'):
    wordmark(f'orfeo-apps-wordmark-{col}', 'Orfeo apps', P[col])
lockup('orfeo-apps-lockup-for-light', 'Orfeo apps', P['petrol'], between(P['aqua']), P['petrol'])
lockup('orfeo-apps-lockup-for-dark', 'Orfeo apps', P['aqua'], between(P['petrol']), P['cream'])
lockup('orfeo-apps-lockup-endorsed-for-light', 'Orfeo apps', P['petrol'], between(P['aqua']), P['petrol'], 'by Calliope', P['aquai'])
lockup('orfeo-apps-lockup-endorsed-for-dark', 'Orfeo apps', P['aqua'], between(P['petrol']), P['cream'], 'by Calliope', P['aquam'])

# ---- "An Orfeo app · by Calliope" badge, optional, for each app's own README or footer ----
def badge(name, bg, stroke, icon_c, c1, c2):
    h, pad, isz, fs = 40, 12, 26, 15
    d1, w1 = MONO.path('An Orfeo app', fs, pad + isz + 9, h / 2 + fs * 0.36)
    d2, w2 = MONO.path(' · by Calliope', fs, pad + isz + 9 + w1, h / 2 + fs * 0.36)
    w = pad + isz + 9 + w1 + w2 + pad + 4
    fill = f'fill="{bg}"' if bg else 'fill="none"'
    st = f' stroke="{stroke}" stroke-width="1.5"' if stroke else ''
    inset = 0.75 if stroke else 0
    body = (f'<rect x="{inset}" y="{inset}" width="{num(w - 2*inset)}" height="{num(h - 2*inset)}" rx="{num(h/2 - inset)}" {fill}{st}/>'
            f'<g transform="translate({pad} {(h - isz)/2}) scale({num(isz/120)})">{between(icon_c)}</g>'
            f'<path fill="{c1}" d="{d1}"/><path fill="{c2}" d="{d2}"/>')
    write(name, w, h, body, 'An Orfeo app, by Calliope')

badge('badge-orfeo-app-petrol', P['petrol'], None, P['aqua'], P['cream'], P['aquam'])
badge('badge-orfeo-app-aqua', P['aqua'], None, P['petrol'], P['petrol'], P['aquai'])
badge('badge-orfeo-app-outline-for-light', None, P['petrol'], P['petrol'], P['petrol'], P['aquai'])
badge('badge-orfeo-app-outline-for-dark', None, P['cream'], P['cream'], P['cream'], P['aquam'])

# ---- contact sheet + per-file PNG pages ----
def bg_for(name):
    if 'for-dark' in name: return '#0D1117'          # GitHub dark
    if 'for-light' in name: return '#FFFFFF'         # GitHub light
    if name.endswith(('-cream', '-aqua', '-lilac')) and not name.startswith('badge'): return P['petrol']
    return '#FFFFFF'

rows = ''.join(f'<div style="background:{bg_for(n)};padding:28px 32px;border-radius:16px;display:flex;align-items:center;justify-content:space-between;gap:20px">'
               f'<img src="../wordmarks/{n}.svg" style="height:{40 if n.startswith("badge") else 60 if "lockup" in n else 56}px"><span style="font:12px JetBrains Mono,monospace;color:#7FB5B0">{n}.svg</span></div>'
               for n, w, h in SHEET)
open(os.path.join(HERE, 'wordmarks-sheet.html'), 'w').write(
    f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="./fonts/fonts.css">'
    f'<style>body{{margin:0;background:#E9E4CF}}</style></head><body><div style="width:1100px;padding:32px;display:grid;gap:12px;box-sizing:border-box">{rows}</div></body></html>')

# transparent PNG export pages, one per SVG, at 4x the SVG size (tile 120 -> 480 px tall)
for n, w, h in SHEET:
    open(os.path.join(HERE, f'wm-{n}.html'), 'w').write(
        f'<!doctype html><html><head><style>html,body{{margin:0;background:transparent}}</style></head>'
        f'<body><img src="../wordmarks/{n}.svg" style="display:block;width:{num(w)}px;height:{num(h)}px"></body></html>')
json.dump([dict(src=f'src/wm-{n}.html', png=f'wordmarks/png/{n}.png', width=round(w), height=round(h), scale=4, transparent=True)
           for n, w, h in SHEET], open(os.path.join(HERE, 'manifest-wordmarks.json'), 'w'), indent=1)
print(len(SHEET), 'svgs')
