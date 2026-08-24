# -*- coding: utf-8 -*-
"""Offers 6, 7, 8 and 10 from the approved promotions sheet."""
from offers_a import (U, NAV_STD, OPERATORY, RES_PATIENT, XRAY_TALK, DOC_RES,
                      SMILE_M, PAIN, OG_OP, PIC, PALT)
SENIOR_JOY = U + '2026/07/iStock-1296176774-1024x683.jpg'
SENIOR_M   = U + '2026/08/istock_61-1024x1024.jpg'
CAMPING    = U + '2026/05/iStock-52-1024x683.jpg'
FREEDOM    = U + '2026/08/istock_56-1024x683.jpg'

IMPLANT_PERKS = [('cal','Book online'),('park','Free parking'),('clock','Monday&ndash;Saturday'),
                 ('card','Financing available'),('star','Dedicated surgery rooms')]

# The three implant packages as cards, reused across the implant pages.
def implant_cards(feature, own_photo=None, own_alt=''):
    single = dict(img=PIC['implant'], imgalt=PALT['implant'], imgpos='center 48%',
        sub='One missing tooth. One complete solution.', h3='Single Implant + Crown',
        amt='from $3,750', strike='Range $3,750&ndash;$5,000',
        d='Replace one missing tooth with coordinated implant placement and a natural-looking ceramic crown.',
        ul=['Clinically appropriate 3D imaging','Digitally planned surgical implant guide','Dental implant placement',
            'Final ceramic crown','Bone grafting when in the selected pathway'],
        fine='The final package price depends on the restoration selected and whether bone grafting is needed.',
        cta='See single-implant pricing')
    full = dict(img=PIC['surgery'], imgalt=PALT['surgery'], imgpos='center 40%',
        sub='A full smile. A fresh start.', h3='Full-Arch Fixed Teeth',
        amt='from $18,000', strike='Per arch &middot; $18,000 &middot; $22,000 &middot; $26,000',
        d='Replace an entire arch of missing or failing teeth with a secure, fixed restoration on four to six implants.',
        ul=['Comprehensive diagnostic work-up','Four to six conventional dental implants','Multi-unit abutments',
            'Interim complete and fixed teeth','Final fixed full-arch restoration'],
        fine='Your treatment tier is based on extractions, grafting, bone condition and case complexity. Advanced '
             'reconstruction or services outside the standard package require a custom treatment plan.',
        cta='See full-arch pricing')
    snap = dict(img=PIC['family'], imgalt=PALT['family'], imgpos='center 30%',
        sub='More stability. More confidence.', h3='Snap-In Dentures',
        amt='from $9,500', strike='Per arch &middot; $9,500 &middot; $12,500 &middot; $17,000',
        d='A secure, removable implant-supported solution with far more stability than a conventional denture.',
        ul=['Comprehensive evaluation and planning','Clinically appropriate imaging','Two or four implants by tier',
            'Implant attachments','Interim and final removable dentures'],
        fine='Complete package pricing based on the selected clinical pathway. Clinical package name: '
             'Implant-Supported Removable Overdenture.',
        cta='See snap-in pricing')
    cards = {'single': single, 'full': full, 'snap': snap}
    for k, c in cards.items():
        if k == feature:
            c['feat'] = True; c['flag'] = 'This offer'; c['cta'] = 'Book my consultation'
            if own_photo:
                c['img'] = own_photo; c['imgalt'] = own_alt; c['imgpos'] = 'center 32%'
    return [cards['single'], cards['full'], cards['snap']]

# ══════════════════════════════════════════════════════════════════════════
IMPLANT = dict(
  cta='Book Appointment',
  slug='dental-implant', id='single-implant-crown-from-3750', banner='SINGLE IMPLANT',
  title='One Missing Tooth. One Complete Solution. — Single Implant + Crown from $3,750 | AIDM Austin',
  desc='Single dental implant with a final ceramic crown from $3,750 at the Austin Institute of Dental Medicine in Mueller, Austin. 3D imaging, guided placement and the crown in one package.',
  ogtitle='One Missing Tooth. One Complete Solution. — Implant + Crown from $3,750 | AIDM',
  ogdesc='3D imaging, a digitally planned surgical guide, implant placement and the final ceramic crown — one package, from $3,750.',
  ogimg=OG_OP,
  nav=NAV_STD, navcta='Book a Consult',
  h1=['One Missing Tooth.', 'One Complete', 'Solution.'],
  pill='Implant + crown, one package', cardtitle='Single Implant + Crown',
  cardprice='<span class="fr">from</span><span class="c">$</span><span class="v">3,750</span>',
  cardsub='Range $3,750&ndash;$5,000',
  included=['Clinically appropriate 3D imaging','Digitally planned surgical implant guide',
            'Dental implant placement','Final ceramic crown','Bone grafting when in the selected pathway'],
  cardcta='Book my consultation', cardfine='One package &mdash; surgery and the crown, not two separate bills.',
  cfk='Single implant &middot; from $3,750', cfh='Book your consultation', cfsubmit='Request my consultation',
  who=['Myself','My partner','My parent','Someone else'],
  cfdone='Thank you &mdash; the implant team will call you back to confirm your consultation and let you know '
         'whether imaging can be done on the same visit.',
  promok='Single implant + crown', promoh2='What the package <em>actually covers.</em>',
  video='7Ci0z84BpDI', videoalt='Dental implants at the Austin Institute of Dental Medicine',
  videoled='Dental implants at AIDM', badge=('$3,750', 'From, all in'),
  promoimg=SMILE_M, promoalt='A man smiling confidently outdoors',
  promofine='The final package price depends on the restoration selected and whether bone grafting is needed, and '
    'sits between $3,750 and $5,000. Package pricing applies only to the services specifically listed and cannot be '
    'combined with insurance benefits, membership pricing or other discounts.',
  perks=IMPLANT_PERKS,
  stepsk='Usually three to six months, start to finish',
  stepsh2='How a single implant <em>actually goes.</em>',
  stepssub='An implant is not one appointment. It is a short sequence with healing in between &mdash; and the fee '
    'covers the whole sequence, not the first part of it.',
  steps=[('Consult and 3D imaging','A cone-beam scan shows the bone that has to hold the implant. That, and the '
          'restoration you choose, is what places you in the $3,750&ndash;$5,000 range.'),
         ('Guided placement','The implant is placed through a digitally planned surgical guide, so its position is '
          'decided on a screen before it is decided in your mouth. Grafting is done here if your pathway includes it.'),
         ('Healing','The implant integrates with the bone over roughly three to six months. You are not left with a '
          'gap in the meantime if the site is visible.'),
         ('The final crown','A ceramic crown is made to match the teeth either side and fitted to the implant. That '
          'crown is in the package price &mdash; it is not a second invoice.')],
  stepsfine='If the tooth is still in place, ask about the extraction and the implant together at the same consult &mdash; '
    'planning them as one sequence usually preserves more bone than dealing with them separately.',
  staffsub='Board-certified faculty, specialists and residents working side by side &mdash; with surgery, '
    'periodontics and prosthodontics in the same building, so the surgeon and the person making your crown are '
    'planning the same case.',
  films=[('7Ci0z84BpDI','Dental implants at AIDM &mdash; how cases are planned and placed','Start here'),
         ('cCUQyiHkJxg','Prosthodontics'),('k9PavRdjiyc','Comfort, sedation &amp; anxiety care'),
         ('QNsMOG1B6G8','Welcome to AIDM'),('2ooc1MlkmNM','What to expect at your first visit'),
         ('f7HHTbB-qe8','Comprehensive dental care')],
  filmlane='More about AIDM', filmsub='The building, the clinicians and the treatments &mdash; in their own words.',
  frows=[dict(img=XRAY_TALK, alt='An AIDM dentist explaining a patient&rsquo;s scan on a chairside screen',
      cap='The bone decides the plan, and you see it too',
      k='Why it matters', h2='The gap does not <em>stay a gap.</em>',
      p='Bone that no longer carries a tooth starts to shrink within months, and the teeth either side drift into '
        'the space while the one above it drops down. What began as one missing tooth quietly becomes a bite problem '
        'and, eventually, a bigger and more expensive reconstruction than the implant would have been.',
      bullets=['An implant loads the bone the way a root does, which is what keeps the bone there',
               'Neighbouring teeth are left untouched &mdash; unlike a bridge, which has to be cut down',
               'The longer a site is left empty, the more likely grafting becomes part of the plan']),
    dict(img=RES_PATIENT, alt='An AIDM clinician reviewing records with a patient chairside',
      cap='Surgery and the crown planned by the same building',
      k='Who treats you', h2='Two clinicians. <em>One fee.</em>',
      p='AIDM is a teaching institute. Residents &mdash; already qualified dentists in advanced postgraduate training '
        '&mdash; treat under the direct supervision of licensed clinical faculty. Surgery, periodontics and '
        'prosthodontics are all in the building, so nobody is working from someone else&rsquo;s letter.',
      bullets=['A second, faculty-level opinion built into the plan at no extra charge',
               'One package covering imaging, the guide, the implant and the final crown',
               'Fees in writing before anything is scheduled'])],
  optsk='Implant options, published',
  optsh2='One tooth, one arch, <em>or somewhere between.</em>',
  optssub='All three implant packages are published in full. Which one applies is a clinical question about how much '
    'is missing and what the bone will carry &mdash; not a budget question.',
  opts=implant_cards('single', XRAY_TALK, 'An AIDM dentist explaining a patient&rsquo;s scan on a chairside screen'),
  faq=[('Why is the price a range and not one number?',
        'Because two things move it: which restoration you choose, and whether the site needs bone grafting before an '
        'implant can be placed. Those are decided from your 3D scan at the consult, and the package price for your own '
        'case &mdash; somewhere between $3,750 and $5,000 &mdash; is given to you in writing before anything starts.'),
       ('Is the crown really included?',
        'Yes. The package covers clinically appropriate 3D imaging, the digitally planned surgical guide, the implant '
        'placement, the final ceramic crown, and bone grafting where it is part of the selected pathway. That is '
        'deliberately the whole sequence, because implant pricing quoted for the surgery alone is how people end up '
        'with a second invoice they did not expect.'),
       ('How long does the whole thing take?',
        'Usually three to six months from placement to the final crown, because the implant has to integrate with the '
        'bone in between. If the site is visible you are not left with a gap while that happens.'),
       ('Is it painful?',
        'Placement is done under local anaesthetic and most people describe it as easier than an extraction. Comfort, '
        'sedation and anxiety care is available and is quoted separately from the treatment fee, so you can see both '
        'numbers and choose.'),
       ('Could a bridge be better for me?',
        'Sometimes &mdash; and you will be told so. The trade-off is that a conventional bridge means cutting down the '
        'healthy teeth either side of the gap, and it does not stop the bone under the gap from shrinking. An implant '
        'leaves the neighbours alone. Which is right depends on those neighbours and on your bone.'),
       ('Will a student be doing my surgery?',
        'You will be treated by a licensed dentist. AIDM is a teaching institute, so residents in advanced postgraduate '
        'training treat under the direct supervision of licensed clinical faculty, and every plan is reviewed by faculty '
        'before it is quoted. That two-clinician model is why the published fees are what they are.'),
       ('Can I use insurance or finance it?',
        'AIDM accepts many PPO plans, and financing may be available subject to approval. Package pricing applies only '
        'to the services listed and cannot be combined with insurance benefits, membership pricing or other discounts '
        'unless expressly stated &mdash; at the consult you will be shown both routes side by side.'),
       ('Do I need a referral, and where do I park?',
        'No referral is needed. There is a garage immediately next door at 1401 Philomena Street and parking is free. '
        'The building is in Mueller, minutes from I-35 and 51st Street.')],
  ctk='Imaging, implant and crown in one package',
  cth2='One missing tooth? <em>Let&rsquo;s look at the bone.</em>',
  ctsub='Leave your details and the implant team will call you back to confirm a consultation &mdash; usually the same '
        'working day. You will have your own package price in writing before anything is scheduled.',
  wholabel='Who is the treatment for?',
  who2=['Myself','My partner','My parent','Someone else'],
  placeholder='How long has the tooth been missing? Any previous scans or a referral letter?',
  ctsubmit='Book my consultation',
  terms=[('The offer','A single dental implant with a final ceramic crown, from $3,750, with the package price for your case falling between $3,750 and $5,000.'),
         ('Who it is for','Patients replacing one missing or failing tooth whose bone and general health make implant treatment appropriate. Suitability is confirmed at your consultation.'),
         ('What is included','Clinically appropriate 3D imaging, a digitally planned surgical implant guide, implant placement, the final ceramic crown, and bone grafting when included in the selected treatment pathway.'),
         ('Eligibility','Package pricing applies only to the services specifically listed and cannot be combined with insurance benefits, membership pricing, financing promotions or other discounts unless expressly stated.'),
         ('Important to know','The final package price depends on the restoration selected and whether bone grafting is needed. Sedation and anaesthesia are additional. Individual treatment results vary.')],
)

# ══════════════════════════════════════════════════════════════════════════
FULLARCH = dict(
  cta='Book Free Consult',
  slug='full-arch', id='full-arch-fixed-teeth-from-18000', banner='FULL-ARCH FIXED TEETH',
  title='A Full Smile. A Fresh Start. — Full-Arch Fixed Teeth from $18,000 an Arch | AIDM Austin',
  desc='Fixed full-arch teeth on four to six dental implants from $18,000 per arch at the Austin Institute of Dental Medicine in Mueller, Austin. Three published tiers: $18,000, $22,000 and $26,000.',
  ogtitle='A Full Smile. A Fresh Start. — Full-Arch Fixed Teeth from $18,000 | AIDM Austin',
  ogdesc='Diagnostics, four to six implants, multi-unit abutments, interim fixed teeth and the final fixed restoration — per arch.',
  ogimg=OG_OP,
  nav=NAV_STD, navcta='Book a Consult',
  h1=['A Full Smile.', 'A Fresh Start.'],
  pill='Three published tiers', cardtitle='Full-Arch Fixed Teeth (All-on-X)',
  cardprice='<span class="fr">from</span><span class="c">$</span><span class="v">18,000</span>',
  cardsub='Per arch &middot; moderate $22,000 &middot; complex $26,000',
  included=['Comprehensive diagnostic work-up','Four to six conventional dental implants',
            'Multi-unit abutments','Interim complete and fixed teeth','Final fixed full-arch restoration'],
  cardcta='Book my consultation', cardfine='Your tier is set by the case, and stated before you commit.',
  cfk='Full-arch fixed teeth &middot; from $18,000', cfh='Book your consultation', cfsubmit='Request my consultation',
  who=['Myself','My partner','My parent','Someone else'],
  cfdone='Thank you &mdash; the implant team will call you back to confirm your consultation. The tier your case '
         'falls into is decided from imaging, and you will have it in writing before anything is booked.',
  promok='Full-arch fixed teeth', promoh2='Fixed teeth. <em>Three published tiers.</em>',
  video='cCUQyiHkJxg', videoalt='Prosthodontics at the Austin Institute of Dental Medicine',
  videoled='Prosthodontics at AIDM', badge=('$18,000', 'Per arch, from'),
  promoimg=SENIOR_JOY, promoalt='An older woman laughing with her daughter',
  promofine='Your treatment tier is based on extractions, grafting, bone condition, and case complexity. Advanced '
    'reconstruction or services outside the standard package require a custom treatment plan. Package pricing applies '
    'only to the services specifically listed and cannot be combined with insurance benefits or other discounts.',
  perks=IMPLANT_PERKS,
  stepsk='One arch, one coordinated plan',
  stepsh2='How a full arch <em>gets rebuilt.</em>',
  stepssub='Full-arch treatment is a sequence, and every stage of it is inside the package price &mdash; including the '
    'interim teeth you wear while the implants integrate.',
  steps=[('Diagnostic work-up','Imaging and a full assessment of what is left, what has to come out, and what the bone '
          'will carry. This is what places your case in the $18,000, $22,000 or $26,000 tier.'),
         ('Implants placed','Any remaining failing teeth are removed and four to six implants are placed in the arch, '
          'with multi-unit abutments fitted to carry the restoration.'),
         ('Interim fixed teeth','You leave with teeth. Interim complete and fixed teeth are part of the package, so '
          'there is no period spent without them while the implants integrate.'),
         ('The final restoration','Once the implants have integrated, the definitive fixed full-arch restoration is '
          'made and fitted. That final restoration is in the tier price.')],
  stepsfine='The three tiers exist because arches differ enormously &mdash; how many teeth have to come out, whether '
    'grafting is needed, and what condition the bone is in. Nobody is quoted a tier before their imaging is read.',
  staffsub='Board-certified faculty, specialists and residents working side by side &mdash; surgery, periodontics and '
    'prosthodontics in one building, which for full-arch work is the difference between one plan and three opinions.',
  films=[('cCUQyiHkJxg','Prosthodontics at AIDM &mdash; rebuilding a full arch','Start here'),
         ('7Ci0z84BpDI','Dental implants'),('k9PavRdjiyc','Comfort, sedation &amp; anxiety care'),
         ('QNsMOG1B6G8','Welcome to AIDM'),('2ooc1MlkmNM','What to expect at your first visit'),
         ('f7HHTbB-qe8','Comprehensive dental care')],
  filmlane='More about AIDM', filmsub='The building, the clinicians and the treatments &mdash; in their own words.',
  frows=[dict(img=SENIOR_M, alt='A man in his sixties smiling confidently outdoors',
      cap='Fixed means fixed — they do not come out at night',
      k='Why it matters', h2='A failing arch is <em>not just a dental problem.</em>',
      p='Teeth that are loose, painful or missing across a whole arch change what you can eat long before they change '
        'how you look, and diet narrows to what can be managed rather than what is good for you. Fixed full-arch teeth '
        'on implants restore chewing function rather than merely covering the gap, and unlike a conventional denture '
        'they do not rest on &mdash; and shrink &mdash; the gum.',
      bullets=['Implants load the jawbone, which is what slows the bone loss a denture accelerates',
               'Fixed, not removable: they are cleaned in place, not taken out',
               'Chewing function is restored rather than approximated']),
    dict(img=DOC_RES, alt='An AIDM faculty member and resident treating a patient together',
      cap='Surgery and prosthodontics planning the same arch',
      k='Who treats you', h2='Two clinicians. <em>One fee.</em>',
      p='AIDM is a teaching institute. Residents in advanced postgraduate training treat under the direct supervision '
        'of licensed clinical faculty, and every full-arch plan is reviewed by faculty before it is quoted. Full-arch '
        'work is where the teaching model pays for itself: it is the treatment most often quoted at two or three times '
        'this figure elsewhere.',
      bullets=['A second, faculty-level opinion built into the plan at no extra charge',
               'Interim fixed teeth included &mdash; you are never sent home without teeth',
               'The tier, and the reason for it, in writing before anything is scheduled'])],
  optsk='Full-arch pricing, by tier',
  optsh2='Three tiers. <em>Same package.</em>',
  optssub='Every tier contains the same five things. What moves the price is the state of the arch it is going into '
    '&mdash; how many extractions, how much grafting, what the bone will carry, and how complex the case is.',
  opts=[dict(img=PIC['implant'], imgalt=PALT['implant'], imgpos='center 48%',
      sub='Straightforward arch', h3='Simple', amt='$18,000', strike='Per arch',
      d='An arch where the extractions are straightforward, the bone is sound and no significant grafting is required.',
      ul=['Comprehensive diagnostic work-up','Four to six conventional dental implants','Multi-unit abutments',
          'Interim complete and fixed teeth','Final fixed full-arch restoration'],
      fine='Tier is based on extractions, grafting, bone condition and case complexity, determined from imaging.',
      cta='Ask which tier I am in'),
    dict(img=PIC['surgery'], imgalt=PALT['surgery'], imgpos='center 40%',
      feat=True, flag='Most common', sub='Some grafting or extractions', h3='Moderate', amt='$22,000',
      strike='Per arch',
      d='An arch needing more extraction work, some grafting, or where bone condition makes placement more demanding.',
      ul=['Comprehensive diagnostic work-up','Four to six conventional dental implants','Multi-unit abutments',
          'Interim complete and fixed teeth','Final fixed full-arch restoration'],
      fine='Tier is based on extractions, grafting, bone condition and case complexity, determined from imaging.',
      cta='Book my consultation'),
    dict(img=PIC['tools'], imgalt=PALT['tools'], imgpos='center 42%',
      sub='Demanding reconstruction', h3='Complex', amt='$26,000', strike='Per arch',
      d='An arch where extensive extraction, grafting or compromised bone makes the reconstruction substantially more involved.',
      ul=['Comprehensive diagnostic work-up','Four to six conventional dental implants','Multi-unit abutments',
          'Interim complete and fixed teeth','Final fixed full-arch restoration'],
      fine='Advanced reconstruction or services outside the standard package require a custom treatment plan.',
      cta='Ask which tier I am in')],
  alsoh='The other implant packages, if a full arch is more than you need',
  also=[('Snap-In Dentures (implant-supported)','Removable, implant-retained &mdash; $9,500 / $12,500 / $17,000 per arch','from $9,500'),
        ('Single Implant + Crown','One missing tooth, imaging, implant and the final ceramic crown','from $3,750'),
        ('Wisdom teeth &amp; extractions','Priced per tooth by surgical position, if teeth have to come out first','from $200')],
  faq=[('What decides whether I am $18,000, $22,000 or $26,000?',
        'Four things: how many teeth have to be extracted, how much grafting the arch needs, the condition of the bone, '
        'and the overall complexity of the case. All four are read from your imaging at the consultation, and the tier '
        'you fall into &mdash; with the reason for it &mdash; is given to you in writing before anything is scheduled.'),
       ('Is that price per arch or for the whole mouth?',
        'Per arch. If both the upper and lower arches need rebuilding, that is two packages. It is stated per arch '
        'precisely so that nobody discovers the distinction at the wrong moment.'),
       ('Will I be without teeth at any point?',
        'No. Interim complete and fixed teeth are part of the package, so you leave the surgical appointment with teeth '
        'and wear them while the implants integrate. The definitive fixed restoration is made and fitted afterwards, '
        'and it is included in the tier price.'),
       ('How is this different from snap-in dentures?',
        'Full-arch fixed teeth are fixed &mdash; they are cleaned in place and you do not take them out. Snap-in dentures '
        'are implant-supported but removable, sit on two or four implants rather than four to six, and start at $9,500 '
        'per arch. Fixed costs more and feels closer to natural teeth; removable costs less and is easier to clean.'),
       ('How long does the whole thing take?',
        'Placement is one surgical appointment; integration takes months, during which you are wearing the interim '
        'fixed teeth; then the final restoration is made and fitted. Your own timeline is set at the consultation once '
        'the imaging has been read.'),
       ('Will a student be doing my surgery?',
        'You will be treated by a licensed dentist. AIDM is a teaching institute, so residents in advanced postgraduate '
        'training treat under the direct supervision of licensed clinical faculty, and every full-arch plan is reviewed '
        'and signed off by faculty. That is exactly why this treatment is priced where it is.'),
       ('Can I use insurance or finance it?',
        'AIDM accepts many PPO plans and financing may be available subject to approval, but neither can be stacked on '
        'top of package pricing. At the consultation the team will show you both routes side by side.'),
       ('What if my case needs more than the standard package?',
        'Then it is quoted as a custom treatment plan rather than squeezed into a tier. Advanced reconstruction and '
        'services outside the standard package are priced separately and stated separately.')],
  ctk='Three published tiers &middot; $18,000 &middot; $22,000 &middot; $26,000',
  cth2='A full smile. <em>Let&rsquo;s start with the scan.</em>',
  ctsub='Leave your details and the implant team will call you back to confirm a consultation &mdash; usually the same '
        'working day. Your tier, and the reason for it, comes in writing before anything is scheduled.',
  wholabel='Who is the treatment for?',
  who2=['Myself','My partner','My parent','Someone else'],
  placeholder='Upper arch, lower arch or both? Any current denture or previous treatment?',
  ctsubmit='Book my consultation',
  terms=[('The offer','Fixed full-arch teeth on four to six conventional dental implants, priced per arch in three tiers: simple $18,000, moderate $22,000, complex $26,000.'),
         ('Who it is for','Patients replacing an entire arch of missing or failing teeth whose bone and general health make implant treatment appropriate. Suitability is confirmed at your consultation.'),
         ('What is included','A comprehensive diagnostic work-up, four to six implants, multi-unit abutments, interim complete and fixed teeth, and the final fixed full-arch restoration — per arch.'),
         ('What sets the tier','Extractions, grafting, bone condition and case complexity, determined from imaging. Advanced reconstruction or services outside the standard package require a custom treatment plan.'),
         ('Eligibility','Package pricing applies only to the services specifically listed and cannot be combined with insurance benefits, membership pricing, financing promotions or other discounts unless expressly stated. Sedation and anaesthesia are additional.')],
)

# ══════════════════════════════════════════════════════════════════════════
SNAPIN = dict(
  cta='Book Free Consult',
  slug='snap-in-dentures', id='snap-in-dentures-from-9500', banner='SNAP-IN DENTURES',
  title='More Stability. More Confidence. — Implant-Supported Dentures from $9,500 an Arch | AIDM Austin',
  desc='Snap-in, implant-supported dentures from $9,500 per arch at the Austin Institute of Dental Medicine in Mueller, Austin. Three published tiers: $9,500, $12,500 and $17,000.',
  ogtitle='More Stability. More Confidence. — Implant-Supported Dentures from $9,500 | AIDM',
  ogdesc='Two or four implants, attachments, and both interim and final removable dentures — per arch, from $9,500.',
  ogimg=OG_OP,
  nav=NAV_STD, navcta='Book a Consult',
  h1=['More Stability.', 'More Confidence.'],
  pill='Three published tiers', cardtitle='Implant-Supported Dentures',
  cardprice='<span class="fr">from</span><span class="c">$</span><span class="v">9,500</span>',
  cardsub='Per arch &middot; moderate $12,500 &middot; complex $17,000',
  included=['Comprehensive evaluation and planning','Clinically appropriate imaging',
            'Two or four implants based on the tier','Implant attachments','Interim and final removable dentures'],
  cardcta='Book my consultation', cardfine='They snap in, and they stay in until you take them out.',
  cfk='Implant-supported dentures &middot; from $9,500', cfh='Book your consultation', cfsubmit='Request my consultation',
  who=['Myself','My partner','My parent','Someone else'],
  cfdone='Thank you &mdash; the team will call you back to confirm your consultation. Which tier applies is decided '
         'from imaging, and you will have it in writing before anything is booked.',
  promok='Snap-in dentures', promoh2='A denture that <em>does not move.</em>',
  video='cCUQyiHkJxg', videoalt='Prosthodontics at the Austin Institute of Dental Medicine',
  videoled='Prosthodontics at AIDM', badge=('$9,500', 'Per arch, from'),
  promoimg=CAMPING, promoalt='A man in his sixties smiling outdoors at a campsite',
  promofine='Complete package pricing is based on the selected clinical pathway; the clinical package name is '
    'Implant-Supported Removable Overdenture. Package pricing applies only to the services specifically listed and '
    'cannot be combined with insurance benefits, membership pricing or other discounts.',
  perks=IMPLANT_PERKS,
  stepsk='Removable, but anchored',
  stepsh2='How snap-in dentures <em>are fitted.</em>',
  stepssub='The difference between this and a conventional denture is two or four implants and the attachments that '
    'clip onto them &mdash; and both are inside the package price, along with both sets of dentures.',
  steps=[('Evaluation and imaging','A full assessment and clinically appropriate imaging establish how much bone there '
          'is to work with. That decides whether your pathway uses two implants or four, and which tier applies.'),
         ('Implants placed','Two or four implants are placed in the arch, depending on the tier. Attachments are fitted '
          'to them &mdash; these are the parts the denture actually clips onto.'),
         ('Interim denture','You wear an interim removable denture while the implants integrate. It is part of the '
          'package, not an extra.'),
         ('The final denture','Once the implants have integrated, the final removable denture is made to fit the '
          'attachments. It snaps in, it stays put while you eat, and it comes out for cleaning.')],
  stepsfine='If you already wear a conventional denture, bring it to the consultation &mdash; how it fits now says a '
    'great deal about how much bone is left and which pathway is realistic.',
  staffsub='Board-certified faculty, specialists and residents working side by side, with surgery and prosthodontics '
    'in the same building &mdash; the people placing the implants and the people making the denture are in the same '
    'case review.',
  films=[('cCUQyiHkJxg','Prosthodontics at AIDM &mdash; dentures, crowns and full-mouth work','Start here'),
         ('7Ci0z84BpDI','Dental implants'),('k9PavRdjiyc','Comfort, sedation &amp; anxiety care'),
         ('QNsMOG1B6G8','Welcome to AIDM'),('2ooc1MlkmNM','What to expect at your first visit'),
         ('f7HHTbB-qe8','Comprehensive dental care')],
  filmlane='More about AIDM', filmsub='The building, the clinicians and the treatments &mdash; in their own words.',
  frows=[dict(img=FREEDOM, alt='Two people cycling along a pier at sunset',
      cap='Eating what you want, in company, without thinking about it',
      k='Why it matters', h2='A denture that slips <em>changes what you eat.</em>',
      p='Conventional dentures rest on the gum, and the gum keeps shrinking underneath them &mdash; which is why they '
        'fit worse every year. What most people notice is not the fit but the retreat: harder foods go first, then '
        'eating in company, then a diet built around what can be managed rather than what is wanted. Implants stop '
        'the denture moving, and loading the bone slows the shrinkage that caused the problem.',
      bullets=['Two or four implants anchor the denture instead of the gum and suction doing all the work',
               'Bite force is meaningfully higher than a conventional denture allows',
               'Still removable, so it is straightforward to clean properly']),
    dict(img=RES_PATIENT, alt='An AIDM clinician reviewing records with a patient chairside',
      cap='Two clinicians at the chair, on the same appointment',
      k='Who treats you', h2='Two clinicians. <em>One fee.</em>',
      p='AIDM is a teaching institute. Residents in advanced postgraduate training treat under the direct supervision '
        'of licensed clinical faculty, and prosthodontics is a named programme here rather than something sent out to '
        'a lab and hoped for.',
      bullets=['A second, faculty-level opinion built into the plan at no extra charge',
               'Both the interim and the final denture are inside the package price',
               'The tier, and the reason for it, in writing before anything is scheduled'])],
  optsk='Snap-in denture pricing, by tier',
  optsh2='Three tiers. <em>Same package.</em>',
  optssub='Every tier contains the same five things. What moves the price is how much bone there is to anchor to, and '
    'therefore whether the pathway uses two implants or four.',
  opts=[dict(img=PIC['implant'], imgalt=PALT['implant'], imgpos='center 48%',
      sub='Two implants', h3='Simple', amt='$9,500', strike='Per arch',
      d='The straightforward pathway: sound bone, a clean arch, and two implants carrying the denture.',
      ul=['Comprehensive evaluation and planning','Clinically appropriate imaging','Two implants',
          'Implant attachments','Interim and final removable dentures'],
      fine='Complete package pricing based on the selected clinical pathway, determined at your evaluation.',
      cta='Ask which tier I am in'),
    dict(img=PIC['family'], imgalt=PALT['family'], imgpos='center 30%',
      feat=True, flag='Most common', sub='More anchorage', h3='Moderate', amt='$12,500', strike='Per arch',
      d='A pathway using more implants or requiring more preparatory work to give the denture solid anchorage.',
      ul=['Comprehensive evaluation and planning','Clinically appropriate imaging','Two or four implants',
          'Implant attachments','Interim and final removable dentures'],
      fine='Complete package pricing based on the selected clinical pathway, determined at your evaluation.',
      cta='Book my consultation'),
    dict(img=PIC['surgery'], imgalt=PALT['surgery'], imgpos='center 40%',
      sub='Compromised bone', h3='Complex', amt='$17,000', strike='Per arch',
      d='An arch where bone condition makes placement substantially more demanding and four implants are required.',
      ul=['Comprehensive evaluation and planning','Clinically appropriate imaging','Four implants',
          'Implant attachments','Interim and final removable dentures'],
      fine='Complete package pricing based on the selected clinical pathway, determined at your evaluation.',
      cta='Ask which tier I am in')],
  alsoh='The other implant packages, side by side',
  also=[('Full-Arch Fixed Teeth (All-on-X)','Fixed rather than removable, on four to six implants &mdash; $18,000 / $22,000 / $26,000','from $18,000'),
        ('Single Implant + Crown','One missing tooth, imaging, implant and the final ceramic crown','from $3,750'),
        ('Wisdom teeth &amp; extractions','Priced per tooth by surgical position, if teeth have to come out first','from $200')],
  faq=[('What is the clinical name for this?',
        'Implant-Supported Removable Overdenture. &ldquo;Snap-in dentures&rdquo; is what patients actually call them, '
        'and it describes what they do &mdash; they clip onto attachments fitted to implants in the jaw, and they come '
        'out for cleaning.'),
       ('What decides whether I am $9,500, $12,500 or $17,000?',
        'How much bone there is to anchor to, and therefore whether the pathway uses two implants or four, plus how much '
        'preparatory work the arch needs. All of that is read from imaging at the evaluation and the tier is given to '
        'you in writing before anything is scheduled.'),
       ('How is this different from full-arch fixed teeth?',
        'These are removable: they snap onto two or four implants and you take them out to clean them, from $9,500 per '
        'arch. Full-arch fixed teeth are permanently fixed on four to six implants and cleaned in place, from $18,000 '
        'per arch. Fixed feels closer to natural teeth; removable costs a good deal less and is easier to clean.'),
       ('Is it better than the denture I have now?',
        'Almost certainly, if your current one moves. A conventional denture is held by suction and by the shape of the '
        'gum, both of which get worse as the bone shrinks underneath. Implants anchor the denture mechanically, so it '
        'stays where it is put while you eat.'),
       ('Is that price per arch?',
        'Yes. If both arches need doing, that is two packages. It is stated per arch specifically so that the '
        'distinction is clear before anyone commits.'),
       ('Do I get a denture while the implants heal?',
        'Yes &mdash; interim and final removable dentures are both inside the package price. You are not sent away '
        'without teeth while the implants integrate.'),
       ('Will a student be treating me?',
        'You will be treated by a licensed dentist. AIDM is a teaching institute, so residents in advanced postgraduate '
        'training treat under the direct supervision of licensed clinical faculty, and every plan is reviewed by faculty '
        'before it is quoted.'),
       ('Can I use insurance or finance it?',
        'AIDM accepts many PPO plans and financing may be available subject to approval, but neither can be combined with '
        'package pricing. At the evaluation you will be shown both routes side by side.')],
  ctk='Three published tiers &middot; $9,500 &middot; $12,500 &middot; $17,000',
  cth2='Tired of a denture that moves? <em>Let&rsquo;s anchor it.</em>',
  ctsub='Leave your details and the team will call you back to confirm a consultation &mdash; usually the same working '
        'day. Bring your current denture if you wear one; it tells us a great deal.',
  wholabel='Who is the treatment for?',
  who2=['Myself','My partner','My parent','Someone else'],
  placeholder='Upper arch, lower arch or both? Do you wear a denture now, and how does it fit?',
  ctsubmit='Book my consultation',
  terms=[('The offer','Implant-supported removable dentures, priced per arch in three tiers: simple $9,500, moderate $12,500, complex $17,000. Clinical package name: Implant-Supported Removable Overdenture.'),
         ('Who it is for','Patients replacing an arch of missing teeth who want implant retention rather than a conventional denture. Suitability is confirmed at your evaluation.'),
         ('What is included','Comprehensive evaluation and planning, clinically appropriate imaging, two or four implants depending on the tier, implant attachments, and both the interim and final removable dentures — per arch.'),
         ('Eligibility','Complete package pricing is based on the selected clinical pathway. Package pricing applies only to the services specifically listed and cannot be combined with insurance benefits, membership pricing, financing promotions or other discounts unless expressly stated.'),
         ('Important to know','Sedation and anaesthesia, additional diagnostics and laboratory fees are additional. Individual treatment results vary.')],
)

# ══════════════════════════════════════════════════════════════════════════
ROOTCANAL = dict(
  cta='Book Appointment',
  slug='root-canal', id='root-canal-from-995', banner='ROOT CANAL',
  title='Save Your Tooth. Restore Your Smile. — Root Canal from $995 | AIDM Austin',
  desc='Root canal treatment from $995 at the Austin Institute of Dental Medicine in Mueller, Austin, or bundled with a ceramic crown at $2,300 to $2,500. Limited-field 3D imaging included.',
  ogtitle='Save Your Tooth. Restore Your Smile. — Root Canal from $995 | AIDM Austin',
  ogdesc='Limited-field 3D imaging, initial root canal treatment, and a crown bundle at $2,300–$2,500 that rebuilds the tooth properly.',
  ogimg=OG_OP,
  nav=NAV_STD, navcta='Book a Consult',
  h1=['Save Your Tooth.', 'Restore Your Smile.'],
  pill='Save it, and rebuild it', cardtitle='Root Canal Treatment',
  cardprice='<span class="fr">from</span><span class="c">$</span><span class="v">995</span>',
  cardsub='With ceramic crown $2,300 &middot; $2,400 &middot; $2,500',
  included=['Limited-field 3D imaging','Initial root canal treatment',
            'Protective core buildup (crown bundle)','Porcelain or ceramic crown (crown bundle)',
            'Coordinated endodontic and restorative care'],
  cardcta='Book my consultation', cardfine='The tooth is saved and rebuilt by the same building.',
  cfk='Root canal &middot; from $995', cfh='Book your consultation', cfsubmit='Request my consultation',
  who=['Myself','My teenager','My child','Someone else'],
  cfdone='Thank you &mdash; the team will call you back to confirm a consultation. If the tooth is painful now, call '
         '<a href="tel:+17374342436">(737) 434-2436</a> and ask for a same-day emergency slot instead.',
  promok='Root canal treatment', promoh2='What $995 <em>actually covers.</em>',
  video='f7HHTbB-qe8', videoalt='Comprehensive dental care at the Austin Institute of Dental Medicine',
  videoled='Comprehensive dental care at AIDM', badge=('$995', 'From'),
  promoimg=OPERATORY, promoalt='An AIDM operatory with a patient being treated using advanced imaging',
  promofine='Advertised price of $995 applies to standard root canal therapy. Complex cases, including highly '
    'calcified canals or retreatments, may require an adjusted fee, and the final fee is presented prior to the start '
    'of any treatment. The package applies to initial root canal treatment; retreatment and procedures not listed are '
    'additional. The protective core buildup and ceramic crown are part of the crown bundle.',
  perks=[('cal','Book online'),('park','Free parking'),('clock','Monday&ndash;Saturday'),
         ('card','Sedation available'),('star','Endodontics on site')],
  stepsk='Usually one or two appointments',
  stepsh2='How a tooth <em>actually gets saved.</em>',
  stepssub='A root canal has a reputation it stopped deserving decades ago. What it does is remove the infected nerve '
    'tissue that is causing the pain &mdash; the appointment is the thing that ends the ache, not the thing that causes it.',
  steps=[('Diagnosis and 3D imaging','Limited-field 3D imaging shows the root anatomy &mdash; how many canals there '
          'are and what shape they are in. That is what separates a standard case from a complex one.'),
         ('The root canal','Under local anaesthetic, the infected pulp is removed, the canals are cleaned and shaped, '
          'and they are sealed. Most people find it comparable to having a filling done.'),
         ('Rebuilding the tooth','A treated tooth is more brittle than a live one, so it needs a protective core '
          'buildup and, in almost every back tooth, a crown. Both are in the crown bundle price.'),
         ('The ceramic crown','A porcelain or ceramic crown is made and fitted, restoring the shape and the chewing '
          'surface. That is what turns a saved tooth into a tooth you can actually use.')],
  stepsfine='If the tooth is hurting now, do not wait for a routine consultation &mdash; call and ask for a same-day '
    'emergency slot. AIDM is open Monday to Saturday, 7:00 a.m. to 7:00 p.m.',
  staffsub='Board-certified faculty, specialists and residents working side by side &mdash; with endodontics and '
    'restorative dentistry in the same building, so the tooth is sealed and rebuilt as one plan rather than two.',
  films=[('f7HHTbB-qe8','Comprehensive dental care at AIDM &mdash; every specialty under one roof','Start here'),
         ('k9PavRdjiyc','Comfort, sedation &amp; anxiety care'),('NtubApnQFt0','Emergency dental &mdash; same-day care'),
         ('QNsMOG1B6G8','Welcome to AIDM'),('2ooc1MlkmNM','What to expect at your first visit'),
         ('cCUQyiHkJxg','Prosthodontics')],
  filmlane='More about AIDM', filmsub='The building, the clinicians and the treatments &mdash; in their own words.',
  frows=[dict(img=XRAY_TALK, alt='An AIDM dentist explaining a patient&rsquo;s X-ray findings on a chairside screen',
      cap='Limited-field 3D imaging, read back to you',
      k='Why it matters', h2='The alternative is <em>losing the tooth.</em>',
      p='Once the nerve inside a tooth is infected, there are two honest options: clean the inside of the tooth out and '
        'seal it, or take the tooth out. Nothing else resolves it. Antibiotics quieten the symptoms and buy days, not '
        'a cure. Keeping your own root in your own jaw is the outcome every replacement option is trying to imitate.',
      bullets=['Your own tooth holds bone and bite better than anything built to replace it',
               'A single implant and crown starts at $3,750 &mdash; saving the tooth is usually the cheaper answer',
               'Infection at a root tip spreads into bone; time makes it worse, not quieter']),
    dict(img=SMILE_M, alt='A man smiling confidently outdoors',
      cap='Local anaesthetic as standard, sedation if you want it',
      k='Comfort', h2='The part people <em>actually dread.</em>',
      p='&ldquo;Painful as a root canal&rdquo; describes the toothache people arrive with, not the treatment. Under '
        'local anaesthetic the procedure itself is comparable to a large filling, and comfort, sedation and anxiety '
        'care is one of the things AIDM is specifically known for.',
      bullets=['Local anaesthetic is standard; sedation is available and quoted separately',
               'Most cases are done in one or two appointments',
               'Written aftercare, and someone to call if it does not settle as expected'])],
  optsk='Root canal pricing, published',
  optsh2='The treatment, <em>and the crown that finishes it.</em>',
  optssub='A root canal without a crown is half a job on a back tooth &mdash; the tooth is saved but left brittle. The '
    'bundle prices below cover the treatment, the core buildup and the ceramic crown together.',
  opts=[dict(img=XRAY_TALK, imgalt='An AIDM dentist explaining a patient&rsquo;s X-ray findings on a chairside screen', imgpos='center 32%',
      feat=True, flag='This offer', sub='Save your tooth. Restore your smile.', h3='Root Canal Treatment',
      amt='$995', strike='Standard root canal therapy',
      d='Initial root canal treatment on an eligible tooth, with the limited-field 3D imaging needed to see the root anatomy.',
      ul=['Limited-field 3D imaging','Initial root canal treatment','Coordinated endodontic and restorative care',
          'Local anaesthetic included','Final fee presented before treatment starts'],
      fine='Applies to standard root canal therapy. Complex cases, including highly calcified canals or retreatments, '
           'may require an adjusted fee. Retreatment and procedures not listed are additional.',
      cta='Book my consultation'),
    dict(img=PIC['smile'], imgalt=PALT['smile'], imgpos='center 44%',
      sub='Front tooth', h3='Root Canal + Crown', amt='$2,300', strike='Anterior tooth',
      d='The complete bundle for a front tooth: the root canal, a protective core buildup and a porcelain or ceramic crown.',
      ul=['Limited-field 3D imaging','Initial root canal treatment','Protective core buildup',
          'Porcelain or ceramic crown','Coordinated endodontic and restorative care'],
      fine='This package applies to initial root canal treatment. Retreatment and procedures not listed in the package '
           'are additional.', cta='Ask about the bundle'),
    dict(img=PIC['mirror'], imgalt=PALT['mirror'], imgpos='center 44%',
      sub='Back tooth', h3='Root Canal + Crown', amt='$2,400&ndash;$2,500', strike='Premolar $2,400 &middot; molar $2,500',
      d='The same complete bundle for a premolar or a molar &mdash; the teeth that do the chewing, and the ones that '
        'most need a crown afterwards.',
      ul=['Limited-field 3D imaging','Initial root canal treatment','Protective core buildup',
          'Porcelain or ceramic crown','Coordinated endodontic and restorative care'],
      fine='This package applies to initial root canal treatment. Retreatment and procedures not listed in the package '
           'are additional.', cta='Ask about the bundle')],
  alsoh='If the tooth turns out not to be savable',
  also=[('Emergency dental care','If it is hurting now &mdash; same-day, Mon&ndash;Sat 7am&ndash;7pm','Same-day care'),
        ('Extractions','Priced per tooth by surgical position, when the tooth cannot be kept','from $200'),
        ('Single Implant + Crown','Replacing the tooth: imaging, implant and the final ceramic crown','from $3,750'),
        ('New Patient Special','Comprehensive examination and X-rays as needed, if you are new to AIDM','$100')],
  faq=[('Does a root canal hurt?',
        'The toothache that sends you in hurts. The treatment is done under local anaesthetic and most people describe '
        'it as comparable to having a large filling done. Comfort, sedation and anxiety care is available if you want '
        'it, quoted separately from the treatment fee.'),
       ('Why is the crown a separate price?',
        'Because not every treated tooth needs one. A front tooth with a small access cavity may not; a molar that does '
        'the chewing almost always does, because a root-treated tooth is more brittle and splits if it is left '
        'unprotected. The bundle prices &mdash; $2,300 anterior, $2,400 premolar, $2,500 molar &mdash; cover the '
        'treatment, the core buildup and the ceramic crown together.'),
       ('What makes a case &ldquo;complex&rdquo;?',
        'Highly calcified canals, unusual root anatomy, or a tooth that has been root treated before and needs '
        'retreatment. Limited-field 3D imaging at your consultation is what identifies those, and the final fee is '
        'presented to you before any treatment is started.'),
       ('Should I just have it pulled instead?',
        'Rarely the better answer. Your own root maintains bone and bite in a way nothing else does, and replacing the '
        'tooth afterwards &mdash; a single implant and crown starts at $3,750 &mdash; usually costs more than saving it '
        'would have. There are teeth that genuinely cannot be kept, and you will be told plainly when yours is one.'),
       ('How many appointments is it?',
        'Most cases are completed in one or two. If a crown is part of the plan, that is fitted at a further '
        'appointment once the tooth has been rebuilt.'),
       ('My tooth is hurting right now.',
        'Call <a href="tel:+17374342436">(737) 434-2436</a> and ask for a same-day emergency slot rather than booking a '
        'routine consultation. AIDM keeps same-day emergency appointments, Monday to Saturday, 7:00 a.m. to 7:00 p.m.'),
       ('Will a student be treating me?',
        'You will be treated by a licensed dentist. AIDM is a teaching institute with endodontics as a named programme, '
        'so residents in advanced postgraduate training treat under the direct supervision of licensed clinical faculty. '
        'That two-clinician model is why the published fee is what it is.'),
       ('Can I use insurance?',
        'AIDM accepts many PPO plans. Package pricing applies only to the services listed and cannot be combined with '
        'insurance benefits, membership pricing or other discounts unless expressly stated &mdash; at your consultation '
        'the team will show you both routes so you can pick whichever leaves you better off.')],
  ctk='From $995 &middot; with a ceramic crown, $2,300&ndash;$2,500',
  cth2='Save the tooth. <em>Let&rsquo;s look at the root.</em>',
  ctsub='Leave your details and the team will call you back to confirm a consultation &mdash; usually the same working '
        'day. If the tooth is painful right now, calling is faster.',
  wholabel='Who is the treatment for?',
  who2=['Myself','My teenager','My child','Someone else'],
  placeholder='Which tooth, how long it has hurt, and whether there is any swelling…',
  ctsubmit='Book my consultation',
  terms=[('The offer','Initial root canal treatment from $995, or bundled with a protective core buildup and a porcelain or ceramic crown at $2,300 anterior, $2,400 premolar and $2,500 molar.'),
         ('Who it is for','Patients with an eligible tooth whose pulp is infected or irreversibly inflamed. Eligibility is confirmed following clinical evaluation and imaging.'),
         ('What is included','Limited-field 3D imaging, initial root canal treatment and coordinated endodontic and restorative care. The protective core buildup and the ceramic crown are included in the crown bundle prices only.'),
         ('Complex cases','Highly calcified canals and retreatments may require an adjusted fee. Retreatment and procedures not listed in the package are additional. The final fee is presented prior to the start of any treatment.'),
         ('Eligibility','Package pricing applies only to the services specifically listed and cannot be combined with insurance benefits, membership pricing, financing promotions or other discounts unless expressly stated. Sedation and anaesthesia are additional.')],
)

ALL = [IMPLANT, FULLARCH, SNAPIN, ROOTCANAL]
