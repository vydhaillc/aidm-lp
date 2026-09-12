#!/usr/bin/env python3
"""Adds Meta pixel Lead + Contact events to every live aidm.dental landing page.

Hand-applied to the generated pages because tools/lp/build.py is currently
broken (AssertionError: sub navcta). Idempotent: a page that already carries
the events is skipped. Aborts before writing anything if any page's anchor
text doesn't match exactly once.
"""
import io, os, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

LEAD_ANCHOR = """          offer_path:    location.pathname
        });
      }
      done(r.ok);"""
LEAD_NEW = """          offer_path:    location.pathname
        });

        /* Meta (pixel 1733193964651493), same confirmed-submission signal.
           Deliberately bare: no name, phone, email or treatment goes to
           Meta. Health data stays off a platform that signs no BAA. */
        if (window.fbq) fbq('track', 'Lead');
      }
      done(r.ok);"""

TEL_ANCHOR = "  /* ── sticky nav ─"
TEL_NEW = """  /* Meta Contact event on a tap of any phone link. Delegated on the
     document, so it also sees tel: links Patient Prism swaps in later. */
  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('a[href^="tel:"]');
    if (a && window.fbq) fbq('track', 'Contact');
  });

  /* ── sticky nav ─"""

MARK = "fbq('track', 'Lead')"

files = subprocess.run(['git', 'ls-files', '*.html'], cwd=ROOT, capture_output=True,
                       text=True).stdout.split()
pages = [f for f in files
         if "fbq('init', '1733193964651493')" in io.open(os.path.join(ROOT, f), encoding='utf-8').read()]

plan, problems = {}, []
for f in pages:
    s = io.open(os.path.join(ROOT, f), encoding='utf-8').read()
    if MARK in s:
        print('already done:', f)
        continue
    n_lead, n_tel = s.count(LEAD_ANCHOR), s.count(TEL_ANCHOR)
    if n_lead != 1 or n_tel != 1:
        problems.append(f'{f}: lead anchor x{n_lead}, tel anchor x{n_tel}')
        continue
    plan[f] = s.replace(LEAD_ANCHOR, LEAD_NEW).replace(TEL_ANCHOR, TEL_NEW)

if problems:
    sys.exit('Nothing written. Anchor mismatch:\n  ' + '\n  '.join(problems))
for f, s in plan.items():
    io.open(os.path.join(ROOT, f), 'w', encoding='utf-8').write(s)
    print('patched:', f)
print(f'{len(plan)} patched, {len(pages) - len(plan)} skipped, {len(pages)} pixel pages total')
