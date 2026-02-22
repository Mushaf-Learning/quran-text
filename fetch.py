#!/usr/bin/env python3
"""
Download Quran text files from Tanzil.net
Source: https://tanzil.net
License: Creative Commons Attribution 3.0

Usage: python3 fetch.py
"""
import urllib.request
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://tanzil.net/pub/download/index.php"

downloads = [
    {
        "params": "quranType=uthmani&outType=txt&agree=true",
        "output": os.path.join(BASE_DIR, "uthmani", "quran-uthmani.txt"),
        "label": "Uthmani text"
    },
    {
        "params": "quranType=uthmani&outType=xml&agree=true",
        "output": os.path.join(BASE_DIR, "uthmani", "quran-uthmani.xml"),
        "label": "Uthmani XML"
    },
    {
        "params": "quranType=simple-clean&outType=txt&agree=true",
        "output": os.path.join(BASE_DIR, "simple", "quran-simple-clean.txt"),
        "label": "Simple Clean text"
    },
    {
        "params": "quranType=simple-clean&outType=xml&agree=true",
        "output": os.path.join(BASE_DIR, "simple", "quran-simple-clean.xml"),
        "label": "Simple Clean XML"
    },
]

success = 0
failed = 0

for dl in downloads:
    url = f"{BASE_URL}?{dl['params']}"
    output = dl["output"]
    label = dl["label"]

    os.makedirs(os.path.dirname(output), exist_ok=True)

    print(f"Downloading {label}...")
    try:
        urllib.request.urlretrieve(url, output)
        size = os.path.getsize(output)
        print(f"  OK: {size:,} bytes -> {output}")
        success += 1
    except Exception as e:
        print(f"  FAILED: {e}")
        failed += 1

print(f"\nComplete: {success} succeeded, {failed} failed")
sys.exit(1 if failed > 0 else 0)
