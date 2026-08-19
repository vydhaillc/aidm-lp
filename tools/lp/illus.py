# -*- coding: utf-8 -*-
"""Generates the procedure illustrations for the AIDM landing pages.

AIDM owns no procedure artwork and the reference images on other dental sites
are licensed medical illustration, so these are drawn for AIDM. Everything is
composed from the same primitives — one gum ridge, three tooth glyphs, one
steel gradient — so a root canal panel and an implant panel read as the same
hand rather than two stock pickups.

    python3 tools/lp/illus.py        # writes assets/illus/*.svg

Canvas is 640x300 with the gum line at y=196, which matches the aspect of the
card band it sits in.
"""
import io, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', 'illus')
GUM = 196

DEFS = '''<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#f5f9fc"/><stop offset="1" stop-color="#e0eaf2"/></linearGradient>
  <linearGradient id="gum" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#ef9aa4"/><stop offset="1" stop-color="#cd6875"/></linearGradient>
  <linearGradient id="bone" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#f7e9d9"/><stop offset="1" stop-color="#e5d0b6"/></linearGradient>
  <linearGradient id="ena" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#ffffff"/><stop offset=".58" stop-color="#f6f9f8"/>
    <stop offset="1" stop-color="#dfe6e3"/></linearGradient>
  <linearGradient id="dent" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#f6e9d3"/><stop offset="1" stop-color="#e2ceac"/></linearGradient>
  <linearGradient id="steel" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#a7b2c0"/><stop offset=".36" stop-color="#f1f5f9"/>
    <stop offset=".64" stop-color="#8b97a6"/><stop offset="1" stop-color="#c2cbd6"/></linearGradient>
  <linearGradient id="tita" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#8b98a6"/><stop offset=".4" stop-color="#dbe3ea"/>
    <stop offset="1" stop-color="#7d8a99"/></linearGradient>
  <linearGradient id="sky" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#2f7fb5"/><stop offset=".5" stop-color="#5cb8e9"/>
    <stop offset="1" stop-color="#2b6f9f"/></linearGradient>
  <linearGradient id="cera" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#e6efe9"/></linearGradient>
  <linearGradient id="acr" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#f2a3ad"/><stop offset="1" stop-color="#d9848f"/></linearGradient>
  <linearGradient id="alg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#bfe6fb"/><stop offset="1" stop-color="#8ccdf0"/></linearGradient>
</defs>'''

# ── tooth glyphs, drawn about (0,0) sitting on the gum line ─────────────────
MOLAR_CROWN = ("M-46 8 C-54 8 -54 -6 -54 -18 L-52 -72 C-50 -98 -34 -110 -20 -106 "
               "C-12 -104 -8 -98 0 -98 C8 -98 12 -104 20 -106 C34 -110 50 -98 52 -72 "
               "L54 -18 C54 -6 54 8 46 8 Z")
MOLAR_ROOT_L = "M-40 4 L-32 66 C-30 84 -18 84 -16 66 L-12 4 Z"
MOLAR_ROOT_R = "M40 4 L32 66 C30 84 18 84 16 66 L12 4 Z"
MOLAR_CUSP   = "M-38 -86 Q-20 -98 0 -90 Q20 -98 38 -86"

PRE_CROWN = ("M-30 8 C-38 8 -38 -6 -38 -18 L-36 -68 C-34 -92 -18 -102 0 -102 "
             "C18 -102 34 -92 36 -68 L38 -18 C38 -6 38 8 30 8 Z")
PRE_ROOT  = "M-22 4 L-14 74 C-12 92 12 92 14 74 L22 4 Z"
PRE_CUSP  = "M-24 -82 Q0 -96 24 -82"

INC_CROWN = ("M-22 8 C-28 8 -28 -4 -28 -14 L-26 -74 C-24 -94 -12 -102 0 -102 "
             "C12 -102 24 -94 26 -74 L28 -14 C28 -4 28 8 22 8 Z")
INC_ROOT  = "M-16 4 L-10 72 C-8 90 8 90 10 72 L16 4 Z"

GLYPH = {'molar': (MOLAR_CROWN, [MOLAR_ROOT_L, MOLAR_ROOT_R], MOLAR_CUSP),
         'pre':   (PRE_CROWN,   [PRE_ROOT],                   PRE_CUSP),
         'inc':   (INC_CROWN,   [INC_ROOT],                   None)}


def tooth(kind, x, y=GUM, s=1.0, rot=0, crown='url(#ena)', root='url(#dent)', extra='',
          roots=True):
    """One tooth, roots first so the gum reads as covering their necks."""
    c, rootpaths, cusp = GLYPH[kind]
    roots_ = rootpaths if roots else []
    t = 'translate(%s %s)' % (x, y)
    if s != 1.0: t += ' scale(%s)' % s
    if rot:      t += ' rotate(%s)' % rot
    out = ['<g transform="%s">' % t]
    for r in roots_:
        out.append('<path d="%s" fill="%s"/>' % (r, root))
    out.append('<path d="%s" fill="%s"/>' % (c, crown))
    if cusp:
        out.append('<path d="%s" fill="none" stroke="#dde4e3" stroke-width="3.4" '
                   'stroke-linecap="round"/>' % cusp)
    out.append(extra)
    out.append('</g>')
    return '\n'.join(out)


def ridge(socket=None, bone_y=GUM + 18, gum_y=GUM):
    """The alveolar bone with the gum ridge over it, and an optional socket."""
    s = ['<path d="M0 %d Q 160 %d 320 %d Q 480 %d 640 %d L640 300 L0 300 Z" fill="url(#bone)"/>'
         % (bone_y, bone_y - 12, bone_y - 6, bone_y, bone_y - 14),
         '<path d="M0 %d Q 150 %d 320 %d Q 500 %d 640 %d L640 300 L0 300 Z" fill="url(#gum)"/>'
         % (gum_y + 4, gum_y - 10, gum_y - 4, gum_y + 2, gum_y - 10)]
    if socket:
        x = socket
        s.append('<path d="M%d %d q-4 40 12 56 q16 12 32 -2 q16 -16 12 -54 z" fill="#a94b58" '
                 'opacity=".55"/>' % (x - 28, gum_y))
    return '\n'.join(s)


def row(spec, y=GUM):
    """spec: list of (kind, x) or (kind, x, scale)."""
    out = []
    for it in spec:
        k, x = it[0], it[1]
        s = it[2] if len(it) > 2 else 1.0
        out.append(tooth(k, x, y=y, s=s))
    return '\n'.join(out)


def svg(name, label, body):
    doc = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 300" width="640" '
           'height="300" role="img" aria-label="%s">\n%s\n<rect width="640" height="300" '
           'fill="url(#bg)"/>\n%s\n</svg>\n' % (label, DEFS, body))
    p = os.path.abspath(os.path.join(OUT, name + '.svg'))
    io.open(p, 'w', encoding='utf-8').write(doc)
    return p


# ══════════════════════════════════════════════════════════════════════════
# The panels. One per procedure; tiered offers get variants that actually
# show the difference rather than the same drawing three times.
# ══════════════════════════════════════════════════════════════════════════
ARCH = [('molar', 74), ('molar', 186), ('pre', 282), ('pre', 356), ('inc', 424),
        ('inc', 476), ('inc', 528), ('pre', 590)]


def p_root_canal():
    """A molar cross-sectioned, pulp and canals exposed, a file in the mesial canal."""
    b = [ridge()]
    b.append(row([('molar', 96), ('pre', 486), ('pre', 566), ('inc', 610)]))
    # the treated molar, cut open
    b.append('<g transform="translate(300 %d)">' % GUM)
    b.append('<path d="%s" fill="url(#dent)"/><path d="%s" fill="url(#dent)"/>'
             % (MOLAR_ROOT_L, MOLAR_ROOT_R))
    b.append('<path d="%s" fill="url(#dent)"/>' % MOLAR_CROWN)
    b.append('<path d="M-54 -18 L-52 -72 C-50 -98 -34 -110 -20 -106 C-12 -104 -8 -98 0 -98 '
             'C8 -98 12 -104 20 -106 C34 -110 50 -98 52 -72 L54 -18 C18 -8 -18 -8 -54 -18 Z" '
             'fill="url(#ena)"/>')
    # pulp chamber, then a canal down the middle of each root
    b.append('<path d="M-26 -66 Q0 -78 26 -66 L26 -40 Q26 -28 17 -22 '
             'L34 56 Q35 68 29 68 Q23 68 23 56 L9 -22 Q0 -28 -9 -22 '
             'L-23 56 Q-24 68 -30 68 Q-36 68 -35 56 L-17 -22 Q-26 -28 -26 -40 Z" fill="#e0596a"/>')
    b.append('<path d="M-26 -66 Q0 -78 26 -66" fill="none" stroke="#c33f52" stroke-width="2" opacity=".6"/>')
    b.append('<path d="%s" fill="none" stroke="#dde4e3" stroke-width="3.4" stroke-linecap="round"/>' % MOLAR_CUSP)
    b.append('</g>')
    # endodontic file, working down the mesial canal
    b.append('<g><g transform="rotate(-3 277 40)">'
             '<rect x="264" y="12" width="26" height="52" rx="7" fill="url(#sky)"/>'
             '<rect x="269" y="20" width="4" height="36" rx="2" fill="#fff" opacity=".45"/>'
             '<rect x="273" y="62" width="8" height="13" rx="2" fill="#7d8895"/></g>'
             '<path d="M275 74 L268 246" stroke="url(#steel)" stroke-width="5" stroke-linecap="round"/>'
             '<path d="M274 104 l-4 7 7 7 -7 7 7 7 -7 7 7 7 -7 7 7 7 -7 7 7 7 -7 7 7 7 -7 7 6 7" '
             'fill="none" stroke="#8f9dab" stroke-width="1.4" opacity=".8"/></g>')
    return svg('root-canal',
               'Cross-section of a molar during root canal treatment: the infected pulp is '
               'removed from the canals and the tooth is sealed', '\n'.join(b))


def p_crown():
    """A ceramic crown seating onto a prepared, root-treated tooth."""
    b = [ridge()]
    b.append(row([('molar', 96), ('pre', 486), ('pre', 566), ('inc', 610)]))
    b.append('<g transform="translate(300 %d)">' % GUM)
    b.append('<path d="%s" fill="url(#dent)"/><path d="%s" fill="url(#dent)"/>'
             % (MOLAR_ROOT_L, MOLAR_ROOT_R))
    # the prepared stump
    b.append('<path d="M-40 8 L-34 -40 Q-32 -54 -18 -56 L18 -56 Q32 -54 34 -40 L40 8 Z" fill="url(#dent)"/>')
    b.append('<path d="M-17 -22 L-24 56 Q-25 68 -31 68 Q-37 68 -36 56 L-18 -22 Z" fill="#c98a6f" opacity=".55"/>')
    b.append('<path d="M17 -22 L24 56 Q25 68 31 68 Q37 68 36 56 L18 -22 Z" fill="#c98a6f" opacity=".55"/>')
    b.append('</g>')
    # the crown, held just above it
    b.append('<g transform="translate(300 108)">'
             '<path d="M-46 6 C-54 6 -54 -8 -54 -20 L-52 -50 C-50 -76 -34 -88 -20 -84 '
             'C-12 -82 -8 -76 0 -76 C8 -76 12 -82 20 -84 C34 -88 50 -76 52 -50 L54 -20 '
             'C54 -8 54 6 46 6 Q0 16 -46 6 Z" fill="url(#cera)" stroke="#cfdcd6" stroke-width="2"/>'
             '<path d="M-38 -64 Q-20 -76 0 -68 Q20 -76 38 -64" fill="none" stroke="#dde4e3" '
             'stroke-width="3.4" stroke-linecap="round"/></g>')
    b.append('<path d="M300 130 L300 156" stroke="#4fc3f7" stroke-width="4" stroke-linecap="round" '
             'stroke-dasharray="7 7" opacity=".85"/>'
             '<path d="M292 150 L300 162 L308 150" fill="none" stroke="#4fc3f7" stroke-width="4" '
             'stroke-linecap="round" stroke-linejoin="round"/>')
    return svg('crown',
               'A ceramic crown being seated onto a prepared, root-treated molar', '\n'.join(b))


def _wisdom(name, label, mode):
    """Third molar at the back of the arch, in one of its three positions."""
    b = [ridge(socket=None)]
    b.append(row([('inc', 60), ('inc', 108), ('pre', 164), ('pre', 232), ('molar', 316), ('molar', 424)]))
    if mode == 'erupted':
        # fully through, forceps on it, lifted clear of an empty socket
        b.append('<path d="M496 %d q-4 40 12 56 q16 12 32 -2 q16 -16 12 -54 z" fill="#a94b58" '
                 'opacity=".55"/>' % GUM)
        b.append('<g transform="translate(24,-46)">')
        b.append('<g transform="rotate(14 528 150)">')
        b.append(tooth('molar', 528, y=150, s=.94))
        b.append('<path d="M516 58 q-30 16 -28 52 q1 22 8 34" stroke="url(#steel)" stroke-width="15" '
                 'stroke-linecap="round" fill="none"/>'
                 '<path d="M540 58 q30 16 28 52 q-1 22 -8 34" stroke="url(#steel)" stroke-width="15" '
                 'stroke-linecap="round" fill="none"/>')
        b.append('</g>')
        b.append('<path d="M486 56 q-22 -30 -12 -60 l-40 -58" stroke="url(#steel)" stroke-width="18" '
                 'stroke-linecap="round" fill="none"/>'
                 '<path d="M572 56 q24 -28 16 -60 l14 -62" stroke="url(#steel)" stroke-width="18" '
                 'stroke-linecap="round" fill="none"/>'
                 '<circle cx="528" cy="46" r="12" fill="#8e9aa8"/>'
                 '<circle cx="528" cy="46" r="5" fill="#e9eef3"/>')
        b.append('</g>')
    elif mode == 'impacted':
        # tilted hard against the tooth in front, the back half of the crown still
        # under the gum — drawn semi-transparent so the tooth stays readable
        b.append(tooth('molar', 534, y=GUM + 4, s=.94, rot=-38))
        b.append('<path d="M474 %d Q 540 %d 640 %d L640 300 L474 300 Z" fill="url(#gum)" '
                 'opacity=".62"/>' % (GUM - 10, GUM - 66, GUM - 40))
        b.append('<path d="M474 %d Q 540 %d 640 %d" fill="none" stroke="#b95766" stroke-width="3" '
                 'opacity=".8"/>' % (GUM - 10, GUM - 66, GUM - 40))
    else:  # bony
        # fully enclosed in bone, shown as if through an X-ray
        b.append(tooth('molar', 536, y=GUM + 42, s=.9, rot=-58))
        b.append('<path d="M466 %d Q 546 %d 640 %d L640 300 L466 300 Z" fill="url(#bone)" '
                 'opacity=".46"/>' % (GUM + 2, GUM - 34, GUM - 18))
        b.append('<path d="M466 %d Q 546 %d 640 %d L640 300 L466 300 Z" fill="url(#gum)" '
                 'opacity=".4"/>' % (GUM - 12, GUM - 46, GUM - 30))
        b.append('<path d="M466 %d Q 546 %d 640 %d" fill="none" stroke="#b95766" stroke-width="3" '
                 'opacity=".75"/>' % (GUM - 12, GUM - 46, GUM - 30))
    return svg(name, label, '\n'.join(b))


def p_braces():
    """Fixed brackets and an archwire across the upper front teeth."""
    b = [ridge()]
    b.append(row(ARCH))
    br = []
    for _, x in ARCH:
        br.append('<rect x="%d" y="%d" width="26" height="24" rx="5" fill="url(#steel)"/>'
                  '<rect x="%d" y="%d" width="26" height="7" rx="3" fill="#7f8b99" opacity=".75"/>'
                  % (x - 13, GUM - 76, x - 13, GUM - 68))
    b.append('<path d="M62 %d Q 320 %d 596 %d" fill="none" stroke="url(#steel)" stroke-width="7" '
             'stroke-linecap="round"/>' % (GUM - 64, GUM - 56, GUM - 64))
    b.append('\n'.join(br))
    b.append('<path d="M62 %d Q 320 %d 596 %d" fill="none" stroke="#e9eef3" stroke-width="2" '
             'stroke-linecap="round" opacity=".7"/>' % (GUM - 66, GUM - 58, GUM - 66))
    return svg('braces', 'Fixed orthodontic brackets bonded to the teeth with an archwire '
               'running through them', '\n'.join(b))


def p_aligner():
    """A clear aligner tray seated over the arch, drawn as a translucent shell."""
    b = [ridge()]
    b.append(row(ARCH))
    shell = []
    for k, x in ARCH:
        w = {'molar': 62, 'pre': 46, 'inc': 34}[k]
        shell.append('<rect x="%d" y="%d" width="%d" height="%d" rx="14" fill="url(#alg)" '
                     'opacity=".5"/>' % (x - w // 2, GUM - 104, w, 112))
    b.append('\n'.join(shell))
    b.append('<path d="M40 %d Q 320 %d 604 %d L604 %d Q 320 %d 40 %d Z" fill="url(#alg)" '
             'opacity=".38"/>' % (GUM - 100, GUM - 116, GUM - 100, GUM + 6, GUM + 14, GUM + 6))
    b.append('<path d="M40 %d Q 320 %d 604 %d" fill="none" stroke="#7fd0f5" stroke-width="3.5" '
             'stroke-linecap="round"/>' % (GUM - 100, GUM - 116, GUM - 100))
    b.append('<path d="M40 %d Q 320 %d 604 %d" fill="none" stroke="#7fd0f5" stroke-width="3.5" '
             'stroke-linecap="round"/>' % (GUM + 6, GUM + 14, GUM + 6))
    b.append('<path d="M96 %d Q 110 %d 128 %d" fill="none" stroke="#ffffff" stroke-width="6" '
             'stroke-linecap="round" opacity=".7"/>' % (GUM - 88, GUM - 96, GUM - 84))
    return svg('aligner', 'A clear aligner tray seated over the arch of teeth', '\n'.join(b))


def p_early_ortho():
    """A mixed dentition with a palatal expander widening a narrow arch."""
    b = [ridge()]
    b.append(row([('molar', 78, .9), ('pre', 176, .82), ('inc', 250, .8), ('inc', 300, .8),
                  ('inc', 350, .8), ('inc', 400, .8), ('pre', 474, .82), ('molar', 572, .9)]))
    # the expander: two bands on the molars, a screw body between them
    b.append('<rect x="46" y="%d" width="64" height="26" rx="8" fill="url(#steel)" opacity=".9"/>'
             '<rect x="540" y="%d" width="64" height="26" rx="8" fill="url(#steel)" opacity=".9"/>'
             % (GUM - 62, GUM - 62))
    b.append('<path d="M110 %d L268 %d M382 %d L540 %d" stroke="url(#steel)" stroke-width="9" '
             'stroke-linecap="round"/>' % (GUM - 50, GUM - 34, GUM - 34, GUM - 50))
    b.append('<rect x="268" y="%d" width="114" height="26" rx="12" fill="url(#steel)"/>'
             '<circle cx="325" cy="%d" r="9" fill="#7f8b99"/>'
             '<circle cx="325" cy="%d" r="3.4" fill="#e9eef3"/>' % (GUM - 47, GUM - 34, GUM - 34))
    # growth arrows, the point of treating early
    for x, d in ((150, -1), (500, 1)):
        b.append('<path d="M%d 84 L%d 84" stroke="#4fc3f7" stroke-width="5" stroke-linecap="round"/>'
                 '<path d="M%d 72 L%d 84 L%d 96" fill="none" stroke="#4fc3f7" stroke-width="5" '
                 'stroke-linecap="round" stroke-linejoin="round"/>'
                 % (x, x + 62 * d, x + 62 * d - 12 * d, x + 62 * d, x + 62 * d - 12 * d))
    return svg('early-ortho', 'A palatal expander fitted across a child&#8217;s upper arch, '
               'widening it while the jaw is still growing', '\n'.join(b))


def p_implant_single():
    """One titanium implant in bone carrying an abutment and a ceramic crown."""
    b = [ridge()]
    b.append(row([('molar', 96), ('pre', 200), ('pre', 452), ('molar', 560)]))
    x = 326
    # the fixture, threaded, seated in bone
    b.append('<g transform="translate(%d %d)">' % (x, GUM))
    b.append('<path d="M-21 6 L-17 62 Q-15 78 0 78 Q15 78 17 62 L21 6 Z" fill="url(#tita)"/>')
    for i in range(7):
        yy = 14 + i * 9
        b.append('<path d="M%s %s L%s %s" stroke="#6f7d8c" stroke-width="2.6" opacity=".75"/>'
                 % (-20 + i * .8, yy, 20 - i * .8, yy - 4))
    b.append('<rect x="-13" y="-26" width="26" height="34" rx="4" fill="url(#tita)"/>')
    b.append('</g>')
    # the crown over it
    b.append('<g transform="translate(%d %d)">' % (x, GUM - 24))
    b.append('<path d="M-46 6 C-54 6 -54 -8 -54 -20 L-52 -60 C-50 -86 -34 -98 -20 -94 '
             'C-12 -92 -8 -86 0 -86 C8 -86 12 -92 20 -94 C34 -98 50 -86 52 -60 L54 -20 '
             'C54 -8 54 6 46 6 Z" fill="url(#cera)"/>')
    b.append('<path d="M-38 -74 Q-20 -86 0 -78 Q20 -86 38 -74" fill="none" stroke="#dde4e3" '
             'stroke-width="3.4" stroke-linecap="round"/>')
    b.append('</g>')
    return svg('implant-single', 'A single titanium dental implant placed in the jawbone, '
               'carrying an abutment and a ceramic crown', '\n'.join(b))


def _full_arch(name, label, n):
    """A fixed full-arch bridge on n implants."""
    b = [ridge()]
    xs = [96 + i * (448 // (n - 1)) for i in range(n)]
    for x in xs:
        b.append('<g transform="translate(%d %d)">'
                 '<path d="M-19 -2 L-15 58 Q-13 74 0 74 Q13 74 15 58 L19 -2 Z" fill="url(#tita)"/>'
                 '<rect x="-11" y="-18" width="22" height="20" rx="4" fill="url(#tita)"/>'
                 '</g>' % (x, GUM))
        for i in range(6):
            yy = GUM + 10 + i * 9
            b.append('<path d="M%s %s L%s %s" stroke="#6f7d8c" stroke-width="2.4" opacity=".7"/>'
                     % (x - 18 + i * .7, yy, x + 18 - i * .7, yy - 4))
    # the bridge: an acrylic base with a row of teeth in it
    b.append('<path d="M44 %d Q 320 %d 596 %d L596 %d Q 320 %d 44 %d Z" fill="url(#acr)" '
             'stroke="#c4737f" stroke-width="2"/>'
             % (GUM - 30, GUM - 46, GUM - 30, GUM + 8, GUM - 4, GUM + 8))
    tb = [('molar', 78), ('molar', 168), ('pre', 244), ('inc', 306), ('inc', 356),
          ('inc', 406), ('pre', 470), ('molar', 560)]
    for k, tx in tb:
        b.append(tooth(k, tx, y=GUM - 26, s=.72, crown='url(#cera)', roots=False))
    b.append('<path d="M44 %d Q 320 %d 596 %d" fill="none" stroke="#c4737f" stroke-width="2.4" '
             'opacity=".7"/>' % (GUM - 30, GUM - 46, GUM - 30))
    return svg(name, label, '\n'.join(b))


def _overdenture(name, label, n):
    """A removable denture clipping onto n implants."""
    b = [ridge()]
    xs = [200, 440] if n == 2 else [140, 268, 396, 524]
    for x in xs:
        b.append('<g transform="translate(%d %d)">'
                 '<path d="M-19 -2 L-15 56 Q-13 72 0 72 Q13 72 15 56 L19 -2 Z" fill="url(#tita)"/>'
                 '<circle cx="0" cy="-14" r="15" fill="url(#tita)"/>'
                 '<circle cx="0" cy="-14" r="6" fill="#eef3f7"/>'
                 '</g>' % (x, GUM))
    # the denture, lifted to show the attachments
    b.append('<g transform="translate(0 -54)">')
    b.append('<path d="M40 %d Q 320 %d 600 %d L600 %d Q 320 %d 40 %d Z" fill="url(#acr)" '
             'stroke="#c4737f" stroke-width="2"/>'
             % (GUM - 30, GUM - 46, GUM - 30, GUM + 14, GUM + 28, GUM + 14))
    for x in xs:
        b.append('<circle cx="%d" cy="%d" r="14" fill="#f6dfe2" stroke="#c4737f" stroke-width="2.5"/>'
                 % (x, GUM + 4))
    tb = [('molar', 76), ('molar', 166), ('pre', 242), ('inc', 304), ('inc', 354),
          ('inc', 404), ('pre', 468), ('molar', 558)]
    for k, tx in tb:
        b.append(tooth(k, tx, y=GUM - 34, s=.7, crown='url(#cera)', roots=False))
    b.append('<path d="M40 %d Q 320 %d 600 %d" fill="none" stroke="#c4737f" stroke-width="2.4" '
             'opacity=".7"/>' % (GUM - 34, GUM - 50, GUM - 34))
    b.append('</g>')
    for x in xs:
        b.append('<path d="M%d %d L%d %d" stroke="#4fc3f7" stroke-width="3.5" stroke-linecap="round" '
                 'stroke-dasharray="6 6" opacity=".8"/>' % (x, GUM - 52, x, GUM - 30))
    return svg(name, label, '\n'.join(b))


def p_exam():
    """A mouth mirror and probe over the arch — the comprehensive examination."""
    b = [ridge()]
    b.append(row(ARCH))
    b.append('<g transform="rotate(-18 200 96)">'
             '<rect x="188" y="-6" width="15" height="96" rx="7" fill="url(#steel)"/>'
             '<circle cx="196" cy="106" r="27" fill="url(#steel)"/>'
             '<circle cx="196" cy="106" r="20" fill="#dbe7f0"/>'
             '<circle cx="189" cy="99" r="7" fill="#ffffff" opacity=".85"/></g>')
    b.append('<g transform="rotate(16 452 92)">'
             '<rect x="444" y="-14" width="14" height="92" rx="7" fill="url(#steel)"/>'
             '<path d="M451 78 q10 26 -6 44" fill="none" stroke="url(#steel)" stroke-width="7" '
             'stroke-linecap="round"/></g>')
    return svg('exam', 'A mouth mirror and probe examining the teeth during a comprehensive '
               'dental examination', '\n'.join(b))


def p_cleaning():
    """An ultrasonic scaler at the gum line, plaque lifting off."""
    b = [ridge()]
    b.append(row(ARCH))
    for x, w in ((186, 54), (282, 40), (356, 40)):
        b.append('<path d="M%d %d q%d -12 %d 0 l0 12 q%d 10 %d 0 z" fill="#e6d9a8" opacity=".85"/>'
                 % (x - w // 2, GUM - 22, w // 4, w, -w // 4, -w))
    b.append('<g transform="rotate(-20 318 70)">'
             '<rect x="300" y="-20" width="34" height="86" rx="16" fill="url(#sky)"/>'
             '<rect x="308" y="-8" width="6" height="58" rx="3" fill="#ffffff" opacity=".4"/>'
             '<path d="M317 66 q6 30 -10 48" fill="none" stroke="url(#steel)" stroke-width="9" '
             'stroke-linecap="round"/></g>')
    for i, (cx, cy, r) in enumerate(((262, 128, 7), (240, 108, 5), (284, 104, 4.5), (222, 138, 4))):
        b.append('<circle cx="%s" cy="%s" r="%s" fill="#bfe6fb" opacity=".85"/>' % (cx, cy, r))
    return svg('cleaning', 'An ultrasonic scaler cleaning plaque and tartar from the teeth at '
               'the gum line', '\n'.join(b))


def p_emergency():
    """A cracked, inflamed molar — what an emergency visit is usually about."""
    b = [ridge()]
    b.append(row([('molar', 96), ('pre', 200), ('pre', 452), ('molar', 560)]))
    b.append('<g transform="translate(326 %d)">' % GUM)
    b.append('<path d="%s" fill="url(#dent)"/><path d="%s" fill="url(#dent)"/>'
             % (MOLAR_ROOT_L, MOLAR_ROOT_R))
    b.append('<path d="%s" fill="url(#ena)"/>' % MOLAR_CROWN)
    b.append('<path d="%s" fill="none" stroke="#dde4e3" stroke-width="3.4" stroke-linecap="round"/>'
             % MOLAR_CUSP)
    # the fracture
    b.append('<path d="M6 -96 L-6 -62 L10 -44 L-4 -14 L6 8" fill="none" stroke="#8d5a4a" '
             'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>')
    # abscess at the apex
    b.append('<circle cx="-24" cy="80" r="19" fill="#d9534f" opacity=".55"/>')
    b.append('<circle cx="-24" cy="80" r="11" fill="#e0596a"/>')
    b.append('</g>')
    # pain radiating
    for i, r in enumerate((44, 62, 80)):
        b.append('<path d="M%d %d a%d %d 0 0 1 %d 0" fill="none" stroke="#e0596a" stroke-width="4" '
                 'stroke-linecap="round" opacity="%s"/>'
                 % (326 - r, GUM - 118, r, r, r * 2, round(.55 - i * .14, 2)))
    return svg('emergency', 'A cracked molar with an abscess forming at the root tip — a dental '
               'emergency', '\n'.join(b))


PANELS = [
    p_root_canal, p_crown, p_braces, p_aligner, p_early_ortho,
    p_implant_single, p_exam, p_cleaning, p_emergency,
    lambda: _wisdom('wisdom-erupted', 'An erupted wisdom tooth being lifted from its socket with '
                    'extraction forceps', 'erupted'),
    lambda: _wisdom('wisdom-impacted', 'An impacted wisdom tooth, tilted against the tooth in front '
                    'with part of the crown still under the gum', 'impacted'),
    lambda: _wisdom('wisdom-bony', 'A complete-bony impacted wisdom tooth, fully enclosed in the '
                    'jawbone', 'bony'),
    lambda: _full_arch('full-arch-4', 'A fixed full-arch bridge carried on four dental implants', 4),
    lambda: _full_arch('full-arch-6', 'A fixed full-arch bridge carried on six dental implants', 6),
    lambda: _overdenture('overdenture-2', 'A removable implant-supported denture clipping onto two '
                         'implants', 2),
    lambda: _overdenture('overdenture-4', 'A removable implant-supported denture clipping onto four '
                         'implants', 4),
]

if __name__ == '__main__':
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    for fn in PANELS:
        print(os.path.basename(fn()))
