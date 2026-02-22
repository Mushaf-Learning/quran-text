#!/bin/bash
# Download Quran text files from Tanzil.net
# Source: https://tanzil.net
# License: Creative Commons Attribution 3.0
#
# Usage: bash download.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_URL="https://tanzil.net/pub/download/index.php"

echo "Downloading Quran text files from Tanzil.net..."
echo ""

download() {
    local params="$1"
    local output="$2"
    local label="$3"

    printf "  %-30s" "$label..."
    if curl -sL -o "$SCRIPT_DIR/$output" "${BASE_URL}?${params}"; then
        local size
        size=$(wc -c < "$SCRIPT_DIR/$output" | tr -d ' ')
        echo "OK (${size} bytes)"
    else
        echo "FAILED"
        return 1
    fi
}

download "quranType=uthmani&outType=txt&agree=true" \
    "uthmani/quran-uthmani.txt" "Uthmani text"

download "quranType=uthmani&outType=xml&agree=true" \
    "uthmani/quran-uthmani.xml" "Uthmani XML"

download "quranType=simple-clean&outType=txt&agree=true" \
    "simple/quran-simple-clean.txt" "Simple Clean text"

download "quranType=simple-clean&outType=xml&agree=true" \
    "simple/quran-simple-clean.xml" "Simple Clean XML"

echo ""
echo "Done. Files saved to: $SCRIPT_DIR"
