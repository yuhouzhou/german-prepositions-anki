# 🇩🇪 German Prepositions Master Suite (Präpositionen im Deutschen)

[![Release](https://img.shields.io/github/v/release/yuhouzhou/german-prepositions-anki?color=blue&label=Release)](https://github.com/yuhouzhou/german-prepositions-anki/releases/latest)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Anki](https://img.shields.io/badge/Anki-Ready-success.svg)](https://apps.ankiweb.net/)

A comprehensive, frequency-sorted Anki flashcard suite covering **439 essential German preposition combinations** across CEFR levels **A1 to C1**.

Organized into **4 distinct subdecks** inside a single unified master package:

```text
German::Prepositions (439 Cards Total)
├── 01 - Verbs with Prepositions (218 cards, sorted V-001 to V-218)
├── 02 - Adjectives with Prepositions (102 cards, sorted A-001 to A-102)
├── 03 - Nouns with Prepositions (68 cards, sorted N-001 to N-068)
└── 04 - Noun-Verb Idioms (51 cards, sorted I-001 to I-051)
```

### 📥 Direct Downloads ([v1.0.0 Release](https://github.com/yuhouzhou/german-prepositions-anki/releases/tag/v1.0.0))

| Deck Package | Content | Cards | Direct Download |
| :--- | :--- | :--- | :--- |
| **Master Suite** | **All 4 Subdecks Combined** | **439** | [⬇️ Download .apkg (408 KB)](https://github.com/yuhouzhou/german-prepositions-anki/releases/download/v1.0.0/German_Prepositions_Master_Deck.apkg) |
| **01. Verbs with Prepositions** | Verbs + Preposition + Case | 218 | [⬇️ Download .apkg (212 KB)](https://github.com/yuhouzhou/german-prepositions-anki/releases/download/v1.0.0/German_Verbs_with_Prepositions.apkg) |
| **02. Adjectives with Prepositions** | Adjectives/Adverbs + Prep + Case | 102 | [⬇️ Download .apkg (132 KB)](https://github.com/yuhouzhou/german-prepositions-anki/releases/download/v1.0.0/German_Adjectives_with_Prepositions.apkg) |
| **03. Nouns with Prepositions** | Nouns + Preposition + Case | 68 | [⬇️ Download .apkg (108 KB)](https://github.com/yuhouzhou/german-prepositions-anki/releases/download/v1.0.0/German_Nouns_with_Prepositions.apkg) |
| **04. Noun-Verb Idioms** | Nomen-Verb-Verbindungen (NVR) | 51 | [⬇️ Download .apkg (100 KB)](https://github.com/yuhouzhou/german-prepositions-anki/releases/download/v1.0.0/German_Noun_Verb_Idioms.apkg) |

---

## 🗂️ How the 4 Subdecks Work

You have complete flexibility in how you study:
- **Study All Mixed**: Click the parent deck **`German::Prepositions`** to review cards from all 4 categories interleaved.
- **Study Category-by-Category**: Click any individual subdeck to focus strictly on verbs, adjectives, nouns, or idioms.
- **Frequency Order**: Cards within each subdeck are ordered sequentially from **highest frequency to lower frequency**.

---

## 🔍 The 4 Preposition Domains in This Suite

| Category | Card Count | Primary Level | Front Prompt | Key Examples |
|---|---|---|---|---|
| **01. Verbs with Prepositions** | **218** | A1 – C1 | *What is the preposition and case?* | `warten auf + Akk.`, `bestehen aus/auf/in`, `abhängen von + Dat.` |
| **02. Adjectives & Adverbs** | **102** | A1 – B2 | *What is the preposition and case?* | `stolz auf + Akk.`, `zufrieden mit + Dat.`, `interessiert an + Dat.` |
| **03. Nouns with Prepositions** | **68** | A1 – B2 | *What is the preposition and case?* | `die Angst vor + Dat.`, `die Hoffnung auf + Akk.`, `der Zweifel an + Dat.` |
| **04. Noun-Verb Idioms (NVR)** | **51** | B1 – C1 | *What is the prepositional phrase?* | `in Frage kommen`, `zur Verfügung stehen/stellen`, `in Kauf nehmen` |

---

## 🏷️ Hierarchical Anki Tags (Exam & Focus Filtering)

Every note is annotated with hierarchical Anki tags for instant Custom Study / Filtered Decks:

- **Level Tags**: `level::A1`, `level::A2`, `level::B1`, `level::B2`, `level::C1`
  *(e.g., filter `tag:level::B1` to prep for Goethe-Zertifikat B1)*
- **Category Tags**: `category::verb`, `category::adjective`, `category::noun`, `category::idiom`
- **Preposition Tags**: `prep::auf`, `prep::an`, `prep::von`, `prep::zu`, `prep::in`, `prep::vor`, `prep::nach`, `prep::über`, etc.
  *(e.g., filter `tag:prep::auf` to master all combinations requiring "auf")*
- **Case Tags**: `case::akk`, `case::dat`, `case::gen`
  *(e.g., filter `tag:case::dat` to practice all dative prepositions)*

---

## 🎨 Card Layout & Mechanics

### Subdecks 01, 02, 03 (Verbs, Adjectives, Nouns)
- **Front Side**:
  - Target word with definite article for nouns (e.g., `warten`, `stolz`, `die Angst`).
  - English meaning to disambiguate multiple prepositions (e.g., `wütend auf` = *furious at person* vs. `wütend über` = *furious about situation*).
  - Authentic German example sentence with the preposition cloze-masked: `[ ... ]`.
  - Sentence English translation hint.
- **Back Side**:
  - Revealed combination with color-coded case pill:
    - 🔴 **Akkusativ**: Rose / Red
    - 🔵 **Dativ**: Royal Blue
    - 🟡 **Genitiv**: Amber
  - Complete German sentence with highlighted preposition.
  - **Da- / Wo- Compounds** (*Worauf? • Darauf / Auf wen?*).
  - **Contrast Box**: Displays all other prepositions belonging to the same word family.
  - Usage advice & grammar nuance notes.

### Subdeck 04 (Noun-Verb Idioms / Nomen-Verb-Verbindungen)
- **Front Side**:
  - Full expression header (e.g., `in Frage kommen`).
  - Equivalent simple verb synonym (e.g., `= möglich sein / denkbar sein`).
  - English translation (e.g., *to be possible / out of the question*).
  - Sentence cloze masking the **preposition and noun phrase**:
    ```text
    "Ein weiterer Aufschub des Projekts kommt für uns keinesfalls [ ... ]."
    What is the prepositional phrase?
    ```
- **Back Side**:
  - Revealed formula: `in Frage kommen`.
  - Complete sentence with highlighted phrase: `... keinesfalls in Frage.`
  - Contrast box with related idioms sharing the same verb.

---

## 🚀 How to Import into Anki

1. Open **Anki** on desktop (Mac / Windows / Linux) or mobile (iOS / Android).
2. Double-click [**`German_Prepositions_Master_Deck.apkg`**](file:///Users/YuhouZhou/projects/german_verb_prep/German_Prepositions_Master_Deck.apkg) *(or select **File → Import...** inside Anki)*.
3. Anki will automatically create the parent deck **`German::Prepositions`** along with all **4 numbered subdecks**.
4. In Deck Options, ensure **New card gather order: Deck / Order added** so you encounter cards from most frequent to less frequent.

---

## 📦 Generated Files Summary

| File | Description |
|---|---|
| [**`German_Prepositions_Master_Deck.apkg`**](file:///Users/YuhouZhou/projects/german_verb_prep/German_Prepositions_Master_Deck.apkg) | **Master Anki Suite** (439 cards across 4 subdecks) |
| [**`German_Verbs_with_Prepositions.apkg`**](file:///Users/YuhouZhou/projects/german_verb_prep/German_Verbs_with_Prepositions.apkg) | Verbs-only package (218 cards) |
| [**`German_Adjectives_with_Prepositions.apkg`**](file:///Users/YuhouZhou/projects/german_verb_prep/German_Adjectives_with_Prepositions.apkg) | Adjectives-only package (102 cards) |
| [**`German_Nouns_with_Prepositions.apkg`**](file:///Users/YuhouZhou/projects/german_verb_prep/German_Nouns_with_Prepositions.apkg) | Nouns-only package (68 cards) |
| [**`German_Noun_Verb_Idioms.apkg`**](file:///Users/YuhouZhou/projects/german_verb_prep/German_Noun_Verb_Idioms.apkg) | Noun-Verb Idioms package (51 cards) |
| [**`german_all_prepositions_combined.tsv`**](file:///Users/YuhouZhou/projects/german_verb_prep/german_all_prepositions_combined.tsv) | Combined TSV for all 439 cards |
| [**`german_verbs_with_prepositions.tsv`**](file:///Users/YuhouZhou/projects/german_verb_prep/german_verbs_with_prepositions.tsv) | Verbs TSV (218 rows) |
| [**`german_adjectives_with_prepositions.tsv`**](file:///Users/YuhouZhou/projects/german_verb_prep/german_adjectives_with_prepositions.tsv) | Adjectives TSV (102 rows) |
| [**`german_nouns_with_prepositions.tsv`**](file:///Users/YuhouZhou/projects/german_verb_prep/german_nouns_with_prepositions.tsv) | Nouns TSV (68 rows) |
| [**`german_noun_verb_idioms.tsv`**](file:///Users/YuhouZhou/projects/german_verb_prep/german_noun_verb_idioms.tsv) | Noun-Verb Idioms TSV (51 rows) |
| [**`german_all_prepositions_combined.json`**](file:///Users/YuhouZhou/projects/german_verb_prep/german_all_prepositions_combined.json) | Complete JSON dataset |

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](file:///Users/YuhouZhou/projects/german_verb_prep/LICENSE) file for details.
