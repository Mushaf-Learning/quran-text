# Quran Text

Open-source Quran text data for developers building Quranic applications.

## What's Included

### Quran Text
- **Uthmani script** -- Standard Mushaf text with full diacritics
- **Simple script** -- Simplified Arabic for search and indexing

### Translations (140+ languages)
Priority translations included:

| Language | Translator | Identifier |
|----------|-----------|-----------|
| English | Sahih International | `en.sahih` |
| English | Yusuf Ali | `en.yusufali` |
| English | Pickthall | `en.pickthall` |
| Urdu | Fateh Muhammad Jalandhri | `ur.jalandhry` |
| Urdu | Mufti Taqi Usmani | `ur.maududi` |
| French | Muhammad Hamidullah | `fr.hamidullah` |
| Turkish | Diyanet Isleri | `tr.diyanet` |
| Malay | Abdullah Basmeih | `ms.basmeih` |
| Indonesian | Ministry of Religious Affairs | `id.indonesian` |

### Metadata
- **Surah info** (`surahs.json`) -- All 114 surahs with Arabic/English names, ayah counts, revelation type and order, ruku counts, juz and page start positions
- **Quran structural data** (`quran-data.xml`) -- Complete Tanzil-format metadata
- **Page mapping** (`pages.json`) -- Madinah Mushaf 604-page mapping (15 lines/page)
- **Juz boundaries** (30 parts)
- **Hizb quarter boundaries** (240 quarters)
- **Manzil boundaries** (7 weekly reading divisions)
- **Ruku markers** (556 thematic sections)
- **Sajdah Tilawah positions** (15 locations: 11 recommended, 4 obligatory)

## Directory Structure

```
uthmani/           # Uthmani script text (TXT, XML)
simple/            # Simple/clean script text (TXT, XML)
translations/      # Translation files by language code
metadata/          # Structural data
  surahs.json      # All 114 surahs with full metadata
  quran-data.xml   # Tanzil-format XML with suras, juzs, hizbs, manzils, rukus, pages, sajdas
  pages.json       # Madinah Mushaf page boundaries (604 pages)
fetch.py           # Script to download Quran text from Tanzil.net
```

## Setup

Download the Quran text files from Tanzil.net:

```bash
python3 fetch.py
```

This downloads:
- `uthmani/quran-uthmani.txt` -- Uthmani text (plain text, one ayah per line)
- `uthmani/quran-uthmani.xml` -- Uthmani text (XML with surah/ayah structure)
- `simple/quran-simple-clean.txt` -- Simple clean text (plain text)
- `simple/quran-simple-clean.xml` -- Simple clean text (XML)

## Data Sources & Attribution

- Quran text: [Tanzil.net](https://tanzil.net) -- verified Uthmani text
- Translations: [Tanzil.net](https://tanzil.net/trans/) -- 140+ translations
- Metadata: [Tanzil.net](https://tanzil.net/docs/quran_metadata)

## Usage

```dart
// Example: Load surah metadata
final metadata = json.decode(await File('metadata/surahs.json').readAsString());
print(metadata[0]['name_arabic']); // الفاتحة
print(metadata[0]['ayah_count']);   // 7
```

## License

MIT -- Free for personal and commercial use. See [LICENSE](LICENSE).

Quran text sourced from Tanzil.net is distributed under Creative Commons Attribution 3.0. Attribution to Tanzil.net must be retained per their terms.
