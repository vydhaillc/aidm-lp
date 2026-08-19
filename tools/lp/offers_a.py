# -*- coding: utf-8 -*-
"""Offers 2, 4, 5 and 9 from the approved promotions sheet."""
U = 'https://aidm.org/wp-content/uploads/'
ORTHO_CHAIR = U + '2026/07/Ortho-Resident-and-Patient-6-1024x683.jpg'
ORTHO_TEAM  = U + '2026/07/Ortho-Team-with-Faculty-Lead-1024x683.jpg'
RES_PATIENT = U + '2026/07/Resident-and-patient-7-1024x683.jpg'
DOC_RES     = U + '2026/07/Ortho-Doc-and-Resident-2-1024x683.jpg'
XRAY_TALK   = U + '2026/01/a-dentist-explains-x-ray-results-to-a-683x1024.jpeg'
EXAM        = U + '2026/07/dentist-examining-a-patient-during-a-dental-1024x683.jpeg'
OPERATORY   = U + '2026/07/a-dentist-examines-a-patient-using-advanced-1024x684.jpeg'
PROCEDURE   = OPERATORY
PAIN        = U + '2026/02/iStock-2-1024x732.jpg'
# AIDM's own emergency-page photography — a patient in the chair holding her jaw,
# and the chairside close-up. Both landscape, both already on aidm.org.
TOOTHACHE   = U + '2025/10/a-dentist-examining-a-young-woman-with-toothache-in-a-dental-clinic.-4971505-1024x683.jpg'
CHAIRSIDE   = U + '2025/09/close-up-of-a-dentist-examining-a-patients-teeth-using-dental-tools.-4269694-1024x683.jpg'
# Card-top portraits, in the spirit of AIDM's printed flyers: a face on every
# package rather than three identical slabs of navy.
SMILE_M     = U + '2026/02/iStock-45-1024x683.jpg'
SMILE_Y     = U + '2026/05/iStock-65-1024x683.jpg'
SMILE_W     = U + '2026/02/iStock-60-1024x683.jpg'
CHAIR_SMILE = U + '2026/04/Pexels-5-1024x683.jpg'
# Treatment photographs the offer itself is about, served from this repo:
# the two clear-aligner shots are AIDM's own orthodontics-page images, and the
# early-treatment boy is lifted from AIDM's Early Orthodontic Treatment flyer.
ALIGNER_IN  = '../aidm-lp-assets/promo/clear-aligner.jpg'
ALIGNER_FIT = '../aidm-lp-assets/promo/clear-aligner-wide.jpg'
ORTHO_PIC = {
 'braces':  ('../aidm-lp-assets/promo/braces-smile.jpg', 'A smile with fixed braces'),
 'aligner': ('../aidm-lp-assets/promo/clear-aligner.jpg', 'A clear aligner being fitted over the teeth'),
 'early':   ('../aidm-lp-assets/promo/early-ortho-boy.jpg', 'A smiling boy with a gap in his front teeth'),
}
EARLY_BOY   = '../aidm-lp-assets/promo/early-ortho-boy.jpg'
OG_LOBBY    = U + '2026/07/13-AIDM-Entrance-Desk-1536x1024.jpg'
OG_OP       = U + '2026/07/16-AIDM-Operatory-01--1536x1024.jpg'


# ── card photography ───────────────────────────────────────────────────────
# All from AIDM's own WordPress library, so nothing here needs a licence we do
# not already have. The card for a page's own offer reuses that page's "why it
# matters" photograph, so the card and the row above describe one offer; the
# rest carry the closest thing the library has to their procedure.
PIC = dict((k, U + v) for k, v in {
 'exam':      '2026/07/dentist-examining-a-patient-during-a-dental-1024x683.jpeg',
 'toothache': '2025/10/a-dentist-examining-a-young-woman-with-toothache-in-a-dental-clinic.-4971505-1024x683.jpg',
 'cleaning':  '2024/08/dental-check-up-6-1024x683.jpeg',
 'appliance': '2024/08/woman-having-dental-check-up-6-1024x683.jpeg',
 'pain':      '2026/01/close-up-of-a-man-holding-his-cheek-displaying-a-wide-open-mouth-against-a-yellow-background.-14624608-1024x683.jpg',
 'aligner':   '2025/10/close-up-of-dental-prosthesis-model-and-tools-in-a-clinic-setting-with-rubber-gloved-hands.-6528782-683x1024.jpg',
 'implant':   '2025/10/detailed-dental-implant-model-showcasing-teeth-structure-for-educational-purposes.-6502305-1024x683.jpg',
 'mirror':    '2025/10/close-up-of-a-childs-mouth-during-a-dental-examination-with-a-mouth-mirror.-6502546-683x1024.jpg',
 'procedure': '2025/09/detailed-close-up-of-a-dental-procedure-with-683x1024.jpeg',
 'xray':      '2025/09/dentist-displaying-dental-x-ray-on-tablet-in-a-modern-clinic.-5355695-683x1024.jpg',
 'child':     '2025/10/a-young-girl-smiling-while-sitting-in-a-dental-chair-ready-for-her-dental-check-up.-7800558-683x1024.jpg',
 'surgery':   '2025/10/dentists-working-on-a-patient-in-a-1024x683.jpeg',
 'tools':     '2025/09/close-up-of-a-dentist-examining-a-patients-teeth-using-dental-tools.-4269694-1024x683.jpg',
 'family':    '2026/07/iStock-1296176774-1024x683.jpg',
 'smile':     '2025/09/close-up-of-a-smiling-woman-with-vibrant-red-lips-and-perfect-teeth.-11956948-1024x1024.jpg',
 'paeds':     '2025/10/dental-professionals-in-protective-gear-attending-to-a-patient-in-a-clinical-setting.-3884093-1024x697.jpg',
}.items())
PALT = {
 'exam':      'A dentist examining a patient in the chair',
 'toothache': 'A patient in the dental chair holding her jaw in pain, with a clinician beside her',
 'cleaning':  'A hygienist cleaning a patient&rsquo;s teeth chairside',
 'appliance': 'A clinician fitting an orthodontic appliance chairside',
 'pain':      'A close-up of an open mouth, the patient holding his cheek in pain',
 'aligner':   'A clear aligner tray held in a gloved hand',
 'implant':   'A model of a dental implant placed in the jawbone beside natural teeth',
 'mirror':    'A mouth mirror examining the teeth during a dental examination',
 'procedure': 'A close-up of a dental procedure in progress',
 'xray':      'A panoramic jaw X-ray displayed on a tablet chairside',
 'child':     'A young girl smiling in the dental chair',
 'surgery':   'Two clinicians carrying out a procedure in the operatory',
 'tools':     'A close-up of a dentist examining a patient&rsquo;s teeth with dental tools',
 'family':    'An older woman laughing with her daughter',
 'smile':     'A close-up of a confident smile',
 'paeds':     'A paediatric dental team attending to a child',
}

NAV_STD = [('office','Our Office'),('promo','The Offer'),('visit','How It Goes'),
           ('staff','Our Team'),('films','Films'),('packages','Pricing'),('faq','FAQ')]
NAV_ORTHO = [('office','Our Office'),('promo','The Offer'),('results','Results'),
             ('staff','Our Team'),('films','Films'),('packages','Options'),('faq','FAQ')]

# The three ortho package cards, reused across the three ortho pages with a
# different one featured on each.
def ortho_cards(feature, own_photo=None, own_alt=''):
    """`own_photo` is the page's own "why it matters" image; the featured card
    takes it so the card and the row above visibly describe one offer."""
    early = dict(img=ORTHO_PIC['early'][0], imgalt=ORTHO_PIC['early'][1], imgpos='center 30%',
        sub='The right care at the right time', h3='Early Orthodontic Treatment',
        amt='$2,500', d='Focused orthodontic care for growing children, when early treatment may help guide dental development.',
        ul=['Limited early orthodontic treatment','Routine treatment visits','Growth-appropriate treatment planning',
            'Retention when included in the treatment plan','Care based on the child&rsquo;s stage of dental development'],
        fine='Standalone appliances and services outside the approved early-treatment plan are priced separately.',
        cta='Ask if this fits')
    braces = dict(img=ORTHO_PIC['braces'][0], imgalt=ORTHO_PIC['braces'][1], imgpos='center 46%',
        sub='Straighten your smile with confidence', h3='Comprehensive Braces',
        amt='$2,950', strike='Promotional fee &mdash; first 100 patients',
        d='A complete fixed-braces package with coordinated orthodontic care from active treatment through standard retention.',
        ul=['Comprehensive braces treatment','Routine orthodontic adjustment visits','Appliance removal',
            'Standard orthodontic retention','Care coordinated throughout treatment'],
        fine='Applies to standard, comprehensive traditional bracket cases. Complex cases, clear aligner therapy or '
             'phase-one interceptive orthodontics may incur additional fees. $2,950 is valid for the first 100 patients, '
             'uninsured and paid in full, and expires 31 October 2026.',
        cta='See the braces offer')
    invis = dict(img=ORTHO_PIC['aligner'][0], imgalt=ORTHO_PIC['aligner'][1], imgpos='center 48%',
        sub='Clear aligners. Confident smile.', h3='Invisalign&reg; Clear Aligners',
        amt='$3,900', d='A discreet, removable option personalised to your smile and supported by routine professional monitoring.',
        ul=['Personalised clear-aligner treatment','Standard aligner laboratory materials','Routine orthodontic visits',
            'Treatment completion and appliance removal','Standard orthodontic retention'],
        fine='Applies to Invisalign&reg; clear-aligner cases. Complex cases, retainers or phase-one interceptive '
             'orthodontics may incur additional fees.',
        cta='Ask if this fits')
    cards = {'early': early, 'braces': braces, 'invis': invis}
    for k, c in cards.items():
        c.setdefault('strike', '&nbsp;')
        if k == feature:
            c['feat'] = True; c['flag'] = 'This offer'; c['cta'] = 'Claim this rate'
            if own_photo:
                c['img'] = own_photo; c['imgalt'] = own_alt; c['imgpos'] = 'center 32%'
    return [cards['early'], cards['braces'], cards['invis']]

LEGAL_ALIGN = ' Invisalign&reg; is a registered trademark of Align Technology, Inc.'

# ══════════════════════════════════════════════════════════════════════════
EMERGENCY = dict(
  cta='Book Appointment',
  slug='emergency', id='emergency-dental-same-day', banner='EMERGENCY DENTAL',
  title='Emergency Dental Care — 7am to 7pm, Monday to Saturday | AIDM Austin',
  desc='Same-day emergency dental appointments at the Austin Institute of Dental Medicine in Mueller. Open Monday to Saturday, 7:00 a.m. to 7:00 p.m., with an onsite surgical centre for urgent extractions.',
  ogtitle='Emergency Dental Care — 7am to 7pm, Mon–Sat | AIDM Austin',
  ogdesc='Seen today. Problem-focused emergency evaluation, X-rays as needed, onsite surgical centre. Mueller, Austin.',
  ogimg=OG_OP,
  nav=NAV_STD, navcta='Get Seen Today', mcall='Call now',
  css='''/* "Same Day Appointments" where the other cards carry a figure — three
   words need to wrap and to sit a size down from the single-word prices. */
.card-price .v.w-tight{font-size:clamp(1.5rem,3.4vw,2.15rem);line-height:1.12;
  max-width:11ch;margin-inline:auto}
/* AIDM's own seven-item list of what counts as an emergency, two-up so it
   does not run the copy column twice the height of the photo beside it. */
.fcopy ul.g2{display:grid;grid-template-columns:1fr 1fr;gap:.55rem 1.4rem}
.fcopy ul.g2 li{font-size:.95rem}
@media(max-width:760px){.fcopy ul.g2{grid-template-columns:1fr}}
/* the footnote marker rides the top of a figure; against wrapped words it
   wants to sit on the last line instead */
/* .ast sets line-height:0 for its superscript trick, which leaves a
   zero-height flex item; give it a box back so flex-end means anything */
.card-price .w-tight ~ .ast-lg{align-self:flex-end;line-height:1;margin-bottom:.15rem}
.opt .amt.amt-words{font-family:var(--head);font-size:1.5rem;font-weight:700;
  line-height:1.16;letter-spacing:0;margin-bottom:.35rem}

''',
  h1=['Emergency Dental Care', '7am to 7pm,', 'Mon&ndash;Sat.'],
  pill='In Pain Today?', cardtitle='Emergency Dental Care',
  cardprice='<span class="v w w-tight">Same Day Appointments</span>',
  included=['Seen today &mdash; same-day appointments',
            'Every specialty under one roof',
            'Problem-focused emergency evaluation',
            'X-rays as needed to diagnose',
            'Onsite surgical centre for urgent extractions'],
  cardcta='Request a same-day slot',
  cardfine='In pain right now? Calling is faster than any form.',
  cfk='Same-day emergency', cfh='Ask for a slot today', cfsubmit='Request a same-day slot',
  who=['Myself','My child','Someone else'],
  cfdone='Thank you &mdash; we will call you straight back to find you a slot. If the pain is severe, '
         'call <a href="tel:+17374342436">(737) 434-2436</a> now rather than waiting for us.',
  promok='Emergency dental care', promoh2='In pain today? <em>Ask for today.</em>',
  video='NtubApnQFt0', videoalt='Emergency dental care at the Austin Institute of Dental Medicine',
  videoled='Emergency dental &mdash; seen today', badge=('7&ndash;7', 'Mon to Sat'),
  promoimg=TOOTHACHE, promoalt='A patient in the dental chair holding her jaw in pain, with a clinician beside her',
  promofine='Emergency appointments are triaged clinically and are subject to availability. A problem-focused '
    'emergency evaluation addresses the presenting problem; any further treatment is quoted before it is started, '
    'and X-rays are taken only where they are needed to diagnose.',
  perks=[('clock','7am&ndash;7pm, Mon&ndash;Sat'),('star','No referral needed'),('park','Free parking'),
         ('card','Insurance welcome'),('cal','Walk-ins triaged')],
  stepsk='From your call to out of pain', stepsh2='How a same-day <em>visit works.</em>',
  stepssub='An emergency appointment is not a check-up. It exists to find what is causing the pain and to stop it '
    'today &mdash; the full plan can wait until you are comfortable.',
  steps=[('Call and describe it','Tell us what hurts, since when, and whether there is swelling, fever or a knocked-out '
          'tooth. That is what decides how fast you need to be seen.'),
         ('Triage and a time','You are given the earliest clinically appropriate slot. Severe swelling, trauma and '
          'uncontrolled bleeding jump the queue.'),
         ('Diagnose the cause','A problem-focused evaluation with the X-rays needed to see what is going on &mdash; '
          'an abscess, a crack, a lost filling, an impacted tooth.'),
         ('Relieve it today','Whatever can be done safely on the day is done on the day, with the fee agreed first. '
          'An onsite surgical centre means an urgent extraction does not need a second appointment elsewhere.')],
  stepsfine='If you have facial swelling that is spreading, difficulty breathing or swallowing, or uncontrolled '
    'bleeding, treat it as a medical emergency and go to an emergency room.',
  staffsub='Board-certified faculty, specialists and residents working side by side &mdash; and an onsite surgical '
    'centre, so an urgent extraction does not become a referral to somewhere else.',
  films=[('NtubApnQFt0','Emergency dental at AIDM &mdash; what happens when you walk in','Start here'),
         ('DV9t9dZJauA','Finding us &amp; where to park'),
         ('k9PavRdjiyc','Comfort, sedation &amp; anxiety care'),
         ('QNsMOG1B6G8','Welcome to AIDM'),('f7HHTbB-qe8','Comprehensive dental care'),
         ('2ooc1MlkmNM','What to expect at your first visit'),('CEgwotre0h8','Orthodontics'),
         ('7Ci0z84BpDI','Dental implants'),('cCUQyiHkJxg','Prosthodontics')],
  filmlane='More about AIDM', filmsub='The building, the clinicians and the treatments &mdash; in their own words.',
  frows=[dict(img=TOOTHACHE, alt='A patient in the dental chair holding her jaw in pain, with a clinician beside her',
      cap='If it causes pain or interrupts your day, call us',
      k='Why it matters', h2='What counts as <em>a dental emergency.</em>',
      p='A dental emergency is anything that causes pain or interrupts your daily life. If you are wondering whether '
        'what you have counts, it is best to call. Here are some examples of things that constitute a dental emergency:',
      two_up=True,
      bullets=['Severe toothache or dental pain','Knocked-out or loosened tooth','Cracked or fractured tooth',
               'Lost filling or crown','Abscess or swelling','Bleeding from the mouth','Trauma to the mouth or jaw']),
    dict(img=CHAIRSIDE, alt='A close-up of an AIDM clinician examining a patient&rsquo;s teeth chairside',
      cap='An onsite surgical centre, in the same building',
      k='Why here', h2='Everything under <em>one roof.</em>',
      p='Most practices that see you urgently then refer you on for whatever you actually need. AIDM has '
        'endodontics, oral surgery, periodontics and prosthodontics in the same building, six days a week, so the '
        'treatment that follows the diagnosis can usually be booked immediately rather than chased.',
      bullets=['Onsite surgical centre for urgent extractions',
               'Sedation and anxiety care available for patients who need it',
               'Open 7:00 a.m. to 7:00 p.m., Monday to Saturday &mdash; before and after work'])],
  optsk='What an emergency usually turns out to be',
  optsh2='The visit is urgent. <em>The price is not a surprise.</em>',
  optssub='An emergency evaluation finds the cause; these are the published package fees for the three things it '
    'most often turns out to need. You are told the fee before anything is started.',
  opts=[dict(img=PIC['xray'], imgalt=PALT['xray'], imgpos='center 42%',
      sub='Save the tooth', h3='Root Canal', amt='from $995',
      strike='With a ceramic crown, $2,300&ndash;$2,500',
      d='Preserve an eligible tooth with root canal treatment, and rebuild it with a protective core and a ceramic crown.',
      ul=['Limited-field 3D imaging','Initial root canal treatment','Protective core buildup (crown bundle)',
          'Porcelain or ceramic crown (crown bundle)','Coordinated endodontic and restorative care'],
      fine='Advertised price of $995 applies to standard root canal therapy. Complex cases, including highly '
           'calcified canals or retreatments, may require an adjusted fee.', cta='See root canal pricing'),
    dict(img=TOOTHACHE, imgalt='A patient in the dental chair holding her jaw in pain, with a clinician beside her', imgpos='center 34%',
      feat=True, flag='You are here', sub='Emergency dental care', h3='Emergency Evaluation',
      amt='Same Day Appointments', strike='Problem-focused evaluation', words=True,
      d='The appointment itself: find out what is causing the pain, and deal with what can safely be dealt with today.',
      ul=['Same-day emergency appointments','Every specialty under one roof','Problem-focused emergency evaluation',
          'X-rays as needed to diagnose','Onsite surgical centre for urgent extractions'],
      fine='Emergency appointments are triaged clinically and subject to availability. Any treatment arising is '
           'quoted before it is started.', cta='Request a same-day slot'),
    dict(img=PIC['surgery'], imgalt=PALT['surgery'], imgpos='center 40%',
      sub='When the tooth cannot be kept', h3='Wisdom Teeth &amp; Extractions', amt='from $200',
      strike='Per tooth, by surgical complexity',
      d='Straightforward extraction pricing based on the position and surgical complexity of each tooth.',
      ul=['Simple erupted extraction &mdash; $200 per tooth','Surgical erupted extraction &mdash; $275 per tooth',
          'Soft-tissue impacted &mdash; $300 per tooth','Partial-bony impacted &mdash; $375 per tooth',
          'Complete-bony impacted &mdash; $450 per tooth'],
      fine='The package covers extractions only. Sedation and anaesthesia are billed separately.',
      cta='See extraction pricing')],
  alsoh='Also useful if you are new to AIDM',
  also=[('New Patient Special','Comprehensive examination and X-rays as needed &mdash; once you are out of pain','$100'),
        ('Comfort &amp; sedation','Sedation and anxiety care for patients who need it, priced separately','On evaluation')],
  faq=[('I am in pain right now. What do I do?',
        'Call <a href="tel:+17374342436">(737) 434-2436</a>. Calling beats any form &mdash; we triage over the phone and '
        'give you the earliest clinically appropriate slot. We are open Monday to Saturday, 7:00 a.m. to 7:00 p.m. If you '
        'have spreading facial swelling, difficulty breathing or swallowing, or uncontrolled bleeding, go to an emergency '
        'room instead; that is beyond what any dental practice should be managing.'),
       ('What does an emergency visit cost?',
        'There is no published flat price, because an emergency visit is priced on what it turns out to be. You get a '
        'problem-focused evaluation and the X-rays needed to diagnose the problem, and the fee for any treatment arising '
        'is presented to you before that treatment starts. The three commonest outcomes have published package prices &mdash; '
        'a root canal from $995, an extraction from $200 per tooth &mdash; so you are rarely in unmapped territory.'),
       ('Can you actually treat it the same day, or just look at it?',
        'Whatever can be done safely on the day is done on the day. AIDM has an onsite surgical centre, so an urgent '
        'extraction does not become a referral somewhere else, and endodontics, periodontics and prosthodontics are in the '
        'same building for whatever follows.'),
       ('I do not have insurance. Can I still be seen?',
        'Yes. AIDM is self-pay friendly and publishes package pricing precisely so that uninsured patients can see the '
        'number before they commit. If you do have a plan, many PPOs are accepted.'),
       ('I knocked a tooth out. What do I do right now?',
        'Handle it by the crown, not the root. If it is clean, try to place it back in the socket and bite gently on a '
        'clean cloth; if you cannot, keep it in milk or in your own saliva &mdash; never in water. Then call us immediately. '
        'The chance of saving a replanted tooth falls sharply with every hour.'),
       ('I am extremely anxious about the dentist.',
        'Say so when you call. Comfort, sedation and anxiety care is one of AIDM&rsquo;s named strengths and can be arranged '
        'for emergency treatment as well as planned treatment. Sedation and anaesthesia are billed separately from the '
        'treatment itself.'),
       ('Do you see children for emergencies?',
        'Yes &mdash; paediatric dentistry is part of the same building and the same hours. Tell us the child&rsquo;s age when '
        'you call.'),
       ('Where do I park, and do I need a referral?',
        'No referral. Free parking in the garage immediately next door at 1401 Philomena Street, Mueller &mdash; minutes from '
        'I-35 and 51st Street.')],
  ctk='Open Monday to Saturday, 7am to 7pm', cth2='In pain? <em>Call us first.</em>',
  ctsub='<a href="tel:+17374342436" style="color:#4fc3f7">(737) 434-2436</a> is the fastest route to a slot today. '
        'If you would rather we call you, leave your details and we will ring straight back.',
  wholabel='Who needs to be seen?', who2=['Myself','My child','My partner or parent','Someone else'],
  placeholder='What hurts, since when, and is there any swelling?',
  ctsubmit='Call me back about a slot today',
  terms=[('The offer','A same-day, problem-focused emergency dental evaluation, with X-rays taken as needed to diagnose.'),
         ('Who it is for','Patients with an urgent dental problem. Appointments are triaged clinically and are subject to availability.'),
         ('Pricing','There is no published price for the emergency evaluation. Fees for any treatment arising are presented before that treatment starts.'),
         ('What is not included','Restorative, surgical and specialty treatment arising from the evaluation, laboratory fees, sedation and anaesthesia are additional.'),
         ('Important to know','If you have spreading facial swelling, difficulty breathing or swallowing, or uncontrolled bleeding, seek emergency medical care rather than a dental appointment.')],
)

# ══════════════════════════════════════════════════════════════════════════
INVISALIGN = dict(
  cta='Book Free Consult',
  slug='invisalign', id='invisalign-3900', banner='INVISALIGN',
  title='Clear Aligners. Confident Smile. — Invisalign® $3,900 | AIDM Austin',
  desc='Invisalign clear aligner treatment for $3,900 at the Austin Institute of Dental Medicine in Mueller, Austin. Complimentary orthodontic evaluation, no referral needed.',
  ogtitle='Clear Aligners. Confident Smile. — Invisalign® $3,900 | AIDM Austin',
  ogdesc='Personalised clear-aligner treatment, routine orthodontic visits and standard retention, $3,900.',
  ogimg=OG_OP,
  nav=NAV_ORTHO, navcta='Book Free Eval',
  h1=['Clear', 'Aligners.', 'Confident Smile.'],
  pill='Complimentary consult', cardtitle='Invisalign&reg; Clear Aligners',
  cardprice='<span class="c">$</span><span class="v">3,900</span>',
  included=['Personalized clear-aligner treatment','Standard aligner laboratory materials',
            'Routine orthodontic visits','Treatment completion and appliance removal',
            'Standard orthodontic retention'],
  cardcta='Book free consult', cardfine='Evaluation complimentary &mdash; no obligation to start.',
  cfk='Complimentary evaluation', cfh='Book your free consult', cfsubmit='Request my free consult',
  who=['Myself','My teenager','My child','Someone else'],
  cfdone='Thank you &mdash; the orthodontic team will call you back to confirm your complimentary evaluation and '
         'talk through whether aligners or braces suit your bite better.',
  promok='Invisalign clear aligners', promoh2='What $3,900 <em>actually covers.</em>',
  video='CEgwotre0h8', videoalt='Orthodontics at the Austin Institute of Dental Medicine',
  videoled='Orthodontics at AIDM', badge=('$3,900', 'Clear aligners'),
  promoimg=ALIGNER_IN, promoalt='A patient seating a clear aligner over the upper teeth',
  promofine='Advertised price of $3,900 applies to Invisalign&reg; clear aligner cases. Complex cases, retainers, or '
    'phase-one interceptive orthodontics may incur additional fees. A complete clinical evaluation is required to '
    'determine case complexity and final fee.',
  perks=[('cal','Book online'),('park','Free parking'),('clock','Monday&ndash;Saturday'),
         ('card','Financing available'),('star','No referral needed')],
  cases='Orthodontic treatment', caseh2='Actual cases. <em>Actual bites.</em>',
  casesub='Intraoral records from orthodontic cases completed at the Austin Institute of Dental Medicine.',
  staffsub='Board-certified faculty, specialists and residents working side by side &mdash; every orthodontic '
    'plan at AIDM is reviewed and signed off by faculty.',
  films=[('CEgwotre0h8','Orthodontics at AIDM &mdash; how cases are planned and treated','Start here'),
         ('QNsMOG1B6G8','Welcome to AIDM'),('2ooc1MlkmNM','What to expect at your first visit'),
         ('f7HHTbB-qe8','Comprehensive dental care'),('k9PavRdjiyc','Comfort, sedation &amp; anxiety care'),
         ('DV9t9dZJauA','Finding us &amp; where to park')],
  filmlane='More about AIDM', filmsub='The building, the clinicians and the treatments &mdash; in their own words.',
  frows=[dict(img=ALIGNER_FIT, alt='A clear aligner tray held over the teeth, all but invisible in place',
      cap='Removable, and nearly invisible in ordinary conversation',
      k='Why it matters', h2='Straight teeth are the <em>visible part.</em>',
      p='Aligned teeth are easier to clean, which lowers plaque, cavity and gum-disease risk and protects enamel '
        'from uneven wear. Correcting the bite spreads load evenly and reduces strain on the jaw joints. Aligners '
        'get you there without brackets on the front of your teeth &mdash; which for adults is often the whole point.',
      bullets=['Removable for eating, brushing and the photograph you cannot avoid',
               'No brackets, no wires, no emergency visits for a poking archwire',
               'Success depends on wear time &mdash; roughly 20 to 22 hours a day, every day']),
    dict(img=ORTHO_TEAM, alt='The AIDM orthodontic team photographed together in the treatment bay',
      cap='The orthodontic team, in the bay they work in',
      k='Who treats you', h2='Two clinicians. <em>One fee.</em>',
      p='AIDM is a teaching institute. Orthodontic residents &mdash; already qualified dentists in advanced '
        'postgraduate training &mdash; treat under the direct supervision of board-certified faculty. You get more '
        'clinical attention, not less, and the economics reflect the teaching mission.',
      bullets=['A second, board-certified opinion built into the plan',
               'Aligners and braces compared honestly, including when braces are the better answer',
               'Fees in writing before anything is scheduled'])],
  optsk='Orthodontic options for every stage', optsh2='Aligners are one of <em>three routes.</em>',
  optssub='Which one is appropriate depends on your bite, not on your budget &mdash; including when the answer is '
    'the cheaper option.',
  opts=ortho_cards('invis', ALIGNER_FIT, 'A clear aligner tray held over the teeth, all but invisible in place'),
  faq=[('Will Invisalign work for my bite, or do I need braces?',
        'That is exactly what the complimentary evaluation answers. Aligners handle a very wide range of cases, but '
        'severe rotations, large vertical movements and some bite corrections are still more predictable with fixed '
        'brackets. You will be told honestly which one suits your case &mdash; including when the answer is the cheaper one.'),
       ('Why is Invisalign $3,900 here?',
        '$3,900 is AIDM&rsquo;s published package fee for Invisalign&reg; clear aligner cases, and it reflects the '
        'teaching model &mdash; residents in advanced postgraduate training treating under board-certified faculty '
        'supervision. It applies to the services listed and cannot be combined with insurance benefits, membership '
        'pricing or other discounts unless expressly stated.'),
       ('What is included in the complimentary evaluation?',
        'A personalised orthodontic evaluation with the team, plus the records needed to plan your case: panoramic '
        'imaging, cephalometric imaging and analysis, clinical photographs and a digital 3D intraoral scan, each when '
        'clinically indicated. There is no charge and no referral is required.'),
       ('How long does treatment take?',
        'Most cases run 12 to 24 months, and minor corrections can be considerably shorter. You will be given a '
        'realistic range for your own case at the evaluation rather than an average.'),
       ('How many hours a day do I have to wear them?',
        'Roughly 20 to 22, every day. Aligners only move teeth while they are in your mouth, and the single biggest '
        'cause of a case running long is wear time. They come out to eat, drink anything but water, and brush.'),
       ('Is retention included, or is that extra later?',
        'Standard orthodontic retention is included in the package, as is treatment completion and appliance removal. '
        'A <em>replacement</em> retainer &mdash; if one is lost or broken &mdash; is charged separately.'),
       ('Can I use insurance or a payment plan?',
        'AIDM accepts many PPO plans, and financing may be available subject to approval. They cannot be stacked on '
        'top of package pricing. At the evaluation the team will show you both routes side by side so you can pick '
        'whichever leaves you better off.'),
       ('Am I too old for aligners?',
        'No. Orthodontics is effective for teens and adults alike, and clear aligners are the option most adults ask '
        'about first for exactly that reason. Treatment can also be coordinated with cosmetic or restorative work in '
        'the same building.')],
  ctk='Complimentary orthodontic evaluation', cth2='Ready for a radiant smile? <em>Let&rsquo;s start today.</em>',
  ctsub='The evaluation is complimentary and commits you to nothing. We will call you back to confirm a time &mdash; '
        'usually the same working day.',
  wholabel='Who is the treatment for?',
  who2=['Myself — adult','My teenager','My child','More than one family member'],
  placeholder='Preferred days, previous orthodontic treatment, concerns…',
  ctsubmit='Book my free evaluation',
  legalextra=LEGAL_ALIGN,
  terms=[('The offer','Invisalign&reg; clear aligner treatment at $3,900, including standard orthodontic retention.'),
         ('Who it is for','Adolescent and adult patients whose cases are suitable for clear-aligner therapy. Suitability is confirmed at your evaluation.'),
         ('Eligibility','Package pricing applies only to the services specifically listed and cannot be combined with insurance benefits, membership pricing, financing promotions or other discounts unless expressly stated.'),
         ('What is not included','Complex cases, replacement retainers and phase-one interceptive orthodontics may incur additional fees, as may additional diagnostics, laboratory fees, sedation and anaesthesia.'),
         ('Important to know','A complete clinical evaluation is required to determine case complexity and the final fee. Individual treatment results vary.')],
)

# ══════════════════════════════════════════════════════════════════════════
EARLY = dict(
  cta='Book Free Consult',
  slug='early-orthodontics', id='early-orthodontic-treatment-2500', banner='EARLY ORTHODONTICS',
  title='The Right Care at the Right Time — Early Orthodontic Treatment $2,500 | AIDM Austin',
  desc='Early orthodontic treatment for growing children, $2,500, at the Austin Institute of Dental Medicine in Mueller, Austin. Complimentary evaluation, no referral needed.',
  ogtitle='The Right Care at the Right Time — Early Orthodontic Treatment $2,500 | AIDM',
  ogdesc='Limited early orthodontic treatment, growth-appropriate planning and retention where the plan includes it, $2,500.',
  ogimg=OG_OP,
  nav=NAV_ORTHO, navcta='Book Free Eval',
  h1=['The Right Care', 'at the Right Time.'],
  pill='Complimentary consult', cardtitle='Early Orthodontic Treatment',
  cardprice='<span class="c">$</span><span class="v">2,500</span>',
  included=['Limited early orthodontic treatment','Routine treatment visits',
            'Growth-appropriate treatment planning','Retention when included in the treatment plan',
            'Care based on the child&rsquo;s stage of development'],
  cardcta='Book my child&rsquo;s free consult',
  cardfine='Evaluation complimentary &mdash; and often the answer is &ldquo;not yet&rdquo;.',
  cfk='Complimentary evaluation', cfh='Book your child&rsquo;s consult', cfsubmit='Request our free consult',
  who=['My child','My teenager','More than one child','Someone else'],
  cfdone='Thank you &mdash; the orthodontic team will call you back to confirm the complimentary evaluation and let '
         'you know what to bring for your child.',
  promok='Early orthodontic treatment', promoh2='What $2,500 <em>actually covers.</em>',
  video='CEgwotre0h8', videoalt='Orthodontics at the Austin Institute of Dental Medicine',
  videoled='Orthodontics at AIDM', badge=('$2,500', 'Early treatment'),
  promoimg=EARLY_BOY, promoalt='A smiling boy with a gap where a baby tooth has come out',
  promofine='Standalone appliances and services outside the approved early-treatment plan are priced separately. '
    'Eligibility, clinical recommendations and the final fee are confirmed after an appropriate evaluation, and '
    'package pricing cannot be combined with insurance benefits, membership pricing or other discounts.',
  perks=[('cal','Book online'),('park','Free parking'),('clock','Monday&ndash;Saturday'),
         ('card','Financing available'),('star','No referral needed')],
  cases='Orthodontic treatment', caseh2='Actual cases. <em>Actual bites.</em>',
  casesub='Intraoral records from orthodontic cases completed at the Austin Institute of Dental Medicine.',
  staffsub='Board-certified faculty, specialists and residents working side by side &mdash; every orthodontic '
    'plan at AIDM is reviewed and signed off by faculty before a single appliance is fitted.',
  films=[('CEgwotre0h8','Orthodontics at AIDM &mdash; how cases are planned and treated','Start here'),
         ('2ooc1MlkmNM','What to expect at your first visit'),('QNsMOG1B6G8','Welcome to AIDM'),
         ('f7HHTbB-qe8','Comprehensive dental care'),('k9PavRdjiyc','Comfort, sedation &amp; anxiety care'),
         ('DV9t9dZJauA','Finding us &amp; where to park')],
  filmlane='More about AIDM', filmsub='The building, the clinicians and the treatments &mdash; in their own words.',
  frows=[dict(img=ORTHO_CHAIR, alt='An AIDM clinician reviewing a young patient&rsquo;s digital records chairside',
      cap='Growth is the one thing you cannot go back for',
      k='Why it matters', h2='Some problems are <em>easier while they grow.</em>',
      p='Early treatment is not braces brought forward. It is a short, limited intervention that uses a child&rsquo;s '
        'own growth to fix things that get much harder once growth stops &mdash; crossbites, severe crowding, a narrow '
        'upper jaw, a habit that is pushing the front teeth out. Done at the right moment it can shorten, simplify or '
        'occasionally avoid the comprehensive treatment that would otherwise follow.',
      bullets=['The American Association of Orthodontists suggests a first orthodontic check at around age seven',
               'Crossbites and narrow arches respond to growth in ways they will not later',
               'Protruding upper front teeth are considerably more prone to trauma']),
    dict(img=ORTHO_TEAM, alt='The AIDM orthodontic team photographed together in the treatment bay',
      cap='The orthodontic team, in the bay they work in',
      k='Who treats your child', h2='Two clinicians. <em>One fee.</em>',
      p='AIDM is a teaching institute. Orthodontic residents &mdash; already qualified dentists in advanced '
        'postgraduate training &mdash; treat under the direct supervision of board-certified faculty, and paediatric '
        'dentistry sits in the same building. Every early-treatment plan is reviewed by faculty before it starts.',
      bullets=['A second, board-certified opinion built into your child&rsquo;s plan',
               'Paediatric dentistry, orthodontics and surgery under one roof',
               'An honest &ldquo;not yet&rdquo; when monitoring is the better answer'])],
  optsk='Orthodontic options for every stage', optsh2='Early treatment is one of <em>three routes.</em>',
  optssub='Which one is appropriate depends on your child&rsquo;s bite and stage of development, not on your budget '
    '&mdash; including when the answer is to wait and watch.',
  opts=ortho_cards('early', ORTHO_CHAIR, 'An AIDM clinician reviewing a young patient&rsquo;s records chairside'),
  faq=[('How young is too young for a first visit?',
        'The usual guidance is a first orthodontic check at around age seven, when enough permanent teeth are through '
        'to see how the bite is developing. That check is not a commitment to treatment &mdash; in a lot of cases the '
        'right answer is to monitor and revisit in a year, and you will be told so plainly.'),
       ('What is the difference between this and braces?',
        'Early treatment is a limited, targeted intervention that works with your child&rsquo;s growth &mdash; typically '
        'expanding a narrow arch, correcting a crossbite or creating room. Comprehensive braces align the full permanent '
        'dentition and usually come later, if they are needed at all. They are separate packages at separate fees.'),
       ('Will my child still need braces afterwards?',
        'Often, yes &mdash; early treatment is not usually a substitute for comprehensive orthodontics. What it does is '
        'make the later phase shorter, simpler or less likely to need extractions or surgery. Any clinician who promises '
        'you it will remove the need for braces entirely is promising something they cannot know.'),
       ('Why is early treatment $2,500?',
        '$2,500 is AIDM&rsquo;s published package fee for limited early orthodontic treatment, and it reflects the '
        'teaching model &mdash; residents in advanced postgraduate training treating under board-certified faculty '
        'supervision. Standalone appliances and services outside the approved early-treatment plan are priced separately.'),
       ('What is included, and what is not?',
        'The package covers limited early orthodontic treatment, routine treatment visits, growth-appropriate planning, '
        'and retention where the treatment plan includes it. Standalone appliances and any service outside the approved '
        'plan are quoted separately, as are additional diagnostics and laboratory fees.'),
       ('What happens at the complimentary evaluation?',
        'A personalised orthodontic evaluation with the team, plus records where clinically indicated: panoramic imaging, '
        'cephalometric imaging and analysis, clinical photographs and a digital 3D intraoral scan. There is no charge and '
        'no referral is required.'),
       ('My child is anxious about the dentist.',
        'Say so when you book. Comfort and anxiety care is one of AIDM&rsquo;s named strengths, and paediatric dentistry '
        'is part of the same building. The first visit is a look and a conversation &mdash; nothing is fitted on the day.'),
       ('Do I need a referral, and where do I park?',
        'No referral is needed. There is a garage immediately next door at 1401 Philomena Street and parking is free. '
        'The building is in Mueller, minutes from I-35 and 51st Street.')],
  ctk='Complimentary orthodontic evaluation', cth2='Not sure if it is time? <em>Let&rsquo;s find out.</em>',
  ctsub='The evaluation is complimentary and commits you to nothing &mdash; including when the honest answer is to '
        'wait a year. We will call you back to confirm a time, usually the same working day.',
  wholabel='Who is the treatment for?',
  who2=['My child','My teenager','More than one child','Myself — adult'],
  placeholder='Your child’s age, preferred days, anything a dentist has already flagged…',
  ctsubmit='Book our free evaluation',
  legalextra=LEGAL_ALIGN,
  terms=[('The offer','Limited early orthodontic treatment for growing children at $2,500.'),
         ('Who it is for','Children whose stage of dental development makes early, limited treatment appropriate. Suitability is confirmed at the evaluation.'),
         ('Eligibility','Package pricing applies only to the services specifically listed and cannot be combined with insurance benefits, membership pricing, financing promotions or other discounts unless expressly stated.'),
         ('What is not included','Standalone appliances and services outside the approved early-treatment plan are priced separately, as are additional diagnostics, laboratory fees, sedation and anaesthesia.'),
         ('Important to know','Early treatment does not always remove the need for comprehensive orthodontics later. Individual treatment results vary.')],
)

# ══════════════════════════════════════════════════════════════════════════
WISDOM = dict(
  cta='Book Appointment',
  slug='wisdom-teeth', id='wisdom-teeth-removal-from-200', banner='WISDOM TEETH',
  title='Comfort-Focused Care with Clear Pricing — Wisdom Teeth from $200 a Tooth | AIDM Austin',
  desc='Wisdom teeth removal from $200 per tooth at the Austin Institute of Dental Medicine in Mueller, Austin. Published price per surgical complexity; four teeth $800 to $1,800.',
  ogtitle='Wisdom Teeth Removal from $200 a Tooth | AIDM Austin',
  ogdesc='Straightforward wisdom tooth pricing based on the position and surgical complexity of each tooth. Onsite surgical centre.',
  ogimg=OG_OP,
  nav=NAV_STD, navcta='Book a Consult',
  h1=['Comfort-Focused Care', 'with Clear Pricing.'],
  pill='Published price, per tooth', cardtitle='Wisdom Teeth Removal',
  cardprice='<span class="fr">from</span><span class="c">$</span><span class="v">200</span>',
  cardsub='Per tooth &middot; four teeth $800&ndash;$1,800',
  included=['Simple erupted extraction &mdash; $200 per tooth',
            'Surgical erupted extraction &mdash; $275 per tooth',
            'Soft-tissue impacted &mdash; $300 per tooth',
            'Partial-bony impacted &mdash; $375 per tooth',
            'Complete-bony impacted &mdash; $450 per tooth'],
  cardcta='Book a consult', cardfine='Sedation and anaesthesia are billed separately.',
  cfk='Wisdom teeth &middot; from $200', cfh='Book your consult', cfsubmit='Request my consult',
  who=['Myself','My teenager','My child','Someone else'],
  cfdone='Thank you &mdash; the surgical team will call you back to confirm a consult and tell you which of the '
         'five price bands your X-ray puts you in.',
  promok='Wisdom teeth removal', promoh2='Five positions. <em>Five published prices.</em>',
  video='k9PavRdjiyc', videoalt='Comfort, sedation and anxiety care at the Austin Institute of Dental Medicine',
  videoled='Comfort, sedation &amp; anxiety care', badge=('$200', 'Per tooth, from'),
  promoimg=CHAIR_SMILE, promoalt='A patient relaxed in the dental chair',
  promofine='The package covers extractions only. Sedation and anaesthesia are billed separately. Which band a tooth '
    'falls into is determined from imaging at your consult, and the fee is confirmed before any treatment is started.',
  perks=[('cal','Book online'),('park','Free parking'),('clock','Monday&ndash;Saturday'),
         ('card','Sedation available'),('star','Onsite surgical centre')],
  stepsk='From consult to a soft-food weekend', stepsh2='How a wisdom tooth <em>actually comes out.</em>',
  stepssub='The fee is decided by the X-ray, not by the day. Once you know which of the five bands each tooth is in, '
    'there is nothing left to be surprised by.',
  steps=[('Consult and imaging','Imaging shows how each wisdom tooth is sitting &mdash; erupted, soft-tissue impacted, '
          'partial-bony or complete-bony. That position is what sets the fee for that tooth.'),
         ('Your written quote','You are given the per-tooth price for your own case, plus the cost of sedation if you '
          'want it, before anything is booked.'),
         ('The appointment','Local anaesthetic as standard, with sedation available for patients who want it. An onsite '
          'surgical centre means the whole thing happens in the same building.'),
         ('Healing','Written aftercare, gauze, and a review if you need one. Most people take it easy for a day or two '
          'and eat soft food for a few days.')],
  stepsfine='Not every wisdom tooth needs removing. If yours are through, in a usable position and cleanable, you will '
    'be told to keep them &mdash; the consult exists to answer that question honestly.',
  staffsub='Board-certified faculty, specialists and residents working side by side, with an onsite surgical centre '
    'and sedation available &mdash; oral surgery does not become a referral somewhere else.',
  films=[('k9PavRdjiyc','Comfort, sedation and anxiety care &mdash; what is available and how it works','Start here'),
         ('QNsMOG1B6G8','Welcome to AIDM'),('2ooc1MlkmNM','What to expect at your first visit'),
         ('NtubApnQFt0','Emergency dental &mdash; seen today'),('f7HHTbB-qe8','Comprehensive dental care'),
         ('DV9t9dZJauA','Finding us &amp; where to park')],
  filmlane='More about AIDM', filmsub='The building, the clinicians and the treatments &mdash; in their own words.',
  frows=[dict(img=OPERATORY, alt='An AIDM operatory with a patient being examined using advanced imaging',
      cap='The X-ray decides the price, not the appointment',
      k='Why it matters', h2='An impacted tooth <em>does not stay quiet.</em>',
      p='A wisdom tooth that is only partly through leaves a flap of gum that cannot be cleaned, and the tissue under '
        'it becomes repeatedly infected. One that is pressing on the tooth in front can decay it from behind, where '
        'neither you nor a toothbrush can reach &mdash; and that second tooth is one you actually need.',
      bullets=['Pericoronitis &mdash; infection under the gum flap &mdash; tends to recur, and each round is worse',
               'Decay on the back of the second molar is difficult to restore and easy to miss',
               'Roots keep forming with age, so removal is usually simpler earlier than later']),
    dict(img=SMILE_M, alt='A man smiling confidently outdoors',
      cap='Local anaesthetic as standard, sedation if you want it',
      k='Comfort', h2='The part people <em>actually dread.</em>',
      p='Comfort, sedation and anxiety care is one of the things AIDM is known for, and it applies to oral surgery as '
        'much as to anything else. Sedation is priced separately from the extraction itself, so you can see both '
        'numbers and decide &mdash; rather than having one folded invisibly into the other.',
      bullets=['Local anaesthetic is included in the extraction fee',
               'Sedation and anaesthesia are quoted separately, before you commit',
               'Written aftercare, and someone to call if the healing does not go to plan'])],
  optsk='Straightforward wisdom tooth pricing',
  optsh2='Priced by position, <em>not by the day.</em>',
  optssub='Each tooth is priced on how it is sitting in the jaw. Four teeth together come to somewhere between $800 '
    'and $1,800 depending on that mix &mdash; and you are told which bands yours are in before anything is booked.',
  opts=[dict(img=PIC['tools'], imgalt=PALT['tools'], imgpos='center 42%',
      sub='Through the gum', h3='Erupted Extraction', amt='$200&ndash;$275',
      strike='Per tooth',
      d='A wisdom tooth that has come through the gum and can be removed without needing to be sectioned or uncovered.',
      ul=['Simple erupted extraction &mdash; $200 per tooth','Surgical erupted extraction &mdash; $275 per tooth',
          'Local anaesthetic included','Written aftercare instructions'],
      fine='The package covers extractions only. Sedation and anaesthesia are billed separately.',
      cta='Ask which band I am in'),
    dict(img=PIC['mirror'], imgalt=PALT['mirror'], imgpos='center 40%',
      feat=True, flag='Most common', sub='Partly covered', h3='Impacted Extraction', amt='$300&ndash;$375',
      strike='Per tooth',
      d='A wisdom tooth held back by gum or by part of the surrounding bone &mdash; the commonest reason wisdom teeth '
        'cause trouble in the first place.',
      ul=['Soft-tissue impacted &mdash; $300 per tooth','Partial-bony impacted &mdash; $375 per tooth',
          'Local anaesthetic included','Onsite surgical centre','Written aftercare instructions'],
      fine='The package covers extractions only. Sedation and anaesthesia are billed separately.',
      cta='Book a consult'),
    dict(img=PIC['surgery'], imgalt=PALT['surgery'], imgpos='center 40%',
      sub='Fully buried', h3='Complete-Bony Impaction', amt='$450',
      strike='Per tooth',
      d='A wisdom tooth completely enclosed in bone. The most involved of the five positions, and the one where an '
        'onsite surgical centre matters most.',
      ul=['Complete-bony impacted &mdash; $450 per tooth','Local anaesthetic included','Onsite surgical centre',
          'Sedation available, priced separately','Written aftercare instructions'],
      fine='The package covers extractions only. Sedation and anaesthesia are billed separately.',
      cta='Book a consult')],
  alsoh='What it adds up to, and what sits next to it',
  also=[('All four wisdom teeth','Depending on the mix of positions across the four','$800&ndash;$1,800'),
        ('Sedation &amp; anaesthesia','Available for patients who want it, quoted separately from the extraction','On consult'),
        ('Emergency dental care','If a wisdom tooth has already flared up &mdash; seen today, Mon&ndash;Sat 7am&ndash;7pm','Same-day'),
        ('New Patient Special','Comprehensive examination and X-rays as needed, if you are new to AIDM','$100')],
  faq=[('How much will all four cost me?',
        'Between $800 and $1,800, depending on how the four are sitting. Each tooth is priced on its own position &mdash; '
        '$200 simple erupted, $275 surgical erupted, $300 soft-tissue impacted, $375 partial-bony, $450 complete-bony '
        '&mdash; so a mouth with four straightforward erupted teeth is at the bottom of that range and four buried ones '
        'at the top. Imaging at your consult tells you exactly which.'),
       ('Is sedation included in that price?',
        'No, and deliberately so. The package covers the extraction; sedation and anaesthesia are billed separately and '
        'quoted separately, so you can see both figures and choose. Local anaesthetic is included as standard.'),
       ('Do I actually need them out?',
        'Not necessarily. If your wisdom teeth are fully through, in a usable position and you can keep them clean, the '
        'right advice is to leave them alone and monitor. The consult exists to answer that question, not to sell you '
        'four extractions.'),
       ('Should I do it now or wait?',
        'Roots continue to form and bone becomes denser with age, so removal is generally simpler and heals faster in '
        'your late teens and twenties than in your forties. That is a reason to decide sooner, not a reason to have '
        'healthy teeth removed.'),
       ('How long is the recovery?',
        'Most people are quiet for a day or two and on soft food for a few days, with swelling peaking around day two '
        'or three. You will be given written aftercare and someone to call. Plan the appointment before a couple of '
        'clear days rather than before something you cannot move.'),
       ('Will I be treated by a student?',
        'You will be treated by a licensed dentist. AIDM is a teaching institute, so residents &mdash; already qualified '
        'dentists in advanced postgraduate training &mdash; treat under the direct supervision of licensed clinical '
        'faculty. That two-clinician model is why the published fees are what they are.'),
       ('Can I use insurance?',
        'AIDM accepts many PPO plans. Package pricing applies only to the services listed and cannot be combined with '
        'insurance benefits, membership pricing or other discounts unless expressly stated &mdash; at your consult the '
        'team will show you both routes so you can pick whichever leaves you better off.'),
       ('What if one flares up before my appointment?',
        'Call <a href="tel:+17374342436">(737) 434-2436</a> and ask for an emergency slot. AIDM keeps same-day emergency '
        'appointments, Monday to Saturday, 7:00 a.m. to 7:00 p.m.')],
  ctk='Published pricing, confirmed from your X-ray',
  cth2='Find out which band <em>your teeth are in.</em>',
  ctsub='Leave your details and we will call you back to book a consult &mdash; usually the same working day. You will '
        'have your own per-tooth price in writing before anything is scheduled.',
  wholabel='Who is the treatment for?',
  who2=['Myself','My teenager','My child','More than one family member'],
  placeholder='Are they hurting now? Any previous X-rays or a referral letter?',
  ctsubmit='Book my consult',
  terms=[('The offer','Wisdom tooth extraction priced per tooth by surgical position: $200 simple erupted, $275 surgical erupted, $300 soft-tissue impacted, $375 partial-bony impacted, $450 complete-bony impacted.'),
         ('Who it is for','Patients whose wisdom teeth are clinically indicated for removal. That indication is confirmed from imaging at your consult.'),
         ('What is not included','The package covers extractions only. Sedation and anaesthesia are billed separately, as are additional diagnostics and laboratory fees.'),
         ('Eligibility','Package pricing applies only to the services specifically listed and cannot be combined with insurance benefits, membership pricing, financing promotions or other discounts unless expressly stated.'),
         ('Important to know','Four teeth together come to $800–$1,800 depending on the mix of positions. Final fees are confirmed following clinical evaluation.')],
)

ALL = [EMERGENCY, INVISALIGN, EARLY, WISDOM]
