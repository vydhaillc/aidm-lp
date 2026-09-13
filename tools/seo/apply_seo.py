#!/usr/bin/env python3
"""Open aidm.dental to search and AI engines — the SEO/GEO layer.

    python3 tools/seo/apply_seo.py

Runs over the *finished* HTML (the lp generator is not needed) and is
idempotent: everything it adds sits between <!-- seo:… --> markers and is
replaced on every run. Run it again after any page edit or rebuild.

Per page it writes: robots/canonical/hreflang/Open Graph tags, one JSON-LD
graph (AIDM's aidm.org entity, the page's Offer + price points, FAQPage,
VideoObject, BreadcrumbList), a short answer-first "At a glance" block built
only from the page's own offer card, a "Current offers" footer link row, alt
text on film/case/slideshow images, and a host redirect so the old
aidm.vydhai.com and aidm-lp.vercel.app copies land on aidm.dental. It also
regenerates robots.txt, sitemap.xml, llms.txt and the IndexNow key file.

Prices are never typed here — every figure is read from the page itself, so
the markup can't drift from what a visitor sees.
"""
import datetime, html, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = 'https://aidm.dental'
ORG = 'https://aidm.org/#organization'
TODAY = datetime.date.today().isoformat()
INDEXNOW_KEY = '7f3c9a51d2e84b6fa0c1d8e2b94a6f07'

# path → page config. `hold` keeps a page noindex (and out of sitemap/llms.txt)
# while everything else still applies. `canonical` points a duplicate at its
# main page instead of indexing it on its own.
PAGES = {
    '':                   dict(kind='home'),
    'new-patient':        dict(hub='https://aidm.org/new-patient-info/', hub_label='New patient information',
                               q='How much is a new patient exam at AIDM® in Austin?',
                               title='$100 New Patient Exam & X-Rays in Austin, TX | AIDM® Mueller',
                               alt='es/paciente-nuevo'),
    'emergency':          dict(hub='https://aidm.org/emergency-dental-care/', hub_label='Emergency dental care',
                               q='Can I see an emergency dentist at AIDM® in Austin today?',
                               title='Emergency Dentist in Austin, TX — Same-Day Appointments Available | AIDM®',
                               alt='es/emergencia'),
    'braces':             dict(hub='https://aidm.org/orthodontics/', hub_label='Orthodontics at AIDM®',
                               q='How much do braces cost at AIDM® in Austin?',
                               title='Braces in Austin, TX — $2,950 Comprehensive Braces | AIDM®'),
    'invisalign':         dict(hub='https://aidm.org/invisalign/', hub_label='Invisalign® at AIDM®',
                               q='How much does Invisalign cost at AIDM® in Austin?',
                               title='Invisalign in Austin, TX — $3,900 Clear Aligners | AIDM®'),
    'early-orthodontics': dict(hub='https://aidm.org/orthodontics/', hub_label='Orthodontics at AIDM®',
                               q='How much does early orthodontic treatment cost at AIDM® in Austin?',
                               title='Early Orthodontic Treatment for Kids in Austin — $2,500 | AIDM®'),
    'dental-implant':     dict(hub='https://aidm.org/dental-implants/', hub_label='Dental implants at AIDM®',
                               q='How much does a single dental implant and crown cost at AIDM® in Austin?',
                               title='Dental Implant + Crown in Austin, TX — From $3,750 | AIDM®'),
    'full-arch':          dict(hub='https://aidm.org/full-mouth-restoration/', hub_label='Full-mouth restoration at AIDM®',
                               q='How much do full-arch fixed teeth (All-on-X) cost at AIDM® in Austin?',
                               title='Full-Arch Dental Implants (All-on-X) in Austin — From $18,000 | AIDM®'),
    'snap-in-dentures':   dict(hub='https://aidm.org/implant-supported-dentures/', hub_label='Implant-supported dentures at AIDM®',
                               q='How much do implant-supported snap-in dentures cost at AIDM® in Austin?',
                               title='Implant-Supported Snap-In Dentures in Austin — From $9,500 | AIDM®'),
    # HOLD: aidm.org/pricing and /oral-surgeries publish wisdom teeth as $749 (2
    # teeth) / $1,499 (4) incl. nitrous; this page publishes $200–$450 per tooth
    # by complexity ($800–$1,800 for four). Two schedules for one service —
    # not indexed until AIDM reconciles them. Flip hold to False to release.
    'wisdom-teeth':       dict(hub='https://aidm.org/oral-surgeries/', hub_label='Oral surgery at AIDM®',
                               q='How much does wisdom tooth removal cost at AIDM® in Austin?',
                               title='Wisdom Teeth Removal in Austin, TX — From $200 a Tooth | AIDM®',
                               hold=True),
    'root-canal':         dict(hub='https://aidm.org/root-canal-therapy/', hub_label='Root canal therapy at AIDM®',
                               q='How much does a root canal cost at AIDM® in Austin?',
                               title='Root Canal in Austin, TX — From $995 | AIDM®'),
    'es/paciente-nuevo':  dict(hub='https://aidm.org/new-patient-info/', hub_label='Información para pacientes nuevos',
                               q='¿Cuánto cuesta un examen para pacientes nuevos en AIDM® en Austin?',
                               title='Dentista en Austin: Examen y Radiografías por $100 | AIDM®',
                               alt='new-patient'),
    'es/emergencia':      dict(hub='https://aidm.org/emergency-dental-care/', hub_label='Atención dental de emergencia',
                               q='¿Puedo ver a un dentista de emergencia hoy en AIDM® en Austin?',
                               title='Dentista de Emergencia en Austin — Citas el Mismo Día Disponibles | AIDM®',
                               alt='emergency'),
    # duplicates — crawlable, but they hand their signals to the main page
    'mailer/braces':      dict(kind='dup', canonical='braces'),
    'mailer/new-patient': dict(kind='dup', canonical='new-patient'),
    'braces-v2':          dict(kind='dup', canonical='braces'),
    'braces-lume':        dict(kind='dup', canonical='braces'),
}

HOME_TITLE = 'Dental Specials in Austin, TX — Current Offers & Prices | AIDM®'
HOME_DESC = ('Current dental offers at the Austin Institute of Dental Medicine in Mueller, Austin: '
             '$100 new patient exam and X-rays, $2,950 braces for the first 100 patients, Invisalign $3,900, '
             'implants from $3,750, root canals from $995. Open 7am–7pm, Monday to Saturday.')

# footer link row — same labels and prices as the homepage tiles
OFFER_LINKS = [
    ('new-patient', 'New Patient Special — $100'), ('emergency', 'Emergency Dentistry — Same-Day Care'),
    ('braces', 'Comprehensive Braces — $2,950'), ('invisalign', 'Invisalign® — $3,900'),
    ('early-orthodontics', 'Early Orthodontics — $2,500'), ('dental-implant', 'Single Implant + Crown — from $3,750'),
    ('full-arch', 'Full-Arch Fixed Teeth — from $18,000'), ('snap-in-dentures', 'Snap-In Dentures — from $9,500'),
    ('wisdom-teeth', 'Wisdom Teeth Removal — from $200'), ('root-canal', 'Root Canal — from $995'),
    ('es/paciente-nuevo', 'Pacientes Nuevos (español) — $100'), ('es/emergencia', 'Emergencia Dental (español)'),
]

# AIDM's YouTube films — titles, upload dates and lengths as published on the channel
VIDEOS = {
    'QNsMOG1B6G8': ('Welcome to AIDM: A Full-Service Dental Practice in East Austin, TX', '2026-07-17T08:32:31-07:00', 176),
    '2ooc1MlkmNM': ('Your First Visit to AIDM: What New Patients Can Expect | Austin Dentist', '2026-08-17T13:47:13-07:00', 75),
    'OBTJIDJHHTc': ('Su Primera Visita Dental en AIDM: Qué Puede Esperar | Dentista en Austin', '2026-07-22T09:20:19-07:00', 49),
    'f7HHTbB-qe8': ('Looking for a Family Dentist in Austin? Every Kind of Care Under One Roof', '2026-07-22T09:16:30-07:00', 62),
    'NtubApnQFt0': ('Dental Emergency in Austin? When You Need Same-Day Care', '2026-07-20T12:06:32-07:00', 60),
    'k9PavRdjiyc': ('Afraid of the Dentist? Sedation and Comfort Options in Austin', '2026-07-22T09:16:04-07:00', 40),
    'CEgwotre0h8': ('Braces and Invisalign in Austin: Which Option Is Right for You?', '2026-07-20T12:07:23-07:00', 66),
    '7Ci0z84BpDI': ('Dental Implants in Austin: Cost, Candidacy and What to Expect', '2026-07-22T09:17:37-07:00', 68),
    'cCUQyiHkJxg': ('What Is a Prosthodontist? Dental Implants, Dentures and Complex Care', '2026-07-20T12:05:00-07:00', 58),
    'DV9t9dZJauA': ('How to Get to AIDM: Directions, Parking and Finding Suite 200 | East Austin', '2026-07-22T09:16:55-07:00', 38),
}

ADDRESS = {'@type': 'PostalAddress', 'streetAddress': '1401 Philomena Street Suite 200',
           'addressLocality': 'Austin', 'addressRegion': 'TX', 'postalCode': '78723', 'addressCountry': 'US'}

# the same entity aidm.org declares (same @id), so engines fold aidm.dental into
# the existing practice instead of minting a second business
ORG_NODE = {
    '@type': ['Dentist', 'Organization'], '@id': ORG,
    'name': 'Austin Institute of Dental Medicine', 'alternateName': 'AIDM®', 'url': 'https://aidm.org',
    'telephone': '+1-737-434-2436', 'address': ADDRESS,
    'geo': {'@type': 'GeoCoordinates', 'latitude': 30.301023, 'longitude': -97.711754},
    'hasMap': 'https://www.google.com/maps/search/?api=1&query=30.301023,-97.711754',
    'openingHours': ['Mo,Tu,We,Th,Fr,Sa 07:00-19:00'],
    'medicalSpecialty': 'Dentistry',
    'logo': 'https://aidm.org/wp-content/uploads/2025/09/Full-Horizontal-Lock-up-Austin-Institute-of-Dental-Medicine-Main-Colorway-RGB-scaled.png',
    'sameAs': ['https://www.facebook.com/AustinInstituteOfDentalMedicine/', 'https://www.instagram.com/aidm365/',
               'https://www.linkedin.com/company/austin-institute-of-dental-medicine/',
               'https://www.youtube.com/@AustinInstituteofDentalMed'],
}

CSS = """<style>
.glance .gl{max-width:900px;margin:0 auto;padding:clamp(1.1rem,2.6vw,1.6rem) clamp(1.1rem,3vw,1.9rem);
  border:1px solid var(--line2);border-radius:var(--r);background:rgba(10,37,64,.6);position:relative;z-index:2}
.glance .gl-k{font-family:var(--head);font-size:.66rem;font-weight:600;letter-spacing:.2em;text-transform:uppercase;
  color:var(--sky);margin:0 0 .55rem}
.glance h2{font-size:clamp(1.12rem,2.3vw,1.42rem);font-weight:700;line-height:1.35;margin:0 0 .7rem;color:#fff}
.glance .gl-a{margin:0;color:var(--pale);line-height:1.72;font-size:.98rem}
.glance .gl-more{margin:.9rem 0 0;font-size:.86rem;color:var(--dim)}
.glance a{color:var(--sky)}
.ft-offers{padding:1.6rem 0 .4rem;border-bottom:1px solid var(--line)}
.ft-offers ul{grid-template-columns:repeat(auto-fill,minmax(230px,1fr));column-gap:1.6rem}
</style>"""

# old hosts serving the same files: send visitors (and crawlers) to aidm.dental
HOST_REDIRECT = ("<script>(function(l){var h=l.hostname;if(h==='aidm.vydhai.com'||h==='aidm-lp.vercel.app'||"
                 "h==='www.aidm.dental'){l.replace('https://aidm.dental'+l.pathname.replace(/index\\.html$/,'')"
                 ".replace(/(.)\\/$/,'$1')+l.search+l.hash)}})(location)</script>")


def A(s):
    """Injected HTML stays pure ASCII (®, — as entities), so it renders right whatever charset a host sends."""
    return s.encode('ascii', 'xmlcharrefreplace').decode()


def T(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s or ''))).replace(' *', '').strip(' *')


def money(s):
    s = T(s).replace('$ ', '$')
    return re.sub(r'\s+', ' ', s).strip()


def prices(s):
    return [int(x.replace(',', '')) for x in re.findall(r'\$\s?([\d,]+)', s)]


def same_as_card(o, d):
    """An option that restates the headline offer (same opening figure) under another name."""
    p, c = prices(o['amt']), prices(d.get('price', ''))
    return (o['name'] == d.get('card') and o['amt'] == d.get('price')) or bool(p and c and p[0] == c[0])


def url(path):
    return SITE + '/' + path if path else SITE + '/'


def strip_blocks(h):
    h = re.sub(r'\n?<!-- seo:(\w+) -->.*?<!-- /seo:\1 -->', '', h, flags=re.S)
    return re.sub(r'\n?<meta name="robots"[^>]*>', '', h)


def parse(h):
    """Pull the page's own offer facts out of the offer card, options, FAQ and films."""
    d = {}
    card = re.search(r'<div class="card-face card-offer">(.*?)<button', h, re.S)
    if card:
        c = card.group(1)
        d['card'] = T(re.search(r'<h2 class="card-t">(.*?)</h2>', c, re.S).group(1))
        d['price'] = money(re.search(r'<div class="card-price">(.*?)</div>', c, re.S).group(1))
        m = re.search(r'<p class="card-sub">(.*?)</p>', c, re.S)
        d['sub'] = T(m.group(1)) if m else ''
        m = re.search(r'<p class="card-disc">(.*?)</p>', c, re.S)
        d['disc'] = T(m.group(1)).lstrip('*').strip() if m else ''
        d['incl'] = [T(x) for x in re.findall(r'<li>(.*?)</li>', c, re.S)]
    d['opts'] = []
    for blk in re.findall(r'<div class="opt[ "].*?</div>', h, re.S):
        n = re.search(r'<h3>(.*?)</h3>', blk, re.S)
        a = re.search(r'<p class="amt">(.*?)</p>', blk, re.S)
        if n and a:
            ds = re.search(r'<p class="d">(.*?)</p>', blk, re.S)
            d['opts'].append(dict(name=T(n.group(1)), amt=money(a.group(1)), desc=T(ds.group(1)) if ds else '',
                                  incl=[T(x) for x in re.findall(r'<li>(.*?)</li>', blk, re.S)]))
    d['faq'] = [(T(q), T(a)) for q, a in
                re.findall(r'<details[^>]*><summary>(.*?)</summary><div class="a">(.*?)</div></details>', h, re.S)]
    d['films'] = list(dict.fromkeys(re.findall(r'data-yt="([A-Za-z0-9_-]{11})"', h)))
    d['captions'] = {i: T(b) for i, b in re.findall(r'<div class="film" data-yt="([^"]+)">.*?<b>(.*?)</b>', h, re.S)}
    d['desc'] = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', h).group(1))
    m = re.search(r'<meta property="og:image" content="([^"]*)"', h)
    d['image'] = m.group(1) if m else ''
    return d


def offer_node(oid, name, amt, desc, canon, service_id):
    o = {'@type': 'Offer', '@id': oid, 'name': f'{name} — {amt}', 'url': canon, 'priceCurrency': 'USD',
         'itemOffered': {'@id': service_id}, 'offeredBy': {'@id': ORG},
         'areaServed': {'@type': 'City', 'name': 'Austin, TX'}}
    if desc:
        o['description'] = desc
    p = prices(amt)
    if p:
        spec = {'@type': 'PriceSpecification', 'priceCurrency': 'USD', 'price': p[0]}
        if len(p) > 1 or re.search(r'(?i)\b(from|desde)\b', amt):
            spec['minPrice'] = p[0]
            if len(p) > 1:
                spec['maxPrice'] = p[-1]
        o['price'] = p[0]
        o['priceSpecification'] = spec
    return o


def video_nodes(ids, captions, lang):
    out = []
    for i in ids:
        if i not in VIDEOS:
            continue
        name, up, secs = VIDEOS[i]
        cap = captions.get(i)
        out.append({'@type': 'VideoObject', '@id': f'https://www.youtube.com/watch?v={i}', 'name': name,
                    'description': f'{cap}. {name}.' if cap else name,
                    'thumbnailUrl': [f'https://i.ytimg.com/vi/{i}/maxresdefault.jpg',
                                     f'https://i.ytimg.com/vi/{i}/hqdefault.jpg'],
                    'uploadDate': up, 'duration': f'PT{secs // 60}M{secs % 60}S',
                    'embedUrl': f'https://www.youtube.com/embed/{i}', 'contentUrl': f'https://www.youtube.com/watch?v={i}',
                    'publisher': {'@id': ORG}, 'inLanguage': 'es-US' if i == 'OBTJIDJHHTc' else 'en-US'})
    return out


def graph(path, cfg, d, title, lang):
    canon = url(path)
    website = {'@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/', 'name': 'AIDM® Current Offers',
               'alternateName': 'aidm.dental', 'publisher': {'@id': ORG}, 'inLanguage': ['en-US', 'es-US']}
    crumbs = [('AIDM®', 'https://aidm.org/'), ('Current offers' if lang == 'en' else 'Ofertas actuales', SITE + '/')]
    page = {'@type': 'WebPage', '@id': canon + '#webpage', 'url': canon, 'name': title, 'description': d['desc'],
            'inLanguage': 'es-US' if lang == 'es' else 'en-US', 'isPartOf': {'@id': SITE + '/#website'},
            'about': {'@id': ORG}, 'dateModified': TODAY, 'breadcrumb': {'@id': canon + '#breadcrumb'}}
    if d['image']:
        page['primaryImageOfPage'] = {'@type': 'ImageObject', 'url': d['image']}
    nodes = [ORG_NODE, website, page]
    if cfg.get('kind') == 'home':
        page['@type'] = 'CollectionPage'
        items = [(p, lab) for p, lab in OFFER_LINKS if not PAGES[p].get('hold')]
        page['mainEntity'] = {'@type': 'ItemList', 'name': 'Current AIDM® offers', 'numberOfItems': len(items),
                              'itemListElement': [{'@type': 'ListItem', 'position': n + 1, 'name': lab, 'url': url(p)}
                                                  for n, (p, lab) in enumerate(items)]}
    else:
        crumbs.append((d['card'], canon))
        sid = canon + '#service'
        page['mainEntity'] = {'@id': canon + '#offer'}
        page['relatedLink'] = [cfg['hub'], 'https://aidm.org/pricing/']
        main_desc = ' '.join(x for x in ['Includes: ' + '; '.join(d['incl']) + '.' if d['incl'] else '', d['disc']] if x)
        offers = [offer_node(canon + '#offer', d['card'], d['price'], main_desc, canon, sid)]
        for n, o in enumerate(d['opts']):
            if same_as_card(o, d):
                continue
            od = ' '.join(x for x in [o['desc'], 'Includes: ' + '; '.join(o['incl']) + '.' if o['incl'] else ''] if x)
            offers.append(offer_node(f'{canon}#option-{n + 1}', o['name'], o['amt'], od, canon, sid))
        nodes.append({'@type': 'Service', '@id': sid, 'name': d['card'], 'serviceType': d['card'],
                      'provider': {'@id': ORG}, 'areaServed': {'@type': 'City', 'name': 'Austin, TX'},
                      'url': canon, 'subjectOf': {'@id': canon + '#webpage'},
                      'offers': [{'@id': o['@id']} for o in offers]})
        nodes += offers
        if d['faq']:
            nodes.append({'@type': 'FAQPage', '@id': canon + '#faq', 'isPartOf': {'@id': canon + '#webpage'},
                          'mainEntity': [{'@type': 'Question', 'name': q,
                                          'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in d['faq']]})
    nodes += video_nodes(d['films'], d['captions'], lang)
    nodes.append({'@type': 'BreadcrumbList', '@id': canon + '#breadcrumb',
                  'itemListElement': [{'@type': 'ListItem', 'position': n + 1, 'name': nm, 'item': u}
                                      for n, (nm, u) in enumerate(crumbs)]})
    return json.dumps({'@context': 'https://schema.org', '@graph': nodes}, ensure_ascii=True, indent=1).replace('</', '<\\/')


def glance(cfg, d, lang):
    """Answer-first block: the page's own card facts, phrased so an engine can lift it whole."""
    es = lang == 'es'
    has_price = bool(prices(d['price']))
    sub = d['sub'] if d['sub'] and 'precio' not in d['sub'].lower() and 'price' not in d['sub'].lower() else ''
    if has_price:
        lead = (f"{d['card']} en el Austin Institute of Dental Medicine (AIDM®) cuesta {d['price']}" if es else
                f"{d['card']} at the Austin Institute of Dental Medicine (AIDM®) is {d['price']}")
    else:
        what = re.sub(r'(?i)same day', 'same-day', d['price']).lower()
        lead = (f"{d['card']} en el Austin Institute of Dental Medicine (AIDM®) ofrece {what}" if es else
                f"{d['card']} at the Austin Institute of Dental Medicine (AIDM®) offers {what}")
    parts = [lead + (f' ({sub[0].lower() + sub[1:]})' if sub else '') + '.']
    if d['incl']:
        parts.append(('Incluye: ' if es else 'Includes: ') + '; '.join(
            i[0].lower() + i[1:] if not i[:2].isupper() else i for i in d['incl']) + '.')
    others = [o for o in d['opts'] if prices(o['amt']) and not same_as_card(o, d)]
    if others:
        parts.append(('Otros precios publicados: ' if es else 'Other published price points: ') +
                     '; '.join(f"{o['name']} {o['amt']}" for o in others) + '.')
    if d['disc']:
        parts.append(d['disc'].rstrip('.') + '.')
    parts.append('AIDM® está en 1401 Philomena Street, Suite 200, en Mueller, Austin, TX, abierto de 7 a.m. a 7 p.m., '
                 'de lunes a sábado. Los honorarios finales se confirman después de una evaluación clínica.' if es else
                 'AIDM® is at 1401 Philomena Street, Suite 200, in Mueller, Austin, TX, open 7am–7pm Monday to '
                 'Saturday. Final fees are confirmed after a clinical evaluation.')
    e = html.escape
    more = (f'Más información: <a href="{cfg["hub"]}">{e(cfg["hub_label"])}</a> en aidm.org · '
            f'Honorarios estándar: <a href="https://aidm.org/pricing/">aidm.org/pricing</a>' if es else
            f'More: <a href="{cfg["hub"]}">{e(cfg["hub_label"])}</a> on aidm.org · '
            f'Standard fees: <a href="https://aidm.org/pricing/">aidm.org/pricing</a>')
    return (f'\n<!-- seo:glance -->\n<section class="pad tight-top tight-bot bg-deep glance" id="at-a-glance">\n'
            f'  <div class="wrap"><div class="gl">\n'
            f'    <p class="gl-k">{"En resumen" if es else "At a glance"}</p>\n'
            f'    <h2>{e(cfg["q"])}</h2>\n'
            f'    <p class="gl-a">{e(" ".join(parts))}</p>\n'
            f'    <p class="gl-more">{more}</p>\n'
            f'  </div></div>\n</section>\n<!-- /seo:glance -->').encode('ascii', 'xmlcharrefreplace').decode()


def offers_row(lang):
    lis = ''.join(f'<li><a href="/{p}">{html.escape(lab)}</a></li>' for p, lab in OFFER_LINKS)
    head = 'Ofertas actuales en AIDM®' if lang == 'es' else 'Current offers at AIDM®'
    return (f'<!-- seo:offers -->\n    <nav class="ft-offers" aria-label="{head}"><h4><a href="/">{head}</a></h4>'
            f'<ul>{lis}</ul></nav>\n    <!-- /seo:offers -->').encode('ascii', 'xmlcharrefreplace').decode()


def alt_text(h, lang):
    def film(m):
        b = re.search(r'<b>(.*?)</b>', m.group(0), re.S)
        label = T(b.group(1)) if b else 'AIDM® film'
        return m.group(0).replace('alt=""', A(f'alt="{html.escape(label)} — {"video" if lang == "es" else "video thumbnail"}"'), 1)
    h = re.sub(r'<div class="film" data-yt="[^"]+">.*?</div>', film, h, flags=re.S)

    def fig(m):
        cap = re.search(r'<figcaption>(.*?)</figcaption>', m.group(0), re.S)
        label = T(cap.group(1)) if cap else 'AIDM® office'
        extra = 'otra vista' if lang == 'es' else 'another view'
        return m.group(0).replace('alt=""', A(f'alt="AIDM® — {html.escape(label)}, {extra}"'))
    h = re.sub(r'<figure class="gt[^"]*slide[^"]*".*?</figure>', fig, h, flags=re.S)
    case = A('Caso de ortodoncia de AIDM®' if lang == 'es' else 'AIDM® orthodontic case photo')
    return re.sub(r'(src="[^"]*assets/cases/[^"]+")\s+alt=""', rf'\1 alt="{case}"', h)


def head_block(path, cfg, d, title, lang):
    canon = url(PAGES[path]['canonical']) if cfg.get('kind') == 'dup' else url(path)
    robots = ('noindex, follow' if cfg.get('hold') else
              'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1')
    tags = [HOST_REDIRECT, f'<meta name="robots" content="{robots}">', f'<link rel="canonical" href="{canon}">']
    if cfg.get('kind') != 'dup':
        if cfg.get('alt'):
            en, es = (path, cfg['alt']) if lang == 'en' else (cfg['alt'], path)
            tags += [f'<link rel="alternate" hreflang="en-US" href="{url(en)}">',
                     f'<link rel="alternate" hreflang="es-US" href="{url(es)}">',
                     f'<link rel="alternate" hreflang="x-default" href="{url(en)}">']
        tags += [f'<meta property="og:url" content="{canon}">', '<meta property="og:type" content="website">',
                 '<meta property="og:site_name" content="AIDM® — Austin Institute of Dental Medicine">',
                 f'<meta property="og:locale" content="{"es_US" if lang == "es" else "en_US"}">',
                 '<meta name="twitter:card" content="summary_large_image">',
                 CSS, f'<script type="application/ld+json">\n{graph(path, cfg, d, title, lang)}\n</script>']
    return A('\n<!-- seo:head -->\n' + '\n'.join(tags) + '\n<!-- /seo:head -->')


def process(path, cfg):
    f = os.path.join(ROOT, path, 'index.html')
    h = strip_blocks(open(f, encoding='utf-8').read())
    # the charset tag must sit in the first 1024 bytes; the tracking scripts pushed it past that
    m = re.search(r'<meta charset="utf-8">\n?', h)
    if m and len(h[:m.start()].encode()) > 1000:
        h = h[:m.start()] + h[m.end():]
        top = re.search(r'<head>\n?', h) or re.search(r'<html[^>]*>\n?', h)
        h = h[:top.end()] + '<meta charset="utf-8">\n' + h[top.end():]
    lang ='es' if re.search(r'<html[^>]*lang="es"', h) else 'en'
    d = parse(h)
    if cfg.get('kind') == 'dup':
        title = T(re.search(r'<title>(.*?)</title>', h, re.S).group(1))
    else:
        title = HOME_TITLE if cfg.get('kind') == 'home' else cfg['title']
        h = re.sub(r'<title>.*?</title>', lambda m: f'<title>{A(html.escape(title, quote=False))}</title>', h, count=1, flags=re.S)
        h = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1) + A(html.escape(title)), h, count=1)
        if cfg.get('kind') == 'home':
            d['desc'] = HOME_DESC
            h = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + A(html.escape(HOME_DESC)), h, count=1)
            h = re.sub(r'(<meta property="og:description" content=")[^"]*', lambda m: m.group(1) + A(html.escape(HOME_DESC)), h, count=1)
        h = alt_text(h, lang)
        anchor = '<div class="terms"' if '<div class="terms"' in h else '<div class="legal">'
        assert anchor in h, f'{path}: no footer anchor'
        h = h.replace(anchor, offers_row(lang) + anchor, 1)
        if cfg.get('kind') != 'home':
            marker = re.search(r'\n<!-- ═+ OFFICE TOUR', h)
            assert marker and 'card' in d, f'{path}: no hero/card'
            h = h[:marker.start()] + glance(cfg, d, lang) + h[marker.start():]
    t = re.search(r'</title>', h)
    h = h[:t.end()] + head_block(path, cfg, d, title, lang) + h[t.end():]
    if 'aidm-hero-1152.mp4' not in h:
        h = h.replace('aidm-hero.mp4', 'aidm-hero-1152.mp4')
    tmp = f + '.tmp'
    open(tmp, 'w', encoding='utf-8').write(h)
    os.replace(tmp, f)
    return d, lang, title


def site_files(data):
    live = [p for p, c in PAGES.items() if c.get('kind') != 'dup' and not c.get('hold')]
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for p in live:
        out.append(f'  <url><loc>{url(p)}</loc><lastmod>{TODAY}</lastmod>')
        alt = PAGES[p].get('alt')
        if alt:
            en, es = (p, alt) if not p.startswith('es/') else (alt, p)
            out += [f'    <xhtml:link rel="alternate" hreflang="en-US" href="{url(en)}"/>',
                    f'    <xhtml:link rel="alternate" hreflang="es-US" href="{url(es)}"/>',
                    f'    <xhtml:link rel="alternate" hreflang="x-default" href="{url(en)}"/>']
        out.append('  </url>')
    out.append('</urlset>')
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write('\n'.join(out) + '\n')

    open(os.path.join(ROOT, 'robots.txt'), 'w').write(
        '# aidm.dental — current offers from the Austin Institute of Dental Medicine (AIDM®).\n'
        '# Open to every search engine and AI crawler. Written by tools/seo/apply_seo.py.\n'
        'User-agent: *\nAllow: /\nDisallow: /api/\nDisallow: /tools/\nDisallow: /sheet-assets/\n\n'
        f'Sitemap: {SITE}/sitemap.xml\n')

    lines = ['# AIDM® — Austin Institute of Dental Medicine: current offers', '',
             '> aidm.dental publishes the current promotional offers and prices of the Austin Institute of Dental '
             'Medicine (AIDM®), a teaching dental practice at 1401 Philomena Street, Suite 200, Austin, TX 78723 '
             '(Mueller). Open 7am–7pm, Monday to Saturday. Phone (737) 434-2436. Main website: https://aidm.org — '
             'standard (non-promotional) fees are at https://aidm.org/pricing/.', '',
             'Promotional prices apply only to qualifying patients, usually with payment in full, and cannot be '
             'combined with insurance, financing, membership discounts or other promotions. Final fees are confirmed '
             'after a clinical evaluation. Treatment may be provided by dental residents under the supervision of '
             'licensed clinical faculty.', '', '## Offers (English)', '']
    for group, want in (('en', 'en'), ('es', 'es')):
        if group == 'es':
            lines += ['', '## Ofertas (español)', '']
        for p in live:
            if p == '' or data[p][1] != want:
                continue
            d = data[p][0]
            sub = d['sub'] if d['sub'] and not re.search(r'(?i)precio|price', d['sub']) else ''
            price = d['price'] + (f' ({sub})' if sub else '')
            lines.append(f"- [{d['card']}]({url(p)}): {price}. " + (('Includes: ' if want == 'en' else 'Incluye: ') +
                         '; '.join(d['incl']) + '.' if d['incl'] else ''))
    lines += ['', '## About AIDM® (aidm.org)', '',
              '- [Austin Institute of Dental Medicine](https://aidm.org/)', '- [Pricing](https://aidm.org/pricing/)',
              '- [Our doctors](https://aidm.org/our-doctors/)', '- [Reviews](https://aidm.org/reviews/)',
              '- [New patient information](https://aidm.org/new-patient-info/)',
              '- [Insurance & financing](https://aidm.org/insurance-financing/)',
              '- [Membership plan](https://aidm.org/membership-plan/)', '- [Contact](https://aidm.org/contact/)', '']
    open(os.path.join(ROOT, 'llms.txt'), 'w').write('\n'.join(lines))
    open(os.path.join(ROOT, f'{INDEXNOW_KEY}.txt'), 'w').write(INDEXNOW_KEY)
    return live


def main():
    data = {}
    for path, cfg in PAGES.items():
        data[path] = process(path, cfg)
        d, lang, title = data[path]
        print(f"{'/' + path:22} {lang}  {'HOLD ' if cfg.get('hold') else ''}{cfg.get('kind', 'offer'):5}  {title}")
    live = site_files(data)
    print(f'\nsitemap: {len(live)} URLs · robots.txt · llms.txt · {INDEXNOW_KEY}.txt')


if __name__ == '__main__':
    sys.exit(main())
