#!/usr/bin/env python3
"""Rebuild every offer landing page from braces/index.html.

    python3 tools/lp/build.py

braces/index.html is the theme. Each page is that document with its
offer-specific blocks swapped out by lpkit.build(), so a theme change is made
once, here, and reappears on all twelve pages after a rebuild. The braces page
itself is edited by hand — it is both the template and offer 3.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lpkit, offers_a, offers_b, offers_es

for offer in offers_a.ALL + offers_b.ALL + offers_es.ALL:
    print(lpkit.build(offer))
