/**
 * AIDM braces LP — lead endpoint.
 *
 * Emails every enquiry to shankar@vydhai.com and appends it to a sheet, so
 * there is a record even if a mail is missed. The data never leaves the
 * Vydhai Google account: no third party sees patient contact details.
 *
 * Deploy (once, ~3 minutes):
 *   1. script.google.com  ->  New project  ->  paste this file over Code.gs
 *   2. Deploy  ->  New deployment  ->  type: Web app
 *        Execute as:        Me (shankar@vydhai.com)
 *        Who has access:    Anyone
 *   3. Authorise when prompted, then copy the /exec URL and send it to me.
 */

var NOTIFY   = 'shankar@vydhai.com';
var SHEET_ID = '';           // optional: paste a Google Sheet id to log leads

function doPost(e) {
  var lead = {};
  try { lead = JSON.parse(e.postData.contents); } catch (err) { lead = e.parameter || {}; }

  var name = ((lead.first_name || '') + ' ' + (lead.last_name || '')).trim() || 'Unknown';

  var rows = [
    ['Name',        name],
    ['Mobile',      lead.phone || ''],
    ['Email',       lead.email || ''],
    ['This is for', lead.patient_type || ''],
    ['Notes',       lead.notes || ''],
    ['Offer',       lead.offer || ''],
    ['Form',        lead.form || ''],
    ['Campaign',    [lead.utm_source, lead.utm_medium, lead.utm_campaign].filter(String).join(' / ')],
    ['gclid',       lead.gclid || ''],
    ['wbraid',      lead.wbraid || ''],
    ['Page',        lead.page || ''],
    ['Submitted',   lead.submitted_at || new Date().toISOString()]
  ];

  var html = '<div style="font:14px/1.6 Arial,Helvetica,sans-serif;color:#222">' +
             '<p><b>New enquiry from the braces landing page</b></p><table cellpadding="6" ' +
             'style="border-collapse:collapse;font-size:14px">' +
             rows.map(function (r) {
               return '<tr><td style="color:#6b7796;white-space:nowrap">' + r[0] +
                      '</td><td><b>' + String(r[1]).replace(/</g, '&lt;') + '</b></td></tr>';
             }).join('') +
             '</table></div>';

  MailApp.sendEmail({
    to: NOTIFY,
    replyTo: lead.email || NOTIFY,
    subject: 'AIDM braces LP — new enquiry from ' + name,
    htmlBody: html,
    body: rows.map(function (r) { return r[0] + ': ' + r[1]; }).join('\n')
  });

  if (SHEET_ID) {
    try {
      SpreadsheetApp.openById(SHEET_ID).getSheets()[0]
        .appendRow(rows.map(function (r) { return r[1]; }));
    } catch (err) { /* a logging failure must never lose the email */ }
  }

  return ContentService
    .createTextOutput(JSON.stringify({ ok: true }))
    .setMimeType(ContentService.MimeType.JSON);
}

/** Apps Script web apps do not answer CORS preflight, which is why the page
 *  posts text/plain-safe JSON without custom headers. */
function doGet() {
  return ContentService.createTextOutput('AIDM lead endpoint is live.');
}
