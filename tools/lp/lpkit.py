# -*- coding: utf-8 -*-
"""Builds an AIDM offer landing page by transforming braces/index.html.

Every page in the family is the same document with its offer-specific blocks
swapped out, so the theme cannot drift between pages: fix the theme once in
braces/index.html and rebuild.
"""
import io, os

ROOT = '/Users/macbook/projects/aidm-lp'
TPL  = os.path.join(ROOT, 'braces/index.html')
EXTRA_CSS = io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'extra.css'),
                    encoding='utf-8').read()

TICK  = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
         '<circle cx="12" cy="12" r="11" fill="#4fc3f7" opacity=".18"/>'
         '<path d="M7 12.4l3.2 3.2L17 8.8" stroke="#4fc3f7" stroke-width="2.4" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')
TICK18 = TICK.replace('width="16" height="16"', 'width="18" height="18"')
TICK17 = ('<svg width="17" height="17" viewBox="0 0 24 24" fill="none">'
          '<path d="M5 12.5l4.2 4.2L19 7" stroke="#4fc3f7" stroke-width="2.8" '
          'stroke-linecap="round" stroke-linejoin="round"/></svg>')

PERK_ICONS = {
 'cal':'<path d="M7 3v3M17 3v3M4 9h16M5 6h14a1 1 0 011 1v12a1 1 0 01-1 1H5a1 1 0 01-1-1V7a1 1 0 011-1z"/>',
 'park':'<path d="M6 3h7a5 5 0 010 10H9m0 0v8m0-8H6"/>',
 'clock':'<path d="M12 7v5l3.2 2M12 3a9 9 0 100 18 9 9 0 000-18z"/>',
 'card':'<path d="M3 7h18v12H3zM3 11h18M7 15h4"/>',
 'star':'<path d="M12 3l2.6 5.6 6.1.8-4.5 4.2 1.2 6L12 16.8 6.6 19.6l1.2-6L3.3 9.4l6.1-.8z"/>',
}
def perk(icon, label):
    return ('<div class="perk"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" '
            'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true">' + PERK_ICONS[icon] + '</svg><b>' + label + '</b></div>')

# The access facts that stand where the braces countdown does. Same on every
# page: they are true regardless of offer, and a shared strip is what makes the
# family read as one campaign.
FACTS = [('7<i class="u">am</i>', 'Opens'), ('7<i class="u">pm</i>', 'Closes'),
         ('6', 'Days/wk'), ('$0', 'Parking')]

def film(vid, label, tag=None):
    t = ('<span class="tag">' + tag + '</span>') if tag else ''
    return ('        <div class="film" data-yt="' + vid + '">' + t +
            '\n          <img loading="lazy" src="https://i.ytimg.com/vi/' + vid +
            '/maxresdefault.jpg" alt="">\n          <span class="pl"><i></i></span><b>' + label + '</b></div>')


def build(o):
    """`o['cta']` is the single label every booking button on the page wears —
    the nav, the mobile bar, the offer card, the card's form face, all three
    package cards and the footer form. The per-element labels in the offer
    dicts are kept as the fallback for anything without one."""
    o = dict(o)
    cta = o.get('cta')
    if cta:
        for k in ('navcta', 'cardcta', 'cfsubmit', 'ctsubmit'):
            o[k] = cta
        o['opts'] = [dict(c, cta=cta) for c in o['opts']]
    s = io.open(TPL, encoding='utf-8').read()

    def cut(start, end, new, label):
        i = s2['v'].find(start); assert i >= 0, 'START ' + label
        j = s2['v'].find(end, i);  assert j >= 0, 'END ' + label
        s2['v'] = s2['v'][:i] + new + s2['v'][j + len(end):]
    def sub(old, new, label):
        assert old in s2['v'], 'sub ' + label
        s2['v'] = s2['v'].replace(old, new)
    s2 = {'v': s}

    # ── head ────────────────────────────────────────────────────────────────
    cut('<title>', '<meta property="og:image" content="https://aidm.org/wp-content/uploads/2026/07/16-AIDM-Operatory-01--1536x1024.jpg">',
        '<title>' + o['title'] + '</title>\n'
        '<meta name="robots" content="noindex, nofollow">\n'
        '<meta name="description" content="' + o['desc'] + '">\n'
        '<meta property="og:title" content="' + o['ogtitle'] + '">\n'
        '<meta property="og:description" content="' + o['ogdesc'] + '">\n'
        '<meta property="og:image" content="' + o['ogimg'] + '">', 'head')
    sub('<link rel="preload" as="image" href="https://aidm.org/wp-content/uploads/2026/07/16-AIDM-Operatory-01--1536x1024.jpg" fetchpriority="high">',
        '<link rel="preload" as="image" href="' + o['ogimg'] + '" fetchpriority="high">', 'preload')
    sub('   AIDM — ORTHODONTICS LP  ·  V3 "dark blue, picture-led"',
        '   AIDM — ' + o['banner'] + ' LP  ·  on the V3 "dark blue, picture-led" theme', 'banner')
    sub('</style>', EXTRA_CSS.replace('NEW-PATIENT PAGE ADDITIONS', 'OFFER-PAGE ADDITIONS') + '</style>', 'css')
    if o.get('css'):
        sub('</style>', o['css'] + '</style>', 'css2')

    # ── nav ─────────────────────────────────────────────────────────────────
    cut('  <ul class="nav-links">', '  </ul>',
        '  <ul class="nav-links">\n' +
        '\n'.join('    <li><a href="#' + h + '">' + t + '</a></li>' for h, t in o['nav']) +
        '\n  </ul>', 'nav')
    sub('>Book Free Consult</a>\n</header>', '>' + o['navcta'] + '</a>\n</header>', 'navcta')
    sub('  <a class="btn btn-sky" href="#contact" data-book>Book Free Consult</a>\n</div>',
        '  <a class="btn btn-sky" href="#contact" data-book>' + o['navcta'] + '</a>\n</div>', 'mbar')
    sub('<a class="btn btn-ghost" href="tel:+17374342436">Call</a>',
        '<a class="btn btn-ghost" href="tel:+17374342436">' + o.get('mcall', 'Call') + '</a>', 'mcall')

    # ── hero headline ───────────────────────────────────────────────────────
    cut('          <h1>\n            <span class="l1">Straighten</span>', '</h1>',
        '          <h1>\n            <span class="l1">' + o['h1'][0] + '</span>\n' +
        '\n'.join('            <span class="l2">' + x + '</span>' for x in o['h1'][1:-1]) +
        '\n            <span class="l3">' + o['h1'][-1] + '</span>\n          </h1>', 'h1')

    # ── offer card ──────────────────────────────────────────────────────────
    cut('           <div class="card-face card-offer">',
        '            <p class="card-fine">Evaluation complimentary &mdash; no obligation to start. <a href="#terms">*Terms &amp; Conditions</a></p>\n           </div>',
'''           <div class="card-face card-offer">
            <div class="rib">
              <span class="rib-tail rib-l" aria-hidden="true"></span>
              <span class="rib-tail rib-r" aria-hidden="true"></span>
              <p class="rib-band">
                <span class="star">&#9733;</span>''' + o['pill'] + '''
                <i class="rib-shine" aria-hidden="true"></i>
                <i class="spk" style="--s:12px;top:12%;left:9%;animation-delay:.4s"></i>
                <i class="spk" style="--s:9px;top:60%;left:30%;animation-delay:1.5s"></i>
                <i class="spk" style="--s:11px;top:16%;right:13%;animation-delay:2.4s"></i>
              </p>
            </div>
            <h2 class="card-t">''' + o['cardtitle'] + '''</h2>

            <div class="card-price">
              ''' + o['cardprice'] + '''<a class="ast ast-lg" href="#terms" aria-label="See fee disclosures">*</a>
              <i class="spk" style="--s:24px;top:0%;left:3%;animation-delay:.9s"></i>
              <i class="spk" style="--s:17px;top:66%;left:16%;animation-delay:2.1s"></i>
              <i class="spk" style="--s:26px;top:56%;right:1%;animation-delay:1.6s"></i>
              <i class="spk" style="--s:13px;bottom:6%;right:22%;animation-delay:3s"></i>
            </div>
''' + ('            <p class="card-sub">' + o['cardsub'] + '</p>\n' if o.get('cardsub') else '') + '''
            <ul class="card-list">
''' + '\n'.join('              <li>' + TICK + x + '</li>' for x in o['included']) + '''
            </ul>

            <div class="card-cd">
              <p class="hours">Open 7am &ndash; 7pm<span class="sp"></span>Mon&ndash;Sat</p>
            </div>

            <button class="btn btn-sky" type="button" id="cardBook">''' + o['cardcta'] + '''</button>
            <p class="card-fine">''' + o['cardfine'] + ''' <a href="#terms">*Terms &amp; Conditions</a></p>
           </div>''', 'card')

    sub('<p class="cf-k">Complimentary evaluation</p>', '<p class="cf-k">' + o['cfk'] + '</p>', 'cfk')
    sub('<h2 class="cf-h">Book your free consult</h2>', '<h2 class="cf-h">' + o['cfh'] + '</h2>', 'cfh')
    sub('<input type="hidden" name="offer" value="ortho-2950-first-100">',
        '<input type="hidden" name="offer" value="' + o['id'] + '">', 'cfoffer')
    sub('<button class="btn btn-sky" type="submit">Book Free Consult</button>',
        '<button class="btn btn-sky" type="submit">' + o['cfsubmit'] + '</button>', 'cfsubmit')
    cut('                   <option>Myself</option>', '</select></div>',
        '                   ' + ''.join('<option>' + x + '</option>' for x in o['who']) +
        '\n                 </select></div>', 'cfwho')
    cut('             <p class="cf-p">Thank you &mdash; the orthodontic team', '</p>',
        '             <p class="cf-p">' + o['cfdone'] + '</p>', 'cfdone')

    # ── office tour ─────────────────────────────────────────────────────────
    sub('<figcaption><em>Treatment</em>Open orthodontic bay</figcaption>',
        '<figcaption><em>Treatment</em>' + o.get('tourcap', 'Open treatment bay') + '</figcaption>', 'tourcap')
    sub('alt="The open orthodontic treatment bay, flooded with daylight"',
        'alt="The open treatment bay, flooded with daylight"', 'touralt')

    # ── promotion band ──────────────────────────────────────────────────────
    i = s2['v'].find('<!-- ══════════════ SPECIAL PROMOTION ══════════════ -->')
    j = s2['v'].find('<!-- ══════════════ BEFORE & AFTER ══════════════ -->')
    assert i > 0 and j > i
    s2['v'] = s2['v'][:i] + '''<!-- ══════════════ THE OFFER + FILM ══════════════
     The screen carries AIDM's own film for this treatment; the column beside
     it is the offer itself, verbatim from the approved promotions sheet. -->
<section class="promo pad tight-top bg-deep2 ph" id="promo" style="--ph:url('../aidm-lp-assets/bg/reception.jpg')">
  <div class="wrap">
    <div class="sh sh-tight rv">
      <p class="promo-k"><span class="star">&#9733;</span>''' + o['promok'] + '''</p>
      <h2>''' + o['promoh2'] + '''</h2>
      <div class="bar"></div>
    </div>
    <div class="promo-grid rv">

      <div class="tv-wrap">
        <div class="tv">
          <div class="tv-scr" id="promoScr" data-yt="''' + o['video'] + '''">
            <img loading="lazy" src="https://i.ytimg.com/vi/''' + o['video'] + '''/maxresdefault.jpg"
                 alt="''' + o['videoalt'] + '''">
            <span class="pl" role="button" tabindex="0" aria-label="Play: ''' + o['videoalt'] + '''"><i></i></span>
          </div>
          <span class="tv-led">''' + o['videoled'] + '''</span>
        </div>
        <div class="tv-foot"></div>
        <div class="tv-base"></div>
        <div class="promo-badge">
          <b>''' + o['badge'][0] + '''</b>
          <i>''' + o['badge'][1] + '''</i>
        </div>
      </div>

      <div class="promo-copy">
        <figure class="promo-ph">
          <img loading="lazy" src="''' + o['promoimg'] + '''"
               alt="''' + o['promoalt'] + '''">
        </figure>
        <ul class="promo-hl">
''' + '\n'.join('          <li>' + TICK18 + x + '</li>' for x in o['included']) + '''
        </ul>
      </div>
    </div>

    <p class="promo-fine"><span class="fs">*</span>''' + o['promofine'] + '''
      <a href="#terms">Read the full offer terms</a>.</p>

    <div class="perks rv">
''' + '\n'.join('      ' + perk(k, v) for k, v in o['perks']) + '''
    </div>

  </div>
</section>

''' + s2['v'][j:]

    # ── the band where braces runs before/after ─────────────────────────────
    i = s2['v'].find('<!-- ══════════════ BEFORE & AFTER ══════════════ -->')
    j = s2['v'].find('<!-- ══════════════ OFFICE STAFF ══════════════ -->')
    assert i > 0 and j > i
    if o.get('cases'):
        # an orthodontic offer — keep the real case rail, relabel the captions
        band = s2['v'][i:j].replace('Comprehensive braces', o['cases'])
        band = band.replace('<h2>Actual cases. <em>Actual bites.</em></h2>',
                            '<h2>' + o['caseh2'] + '</h2>')
        band = band.replace('Intraoral records from orthodontic cases completed at the Austin Institute of Dental Medicine.',
                            o['casesub'])
        band = band.replace('illustrative of typical\n      comprehensive orthodontic treatment',
                            'illustrative of typical\n      comprehensive orthodontic treatment')
        band = band.replace('— before and after"', ' — before and after"')
    else:
        steps = '\n'.join(
            '      <li class="step">\n        <span class="step-n">' + str(n + 1) + '</span>\n'
            '        <b>' + t + '</b>\n        <p>' + p + '</p>\n      </li>'
            for n, (t, p) in enumerate(o['steps']))
        band = '''<!-- ══════════════ HOW IT GOES ══════════════
     The braces page runs its intraoral before/after rail here. Those records
     belong to orthodontics, so on this page the band carries the sequence of
     the treatment itself instead. -->
<section class="pad bg-deep ph" id="visit" style="--ph:url('../aidm-lp-assets/bg/operatory-02.jpg')">
  <div class="wrap">
    <div class="sh rv">
      <p class="k">''' + o['stepsk'] + '''</p>
      <h2>''' + o['stepsh2'] + '''</h2>
      <div class="bar"></div>
      <p>''' + o['stepssub'] + '''</p>
    </div>
    <ol class="steps rv">
''' + steps + '''
    </ol>
    <p class="steps-fine">''' + o['stepsfine'] + '''</p>
  </div>
</section>

'''
    s2['v'] = s2['v'][:i] + band + s2['v'][j:]

    # ── staff ───────────────────────────────────────────────────────────────
    sub('''      <p>Board-certified faculty, specialists and residents working side by side &mdash; every orthodontic
        plan at AIDM is reviewed and signed off by faculty.</p>''',
        '      <p>' + o['staffsub'] + '</p>', 'staffsub')
    sub('<figcaption><em>Orthodontics</em>The team in the bay</figcaption>',
        '<figcaption><em>Clinical team</em>The team in the bay</figcaption>', 'staffcap')
    sub('alt="The AIDM orthodontic residents and clinical team in the treatment bay"',
        'alt="AIDM residents and the clinical team in the treatment bay"', 'staffalt')

    # ── film wall ───────────────────────────────────────────────────────────
    cut('    <div class="fstage rv">', '''    </div>

    <div class="flane rv">
      <p class="flane-h">Treatments explained</p>
      <div class="frail">''',
'''    <div class="fstage rv">
      <div class="film" data-yt="''' + o['films'][0][0] + '''">
        <span class="tag">''' + o['films'][0][2] + '''</span>
        <img loading="lazy" src="https://i.ytimg.com/vi/''' + o['films'][0][0] + '''/maxresdefault.jpg" alt="">
        <span class="pl"><i></i></span><b>''' + o['films'][0][1] + '''</b></div>
      <div class="fside">
''' + '\n'.join(film(v, l) for v, l in o['films'][1:3]) + '''
      </div>
    </div>

    <div class="flane rv">
      <p class="flane-h">''' + o['filmlane'] + '''</p>
      <div class="frail">''', 'fstage')
    cut('        <div class="film" data-yt="f7HHTbB-qe8">',
        '          <span class="pl"><i></i></span><b>Prosthodontics</b></div>\n      </div>',
        '\n'.join(film(v, l) for v, l in o['films'][3:]) + '\n      </div>', 'frail')
    sub('      <p>The building, the clinicians and the treatments &mdash; in their own words.</p>',
        '      <p>' + o['filmsub'] + '</p>', 'filmsub')

    # ── feature rows ────────────────────────────────────────────────────────
    i = s2['v'].find('<!-- ══════════════ PICTURE-LED FEATURE ROWS ══════════════ -->')
    j = s2['v'].find('<!-- ══════════════ OPTIONS ══════════════ -->')
    assert i > 0 and j > i
    rows = []
    for n, r in enumerate(o['frows']):
        rows.append('''    <div class="frow ''' + ('flip ' if n == 0 else '') + '''rv">
      <div class="fimg-wrap"><figure class="fimg">
        <img loading="lazy" src="''' + r['img'] + '''" alt="''' + r['alt'] + '''">
        <figcaption>''' + r['cap'] + '''</figcaption>
      </figure></div>
      <div class="fcopy">
        <p class="k">''' + r['k'] + '''</p>
        <h2>''' + r['h2'] + '''</h2>
        <p>''' + r['p'] + '''</p>
        <ul''' + (' class="g2"' if r.get('two_up') else '') + '''>
''' + '\n'.join('          <li>' + TICK17 + b + '</li>' for b in r['bullets']) + '''
        </ul>
      </div>
    </div>''')
    s2['v'] = s2['v'][:i] + '''<!-- ══════════════ PICTURE-LED FEATURE ROWS ══════════════ -->
<section class="pad bg-deep2 ph" id="treatment" style="--ph:url('../aidm-lp-assets/bg/ortho-bay.jpg')">
  <div class="wrap">

''' + '\n\n'.join(rows) + '''

  </div>
</section>

''' + s2['v'][j:]

    # ── options / price points ──────────────────────────────────────────────
    i = s2['v'].find('<!-- ══════════════ OPTIONS ══════════════ -->')
    j = s2['v'].find('<!-- ══════════════ REVIEWS ══════════════ -->')
    assert i > 0 and j > i
    cards = []
    for c in o['opts']:
        cards.append('      <div class="opt' + (' feat' if c.get('feat') else '') +
            (' has-ph' if c.get('img') else '') + ' rv">\n' +
            ('        <span class="opt-flag">' + c['flag'] + '</span>\n' if c.get('flag') else '') +
            ('        <figure class="opt-ph' + (' is-art' if c['img'].endswith('.svg') else '') +
             '"><img loading="lazy" src="' + c['img'] +
             '" alt="' + c.get('imgalt', '') + '"' +
             (' style="object-position:' + c['imgpos'] + '"' if c.get('imgpos') else '') +
             '></figure>\n' if c.get('img') else '') +
            '        <p class="sub">' + c['sub'] + '</p>\n'
            '        <h3>' + c['h3'] + '</h3>\n'
            '        <p class="amt' + (' amt-words' if c.get('words') else '') + '">' + c['amt'] +
            '<a class="ast" href="#terms" aria-label="See fee disclosures">*</a></p>\n'
            '        <p class="strike">' + c.get('strike', '&nbsp;') + '</p>\n'
            '        <p class="d">' + c['d'] + '</p>\n'
            '        <ul>' + ''.join('<li>' + x + '</li>' for x in c['ul']) + '</ul>\n'
            '        <p class="optfine">*' + c['fine'] + '</p>\n'
            '        <a class="btn ' + ('btn-gold' if c.get('feat') else 'btn-ghost') + '" href="#contact">' + c['cta'] + '</a>\n'
            '      </div>')
    also = ''
    if o.get('also'):
        also = '''
    <div class="alsobox rv">
      <p class="also-h">''' + o['alsoh'] + '''</p>
      <ul class="also">
''' + '\n'.join('        <li><b>' + a + '</b><span>' + b + '</span><i>' + c + '</i></li>' for a, b, c in o['also']) + '''
      </ul>
      <p class="optfine" style="margin:1.1rem 0 0">Package pricing applies only to the services specifically listed.
        Final recommendations, eligibility and fees are determined following a comprehensive clinical evaluation.</p>
    </div>'''
    s2['v'] = s2['v'][:i] + '''<!-- ══════════════ PRICE POINTS ══════════════
     The braces page carries "Orthodontic options for every stage" here. On
     this page the same band carries this offer's own tiers and the packages
     next to it, so nobody has to leave to find the number that applies. -->
<section class="pad bg-deep ph" id="packages" style="--ph:url('../aidm-lp-assets/bg/lobby-lounge.jpg')">
  <div class="wrap">
    <div class="sh rv">
      <p class="k">''' + o['optsk'] + '''</p>
      <h2>''' + o['optsh2'] + '''</h2>
      <div class="bar"></div>
      <p>''' + o['optssub'] + '''</p>
    </div>
    <div class="opts">
''' + '\n'.join(cards) + '''
    </div>''' + also + '''
  </div>
</section>

''' + s2['v'][j:]

    # ── FAQ ─────────────────────────────────────────────────────────────────
    cut('    <div class="faq rv">', '''    </div>
  </div>
</section>

<!-- ══════════════ CONTACT ══════════════ -->''',
        '    <div class="faq rv">\n' +
        '\n'.join('      <details' + (' open' if n == 0 else '') + '><summary>' + q +
                  '</summary><div class="a">' + a + '</div></details>'
                  for n, (q, a) in enumerate(o['faq'])) +
        '''\n    </div>
  </div>
</section>

<!-- ══════════════ CONTACT ══════════════ -->''', 'faq')

    # ── contact ─────────────────────────────────────────────────────────────
    cut('      <p class="k">Limited to the first 100 orthodontic patients</p>',
        '        time — usually the same working day.</p>',
        '      <p class="k">' + o['ctk'] + '</p>\n'
        '      <h2>' + o['cth2'] + '</h2>\n'
        '      <div class="bar"></div>\n'
        '      <p>' + o['ctsub'] + '</p>', 'cthead')
    cut('            <div class="fld full"><label for="who">Who is the treatment for?</label>',
        '</select></div>',
        '            <div class="fld full"><label for="who">' + o['wholabel'] + '</label>\n'
        '              <select id="who" name="patient_type">\n'
        '                <option value="">Please choose…</option>\n' +
        '\n'.join('                <option>' + x + '</option>' for x in o['who2']) +
        '\n              </select></div>', 'ctwho')
    sub('<textarea id="cf_msg" name="notes" placeholder="Preferred days, previous orthodontic treatment, concerns…"></textarea>',
        '<textarea id="cf_msg" name="notes" placeholder="' + o['placeholder'] + '"></textarea>', 'cfmsg')
    sub('<textarea id="msg" name="notes" placeholder="Preferred days, previous orthodontic treatment, concerns…"></textarea>',
        '<textarea id="msg" name="notes" placeholder="' + o['placeholder'] + '"></textarea>', 'ctmsg')
    sub('<input type="hidden" name="offer" value="ortho-comprehensive-braces-2950">',
        '<input type="hidden" name="offer" value="' + o['id'] + '">', 'ctoffer')
    sub('<button class="btn btn-sky btn-lg" type="submit">Book Free Consult</button>',
        '<button class="btn btn-sky btn-lg" type="submit">' + o['ctsubmit'] + '</button>', 'ctsubmit')

    # ── footer terms + legal ────────────────────────────────────────────────
    cut('    <div class="terms" id="terms">', '    </div>\n\n    <div class="legal">',
        '    <div class="terms" id="terms">\n' +
        '\n'.join('      <div><b>' + a + '</b>' + b + '</div>' for a, b in o['terms']) +
        '\n    </div>\n\n    <div class="legal">', 'terms')
    cut('      <p><b>Pricing.</b> Package eligibility',
        '      <p style="color:#4a6d87">© 2026 Austin Institute of Dental Medicine. All rights reserved.</p>',
        o.get('legal_html') or '''      <p><b>Pricing.</b> Promotional offers, package pricing and included services are subject to change,
        modification or discontinuation at any time without prior notice. Offers are available for a limited time
        and may be withdrawn at the sole discretion of Austin Institute of Dental Medicine. Promotions are valid
        only for eligible patients who meet clinical criteria as determined by the treating dentist or specialist
        following an appropriate examination. Package pricing applies only to the services specifically listed and
        cannot be combined with insurance benefits, membership pricing, financing promotions or other discounts
        unless expressly stated. Additional treatment, diagnostic procedures, specialty services, laboratory fees,
        sedation or other clinically necessary procedures may result in additional charges. Final treatment
        recommendations, eligibility and fees are determined following a comprehensive clinical evaluation. AIDM
        reserves the right to modify pricing, eligibility requirements, package contents, promotional periods and
        terms and conditions at any time without notice.</p>
      <p><b>Your right to cancel (Texas).</b> The patient and any other person responsible for payment has a right
        to refuse to pay, cancel payment, or be reimbursed for payment for any other service, examination, or
        treatment that is performed as a result of and within 72 hours of responding to the advertisement for the
        free, discounted fee, or reduced fee service, examination, or treatment.</p>
      <p><b>Who treats you.</b> AIDM is a premier educational institute. Treatment under these promotional offers
        may be provided by dental residents participating in advanced training programmes under the direct
        supervision of our licensed clinical faculty. All promotional pricing is subject to clinical qualification
        and medical clearance as determined by the attending doctor.</p>
      <p><b>Provider.</b> Dental services are provided by Philomena Street PLLC, supported by AIDM. Services at the
        Austin Institute of Dental Medicine are provided by General Dentists, Residents and Faculty Members.
        Terms such as &ldquo;Advanced,&rdquo; &ldquo;Complex&rdquo; or &ldquo;Institute&rdquo; refer to the scope of
        training and services offered and do not imply a specific specialisation unless the provider is explicitly
        designated as a Specialist recognised by the American Dental Association (ADA).''' +
        o.get('legalextra', '') + '''</p>
      <p style="color:#4a6d87">© 2026 Austin Institute of Dental Medicine. All rights reserved.</p>''', 'legal')

    # ── JS ──────────────────────────────────────────────────────────────────
    sub("""    data._subject     = 'AIDM braces LP — new enquiry from ' +""",
        "    data._subject     = 'AIDM " + o['slug'] + " LP — new enquiry from ' +", 'subject')
    # (the template lost its countdown on 2026-08-19 — nothing to strip here)
    sub("""        'title="Orthodontics at AIDM" allow="accelerometer; autoplay; encrypted-media; ' +""",
        "        'title=\"" + o['videoled'].replace('&mdash;', '-') + "\" allow=\"accelerometer; autoplay; encrypted-media; ' +", 'promotitle')

    if o.get('lang'):
        s2['v'] = s2['v'].replace('<html lang="en">', '<html lang="%s">' % o['lang'], 1)

    # a page one level deeper than /braces/ needs one more ../ on shared assets
    up = '../' * (o['slug'].count('/') + 1)
    if up != '../':
        s2['v'] = s2['v'].replace('../aidm-lp-assets/', up + 'aidm-lp-assets/')
        s2['v'] = s2['v'].replace('../assets/', up + 'assets/')

    # literal swaps for the chrome the template hard-codes (nav, form labels,
    # the standing section headings) — how the Spanish pages get translated
    miss = []
    for a, b in o.get('i18n', []):
        if a not in s2['v']:
            miss.append(a[:70]); continue
        s2['v'] = s2['v'].replace(a, b)
    if miss:
        print('  i18n MISSED in %s:' % o['slug'])
        for m in miss: print('    -', m)

    out = os.path.join(ROOT, o['slug'], 'index.html')
    if not os.path.isdir(os.path.dirname(out)):
        os.makedirs(os.path.dirname(out))
    io.open(out, 'w', encoding='utf-8').write(s2['v'])
    return out
