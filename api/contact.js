import { Resend } from "resend";
import { createClient } from "@supabase/supabase-js";

/**
 * AIDM landing pages — lead endpoint, shared by all twelve offer pages.
 * Mirrors the De Anza Smiles route: insert into the shared Supabase `leads`
 * table AND email via Resend, succeeding if either one works, so a database
 * outage never costs the practice a lead.
 */
const LEAD_SOURCE = "aidm-lp";

/**
 * The `offer` hidden field on every page keys this table, which is what puts
 * the offer — not the patient's name — in the subject line. Anything not
 * listed still sends; it just falls back to the raw offer id.
 */
const OFFERS = {
  "new-patient-special-100":          { label: "New Patient Special", price: "$100" },
  "new-patient-special-100-es":       { label: "New Patient Special (ES)", price: "$100" },
  "emergency-dental-same-day":        { label: "Emergency Dental Care" },
  "emergency-dental-same-day-es":     { label: "Emergency Dental Care (ES)" },
  "ortho-2950-first-100":             { label: "Braces", price: "$2,950" },
  "ortho-comprehensive-braces-2950":  { label: "Braces", price: "$2,950" },
  "invisalign-3900":                  { label: "Invisalign", price: "$3,900" },
  "early-orthodontic-treatment-2500": { label: "Early Orthodontics", price: "$2,500" },
  "single-implant-crown-from-3750":   { label: "Single Implant + Crown", price: "from $3,750" },
  "full-arch-fixed-teeth-from-18000": { label: "Full-Arch Fixed Teeth", price: "from $18,000/arch" },
  "snap-in-dentures-from-9500":       { label: "Snap-In Dentures", price: "from $9,500/arch" },
  "wisdom-teeth-removal-from-200":    { label: "Wisdom Teeth", price: "from $200/tooth" },
  "root-canal-from-995":              { label: "Root Canal", price: "from $995" },
};

function offerOf(f) {
  const o = OFFERS[f.offer];
  if (o) return o;
  return { label: f.offer || "Enquiry" };          // an offer we have not mapped yet
}

/** "New Lead: Braces ($2,950) — via Vydhai" */
function subjectFor(f) {
  const o = offerOf(f);
  const priced = o.price ? `${o.label} (${o.price})` : o.label;
  return `New Lead: ${priced} — via Vydhai`;
}

function getEnv(name) {
  const v = process.env[name];
  if (!v) throw new Error(`Missing required env var: ${name}`);
  return v;
}

function splitAddressList(value) {
  if (!value) return undefined;
  const list = value.split(",").map((s) => s.trim()).filter(Boolean);
  return list.length ? list : undefined;
}

/**
 * Records the lead in GA4 via the Measurement Protocol, server-side. The
 * pages sit behind AIDM's GTM container (GTM-P5MV8V6G), which Vydhai cannot
 * publish into, so a client-side gtag('event', 'generate_lead') never
 * reaches G-XT8WC3BQ96 -- confirmed by observing the network traffic a real
 * submission produces, not assumed. Firing from here, on a request the
 * server actually accepted, sidesteps the container entirely.
 *
 * Needs GA4_MP_API_SECRET (created once in GA4: Admin > Data Streams >
 * aidm.dental stream > Measurement Protocol API secrets). Silently skipped
 * until that exists, so a lead is never blocked on it.
 */
async function sendGA4Lead(f, leadId) {
  const secret = process.env.GA4_MP_API_SECRET;
  if (!secret) return;
  const measurementId = process.env.GA4_MEASUREMENT_ID || "G-XT8WC3BQ96";
  // f.ga_client_id is read off the visitor's own _ga cookie on the page, so
  // this event joins their real GA4 session. A submission without that
  // cookie (blocked storage, ad blocker) still gets counted, just unlinked.
  const clientId = f.ga_client_id || `${Date.now()}.${Math.floor(Math.random() * 1e9)}`;
  try {
    const resp = await fetch(
      `https://www.google-analytics.com/mp/collect?measurement_id=${measurementId}&api_secret=${secret}`,
      {
        method: "POST",
        body: JSON.stringify({
          client_id: clientId,
          non_personalized_ads: false,
          events: [
            {
              name: "generate_lead",
              params: {
                lead_id: leadId || undefined,
                offer: f.offer || undefined,
                form_location: f.form || undefined,
                page_location: f.page || undefined,
                currency: "USD",
                value: 0,
              },
            },
          ],
        }),
      }
    );
    if (!resp.ok) {
      console.error("[contact] GA4 Measurement Protocol rejected:", resp.status, await resp.text());
    }
  } catch (err) {
    console.error("[contact] GA4 Measurement Protocol send failed:", err.message || err);
  }
}

function esc(v) {
  return String(v == null ? "" : v).replace(/[<>&]/g, (c) =>
    ({ "<": "&lt;", ">": "&gt;", "&": "&amp;" }[c])
  );
}

const VYDHAI_FOOTER = `
  <hr style="margin-top:32px;border:none;border-top:1px solid #eee;" />
  <p style="font-size:12px;color:#999;margin-top:8px;">
    This lead was captured by an AIDM landing page, built &amp; managed by
    <a href="https://vydhai.com" style="color:#999;">Vydhai</a>.
  </p>
`;

function renderHtml(f) {
  const row = (k, v) =>
    v ? `<p style="margin:4px 0"><strong>${k}:</strong> ${esc(v)}</p>` : "";
  const campaign = [f.utm_source, f.utm_medium, f.utm_campaign]
    .filter(Boolean)
    .join(" / ");
  const o = offerOf(f);
  return `
    <h2 style="color:#0d3b66;">New Lead &mdash; AIDM ${esc(o.label)}${o.price ? " " + esc(o.price) : ""}</h2>
    ${row("Name", `${f.first_name || ""} ${f.last_name || ""}`.trim())}
    ${row("Mobile", f.phone)}
    ${row("Email", f.email)}
    ${row("This is for", f.patient_type)}
    ${row("Message", f.notes)}
    ${row("Offer", f.offer)}
    ${row("Campaign", campaign)}
    ${row("gclid", f.gclid)}
    ${row("wbraid", f.wbraid)}
    ${row("Page", f.page)}
    ${VYDHAI_FOOTER}
  `;
}

/**
 * Bare Vercel functions do not reliably pre-parse the body: depending on the
 * runtime it arrives parsed, as a string, as a Buffer, or not at all. Read
 * the stream ourselves when it is missing so a submission is never lost to
 * a runtime detail.
 */
async function readBody(req) {
  const b = req.body;
  if (b && typeof b === "object" && !Buffer.isBuffer(b)) return b;
  let text = "";
  if (typeof b === "string") text = b;
  else if (Buffer.isBuffer(b)) text = b.toString("utf8");
  else {
    const chunks = [];
    for await (const c of req) chunks.push(c);
    text = Buffer.concat(chunks).toString("utf8");
  }
  if (!text) return {};
  try {
    return JSON.parse(text);
  } catch {
    return Object.fromEntries(new URLSearchParams(text));   // form-encoded
  }
}

/* The page is served from GitHub Pages and Vercel, so the POST is
   cross-origin. Allowlist the hosts it can legitimately come from rather
   than opening this up with a wildcard. */
const ALLOWED_ORIGINS = [
  "https://aidm.vydhai.com",
  "https://aidm-lp.vercel.app",
  "https://aidm.dental",
  "http://localhost:8901",
  "http://localhost:8904",
];

function cors(req, res) {
  const origin = req.headers.origin;
  if (origin && ALLOWED_ORIGINS.includes(origin)) {
    res.setHeader("Access-Control-Allow-Origin", origin);
    res.setHeader("Vary", "Origin");
  }
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  res.setHeader("Access-Control-Max-Age", "86400");
}

export default async function handler(req, res) {
  cors(req, res);
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method Not Allowed" });
  }

  const raw = await readBody(req);
  // The other client sites post {form:{…}}; this page posts a flat object and
  // carries its own `form` field naming which of the two forms was used. Only
  // treat `form` as the envelope when it is actually an object, or the string
  // gets unwrapped into a lookalike and every field reads as undefined.
  const f =
    raw && typeof raw.form === "object" && raw.form !== null ? raw.form : raw || {};
  const name = `${f.first_name || ""} ${f.last_name || ""}`.trim() || f.name;

  // Every offer page labels email "(optional)" and only validates name +
  // phone client-side — email must not be required here too, or a patient
  // who leaves it blank (as the form invites) gets a false "that did not
  // go through" and their lead is dropped.
  if (!name || !f.phone) {
    return res.status(400).json({
      error: "Missing required fields.",
      received: Object.keys(f || {}).slice(0, 20),
    });
  }

  let leadId = null;
  let dbError = null;

  if (process.env.SUPABASE_URL && process.env.SUPABASE_SERVICE_ROLE_KEY) {
    try {
      const supabase = createClient(
        process.env.SUPABASE_URL,
        process.env.SUPABASE_SERVICE_ROLE_KEY
      );
      const { data, error } = await supabase
        .from("leads")
        .insert({
          source: LEAD_SOURCE,
          form_type: f.form || "aidm-lp",
          name,
          email: f.email,
          phone: f.phone,
          data: {
            patient_type: f.patient_type || null,
            notes: f.notes || null,
            offer: f.offer || null,
            gclid: f.gclid || null,
            wbraid: f.wbraid || null,
            utm_source: f.utm_source || null,
            utm_medium: f.utm_medium || null,
            utm_campaign: f.utm_campaign || null,
            page: f.page || null,
            submitted_at: f.submitted_at || null,
          },
        })
        .select("id")
        .single();
      if (error) throw error;
      leadId = data?.id ?? null;
    } catch (err) {
      dbError = err.message || String(err);
      console.error("[contact] Supabase insert failed:", dbError);
    }
  }

  let emailError = null;
  try {
    const resend = new Resend(getEnv("RESEND_API_KEY"));
    await resend.emails.send({
      from: getEnv("MAIL_FROM"),
      to: splitAddressList(getEnv("MAIL_TO")),
      cc: splitAddressList(process.env.MAIL_CC),
      bcc: splitAddressList(process.env.MAIL_BCC),
      subject: subjectFor(f),
      html: renderHtml(f),
      reply_to: f.email || undefined,   // an empty string is not a valid reply-to
    });
  } catch (err) {
    emailError = err.message || String(err);
    console.error("[contact] Resend send failed:", emailError);
  }

  if (emailError && !leadId) {
    return res.status(500).json({
      error: "Submission failed. Please try again or call us directly.",
    });
  }

  await sendGA4Lead(f, leadId);

  return res.status(200).json({
    ok: true,
    leadId,
    emailDelivered: !emailError,
    ...(emailError ? { emailError } : {}),
    ...(dbError ? { dbWarning: dbError } : {}),
  });
}
