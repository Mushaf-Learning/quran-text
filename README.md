# Quran Text

Open-source Quran text data for developers building Quranic applications.

## What's Included

### Quran Text
- **Uthmani script** — Standard Mushaf text with full diacritics
- **Simple script** — Simplified Arabic for search and indexing

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
- **Surah info** — Names (Arabic/English), ayah counts, revelation order, Makki/Madani
- **Juz boundaries** (30 parts)
- **Hizb boundaries** (60 groups)
- **Rub al-Hizb boundaries** (240 quarters)
- **Ruku markers**
- **Madinah Mushaf page mapping** (604 pages, 15 lines/page)
- **Sajdah Tilawah positions** (15 locations)

## Directory Structure

```
uthmani/          # Uthmani script text (XML, JSON, SQL)
simple/           # Simple script text
translations/     # Translation files by language code
metadata/         # Structural data (juz, hizb, rub, sajdah, pages)
```

## Data Sources & Attribution

- Quran text: [Tanzil.net](https://tanzil.net) — verified Uthmani text
- Translations: [Tanzil.net](https://tanzil.net/trans/) — 140+ translations
- Metadata: [Tanzil.net](https://tanzil.net/docs/quran_metadata)

## Usage

```dart
// Example: Load surah metadata
final metadata = json.decode(await File('metadata/surahs.json').readAsString());
print(metadata[0]['name_arabic']); // الفاتحة
print(metadata[0]['ayah_count']);   // 7
```

## License

MIT — Free for personal and commercial use. See [LICENSE](LICENSE).

Quran text sourced from Tanzil.net must retain attribution per their terms.
