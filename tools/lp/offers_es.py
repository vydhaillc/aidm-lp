# -*- coding: utf-8 -*-
"""Rows 11 and 12 of the approved promotions sheet — the Spanish pages.

Inclusions and fine print are the sheet's own Spanish, verbatim. Everything
else is translated here and is flagged for AIDM review before launch — in
particular the Texas 72-hour disclosure, which is statutory language.
"""
from offers_a import (NAV_STD, OPERATORY, EXAM, XRAY_TALK, RES_PATIENT, PAIN,
                      CHAIR_SMILE, OG_OP, OG_LOBBY, ILLUS, ALT)

# Every standing string the template hard-codes, translated once.
CHROME = [
 ('aria-label="4.9 star Google rating — read the reviews"',
  'aria-label="Calificaci&oacute;n de 4.9 estrellas en Google — lea las rese&ntilde;as"'),
 ('<span class="grev-t">Google reviews</span>', '<span class="grev-t">Rese&ntilde;as de Google</span>'),
 ('>Call (737) 434-2436</a>', '>Llame al (737) 434-2436</a>'),
 ('<p class="hteam-h">AIDM Team</p>', '<p class="hteam-h">Equipo AIDM</p>'),
 ('<button class="cf-back" type="button" id="cardBack">&larr; Back to the offer</button>',
  '<button class="cf-back" type="button" id="cardBack">&larr; Volver a la oferta</button>'),
 ('<label for="cf_fn">First name</label>', '<label for="cf_fn">Nombre</label>'),
 ('<label for="cf_ln">Last name</label>', '<label for="cf_ln">Apellido</label>'),
 ('<label for="cf_ph">Mobile number</label>', '<label for="cf_ph">Tel&eacute;fono m&oacute;vil</label>'),
 ('<label for="cf_em">Email</label>', '<label for="cf_em">Correo electr&oacute;nico</label>'),
 ('<label for="cf_who">This is for</label>', '<label for="cf_who">La cita es para</label>'),
 ('<p class="cf-fine">No obligation. We call back the same working day.</p>',
  '<p class="cf-fine">Sin compromiso. Le devolvemos la llamada el mismo d&iacute;a h&aacute;bil.</p>'),
 ('<p class="cf-p cf-tel">Need us sooner? <a href="tel:+17374342436">(737) 434-2436</a></p>',
  '<p class="cf-p cf-tel">&iquest;Necesita atenci&oacute;n antes? <a href="tel:+17374342436">(737) 434-2436</a></p>'),
 ('<p class="k">1401 Philomena Street, Mueller</p>', '<p class="k">1401 Philomena Street, Mueller</p>'),
 ('<h2>Take the <em>office tour.</em></h2>', '<h2>Conozca <em>nuestra cl&iacute;nica.</em></h2>'),
 ('<figcaption><em>1401 Philomena Street</em>The building</figcaption>',
  '<figcaption><em>1401 Philomena Street</em>El edificio</figcaption>'),
 ('<figcaption><em>Ground floor</em>Reception &amp; arrival</figcaption>',
  '<figcaption><em>Planta baja</em>Recepci&oacute;n y llegada</figcaption>'),
 ('<figcaption><em>Treatment</em>Open treatment bay</figcaption>',
  '<figcaption><em>Tratamiento</em>&Aacute;rea de tratamiento abierta</figcaption>'),
 ('<figcaption><em>Arrival</em>Two-storey lobby</figcaption>',
  '<figcaption><em>Llegada</em>Vest&iacute;bulo de doble altura</figcaption>'),
 ('<figcaption><em>Treatment</em>Private operatory</figcaption>',
  '<figcaption><em>Tratamiento</em>Consultorio privado</figcaption>'),
 ('<figcaption><em>Planning</em>Case-review room</figcaption>',
  '<figcaption><em>Planificaci&oacute;n</em>Sala de revisi&oacute;n de casos</figcaption>'),
 ('<figcaption><em>Comfort</em>Waiting lounge</figcaption>',
  '<figcaption><em>Comodidad</em>Sala de espera</figcaption>'),
 ('<figcaption><em>Free parking</em>The approach</figcaption>',
  '<figcaption><em>Estacionamiento gratis</em>La entrada</figcaption>'),
 ('<p class="k">Who you will meet</p>', '<p class="k">A qui&eacute;nes conocer&aacute;</p>'),
 ('<h2>The people <em>behind the chair.</em></h2>', '<h2>Las personas <em>detr&aacute;s del sill&oacute;n.</em></h2>'),
 ('<figcaption><em>Faculty</em>The specialists who sign off every plan</figcaption>',
  '<figcaption><em>Docentes</em>Los especialistas que aprueban cada plan</figcaption>'),
 ('<figcaption><em>Clinical team</em>The team in the bay</figcaption>',
  '<figcaption><em>Equipo cl&iacute;nico</em>El equipo en el &aacute;rea de tratamiento</figcaption>'),
 ('<figcaption><em>At the chair</em>Two clinicians on every appointment</figcaption>',
  '<figcaption><em>En el sill&oacute;n</em>Dos cl&iacute;nicos en cada cita</figcaption>'),
 ('<figcaption><em>Your records</em>Reviewed with you, before anything is booked</figcaption>',
  '<figcaption><em>Sus registros</em>Revisados con usted, antes de agendar nada</figcaption>'),
 ('<p class="k">See it for yourself</p>', '<p class="k">V&eacute;alo usted mismo</p>'),
 ('<h2>Films from <em>inside AIDM.</em></h2>', '<h2>Videos desde <em>adentro de AIDM.</em></h2>'),
 ('<p class="k">Patients, in their words</p>', '<p class="k">Pacientes, en sus propias palabras</p>'),
 ('<h2>&ldquo;Not your regular <em>dental experience.</em>&rdquo;</h2>',
  '<h2>&ldquo;No es la experiencia dental <em>de siempre.</em>&rdquo;</h2>'),
 ('<p>Straight from AIDM&rsquo;s Google Business Profile &mdash; the newest ones first.</p>',
  '<p>Directamente de las rese&ntilde;as de Google de AIDM &mdash; las m&aacute;s recientes primero. '
  'Las rese&ntilde;as se muestran en su idioma original.</p>'),
 ('<p class="k">Before you ask</p><h2>Frequently asked <em>questions.</em></h2>',
  '<p class="k">Antes de que pregunte</p><h2>Preguntas <em>frecuentes.</em></h2>'),
 ('<label for="fn">First name</label>', '<label for="fn">Nombre</label>'),
 ('<label for="ln">Last name</label>', '<label for="ln">Apellido</label>'),
 ('<label for="ph">Mobile number</label>', '<label for="ph">Tel&eacute;fono m&oacute;vil</label>'),
 ('<label for="em">Email</label>', '<label for="em">Correo electr&oacute;nico</label>'),
 ('<label for="cf_msg">Message <span style="text-transform:none;letter-spacing:0;font-weight:400">(optional)</span></label>',
  '<label for="cf_msg">Mensaje <span style="text-transform:none;letter-spacing:0;font-weight:400">(opcional)</span></label>'),
 ('<label for="msg">Message <span style="text-transform:none;letter-spacing:0;font-weight:400">(optional)</span></label>',
  '<label for="msg">Mensaje <span style="text-transform:none;letter-spacing:0;font-weight:400">(opcional)</span></label>'),
 ('<option value="">Please choose…</option>', '<option value="">Seleccione…</option>'),
 ('<p class="fnote">By submitting you agree to be contacted about your enquiry. Promotional pricing is\n'
  '          subject to clinical qualification determined at your evaluation.</p>',
  '<p class="fnote">Al enviar este formulario, usted acepta que lo contactemos sobre su solicitud. Los precios\n'
  '          promocionales est&aacute;n sujetos a la evaluaci&oacute;n cl&iacute;nica correspondiente.</p>'),
 ('<span>1401 Philomena Street, Austin, TX 78723 · Free parking in the garage next door<br>',
  '<span>1401 Philomena Street, Austin, TX 78723 · Estacionamiento gratuito en el garaje de al lado<br>'),
 ('<p style="margin:0;max-width:34ch;line-height:1.62">A teaching dental institute in Mueller, Austin — every specialty under one roof, six days a week.</p>',
  '<p style="margin:0;max-width:34ch;line-height:1.62">Un instituto dental docente en Mueller, Austin — todas las especialidades bajo un mismo techo, seis d&iacute;as a la semana.</p>'),
 ('<div><h4>Visit</h4><ul><li>1401 Philomena Street<br>Austin, TX 78723</li><li>Free parking next door</li><li>Monday – Saturday</li></ul></div>',
  '<div><h4>Vis&iacute;tenos</h4><ul><li>1401 Philomena Street<br>Austin, TX 78723</li><li>Estacionamiento gratuito al lado</li><li>Lunes a s&aacute;bado</li></ul></div>'),
 ('<div><h4>Contact</h4>', '<div><h4>Contacto</h4>'),
 ("data.form         = form.id === 'cardForm' ? 'hero offer card' : 'contact section';",
  "data.form         = form.id === 'cardForm' ? 'hero offer card (ES)' : 'contact section (ES)';"),
 ("err.innerHTML = 'That did not go through. Please call ' +\n      '<a href=\"tel:+17374342436\">(737) 434-2436</a> and we will book you in.';",
  "err.innerHTML = 'No se pudo enviar. Por favor llame al ' +\n      '<a href=\"tel:+17374342436\">(737) 434-2436</a> y con gusto lo agendamos.';"),
 ("cbtn.disabled = true; cbtn.textContent = 'Sending…';", "cbtn.disabled = true; cbtn.textContent = 'Enviando…';"),
 ("btn.disabled = true; btn.textContent = 'Sending…';", "btn.disabled = true; btn.textContent = 'Enviando…';"),
 ("btn.textContent = 'Thank you — we will call you shortly ✓';",
  "btn.textContent = 'Gracias — le llamaremos en breve ✓';"),
 ('<a href="#terms">*Terms &amp; Conditions</a>', '<a href="#terms">*T&eacute;rminos y Condiciones</a>'),
 ('aria-label="See fee disclosures"', 'aria-label="Ver los t&eacute;rminos de honorarios"'),
 ('<p class="hours">Open 7am &ndash; 7pm<span class="sp"></span>Mon&ndash;Sat</p>',
  '<p class="hours">Abierto 7am &ndash; 7pm<span class="sp"></span>Lun&ndash;S&aacute;b</p>'),
 ('<a href="#terms">Read the full offer terms</a>', '<a href="#terms">Lea los t&eacute;rminos completos de la oferta</a>'),
 ('aria-label="Media viewer"', 'aria-label="Visor de medios"'),
 ('<button class="lb-x" id="lbx" aria-label="Close">', '<button class="lb-x" id="lbx" aria-label="Cerrar">'),
 ('title="AIDM film"', 'title="Video de AIDM"'),
 ('title="Map to Austin Institute of Dental Medicine, 1401 Philomena Street, Austin TX 78723"',
  'title="Mapa al Austin Institute of Dental Medicine, 1401 Philomena Street, Austin TX 78723"'),
]

FACTS_ES = [('7<i class="u">am</i>', 'Abre'), ('7<i class="u">pm</i>', 'Cierra'),
            ('6', 'D&iacute;as/sem'), ('$0', 'Parqueo')]

LEGAL_ES = (
 ' Esta p&aacute;gina es una traducci&oacute;n de cortes&iacute;a. En caso de discrepancia, prevalece la '
 'versi&oacute;n en ingl&eacute;s de los t&eacute;rminos publicados por Austin Institute of Dental Medicine.')

LEGAL_ES_HTML = '''      <p><b>Precios.</b> Las ofertas promocionales, los precios por paquete y los servicios incluidos est&aacute;n
        sujetos a cambio, modificaci&oacute;n o descontinuaci&oacute;n en cualquier momento y sin aviso previo. Las
        ofertas est&aacute;n disponibles por tiempo limitado y pueden retirarse a discreci&oacute;n exclusiva de Austin
        Institute of Dental Medicine. Las promociones son v&aacute;lidas &uacute;nicamente para pacientes elegibles que
        cumplan los criterios cl&iacute;nicos determinados por el dentista o especialista tratante tras un examen
        apropiado. El precio del paquete aplica &uacute;nicamente a los servicios expresamente listados y no se puede
        combinar con beneficios de seguro, precios de membres&iacute;a, promociones de financiamiento u otros
        descuentos, salvo indicaci&oacute;n expresa. Los tratamientos adicionales, procedimientos de diagn&oacute;stico,
        servicios de especialidad, honorarios de laboratorio, sedaci&oacute;n u otros procedimientos cl&iacute;nicamente
        necesarios pueden generar cargos adicionales. Las recomendaciones finales de tratamiento, la elegibilidad y los
        honorarios se determinan tras una evaluaci&oacute;n cl&iacute;nica completa. AIDM se reserva el derecho de
        modificar precios, requisitos de elegibilidad, contenido de los paquetes, periodos promocionales y
        t&eacute;rminos y condiciones en cualquier momento y sin aviso.</p>
      <p><b>Su derecho a cancelar (Texas).</b> El paciente y cualquier otra persona responsable del pago tiene derecho a
        negarse a pagar, cancelar el pago, o ser reembolsado por el pago de cualquier otro servicio, examen o
        tratamiento realizado como resultado de, y dentro de las 72 horas siguientes a, responder al anuncio del
        servicio, examen o tratamiento gratuito, con descuento o de tarifa reducida.</p>
      <p><b>Qui&eacute;n lo atiende.</b> AIDM es un instituto educativo de primer nivel. El tratamiento bajo estas
        ofertas promocionales puede ser proporcionado por residentes dentales con licencia que participan en programas
        de formaci&oacute;n avanzada, bajo la supervisi&oacute;n directa de nuestros docentes cl&iacute;nicos con
        licencia. Todos los precios promocionales est&aacute;n sujetos a la calificaci&oacute;n cl&iacute;nica y a la
        autorizaci&oacute;n m&eacute;dica que determine el doctor tratante.</p>
      <p><b>Proveedor.</b> Los servicios dentales son proporcionados por Philomena Street PLLC, con el apoyo de AIDM.
        Los servicios en el Austin Institute of Dental Medicine son proporcionados por Dentistas Generales, Residentes y
        Docentes con licencia. T&eacute;rminos como &ldquo;Avanzado&rdquo;, &ldquo;Complejo&rdquo; o
        &ldquo;Instituto&rdquo; se refieren al alcance de la formaci&oacute;n y de los servicios ofrecidos y no implican
        una especializaci&oacute;n espec&iacute;fica, salvo que el proveedor est&eacute; expresamente designado como
        Especialista reconocido por la American Dental Association (ADA). Esta p&aacute;gina es una traducci&oacute;n de
        cortes&iacute;a; en caso de discrepancia, prevalece la versi&oacute;n en ingl&eacute;s de los t&eacute;rminos
        publicados por Austin Institute of Dental Medicine.</p>
      <p style="color:#4a6d87">© 2026 Austin Institute of Dental Medicine. Todos los derechos reservados.</p>'''

NAV_ES = [('office','La Cl&iacute;nica'),('promo','La Oferta'),('visit','C&oacute;mo Funciona'),
          ('staff','Nuestro Equipo'),('films','Videos'),('packages','Precios'),('faq','Preguntas')]

# ══════════════════════════════════════════════════════════════════════════
ES_NUEVO = dict(
  cta='Agendar Cita',
  slug='es/paciente-nuevo', id='new-patient-special-100-es', banner='PACIENTE NUEVO (ES)', lang='es',
  title='Su Nuevo Hogar Dental en Mueller — Especial para Pacientes Nuevos $100 | AIDM Austin',
  desc='Especial para pacientes nuevos en Austin Institute of Dental Medicine, Mueller: examen dental completo y radiografías según sea necesario por $100. Abierto de lunes a sábado, 7 a.m. a 7 p.m.',
  ogtitle='Su Nuevo Hogar Dental en Mueller — Especial para Pacientes Nuevos $100 | AIDM',
  ogdesc='Examen dental completo y radiografías según sea necesario, $100, en el instituto dental docente de Austin.',
  ogimg=OG_LOBBY,
  nav=NAV_ES, navcta='Agendar Cita', mcall='Llamar', facts=FACTS_ES, i18n=CHROME,
  h1=['Su Nuevo', 'Hogar Dental', 'en Mueller.'],
  pill='Pacientes nuevos &ndash; seis d&iacute;as', cardtitle='Especial para Pacientes Nuevos',
  cardprice='<span class="c">$</span><span class="v">100</span>',
  included=['Examen dental completo','Radiograf&iacute;as dentales seg&uacute;n sea necesario',
            'Evaluaci&oacute;n del riesgo de caries e higiene oral','Plan de tratamiento personalizado'],
  cardcta='Agendar mi primera cita',
  cardfine='No se necesita referencia &mdash; ni seguro dental.',
  cfk='Especial para pacientes nuevos &middot; $100', cfh='Agende su primera cita',
  cfsubmit='Solicitar mi cita',
  who=['Para m&iacute;','Para mi hijo o hija','Para toda mi familia','Para otra persona'],
  cfdone='Gracias &mdash; nuestra coordinadora de pacientes le llamar&aacute; para confirmar su primera cita y '
         'decirle qu&eacute; debe traer.',
  promok='Especial para pacientes nuevos', promoh2='Qu&eacute; cubre <em>realmente</em> los $100.',
  video='OBTJIDJHHTc', videoalt='Qu&eacute; esperar en su primera visita al Austin Institute of Dental Medicine',
  videoled='Qu&eacute; esperar &mdash; su primera visita', badge=('$100', 'Examen + rayos X'),
  promoimg=EXAM, promoalt='Un dentista realizando un examen dental completo a un paciente',
  promofine='El precio anunciado de $100 aplica a un examen dental completo para pacientes nuevos y '
    'radiograf&iacute;as tomadas &uacute;nicamente cuando sea cl&iacute;nicamente indicado. La limpieza dental '
    'profesional y el barniz de fl&uacute;or no est&aacute;n incluidos y se cobran por separado.',
  perks=[('cal','Agende en l&iacute;nea'),('park','Parqueo gratis'),('clock','7am&ndash;7pm, Lun&ndash;S&aacute;b'),
         ('card','Aceptamos seguros'),('star','Sin referencia')],
  stepsk='Entre 60 y 90 minutos, de principio a fin',
  stepsh2='Su primera cita, <em>paso a paso.</em>',
  stepssub='No se trata nada el mismo d&iacute;a que llega, a menos que tenga dolor y lo solicite. La primera cita '
    'existe para saber c&oacute;mo est&aacute; su salud oral y ponerle por escrito un plan y un precio.',
  steps=[('Llegada y registro','Parqueo gratuito en el garaje de al lado. Traiga identificaci&oacute;n con foto, su '
          'tarjeta de seguro si la tiene, y una lista de sus medicamentos. Los formularios se pueden llenar en l&iacute;nea.'),
         ('Radiograf&iacute;as, si se necesitan','Se toman im&aacute;genes digitales &uacute;nicamente donde est&aacute;n '
          'cl&iacute;nicamente indicadas &mdash; lo suficiente para ver entre y debajo de los dientes, y nada m&aacute;s.'),
         ('Examen dental completo','Dientes, trabajos previos, enc&iacute;as, mordida y tejidos blandos, m&aacute;s una '
          'revisi&oacute;n de detecci&oacute;n de c&aacute;ncer oral y una evaluaci&oacute;n del riesgo de caries.'),
         ('Su plan, por escrito','Le mostramos los hallazgos en pantalla, ordenados entre lo que hay que hacer ahora y '
          'lo que puede esperar, con el costo de cada paso por escrito antes de agendar nada.')],
  stepsfine='Si tambi&eacute;n necesita una limpieza dental profesional, se agenda por separado &mdash; la limpieza y '
    'el fl&uacute;or no forman parte del especial de $100.',
  staffsub='Docentes certificados, especialistas y residentes trabajando lado a lado &mdash; cada plan de tratamiento '
    'en AIDM es revisado y aprobado por un docente antes de darle un precio.',
  films=[('OBTJIDJHHTc','Qu&eacute; esperar en AIDM &mdash; en espa&ntilde;ol','Empiece aqu&iacute;'),
         ('QNsMOG1B6G8','Bienvenido a AIDM'),('DV9t9dZJauA','C&oacute;mo llegar y d&oacute;nde parquear'),
         ('f7HHTbB-qe8','Atenci&oacute;n dental integral'),('NtubApnQFt0','Atenci&oacute;n dental de emergencia'),
         ('k9PavRdjiyc','Comodidad, sedaci&oacute;n y manejo de la ansiedad'),
         ('CEgwotre0h8','Ortodoncia'),('7Ci0z84BpDI','Implantes dentales'),('cCUQyiHkJxg','Prostodoncia')],
  filmlane='Lo que hacemos', filmsub='El edificio, los cl&iacute;nicos y los tratamientos &mdash; en sus propias '
    'palabras. Los videos est&aacute;n en ingl&eacute;s, salvo donde se indique.',
  frows=[dict(img=XRAY_TALK, alt='Un dentista de AIDM explicando las radiograf&iacute;as a una paciente',
      cap='Sus radiograf&iacute;as, explicadas en pantalla &mdash; no archivadas',
      k='Por qu&eacute; importa', h2='Lo que duele <em>rara vez fue lo que empez&oacute;.</em>',
      p='Para cuando un diente duele, la caries lleva normalmente meses avanzando. Un examen completo con '
        'radiograf&iacute;as encuentra lo que usted todav&iacute;a no ve ni siente &mdash; caries entre los dientes, '
        'p&eacute;rdida &oacute;sea bajo la enc&iacute;a, restauraciones fracturadas, un absceso form&aacute;ndose en '
        'la ra&iacute;z &mdash; cuando todav&iacute;a es peque&ntilde;o, barato e indoloro de resolver.',
      bullets=['Una caries detectada en radiograf&iacute;a es una restauraci&oacute;n; esa misma caries detectada por dolor suele ser endodoncia y corona',
               'La enfermedad de las enc&iacute;as no duele en sus etapas iniciales y es la principal causa de p&eacute;rdida de dientes en adultos',
               'Cada examen incluye una revisi&oacute;n de detecci&oacute;n de c&aacute;ncer oral']),
    dict(img=RES_PATIENT, alt='Un residente y un docente de AIDM revisando registros con una paciente',
      cap='Dos cl&iacute;nicos en el sill&oacute;n, en la misma cita',
      k='Qui&eacute;n lo atiende', h2='Dos cl&iacute;nicos. <em>Un solo precio.</em>',
      p='AIDM es un instituto docente. Los residentes &mdash; dentistas ya titulados en formaci&oacute;n de posgrado '
        'avanzada &mdash; atienden bajo la supervisi&oacute;n directa de docentes cl&iacute;nicos con licencia. Usted '
        'recibe m&aacute;s atenci&oacute;n cl&iacute;nica, no menos, y esa misi&oacute;n docente es la raz&oacute;n por '
        'la que un examen completo con radiograf&iacute;as puede costar $100.',
      bullets=['Una segunda opini&oacute;n, a nivel docente, incluida en el plan sin costo adicional',
               'Ortodoncia, endodoncia, periodoncia, cirug&iacute;a, prostodoncia y odontopediatr&iacute;a bajo un mismo techo',
               'Todos los honorarios por escrito antes de agendar cualquier tratamiento'])],
  optsk='Paquetes para pacientes nuevos', optsh2='Empiece en $100 &mdash; o <em>empiece con todo.</em>',
  optssub='El especial de $100 cubre el examen y las radiograf&iacute;as. Si ya sabe que quiere la limpieza en la '
    'misma visita, el paquete de al lado la incluye &mdash; y puede decidirlo despu&eacute;s del examen, no antes.',
  opts=[dict(img=XRAY_TALK, imgalt='Un dentista de AIDM explicando las radiograf&iacute;as a una paciente', imgpos='center 32%',
      feat=True, flag='Oferta anunciada', sub='Su nuevo hogar dental en Mueller',
      h3='Especial para Pacientes Nuevos', amt='$100',
      strike='Examen y radiograf&iacute;as &mdash; limpieza por separado',
      d='Una introducci&oacute;n completa a AIDM: c&oacute;mo est&aacute; realmente su boca, y un plan por escrito de qu&eacute; hacer al respecto.',
      ul=['Examen dental completo','Radiograf&iacute;as dentales seg&uacute;n sea necesario',
          'Evaluaci&oacute;n del riesgo de caries e higiene oral','Plan de tratamiento personalizado'],
      fine='Aplica a un examen dental completo para pacientes nuevos y radiograf&iacute;as tomadas &uacute;nicamente '
           'cuando sea cl&iacute;nicamente indicado. La limpieza profesional y el fl&uacute;or no est&aacute;n '
           'incluidos y se cobran por separado.', cta='Agendar esta cita'),
    dict(img=ILLUS['cleaning'], imgalt='Un ultrasonido retirando placa y sarro de los dientes en la l&iacute;nea de las enc&iacute;as', imgpos='center 54%',
      sub='Examen, radiograf&iacute;as y su limpieza', h3='Establecer Atenci&oacute;n', amt='$450',
      strike='Una sola cita, todo cubierto',
      d='La primera visita completa para quienes ya saben que tambi&eacute;n les toca limpieza: examen, radiograf&iacute;as de boca completa y la limpieza juntas.',
      ul=['Examen dental completo','Radiograf&iacute;as de boca completa','Limpieza dental de adulto cuando corresponde',
          'Barniz de fl&uacute;or','Evaluaci&oacute;n del riesgo de caries e higiene oral'],
      fine='La limpieza incluida aplica cuando una limpieza preventiva de rutina es cl&iacute;nicamente apropiada. '
           'Los pacientes que requieran tratamiento periodontal recibir&aacute;n una recomendaci&oacute;n distinta.',
      cta='Preguntar si me conviene'),
    dict(img=ILLUS['emergency'], imgalt='Un molar fracturado con un absceso en la punta de la ra&iacute;z', imgpos='center 52%',
      sub='Atenci&oacute;n el mismo d&iacute;a', h3='Emergencia Dental', amt='El mismo d&iacute;a',
      strike='Sin precio publicado',
      d='Si tiene dolor hoy, la cita de emergencia es la correcta &mdash; no el examen de paciente nuevo.',
      ul=['Atenci&oacute;n el mismo d&iacute;a','Abierto de lunes a s&aacute;bado, 7 a.m. a 7 p.m.',
          'Evaluaci&oacute;n enfocada en el problema','Radiograf&iacute;as necesarias para el diagn&oacute;stico',
          'Centro quir&uacute;rgico en las instalaciones'],
      fine='Las citas de emergencia se priorizan cl&iacute;nicamente y est&aacute;n sujetas a disponibilidad.',
      cta='Ver atenci&oacute;n de emergencia')],
  faq=[('&iquest;Qu&eacute; incluye exactamente por $100?',
        'Un examen dental completo, radiograf&iacute;as dentales donde est&eacute;n cl&iacute;nicamente indicadas, una '
        'evaluaci&oacute;n del riesgo de caries con orientaci&oacute;n de higiene oral, y un plan de tratamiento '
        'personalizado que revisamos con usted antes de que se vaya. La limpieza dental profesional y el fl&uacute;or '
        '<em>no</em> est&aacute;n incluidos en los $100.'),
       ('&iquest;Por qu&eacute; no se incluye la limpieza?',
        'Porque todav&iacute;a no sabemos qu&eacute; limpieza necesita. Una limpieza preventiva de rutina y el raspado '
        'profundo que requiere la enfermedad de las enc&iacute;as son tratamientos distintos con precios distintos, y '
        'cu&aacute;l corresponde es precisamente lo que determinan el examen y las radiograf&iacute;as. Si prefiere '
        'todo en una sola visita, el paquete Establecer Atenci&oacute;n de $450 incluye la limpieza.'),
       ('&iquest;Me va a atender un estudiante?',
        'Lo atender&aacute; un dentista con licencia. AIDM es un instituto docente, as&iacute; que los residentes '
        '&mdash; dentistas ya titulados en formaci&oacute;n de posgrado avanzada &mdash; atienden bajo la '
        'supervisi&oacute;n directa de docentes cl&iacute;nicos con licencia, y su plan es revisado por un docente '
        'antes de darle un precio. Ese modelo de dos cl&iacute;nicos es exactamente por lo que el precio es el que es.'),
       ('&iquest;Necesito seguro dental? &iquest;Puedo usar el m&iacute;o?',
        'No necesita seguro &mdash; el especial de $100 es un paquete de pago directo, y esa es una de las razones por '
        'las que existe. Si tiene un plan, AIDM acepta muchos PPO, pero los precios promocionales no se pueden combinar '
        'con beneficios de seguro, precios de membres&iacute;a ni otros descuentos.'),
       ('&iquest;Cu&aacute;nto dura la primera cita y qu&eacute; debo llevar?',
        'Calcule entre 60 y 90 minutos. Lleve identificaci&oacute;n con foto, su tarjeta de seguro si la tiene, y una '
        'lista de los medicamentos que toma. Los formularios de paciente nuevo se pueden completar en l&iacute;nea antes '
        'de venir, lo que suele ahorrar quince minutos en recepci&oacute;n.'),
       ('Tengo dolor hoy. &iquest;Es esta la cita correcta?',
        'Si tiene dolor, pida la cita de emergencia. AIDM reserva espacios para el mismo d&iacute;a, de lunes a '
        's&aacute;bado, de 7:00 a.m. a 7:00 p.m., con centro quir&uacute;rgico en las instalaciones para extracciones '
        'urgentes. Llame al <a href="tel:+17374342436">(737) 434-2436</a> y diga que es urgente.'),
       ('&iquest;Puedo llevar a mis hijos el mismo d&iacute;a?',
        'S&iacute; &mdash; AIDM atiende a ni&ntilde;os y adultos en el mismo edificio, y las familias se agendan '
        'habitualmente una cita tras otra. D&iacute;ganos cu&aacute;ntas personas vienen al momento de agendar y '
        'reservamos el tiempo.'),
       ('&iquest;Necesito referencia y d&oacute;nde puedo parquear?',
        'No se necesita referencia. Hay un garaje justo al lado, en 1401 Philomena Street, y el parqueo es gratuito. '
        'El edificio est&aacute; en Mueller, a minutos de la I-35 y la calle 51.')],
  ctk='Abierto de lunes a s&aacute;bado, 7 a.m. a 7 p.m.',
  cth2='&iquest;Es su primera vez? <em>Con gusto lo atendemos.</em>',
  ctsub='D&eacute;jenos sus datos y nuestra coordinadora de pacientes le llamar&aacute; para confirmar una hora '
        '&mdash; normalmente el mismo d&iacute;a h&aacute;bil. Atendemos en espa&ntilde;ol.',
  wholabel='&iquest;Para qui&eacute;n es la cita?',
  who2=['Para m&iacute; — adulto','Para mi hijo o hija','Para toda mi familia','Para otra persona'],
  placeholder='Días y horas preferidas, algo que le moleste, ansiedad dental…',
  ctsubmit='Agendar mi cita de paciente nuevo',
  legalextra=LEGAL_ES,
  terms=[('La oferta','Un examen dental completo para pacientes nuevos con radiograf&iacute;as seg&uacute;n sea necesario, por $100.'),
         ('Para qui&eacute;n es','Pacientes nuevos en Austin Institute of Dental Medicine. La idoneidad y cualquier tratamiento adicional se confirman en su examen.'),
         ('Qu&eacute; no incluye','La limpieza dental profesional y el barniz de fl&uacute;or no est&aacute;n incluidos en los $100 y se cobran por separado, al igual que el tratamiento restaurativo, los servicios de especialidad, los honorarios de laboratorio y la sedaci&oacute;n.'),
         ('Elegibilidad','El precio del paquete aplica &uacute;nicamente a los servicios expresamente listados y no se puede combinar con beneficios de seguro, precios de membres&iacute;a, promociones de financiamiento u otros descuentos, salvo indicaci&oacute;n expresa.'),
         ('Importante','Las radiograf&iacute;as se toman &uacute;nicamente cuando est&aacute;n cl&iacute;nicamente indicadas. Las recomendaciones finales de tratamiento, la elegibilidad y los honorarios se determinan tras una evaluaci&oacute;n cl&iacute;nica completa.')],
)

# ══════════════════════════════════════════════════════════════════════════
ES_EMERGENCIA = dict(
  cta='Agendar Cita',
  slug='es/emergencia', id='emergency-dental-same-day-es', banner='EMERGENCIA (ES)', lang='es',
  title='Atención Dental de Emergencia — 7AM a 7PM, Lun a Sáb | AIDM Austin',
  desc='Citas dentales de emergencia el mismo día en Austin Institute of Dental Medicine, Mueller. Abierto de lunes a sábado, 7 a.m. a 7 p.m., con centro quirúrgico en las instalaciones.',
  ogtitle='Atención Dental de Emergencia — 7AM a 7PM, Lun–Sáb | AIDM Austin',
  ogdesc='Atención el mismo día. Evaluación enfocada en el problema, radiografías necesarias y centro quirúrgico en las instalaciones.',
  ogimg=OG_OP,
  nav=NAV_ES, navcta='Atenci&oacute;n Hoy', mcall='Llamar', facts=FACTS_ES, i18n=CHROME,
  h1=['Atenci&oacute;n Dental', 'de Emergencia', '7am a 7pm, Lun&ndash;S&aacute;b.'],
  pill='Citas el mismo d&iacute;a', cardtitle='Atenci&oacute;n Dental de Emergencia',
  cardprice='<span class="v w">Atenci&oacute;n hoy</span>', cardsub='Sin precio publicado',
  included=['Atenci&oacute;n el mismo d&iacute;a','Abierto de lunes a s&aacute;bado, 7 a.m. a 7 p.m.',
            'Evaluaci&oacute;n enfocada en el problema','Radiograf&iacute;as necesarias para el diagn&oacute;stico',
            'Centro quir&uacute;rgico en las instalaciones'],
  cardcta='Solicitar cita para hoy',
  cardfine='&iquest;Tiene dolor ahora? Llamar es m&aacute;s r&aacute;pido que cualquier formulario.',
  cfk='Emergencia el mismo d&iacute;a', cfh='Pida una cita para hoy', cfsubmit='Solicitar cita para hoy',
  who=['Para m&iacute;','Para mi hijo o hija','Para otra persona'],
  cfdone='Gracias &mdash; le llamaremos de inmediato para buscarle un espacio. Si el dolor es fuerte, llame al '
         '<a href="tel:+17374342436">(737) 434-2436</a> ahora en lugar de esperar.',
  promok='Atenci&oacute;n dental de emergencia', promoh2='&iquest;Dolor hoy? <em>Pida hoy.</em>',
  video='NtubApnQFt0', videoalt='Atenci&oacute;n dental de emergencia en el Austin Institute of Dental Medicine',
  videoled='Emergencia dental &mdash; atenci&oacute;n hoy', badge=('7&ndash;7', 'Lun a S&aacute;b'),
  promoimg=PAIN, promoalt='Un hombre con una bolsa de hielo en la mand&iacute;bula por dolor de muelas',
  promofine='Las citas de emergencia se priorizan cl&iacute;nicamente y est&aacute;n sujetas a disponibilidad. Una '
    'evaluaci&oacute;n de emergencia atiende el problema que le trae; cualquier tratamiento adicional se cotiza antes '
    'de iniciarse, y las radiograf&iacute;as se toman &uacute;nicamente donde son necesarias para el diagn&oacute;stico.',
  perks=[('clock','7am&ndash;7pm, Lun&ndash;S&aacute;b'),('star','Sin referencia'),('park','Parqueo gratis'),
         ('card','Aceptamos seguros'),('cal','Atendemos en espa&ntilde;ol')],
  stepsk='De su llamada a salir sin dolor', stepsh2='C&oacute;mo funciona <em>una cita el mismo d&iacute;a.</em>',
  stepssub='Una cita de emergencia no es un chequeo. Existe para encontrar qu&eacute; causa el dolor y detenerlo hoy '
    '&mdash; el plan completo puede esperar a que usted est&eacute; c&oacute;modo.',
  steps=[('Llame y descr&iacute;balo','D&iacute;ganos qu&eacute; le duele, desde cu&aacute;ndo, y si hay '
          'inflamaci&oacute;n, fiebre o un diente que se sali&oacute;. Eso determina con qu&eacute; rapidez debe verlo un cl&iacute;nico.'),
         ('Prioridad y hora','Le damos el espacio m&aacute;s pronto que sea cl&iacute;nicamente apropiado. La '
          'inflamaci&oacute;n severa, los traumatismos y el sangrado no controlado tienen prioridad.'),
         ('Diagnosticar la causa','Una evaluaci&oacute;n enfocada en el problema, con las radiograf&iacute;as '
          'necesarias para ver qu&eacute; ocurre &mdash; un absceso, una fractura, una restauraci&oacute;n perdida, un diente retenido.'),
         ('Aliviarlo hoy','Todo lo que se pueda hacer con seguridad el mismo d&iacute;a se hace el mismo d&iacute;a, '
          'con el costo acordado antes. El centro quir&uacute;rgico en las instalaciones significa que una '
          'extracci&oacute;n urgente no necesita una segunda cita en otro lugar.')],
  stepsfine='Si tiene inflamaci&oacute;n facial que se est&aacute; extendiendo, dificultad para respirar o tragar, o '
    'sangrado no controlado, trátelo como una emergencia m&eacute;dica y acuda a una sala de emergencias.',
  staffsub='Docentes certificados, especialistas y residentes trabajando lado a lado &mdash; y un centro '
    'quir&uacute;rgico en las instalaciones, para que una extracci&oacute;n urgente no se convierta en una referencia a otro lugar.',
  films=[('NtubApnQFt0','Emergencia dental en AIDM &mdash; qu&eacute; ocurre cuando llega','Empiece aqu&iacute;'),
         ('OBTJIDJHHTc','Qu&eacute; esperar en AIDM &mdash; en espa&ntilde;ol'),
         ('DV9t9dZJauA','C&oacute;mo llegar y d&oacute;nde parquear'),
         ('QNsMOG1B6G8','Bienvenido a AIDM'),('f7HHTbB-qe8','Atenci&oacute;n dental integral'),
         ('k9PavRdjiyc','Comodidad, sedaci&oacute;n y manejo de la ansiedad'),
         ('CEgwotre0h8','Ortodoncia'),('7Ci0z84BpDI','Implantes dentales'),('cCUQyiHkJxg','Prostodoncia')],
  filmlane='Lo que hacemos', filmsub='El edificio, los cl&iacute;nicos y los tratamientos &mdash; en sus propias '
    'palabras. Los videos est&aacute;n en ingl&eacute;s, salvo donde se indique.',
  frows=[dict(img=PAIN, alt='Un hombre con una bolsa de hielo en la mand&iacute;bula por dolor de muelas',
      cap='El dolor que lo despierta no es dolor que espere',
      k='Por qu&eacute; importa', h2='El dolor dental <em>no se resuelve solo.</em>',
      p='Un dolor de muelas que ya lleg&oacute; al nervio, un absceso en la ra&iacute;z o una c&uacute;spide fracturada '
        'no se resuelven con analg&eacute;sicos &mdash; solo los enmascaran mientras la causa contin&uacute;a. La '
        'infecci&oacute;n de un diente puede extenderse al hueso y a los tejidos blandos de la cara, y lo que pudo '
        'haber sido una endodoncia termina siendo una extracci&oacute;n.',
      bullets=['La inflamaci&oacute;n que se extiende hacia el ojo o el piso de la boca es un problema de sala de emergencias, no dental',
               'Un diente permanente que se sali&oacute; muchas veces se puede reimplantar &mdash; pero la ventana se mide en horas',
               'Los analg&eacute;sicos y antibi&oacute;ticos manejan s&iacute;ntomas; solo tratar la causa lo termina']),
    dict(img=OPERATORY, alt='Un consultorio de AIDM con un paciente siendo atendido',
      cap='Centro quir&uacute;rgico, en el mismo edificio',
      k='Por qu&eacute; aqu&iacute;', h2='Todo bajo <em>un mismo techo.</em>',
      p='La mayor&iacute;a de las cl&iacute;nicas que lo atienden de urgencia luego lo refieren a otro lado para lo que '
        'realmente necesita. AIDM tiene endodoncia, cirug&iacute;a oral, periodoncia y prostodoncia en el mismo '
        'edificio, seis d&iacute;as a la semana, as&iacute; que el tratamiento que sigue al diagn&oacute;stico se '
        'suele agendar de inmediato.',
      bullets=['Centro quir&uacute;rgico en las instalaciones para extracciones urgentes',
               'Sedaci&oacute;n y manejo de la ansiedad disponibles para quien los necesite',
               'Abierto de 7:00 a.m. a 7:00 p.m., de lunes a s&aacute;bado &mdash; antes y despu&eacute;s del trabajo'])],
  optsk='En qu&eacute; suele resultar una emergencia',
  optsh2='La cita es urgente. <em>El precio no es sorpresa.</em>',
  optssub='Una evaluaci&oacute;n de emergencia encuentra la causa; estos son los precios publicados de las tres cosas '
    'en las que m&aacute;s a menudo resulta. Usted conoce el costo antes de que se inicie cualquier tratamiento.',
  opts=[dict(img=ILLUS['root-canal'], imgalt='Corte transversal de un molar durante el tratamiento de conducto', imgpos='center 55%',
      sub='Salvar el diente', h3='Endodoncia', amt='desde $995',
      strike='Con corona cer&aacute;mica, $2,300&ndash;$2,500',
      d='Conserve un diente elegible con tratamiento de conducto, un mu&ntilde;&oacute;n de protecci&oacute;n y una corona cer&aacute;mica.',
      ul=['Imagen 3D de campo limitado','Tratamiento de conducto inicial','Mu&ntilde;&oacute;n de protecci&oacute;n (paquete con corona)',
          'Corona de porcelana o cer&aacute;mica (paquete con corona)','Atenci&oacute;n endod&oacute;ntica y restaurativa coordinada'],
      fine='El precio anunciado de $995 aplica a la terapia de conducto est&aacute;ndar. Los casos complejos, incluidos '
           'conductos muy calcificados o retratamientos, pueden requerir un honorario ajustado.', cta='Ver precios de endodoncia'),
    dict(img=PAIN, imgalt='Un hombre con dolor de muelas sujet&aacute;ndose la mand&iacute;bula', imgpos='center 34%',
      feat=True, flag='Usted est&aacute; aqu&iacute;', sub='Atenci&oacute;n dental de emergencia',
      h3='Evaluaci&oacute;n de Emergencia', amt='Atenci&oacute;n hoy',
      strike='Enfocada en el problema &mdash; sin precio publicado',
      d='La cita en s&iacute;: averiguar qu&eacute; causa el dolor y resolver lo que se pueda resolver hoy con seguridad.',
      ul=['Atenci&oacute;n el mismo d&iacute;a','Abierto de lunes a s&aacute;bado, 7 a.m. a 7 p.m.',
          'Evaluaci&oacute;n enfocada en el problema','Radiograf&iacute;as necesarias para el diagn&oacute;stico',
          'Centro quir&uacute;rgico en las instalaciones'],
      fine='Las citas de emergencia se priorizan cl&iacute;nicamente y est&aacute;n sujetas a disponibilidad. Cualquier '
           'tratamiento que resulte se cotiza antes de iniciarse.', cta='Solicitar cita para hoy'),
    dict(img=ILLUS['wisdom-erupted'], imgalt='Una muela del juicio siendo extra&iacute;da con f&oacute;rceps', imgpos='center 56%',
      sub='Cuando el diente no se puede conservar', h3='Extracciones', amt='desde $200',
      strike='Por diente, seg&uacute;n complejidad quir&uacute;rgica',
      d='Precios claros de extracci&oacute;n seg&uacute;n la posici&oacute;n y la complejidad quir&uacute;rgica de cada diente.',
      ul=['Extracci&oacute;n simple de diente erupcionado &mdash; $200 por diente',
          'Extracci&oacute;n quir&uacute;rgica de diente erupcionado &mdash; $275 por diente',
          'Retenci&oacute;n en tejido blando &mdash; $300 por diente','Retenci&oacute;n &oacute;sea parcial &mdash; $375 por diente',
          'Retenci&oacute;n &oacute;sea completa &mdash; $450 por diente'],
      fine='El paquete cubre &uacute;nicamente las extracciones. La sedaci&oacute;n y la anestesia se cobran por separado.',
      cta='Ver precios de extracci&oacute;n')],
  alsoh='Tambi&eacute;n &uacute;til si es nuevo en AIDM',
  also=[('Especial para Pacientes Nuevos','Examen dental completo y radiograf&iacute;as seg&uacute;n sea necesario, una vez sin dolor','$100'),
        ('Comodidad y sedaci&oacute;n','Sedaci&oacute;n y manejo de la ansiedad para quien los necesite, cotizados por separado','En evaluaci&oacute;n')],
  faq=[('Tengo dolor ahora mismo. &iquest;Qu&eacute; hago?',
        'Llame al <a href="tel:+17374342436">(737) 434-2436</a>. Llamar es m&aacute;s r&aacute;pido que cualquier '
        'formulario &mdash; priorizamos por tel&eacute;fono y le damos el espacio m&aacute;s pronto que sea '
        'cl&iacute;nicamente apropiado. Abrimos de lunes a s&aacute;bado, de 7:00 a.m. a 7:00 p.m. Si tiene '
        'inflamaci&oacute;n facial que se extiende, dificultad para respirar o tragar, o sangrado no controlado, '
        'acuda a una sala de emergencias.'),
       ('&iquest;Cu&aacute;nto cuesta una cita de emergencia?',
        'No hay un precio &uacute;nico publicado, porque una emergencia se cobra seg&uacute;n lo que resulte ser. '
        'Usted recibe una evaluaci&oacute;n enfocada en el problema y las radiograf&iacute;as necesarias para '
        'diagnosticarlo, y el costo de cualquier tratamiento se le presenta antes de iniciarlo. Los tres desenlaces '
        'm&aacute;s comunes tienen precios publicados &mdash; endodoncia desde $995, extracci&oacute;n desde $200 por diente.'),
       ('&iquest;De verdad lo pueden tratar el mismo d&iacute;a?',
        'Todo lo que se pueda hacer con seguridad el mismo d&iacute;a se hace el mismo d&iacute;a. AIDM tiene centro '
        'quir&uacute;rgico en las instalaciones, as&iacute; que una extracci&oacute;n urgente no se convierte en una '
        'referencia a otro lugar, y endodoncia, periodoncia y prostodoncia est&aacute;n en el mismo edificio.'),
       ('&iquest;Atienden en espa&ntilde;ol?',
        'S&iacute;. Puede llamar y agendar en espa&ntilde;ol, y d&iacute;galo al llamar para que le asignemos personal '
        'que hable espa&ntilde;ol en su cita.'),
       ('No tengo seguro dental. &iquest;Me pueden atender?',
        'S&iacute;. AIDM atiende pacientes de pago directo y publica precios por paquete precisamente para que quien no '
        'tiene seguro pueda ver la cifra antes de comprometerse. Si s&iacute; tiene un plan, se aceptan muchos PPO.'),
       ('Se me sali&oacute; un diente. &iquest;Qu&eacute; hago ahora?',
        'T&oacute;melo por la corona, nunca por la ra&iacute;z. Si est&aacute; limpio, intente colocarlo de vuelta en su '
        'lugar y muerda suavemente sobre un pa&ntilde;o limpio; si no puede, gu&aacute;rdelo en leche o en su propia '
        'saliva &mdash; nunca en agua. Luego ll&aacute;menos de inmediato. La probabilidad de salvarlo baja mucho con '
        'cada hora que pasa.'),
       ('Tengo mucha ansiedad al dentista.',
        'D&iacute;galo al llamar. La comodidad, la sedaci&oacute;n y el manejo de la ansiedad son una de las fortalezas '
        'reconocidas de AIDM y se pueden coordinar tambi&eacute;n para tratamiento de emergencia. La sedaci&oacute;n y '
        'la anestesia se cobran por separado del tratamiento.'),
       ('&iquest;Necesito referencia y d&oacute;nde puedo parquear?',
        'No se necesita referencia. Hay parqueo gratuito en el garaje justo al lado, en 1401 Philomena Street, Mueller '
        '&mdash; a minutos de la I-35 y la calle 51.')],
  ctk='Abierto de lunes a s&aacute;bado, 7 a.m. a 7 p.m.',
  cth2='&iquest;Tiene dolor? <em>Ll&aacute;menos primero.</em>',
  ctsub='El <a href="tel:+17374342436" style="color:#4fc3f7">(737) 434-2436</a> es la v&iacute;a m&aacute;s r&aacute;pida '
        'para conseguir un espacio hoy. Si prefiere que le llamemos, d&eacute;jenos sus datos. Atendemos en espa&ntilde;ol.',
  wholabel='&iquest;Qui&eacute;n necesita atenci&oacute;n?',
  who2=['Para mí','Para mi hijo o hija','Para mi pareja o madre/padre','Para otra persona'],
  placeholder='Qué le duele, desde cuándo, y si hay inflamación…',
  ctsubmit='Ll&aacute;menme para una cita hoy',
  legalextra=LEGAL_ES,
  terms=[('La oferta','Una evaluaci&oacute;n dental de emergencia el mismo d&iacute;a, enfocada en el problema, con radiograf&iacute;as seg&uacute;n sean necesarias para el diagn&oacute;stico.'),
         ('Para qui&eacute;n es','Pacientes con un problema dental urgente. Las citas se priorizan cl&iacute;nicamente y est&aacute;n sujetas a disponibilidad.'),
         ('Precio','No hay precio publicado para la evaluaci&oacute;n de emergencia. El costo de cualquier tratamiento que resulte se presenta antes de iniciarlo.'),
         ('Qu&eacute; no incluye','El tratamiento restaurativo, quir&uacute;rgico y de especialidad derivado de la evaluaci&oacute;n, los honorarios de laboratorio, la sedaci&oacute;n y la anestesia son adicionales.'),
         ('Importante','Si tiene inflamaci&oacute;n facial que se extiende, dificultad para respirar o tragar, o sangrado no controlado, acuda a una sala de emergencias en lugar de agendar una cita dental.')],
)

ALSOFINE_ES = [(
 '''<p class="optfine" style="margin:1.1rem 0 0">Package pricing applies only to the services specifically listed.
        Final recommendations, eligibility and fees are determined following a comprehensive clinical evaluation.</p>''',
 '''<p class="optfine" style="margin:1.1rem 0 0">El precio del paquete aplica &uacute;nicamente a los servicios
        expresamente listados. Las recomendaciones finales, la elegibilidad y los honorarios se determinan tras una
        evaluaci&oacute;n cl&iacute;nica completa.</p>''')]
ES_EMERGENCIA['i18n'] = CHROME + ALSOFINE_ES

for _o in (ES_NUEVO, ES_EMERGENCIA):
    _o['legal_html'] = LEGAL_ES_HTML

ALL = [ES_NUEVO, ES_EMERGENCIA]
