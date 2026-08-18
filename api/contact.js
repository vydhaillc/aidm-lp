import { Resend } from "resend";
import { createClient } from "@supabase/supabase-js";

/**
 * AIDM braces landing page — lead endpoint.
 * Mirrors the De Anza Smiles route: insert into the shared Supabase `leads`
 * table AND email via Resend, succeeding if either one works, so a database
 * outage never costs the practice a lead.
 */
const LEAD_SOURCE = "aidm-braces-lp";

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

function esc(v) {
  return String(v == null ? "" : v).replace(/[<>&]/g, (c) =>
    ({ "<": "&lt;", ">": "&gt;", "&": "&amp;" }[c])
  );
}

const VYDHAI_FOOTER = `
  <hr style="margin-top:32px;border:none;border-top:1px solid #eee;" />
  <p style="font-size:12px;color:#999;margin-top:8px;">
    This lead was captured by the braces landing page, built &amp; managed by
    <a href="https://vydhai.com" style="color:#999;">Vydhai</a>.
  </p>
`;

function renderHtml(f) {
  const row = (k, v) =>
    v ? `<p style="margin:4px 0"><strong>${k}:</strong> ${esc(v)}</p>` : "";
  const campaign = [f.utm_source, f.utm_medium, f.utm_campaign]
    .filter(Boolean)
    .join(" / ");
  return `
    <h2 style="color:#0d3b66;">New Lead — AIDM Comprehensive Braces $2,950</h2>
    ${row("Name", `${f.first_name || ""} ${f.last_name || ""}`.trim())}
    ${row("Mobile", f.phone)}
    ${row("Email", f.email)}
    ${row("This is for", f.patient_type)}
    ${row("Notes", f.notes)}
    ${row("Filled in on", f.form)}
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

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method Not Allowed" });
  }

  const raw = await readBody(req);
  const f = raw?.form || raw || {};
  const name = `${f.first_name || ""} ${f.last_name || ""}`.trim() || f.name;

  if (!name || !f.email || !f.phone) {
    return res.status(400).json({
      error: "Missing required fields.",
      received: Object.keys(f || {}),
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
          form_type: f.form || "braces-lp",
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
      subject: `New Braces Lead ($2,950) — ${name} — via Vydhai`,
      html: renderHtml(f),
      reply_to: f.email,
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

  return res.status(200).json({
    ok: true,
    leadId,
    emailDelivered: !emailError,
    ...(emailError ? { emailError } : {}),
    ...(dbError ? { dbWarning: dbError } : {}),
  });
}
