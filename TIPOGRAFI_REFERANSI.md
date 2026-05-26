# TİPOGRAFİ REFERANSI
## Slanted №41 — Message Design · Paragraph Style Şeması

> **Kaynak:** dergi_son.html CSS — tüm değerler birebir oradan alındı.
> **Amaç:** InDesign'da paragraph/character styles kurmak için tek sayfa referans.
> **Not:** Tüm değerler **point (pt)** cinsinden. Leading formatı: **size/leading** (örn. `9/13pt`). Tracking değerleri InDesign tracking birimindedir (1000 = 1em).

---

## 1 · FONT AİLELERİ (üç font, başka yok)

| Rol | Font | Ağırlıklar | Stil |
|---|---|---|---|
| **Display + Body** | **Inter** | Regular 400, Medium 500, SemiBold 600, Bold 700, Black 900 | Roman |
| **Mono / Teknik** | **IBM Plex Mono** | Regular 400, Medium 500 | Roman |
| **Pull Quote** | **EB Garamond** | Regular 400 | **Italic** |

> Italic sadece Garamond. Inter italic kullanılmaz, Mono italic kullanılmaz.

---

## 2 · RENK PALETİ (hatırlatma)

| Adı | HEX | CMYK | Kullanım |
|---|---|---|---|
| **Ink** | `#0A0A0A` | K100 | Body, headings — varsayılan |
| **Paper** | `#EDEAE3` | C2 M3 Y6 | Zemin |
| **Red** | `#CC1A0A` | M100 Y100 (Pantone 1797 C spot) | Chapter no, pull-quote rule, dataviz noise — **sadece 4 yer** |
| **Gray** | `#8A8580` | K40 | Sidenote, dataviz annotation |
| **Gray-soft** | `#B8B5AC` | K30 | Decay ghost, draft layer |

---

## 3 · SAYFADA HER YERDE (running)

| Eleman | Font | Size/Lead | Tracking | Case |
|---|---|---|---|---|
| `page-header` | Mono Regular | 7pt | 60 (0.06em) | as-typed |
| `page-folio` (sayfa no) | Mono Regular | 8pt | 0 | — |

---

## 4 · BODY METİN (gövde paragrafları)

| Eleman | Font | Size/Lead | Tracking | Case |
|---|---|---|---|---|
| **Body** (varsayılan p) | Inter Regular | **9/13pt** | 0 | as-typed |
| **Three-col body** | Inter Regular | 9/13pt | 0 | as-typed |
| **Two-col body** | Inter Regular | 9/13pt | 0 | as-typed |
| **Sidenote** (yan not, gri) | Inter Regular | 8/11pt | 0 | as-typed |

> Tüm body metin tek bir paragraph style: **`Body / Inter 9-13`**. Sütun varyasyonları aynı style'ı paylaşır, sadece text frame genişliği değişir.

### Body başlıkları (column heads)

| Eleman | Font | Size/Lead | Tracking | Case |
|---|---|---|---|---|
| `col-h2` (büyük section başlık) | Inter SemiBold (600) | **14/16pt** | -5 (-0.005em) | as-typed |
| `col-h3` (küçük section başlık) | Inter Medium (500) | 9/13pt | 100 (0.1em) | **UPPERCASE** |

### Drop-cap'ler

| Eleman | Font | Size | Notlar |
|---|---|---|---|
| Normal drop-cap (`drop-cap::first-letter`) | Inter Black (900) | **70pt** | line-height 0.85, ilk harfin 3-4 satır boyu |
| Bleed drop-cap (`drop-cap-bleed::first-letter`) | Inter Black (900) | **180pt** | line-height 0.78, tracking -60 (-0.06em); sayfa 22 için |

---

## 5 · BAŞLIKLAR (genel hiyerarşi)

| Eleman | Font | Size/Lead | Tracking | Case |
|---|---|---|---|---|
| `h1` (büyük başlık) | Inter Black (900) | **90/86pt** | -25 (-0.025em) | as-typed |
| `h1.massive` | Inter Black (900) | **200pt** / lh 0.9 | -40 (-0.04em) | as-typed |
| `h1.medium` | Inter Black (900) | **48/50pt** | 0 | as-typed |
| `h2` (orta başlık) | Inter SemiBold (600) | 16/20pt | -5 | as-typed |
| `h2-slash` | Inter Bold (700) | 14/16pt | -5 | as-typed |
| `h3` (küçük başlık) | Inter Medium (500) | 11/13pt | 80 (0.08em) | **UPPERCASE** |
| `intro-question` (sayfa 4-5) | Inter Black (900) | **72/70pt** | -20 (-0.02em) | as-typed |
| `closing-statement` (sayfa 50) | Inter Black (900) | **36/42pt** | -20 | as-typed |

---

## 6 · MONO ETİKETLER (Plex Mono kullanılan her yer)

Tümü uppercase, çoğu yüksek tracking. Bunlar Slanted'in teknik dokuz dokunuş.

| Eleman | Size/Lead | Tracking | Notlar |
|---|---|---|---|
| `chapter-number` | 11/13pt | 160 (0.16em) | Caps, bölüm numarası |
| `caption` | 7/10pt | 40 (0.04em) | as-typed, görsel caption |
| `dataviz-tag` | 7pt | 60 (0.06em) | Caps |
| `fig-tape` | 7pt | 160 | Caps, FIG. tape etiketleri |
| `dataviz-annotation` | 6pt | 120 | Caps, dataviz kenar notları |
| `dataviz-spec-block` | 6/9pt | 60 | Caps, TRIM/SCALE blokları |
| `attribution-strip` | 7pt | 160 | Pettersson attribution strip |
| `marginal-vertical` | 7pt | 160 | Caps, 90° dikey kenar notu |
| `marginal-vertical-r` | 7pt | 180 (0.18em) | Caps, sağ kenar varyantı |
| `recap` (section break içinde) | 7pt | 160 | Caps |
| `next` (section break içinde) | 6pt | 160 | "↓ NEXT · CH 02 ·" formatı |
| `toc-title` (Inter, mono değil) | Inter SemiBold 11pt | 100 | Caps |
| `signature` (overload sayfası) | 7pt | 160 | "INFORMATION × 27 ·" satırı |
| `footer-spec` | 6pt | 120 | Sayfa 24 alt satır |

---

## 7 · PULL QUOTE'LAR (5 varyant — hepsi EB Garamond Italic)

Slanted disiplini: her bölümde farklı bir pull quote varyantı.

| Eleman | Size/Lead | Tracking | Nerede |
|---|---|---|---|
| `pull-quote` (standart, ince kural) | **14/20pt** | 0 | Sayfa 13, 25 — body içinde inline |
| `pull-quote-box` (kutulu) | **16/22pt** | 0 | Sayfa 39 — Ch04 |
| `pull-quote-rotated` (90° döndürülmüş) | **16/22pt** | 0 | Sayfa 31 — Ch03 |
| `pull-quote-redacted` (sansürlü) | **18/26pt** | 0 | Sayfa 47 — Ch05 |
| `pull-quote-giant` (tam sayfa) | **56/60pt** | -10 (-0.01em) | Sayfa 49 — Ch05 closing |

### Diğer italic kullanımlar

| Eleman | Size/Lead | Nerede |
|---|---|---|
| `decay-text` (orijinal alıntı) | 22/30pt | Sayfa 14 |
| `decay-broken` (parçalanmış alıntı) | 22/32pt | Sayfa 15 |
| `ghost-quote` (section break ghost) | 36/42pt | Sayfa 18, 26, 36, 44 |

> **Pull Quote paragraph style ayarı (HANDOFF'tan):** Tracking 0, Case Normal, 14/20pt EB Garamond Italic, **1pt red rule above**.

---

## 8 · BÖLÜM AÇILIŞLARI (her bölüm farklı, kasıtlı)

Beş bölümün her birinin opener tipografisi farklı — bölüm konseptini fiziksel olarak somutlaştırıyor.

| Bölüm | Class | Display Size | Subtitle | Notlar |
|---|---|---|---|---|
| **01 SIGNAL** (p.9) | `opener-explosion .letter` | Harfler ayrı boylarda: **S 88pt / I 64pt / G 130pt (red) / N 72pt / A 100pt / L 56pt** | EB Garamond Italic 13pt | Takımyıldız dağılımı |
| **02 NOISE** (p.19) | `opener-band .title` `.ruis` | Inter Black **150pt**, lh 0.85, tracking -50 | EB Garamond Italic 12pt | Çift dilli (RUIS + NOISE), 28° diyagonal |
| **03 FRAME** (p.27) | `opener-bleed-frame .word-bleed` | Inter Black **380pt**, lh 0.82, tracking -60 | EB Garamond Italic 13pt | Dört kenardan bleed |
| **04 TOOLS** (p.37) | `opener-empty .word-quiet` | Inter **Regular** 64pt (NOT Black — fısıltı), lh 0.9, tracking -20 | (legend mono 7pt) | Büyük negatif alan |
| **05 MEANING** (p.45) | `opener-mirror .word-half` | Inter Black **130pt**, lh 0.85, tracking -40 | EB Garamond Italic 13pt | Yarısı mirror'lanmış |

### Genel opener helper'ları

| Eleman | Size/Lead | Notlar |
|---|---|---|
| `opener-title` | Inter Black 150pt, lh 0.85 | Eski opener (kullanılmıyorsa silinebilir) |
| `opener-subtitle` | EB Garamond Italic 14pt | Genel subtitle |
| `opener-massive-number` | Inter Black 220pt | Bölüm numarası dev versiyonu |
| `opener-cropped-letters` | Inter Black 320pt | Kenardan kırpılmış harfler |
| `overprint-title` | Inter Black 240pt | Sayfa 51 multilingual overprint örneği |

---

## 9 · TOC / PUBLICATION MAP (sayfa 6-7)

| Eleman | Font | Size/Lead | Tracking | Case |
|---|---|---|---|---|
| `toc-title` | Inter SemiBold | 11pt | 100 | UPPERCASE |
| `toc-entry .ch-mark` (01, 02…) | Mono Regular | 11pt | 160 | as-typed |
| `toc-entry .ch-name` | Inter Bold (700) | 16pt | -10 | as-typed |
| `toc-entry .ch-page` | Mono Regular | 9pt | 0 | — |
| `toc-entry .ch-blurb` | Inter Regular | 8/11pt | 0 | as-typed |

### Publication map (sayfa 6) — boyut bölüm sayfa sayısıyla orantılı

| Eleman | Font | Size | Tracking | Case |
|---|---|---|---|---|
| `pub-map-block .num` | Mono Regular | 11pt | 160 | as-typed |
| `pub-map-block .name` (10 sayfalık bölüm) | Inter Black | **32pt** | -20 | as-typed |
| `pub-map-block .name` (8 sayfalık bölüm) | Inter Black | **26pt** | -20 | as-typed |
| `pub-map-block .name` (7 sayfalık ya da küçük) | Inter Black | **22pt** | -20 | as-typed |
| `pub-map-block .pages` | Mono Regular | 8pt | 0 | — |
| `pub-map-block .blurb` | Inter Regular | 7/10pt | 0 | as-typed |

---

## 10 · ÖZEL ZONE TİPOGRAFİSİ

### Pyramid (sayfa 20 — DIKW)

| Layer | Size | Font |
|---|---|---|
| L1 (DATA, en geniş) | **28pt** | Inter Black |
| L2 (INFORMATION) | **24pt** | Inter Black |
| L3 (KNOWLEDGE) | **20pt** | Inter Black |
| L4 (WISDOM, en dar) | **16pt** | Inter Black |

> Hepsi tracking -20 (-0.02em), text-transform none.

### Principles Grid (sayfa 28-29 — 16 prensip)

| Eleman | Font | Size/Lead | Tracking | Case |
|---|---|---|---|---|
| `cell .num` | Mono Medium | 20pt | -20 | — |
| `cell .name` | Inter Black | 11/12pt | -10 | UPPERCASE |
| `cell .def` (italic tanım) | EB Garamond Italic | 8/10pt | 0 | as-typed |
| `cell .lang` (EN / NL) | Mono Regular | 5pt | 160 | as-typed |

### Tools Matrix (sayfa 38)

| Eleman | Font | Size | Tracking | Case |
|---|---|---|---|---|
| `th` (kolon başlığı: Clarity, Emotion…) | Mono Medium | 7pt | 160 | UPPERCASE |
| `td.tool-name` (PEN, EYE, RULER…) | Inter Bold (700) | 14pt | -10 | as-typed |
| `dot-scale` (●●●●○) | Mono Regular | 12pt | **400 (0.4em)** | — |

### Four Readings (sayfa 46-47)

| Eleman | Font | Size/Lead | Tracking | Case |
|---|---|---|---|---|
| `reading-label` ([01] — [02]…) | Mono Regular | 7pt | 160 | UPPERCASE |
| `reading-caption` | Inter Regular | 8/11pt | 0 | as-typed |

### Information Overload (sayfa 24)

| Eleman | Font | Size | Notlar |
|---|---|---|---|
| `overload-extreme .w` | Inter Black | **değişken — 8pt'den 220pt'ye** | 27 örnek, line-height 0.9, tracking -30 |

---

## 11 · BACK MATTER (sayfa 53-55)

### Bibliography (sayfa 53)

| Eleman | Font | Size/Lead | Tracking | Case |
|---|---|---|---|---|
| `group-head` (PRIMARY, DESIGN, COMM…) | Mono Regular | 8pt | 160 | UPPERCASE |
| `bib-group p` (entry) | Mono Regular | 7/11pt | 0 | as-typed |

### Index (sayfa 54)

| Eleman | Font | Size/Lead | Tracking | Case |
|---|---|---|---|---|
| `letter-head` (A, B, C…) | Mono Medium | 14pt | 40 | as-typed |
| `index-letter p` (entry) | Inter Regular | 8/12pt | 0 | as-typed |

### Colophon (sayfa 3, 55)

| Eleman | Font | Size/Lead | Tracking | Case |
|---|---|---|---|---|
| `colophon-title` (kategori başlığı) | Mono Medium | 9pt | 80 | UPPERCASE |
| `colophon-stack p` | Mono Regular | 7/10pt | 0 | as-typed |

---

## 12 · SECTION BREAKS (sayfa 18, 26, 36, 44)

Her bölüm sonunda aynı şablon. Tek bir Master Page olarak InDesign'da kurulabilir.

| Eleman | Font | Size/Lead | Tracking | Case |
|---|---|---|---|---|
| `big-slash` (dev kırmızı `/`) | Inter Black | **220pt**, lh 0.85 | 0 | — |
| `ghost-quote` (10% opak) | EB Garamond Italic | 36/42pt | -10 | as-typed |
| `recap` (özet satır) | Mono Regular | 7pt | 160 | UPPERCASE |
| `next` (sonraki bölüm pointer) | Mono Regular | 6pt | 160 | as-typed |

---

## 13 · COVER (sayfa 1) — SVG içinde

SVG'deki text'ler InDesign paragraph style değil, doğrudan SVG `font-size`. **Cover finalize edildi, dokunma.** Yine de referans için:

| Eleman | Font | Size (SVG unit) |
|---|---|---|
| SLANTED PUBLISHER (üst) | Mono Regular | ~3pt SVG |
| RESEARCH SERIES №41 — MESSAGE DESIGN | Mono Regular | ~3pt SVG |
| M E S S AGE (büyük) | Inter Black | büyük letter cluster |
| DESIGN | Inter Black | monumental |
| №41 (ghost sağ alt) | Inter Black | 44pt, opacity 0.08 |

---

## ⚡ HIZLI ÖZET — InDesign'da Kuracağın 10 Paragraph Style

Tüm yayını 10 paragraph style ile yönetebilirsin. Geri kalan her şey **Character Style** veya local override.

1. **`Body / Inter 9-13`** — Inter Regular 9/13pt — tüm body
2. **`Sidenote / Inter 8-11 Gray`** — Inter Regular 8/11pt, gray fill
3. **`H1 / Inter Black 90`** — Inter Black 90/86pt, tracking -25
4. **`H2 / Inter SemiBold 14-16`** — Inter SemiBold 14/16pt
5. **`H3 / Inter Medium 11 Caps`** — Inter Medium 11pt, tracking 80, UPPERCASE
6. **`Chapter Number / Mono 11 Red`** — Mono 11pt, tracking 160, UPPERCASE, red fill
7. **`Caption / Mono 7-10`** — Mono Regular 7/10pt, tracking 40
8. **`Fig Tape / Mono 7 Caps`** — Mono 7pt, tracking 160, UPPERCASE
9. **`Pull Quote / Garamond Italic 14-20`** — EB Garamond Italic 14/20pt, **1pt red rule above**
10. **`Chapter Subtitle / Garamond Italic 13-16 Tint`** — EB Garamond Italic 13/16pt, paper @ 70% tint

> Opener'lar, pyramid, principles grid, tools matrix gibi tek seferlik tipografi block'ları **paragraph style yerine local formatting** olarak bırakılabilir — tek kez kullanılıyorlar.

---

## 🔧 InDesign Setup İpuçları

- **Baseline grid: 13pt** — body leading'le eşleşir. View → Grids & Guides → Show Baseline Grid ile kontrol et.
- **Tracking dönüştürme:** CSS'teki `letter-spacing: 0.16em` → InDesign'da `tracking 160`. (em değeri × 1000)
- **Leading conversion:** CSS `line-height: 13pt` → InDesign leading 13pt. CSS `line-height: 0.85` (unitless) → leading'i font-size × 0.85 olarak hesapla (örn. 150pt × 0.85 = 127.5pt leading).
- **Inter family OpenType:** Display weight'leri için Inter'in **TrueType (.ttf)** veya **OpenType (.otf)** dosyalarını yükle. Variable font versiyonu da çalışır.
- **EB Garamond:** Sadece Italic kullanılıyor — Regular varyantını yüklemene gerek yok.
- **IBM Plex Mono:** Regular ve Medium yeterli. Bold/italic gerekmiyor.

---

*Son güncelleme: 25 May 2026 · Kaynak: dergi_son.html CSS*
