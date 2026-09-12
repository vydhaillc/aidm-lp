#!/usr/bin/env python3
"""Meta ad creatives, v2 — price-forward per Dr. Suman's Sep 9 feedback.

One HTML template rendered with Playwright at 1080x1350 (4:5). The offer
price sits in a red badge as the first thing the eye lands on; copy is cut
to a headline, one tagline and the hours line.
"""
import base64, os, sys
import html as html_mod
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
PROJ = os.path.abspath(os.path.join(ROOT, '..'))
OUT = os.path.join(ROOT, 'sheet-assets', 'creatives', 'v2')
os.makedirs(OUT, exist_ok=True)

def b64(path):
    ext = path.rsplit('.', 1)[-1].lower()
    mime = {'jpg': 'image/jpeg', 'jpeg': 'image/jpeg', 'png': 'image/png'}[ext]
    with open(path, 'rb') as f:
        return f'data:{mime};base64,' + base64.b64encode(f.read()).decode()

LOGO = b64(os.path.join(PROJ, 'vydhai/aidm-creative/assets/logo_horizontal_white.png'))
MARK = b64(os.path.join(ROOT, 'aidm-lp-assets/brand-watermark.png'))

SPECS = {
    'a1': dict(
        layout='a1',
        photo=os.path.join(PROJ, 'vydhai/aidm-creative/assets/a1_front_desk.jpg'),
        pos='50% 60%',
        circles=[os.path.join(PROJ, 'vydhai/aidm-creative/assets/a1_exterior.jpg'),
                 os.path.join(PROJ, 'vydhai/aidm-creative/assets/a1_waiting.jpg'),
                 os.path.join(PROJ, 'vydhai/aidm-creative/assets/a1_treatment.jpg')],
        head='Your Family&rsquo;s New<br>Dental Home.',
    ),
    'a2': dict(
        layout='a2',
        photo=os.path.join(PROJ, 'vydhai/aidm-creative/assets/a2_openbay.jpg'),
        pos='50% 55%',
        circles=[os.path.join(PROJ, 'vydhai/aidm-creative/assets/a1_exterior.jpg'), os.path.join(PROJ, 'vydhai/aidm-creative/assets/a1_front_desk.jpg'), os.path.join(PROJ, 'vydhai/aidm-creative/assets/a2_lounge.jpg'), os.path.join(PROJ, 'vydhai/aidm-creative/assets/a1_waiting.jpg')],
        head='Comprehensive Dental Care.<br>One Modern Location.',
    ),
    'b1': dict(
        photo=os.path.join(ROOT, 'aidm-lp-assets/staff/resident-patient.jpg'),
        pos='50% 35%', badge_style='--s:420px;top:396px;right:76px', shift=36,
        badge='circle', price='$100', badge_top='NEW PATIENT', badge_bottom='SPECIAL',
        badge_note='Exam + X-rays',
        script='Now Accepting', caps='New Patients',
        tagline='',
    ),
    'b2': dict(
        photo=os.path.join(PROJ, 'vydhai/aidm-creative/assets/clinician_patient_screen_smiling.jpg'),
        pos='42% 40%', badge_style='--s:420px;top:400px;right:76px', shift=36,
        badge='circle', price='$2,950', badge_top='BRACES', badge_bottom='SPECIAL',
        badge_note='First 100 patients',
        script='Comprehensive', caps='Braces Treatment',
        tagline='',
    ),
    'b3': dict(
        photo=os.path.join(PROJ, 'vydhai/aidm-creative/assets/b3_xray_screen_behind.jpg'),
        pos='50% 40%', badge_style='--s:420px;top:400px;right:76px', shift=36,
        badge='circle', price='$3,900', badge_top='INVISALIGN', badge_bottom='SPECIAL',
        badge_note='Free consultation',
        script='Invisalign', caps='Clear Aligners',
        tagline='',
    ),
    'b4': dict(
        photo=os.path.join(PROJ, 'vydhai/aidm-creative/assets/b4_two_clinicians_wide.jpg'),
        pos='50% 40%', badge_style='--s:420px;top:400px;right:76px', shift=36,
        badge='circle', price='$2,500', badge_top='EARLY ORTHO', badge_bottom='SPECIAL',
        badge_note='Free consultation',
        script='Does your child', caps='Need Braces Yet?',
        tagline='',
    ),
    'b5': dict(
        photo=os.path.join(PROJ, 'vydhai/aidm-creative/assets/b5_consult_male_patient.jpg'),
        pos='70% 40%', badge_style='--s:400px;top:446px;right:70px', shift=50,
        badge='circle', pre='FROM', price='$3,750', badge_top='IMPLANT + CROWN', badge_bottom='SPECIAL',
        badge_note='Free consultation',
        script='Single Implant', caps='& Ceramic Crown',
        tagline='',
    ),
    'b6': dict(
        photo=os.path.join(PROJ, 'vydhai/aidm-creative/assets/b6_scanner.jpg'),
        pos='50% 40%', badge_style='--s:420px;top:400px;right:76px', shift=36,
        badge='circle', pre='FROM', price='$18,000', badge_top='PER ARCH', badge_bottom='SPECIAL',
        badge_note='Free consultation',
        script='A full smile.', caps='Fixed Full-Arch Teeth',
        tagline='',
    ),
    'b7': dict(
        photo=os.path.join(PROJ, 'vydhai/aidm-creative/assets/b7_two_clinicians_close.jpg'),
        pos='50% 30%', badge_style='--s:420px;top:400px;right:76px', shift=36,
        badge='circle', pre='FROM', price='$9,500', badge_top='PER ARCH', badge_bottom='SPECIAL',
        badge_note='Free consultation',
        script='Snap-In', caps='Dentures',
        tagline='',
    ),
    'c1': dict(
        photo=os.path.join(ROOT, 'aidm-lp-assets/staff/resident-patient.jpg'),
        pos='50% 35%', badge_style='--s:420px;top:396px;right:76px', shift=36,
        badge='circle', price='$100', badge_top='PACIENTE NUEVO', badge_bottom='PROMOCI&Oacute;N',
        badge_note='Examen + radiografías',
        script='Ahora aceptamos', caps='Pacientes Nuevos',
        tagline='', note='Hablamos español', fine='*Aplican ciertas restricciones.',
        hours='Lun&ndash;S&aacute;b 7am&ndash;7pm &nbsp;&middot;&nbsp; Estacionamiento gratis &nbsp;&middot;&nbsp; Mueller, Austin',
    ),
    'c2': dict(
        layout='a1',
        photo=os.path.join(PROJ, 'vydhai/aidm-creative/assets/a1_front_desk.jpg'),
        pos='50% 60%',
        circles=[os.path.join(PROJ, 'vydhai/aidm-creative/assets/a1_exterior.jpg'), os.path.join(PROJ, 'vydhai/aidm-creative/assets/a1_waiting.jpg'), os.path.join(PROJ, 'vydhai/aidm-creative/assets/a1_treatment.jpg')],
        head='El nuevo hogar dental<br>de tu familia.', head_size=86, note='Hablamos español',
        hours='Lun&ndash;S&aacute;b 7am&ndash;7pm &nbsp;&middot;&nbsp; Estacionamiento gratis &nbsp;&middot;&nbsp; Mueller, Austin',
    ),
}

CSS = '''
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Montserrat:wght@500;600;700;800&family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;overflow:hidden;background:#0b1727;font-family:'Cormorant Garamond',serif;color:#fff;position:relative}
.photo{position:absolute;inset:0 0 auto 0;height:800px;width:1080px;object-fit:cover}
.wave{position:absolute;left:0;top:560px;width:1080px;height:790px}
.mark{position:absolute;right:-140px;bottom:-120px;width:720px;opacity:.10}
.logo{position:absolute;left:50%;top:calc(796px + var(--y));transform:translateX(-50%);width:380px}
.dia{position:absolute;left:50%;transform:translateX(-50%);display:flex;align-items:center;gap:10px;color:#6fc3ee;font-size:16px}
.dia i{display:block;width:120px;height:1px;background:linear-gradient(90deg,transparent,#6fc3ee)}
.dia i.r{background:linear-gradient(90deg,#6fc3ee,transparent)}
.script{position:absolute;left:0;right:0;top:calc(922px + var(--y));text-align:center;font-family:'Great Vibes',cursive;font-size:118px;line-height:1;color:#7fcbf3;text-shadow:0 4px 30px rgba(0,0,0,.45)}
.caps{position:absolute;left:0;right:0;top:calc(1036px + var(--y));text-align:center;font-weight:600;font-size:84px;line-height:1;letter-spacing:.06em;text-transform:uppercase}
.rule{position:absolute;left:50%;top:1150px;transform:translateX(-50%);width:300px;height:2px;background:linear-gradient(90deg,transparent,#3fa9e6,transparent)}
.tag{position:absolute;left:0;right:0;top:1170px;text-align:center;font-style:italic;font-weight:500;font-size:40px;color:#9fd8f7}
.note{position:absolute;left:0;right:0;top:calc(1168px + var(--y));text-align:center;font-style:italic;font-weight:500;font-size:34px;color:#9fd8f7}
.a1 .note{top:1214px;font-size:32px}
.badge .p sup{font-size:.34em;vertical-align:baseline;position:relative;top:-1.3em;margin-left:.03em;font-weight:800}
.fine{position:absolute;left:0;right:0;top:1310px;text-align:center;font-family:Montserrat,sans-serif;font-weight:500;font-size:15px;letter-spacing:.06em;color:#6f8aa6}
.hours{position:absolute;left:0;right:0;top:1268px;text-align:center;font-family:Montserrat,sans-serif;font-weight:600;font-size:19px;letter-spacing:.24em;color:#8fb6d3;text-transform:uppercase}


/* ---- A1 brand layout ---- */
.a1 .photo{height:620px}
.a1 .wave{top:440px;height:910px}
.circ{position:absolute;top:520px;width:300px;height:300px;border-radius:50%;overflow:hidden;border:6px solid #5fc0f0;box-shadow:0 16px 36px rgba(0,0,0,.55)}
.circ img{width:100%;height:100%;object-fit:cover}
.a1 .logo{top:896px;width:360px}
.head{position:absolute;left:0;right:0;top:976px;text-align:center;font-family:'Source Serif 4',serif;font-weight:700;font-size:92px;line-height:1.1;color:#fff;letter-spacing:-.005em}
.a1 .rule{top:1196px;width:520px}
.a1 .dia{top:1216px}


/* ---- A2 brand layout (navy top, photo bottom) ---- */
.a2 .photo{top:auto;bottom:0;height:820px}
.a2 .wave{top:0;height:800px}
.a2 .mark{right:auto;left:-260px;top:-200px;bottom:auto;width:760px;opacity:.10}
.a2 .logo{top:70px;width:400px}
.a2 .head{top:214px;font-size:84px;font-weight:600;letter-spacing:.004em;line-height:1.16}
.a2 .rule{top:452px;width:520px}
.a2 .dia{top:472px}
.a2 .circ{border-width:5px}

/* ---- price badge ---- */
.badge{--s:320px;position:absolute;right:48px;top:500px;width:var(--s);height:var(--s);transform:rotate(-8deg);filter:drop-shadow(0 18px 34px rgba(0,0,0,.55))}
.badge svg{position:absolute;inset:0;width:100%;height:100%}
.badge .txt{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:Montserrat,sans-serif;text-align:center;line-height:1}
.badge .t{font-weight:700;font-size:calc(var(--s) * .08);letter-spacing:.2em;color:#ffe3e3}
.badge .p{font-weight:800;font-size:calc(var(--s) * .31);letter-spacing:-.03em;margin:6px 0 2px;color:#fff}
.badge .b{font-weight:800;font-size:calc(var(--s) * .105);letter-spacing:.28em;color:#fff}
.badge .n{margin-top:calc(var(--s) * .04);font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:500;font-size:calc(var(--s) * .085);color:#ffd9d9;letter-spacing:.02em}
.circle .txt{padding-bottom:calc(var(--s) * .30)}
.circle .p{margin:0 0 calc(var(--s) * .03)}
.circle .t{color:#fff}
.circle .n{margin-top:calc(var(--s) * .02)}
.circle.long .txt{padding-bottom:calc(var(--s) * .24)}
.badge .pre{font-weight:700;font-size:calc(var(--s) * .055);letter-spacing:.3em;color:#ffd9d9;margin-bottom:calc(var(--s) * -.01)}
.circle.xlong .p{font-size:calc(var(--s) * .18);letter-spacing:-.04em}
.circle.widelabel .t{font-size:calc(var(--s) * .062);letter-spacing:.16em}
.circle.long .p{font-size:calc(var(--s) * .23);letter-spacing:-.04em}
.circle.long .n{margin-top:calc(var(--s) * .01)}
.rosette .p{font-size:calc(var(--s) * .28)}
'''

def circle_svg(label):
    # Red seal with a ribbon sash wrapped across its lower third; the tails sit
    # behind the disc and the band in front, so it reads as wrapped around it.
    return f'''<svg viewBox="0 0 340 340" style="overflow:visible">
<defs><radialGradient id="g" cx="35%" cy="30%" r="80%"><stop offset="0" stop-color="#e5203f"/><stop offset=".6" stop-color="#c8102e"/><stop offset="1" stop-color="#8a0a20"/></radialGradient>
<linearGradient id="rb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3fc9f5"/><stop offset="1" stop-color="#2bbff0"/></linearGradient></defs>
<polygon points="-44,246 46,246 46,310 -44,310 -22,278" fill="#1a9ccb"/>
<polygon points="384,246 294,246 294,310 384,310 362,278" fill="#1a9ccb"/>
<circle cx="170" cy="170" r="168" fill="url(#g)"/>
<circle cx="170" cy="170" r="150" fill="none" stroke="#fff" stroke-opacity=".55" stroke-width="2" stroke-dasharray="4 6"/>
<polygon points="30,246 46,232 46,246" fill="#0f6f93"/>
<polygon points="310,246 294,232 294,246" fill="#0f6f93"/>
<rect x="30" y="232" width="280" height="64" fill="url(#rb)"/>
<rect x="30" y="232" width="280" height="64" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="1.5"/>
<text x="170" y="278" text-anchor="middle" font-family="'Cormorant Garamond',serif" font-weight="700" font-size="{50 if len(html_mod.unescape(label)) <= 7 else 42}" letter-spacing="{5 if len(html_mod.unescape(label)) <= 7 else 3}" fill="#0b1727">{label}</text>
</svg>'''

def rosette_svg():
    import math
    pts = []
    n = 36
    for i in range(n * 2):
        a = math.pi * 2 * i / (n * 2)
        r = 168 if i % 2 == 0 else 154
        pts.append(f'{170 + r * math.cos(a):.1f},{170 + r * math.sin(a):.1f}')
    poly = ' '.join(pts)
    return f'''<svg viewBox="0 0 340 340">
<defs><radialGradient id="g" cx="35%" cy="30%" r="80%"><stop offset="0" stop-color="#e5203f"/><stop offset=".6" stop-color="#c8102e"/><stop offset="1" stop-color="#8a0a20"/></radialGradient></defs>
<polygon points="{poly}" fill="url(#g)"/>
<circle cx="170" cy="170" r="140" fill="none" stroke="#fff" stroke-opacity=".6" stroke-width="2"/>
<circle cx="170" cy="170" r="134" fill="none" stroke="#fff" stroke-opacity=".25" stroke-width="1"/>
</svg>'''

WAVE = '''<svg class="wave" viewBox="0 0 1080 790" preserveAspectRatio="none">
<defs><linearGradient id="w" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#101f33"/><stop offset="1" stop-color="#070f1b"/></linearGradient></defs>
<path d="M0,120 C260,10 520,250 800,150 C930,105 1010,60 1080,30 L1080,790 L0,790 Z" fill="url(#w)"/>
<path d="M0,120 C260,10 520,250 800,150 C930,105 1010,60 1080,30" fill="none" stroke="#5fc0f0" stroke-width="5" stroke-opacity=".85"/>
</svg>'''


def html_a1(s):
    circ = ''.join(f'<div class="circ" style="left:{x}px"><img src="{b64(p)}"></div>'
                   for x, p in zip((60, 390, 720), s['circles']))
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="a1" style="--y:0px">
<img class="photo" src="{b64(s['photo'])}" style="object-position:{s['pos']}">
{WAVE.replace('viewBox="0 0 1080 790"', 'viewBox="0 0 1080 790"')}
<img class="mark" src="{MARK}">
{circ}
<img class="logo" src="{LOGO}">
<div class="head" style="font-size:{s.get('head_size', 92)}px">{s['head']}</div>
<div class="rule"></div>
{'<div class="note">' + s['note'] + '</div>' if s.get('note') else '<div class="dia"><i></i>&#9670;<i class="r"></i></div>'}
<div class="hours">{s.get('hours', 'Mon&ndash;Sat 7am&ndash;7pm &nbsp;&middot;&nbsp; Free parking &nbsp;&middot;&nbsp; Mueller, Austin')}</div>
</body></html>'''


WAVE_A2 = '''<svg class="wave" viewBox="0 0 1080 800" preserveAspectRatio="none">
<defs><linearGradient id="w2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#070f1b"/><stop offset="1" stop-color="#101f33"/></linearGradient></defs>
<path d="M0,0 L1080,0 L1080,640 C900,600 720,700 520,720 C320,740 150,770 0,760 Z" fill="url(#w2)"/>
<path d="M1080,640 C900,600 720,700 520,720 C320,740 150,770 0,760" fill="none" stroke="#5fc0f0" stroke-width="5" stroke-opacity=".85"/>
</svg>'''

def html_a2(s):
    # Staggered, overlapping, shrinking left to right and rising slightly, as
    # in the original; earlier circles sit in front of later ones.
    geo = [(224, 640, 290), (447, 632, 253), (670, 618, 223), (879, 604, 194)]
    circ = ''.join(f'<div class="circ" style="left:{cx - d // 2}px;top:{cy - d // 2}px;width:{d}px;height:{d}px;z-index:{9 - i}"><img src="{b64(p)}"></div>'
                   for i, ((cx, cy, d), p) in enumerate(zip(geo, s['circles'])))
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="a2" style="--y:0px">
<img class="photo" src="{b64(s['photo'])}" style="object-position:{s['pos']}">
{WAVE_A2}
<img class="mark" src="{MARK}">
<img class="logo" src="{LOGO}">
<div class="head">{s['head']}</div>
<div class="rule"></div>
<div class="dia"><i></i>&#9670;<i class="r"></i></div>
{circ}
</body></html>'''

def html(s):
    if s.get('layout') == 'a1':
        return html_a1(s)
    if s.get('layout') == 'a2':
        return html_a2(s)
    badge_svg = circle_svg(s['badge_bottom']) if s['badge'] == 'circle' else rosette_svg()
    tag = f'<div class="rule"></div><div class="tag">{s["tagline"]}</div>' if s['tagline'] else ''
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body style="--y:{s.get('shift',0)}px">
<img class="photo" src="{b64(s['photo'])}" style="object-position:{s['pos']}">
{WAVE}
<img class="mark" src="{MARK}">
<img class="logo" src="{LOGO}">
<div class="dia" style="top:calc(890px + var(--y))"><i></i>&#9670;<i class="r"></i></div>
<div class="script">{s['script']}</div>
<div class="caps" style="font-size:{84 if len(s['caps']) <= 16 else 66}px">{s['caps']}</div>
{tag}
{'<div class="note">' + s['note'] + '</div>' if s.get('note') else ''}
<div class="hours">{s.get('hours', 'Mon&ndash;Sat 7am&ndash;7pm &nbsp;&middot;&nbsp; Free parking &nbsp;&middot;&nbsp; Mueller, Austin')}</div>
<div class="fine">{s.get('fine', '*Certain restrictions apply.')}</div>
<div class="badge {s['badge']}{' long' if len(s['price']) > 4 else ''}{' xlong' if len(s['price']) > 6 else ''}{' widelabel' if len(s['badge_top']) > 12 else ''}" style="{s.get('badge_style','')}">{badge_svg}<div class="txt">
{'' if s['badge'] == 'circle' else '<div class="t">' + s['badge_top'] + '</div>'}{'<div class="pre">' + s['pre'] + '</div>' if s.get('pre') else ''}<div class="p">{s['price']}<sup>*</sup></div>{'<div class="t">' + s['badge_top'] + '</div>' if s['badge'] == 'circle' else '<div class="b">' + s['badge_bottom'] + '</div>'}<div class="n">{s['badge_note']}</div>
</div></div>
</body></html>'''

def main(ids):
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=1)
        for i in ids:
            pg.set_content(html(SPECS[i]))
            pg.wait_for_timeout(1500)  # web fonts
            pg.evaluate('document.fonts.ready')
            out = os.path.join(OUT, f'{i}.jpg')
            pg.screenshot(path=out, type='jpeg', quality=92)
            print('wrote', out)
        br.close()

if __name__ == '__main__':
    main(sys.argv[1:] or list(SPECS))
