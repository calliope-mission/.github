FONTS='<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;800&amp;family=JetBrains+Mono:wght@400;700&amp;display=swap" rel="stylesheet">'
def page(title, link, css, body):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>
body{{margin:0}}
{link}
{css}
</style>
</helmet>
{body}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1280,"height":800}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''
def svg(size, inner, extra=''):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 120 120" aria-hidden="true"{extra}>{inner}</svg>'
def lyre(c, w=10, s=5, r=11):
    return (f'<g fill="none" stroke="{c}" stroke-linecap="round" stroke-linejoin="round"><path d="M38 66H82M38 66C20 56 14 34 22 10M82 66C100 56 106 34 98 10M18 22H102M60 66V86M60 86L44 110M60 86L76 110" stroke-width="{w}"></path>'
            f'<path d="M44 22V60M76 22V60" stroke-width="{s}"></path></g><circle cx="60" cy="42" r="{r}" fill="{c}"></circle>')
def walk(c,w=12):
    return f'<g fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"><path d="M62 42L56 74M56 74L40 104M56 74L76 102M60 50L84 62M60 50L38 66"></path></g><circle cx="66" cy="22" r="13" fill="{c}"></circle>'
def eye(c):
    return f'<path d="M12 60Q60 14 108 60Q60 106 12 60Z" fill="none" stroke="{c}" stroke-width="12" stroke-linejoin="round"></path><circle cx="60" cy="60" r="14" fill="{c}"></circle>'
def wave(c):
    return f'<g fill="none" stroke="{c}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"><path d="M10 60C20 30 32 30 42 60S64 90 74 60H110"></path></g>'
def crew(c):
    return f'<g fill="none" stroke="{c}" stroke-width="12" stroke-linecap="round"><path d="M28 56V100M60 56V100M92 56V100M12 74H108"></path></g><g fill="{c}"><circle cx="28" cy="34" r="11"></circle><circle cx="60" cy="34" r="11"></circle><circle cx="92" cy="34" r="11"></circle></g>'
def bubble(c, inner):
    return f'<path d="M18 20H102V80H58L36 102V80H18Z" fill="none" stroke="{c}" stroke-width="10" stroke-linejoin="round"></path>{inner}'
def laiive(c):
    return bubble(c, f'<circle cx="52" cy="62" r="9" fill="{c}"></circle><path d="M60 62V36L76 42" fill="none" stroke="{c}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"></path>')
def vaivia(c):
    return bubble(c, f'<path d="M34 66C44 52 54 64 64 52S78 40 84 38" fill="none" stroke="{c}" stroke-width="7" stroke-linecap="round"></path><circle cx="34" cy="66" r="6" fill="{c}"></circle><circle cx="86" cy="37" r="7" fill="{c}"></circle>')
def territory(c):
    return f'<g fill="none" stroke="{c}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"><path d="M14 100V64L36 44L58 64V100M58 100V54L82 32L106 54V100M8 100H112"></path></g><rect x="76" y="70" width="12" height="16" rx="2" fill="{c}"></rect><rect x="30" y="76" width="12" height="14" rx="2" fill="{c}"></rect>'
def mappin(c):
    return f'<path d="M60 108C60 108 26 72 26 46A34 34 0 0 1 94 46C94 72 60 108 60 108Z" fill="none" stroke="{c}" stroke-width="10" stroke-linejoin="round"></path><circle cx="60" cy="46" r="11" fill="{c}"></circle>'
def shop(c):
    return f'<g fill="none" stroke="{c}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"><path d="M14 44L24 20H96L106 44M14 44Q25 60 37 44Q48 60 60 44Q71 60 83 44Q94 60 106 44M24 58V102H96V58M50 102V76H70V102"></path></g>'
def radar(c):
    return (f'<g fill="none" stroke="{c}" stroke-width="10" stroke-linecap="round"><circle cx="60" cy="60" r="46"></circle><path d="M60 60L92 28M60 34A26 26 0 0 1 86 60"></path></g>'
            f'<circle cx="60" cy="60" r="8" fill="{c}"></circle><circle cx="36" cy="80" r="8" fill="{c}"></circle>')
def between(c):
    return (f'<g fill="none" stroke="{c}" stroke-linecap="round" stroke-linejoin="round"><path d="M22 58V86M22 86L14 104M22 86L30 104M98 56V104M22 62H98" stroke-width="9"></path>'
            f'<path d="M60 46V78M60 78L48 104M60 78L72 104" stroke-width="10"></path></g>'
            f'<circle cx="22" cy="42" r="9" fill="{c}"></circle><circle cx="60" cy="28" r="11" fill="{c}"></circle><circle cx="98" cy="42" r="15" fill="{c}"></circle>')
def rooted(c):
    return (f'<g fill="none" stroke="{c}" stroke-linecap="round" stroke-linejoin="round"><path d="M60 56L32 30M60 56L88 30M60 50V84" stroke-width="11"></path>'
            f'<path d="M14 84H106" stroke-width="8"></path><path d="M60 84V110M60 90L44 108M60 90L76 108" stroke-width="6"></path></g><circle cx="60" cy="20" r="12" fill="{c}"></circle>')
def horizon(c):
    return (f'<g fill="none" stroke="{c}" stroke-linecap="round" stroke-linejoin="round"><path d="M8 104Q60 76 112 104" stroke-width="9"></path>'
            f'<path d="M58 60L30 44M58 60L86 44M58 52V76M58 76L46 90M58 76L70 90" stroke-width="10"></path></g><circle cx="58" cy="36" r="11" fill="{c}"></circle><circle cx="96" cy="22" r="10" fill="{c}"></circle>')
def cheer(c, w=12, r=13):
    return (f'<g fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"><path d="M60 64L28 36M60 64L92 36M60 64V82M60 82L42 106M60 82L78 106"></path></g>'
            f'<circle cx="60" cy="24" r="{r}" fill="{c}"></circle>')
