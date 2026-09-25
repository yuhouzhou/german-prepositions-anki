# German Verbs with Prepositions (Verben mit Präpositionen) 🇩🇪

An optimized, frequency-sorted Anki flashcard deck and dataset covering **218 essential German verb-preposition combinations** across CEFR levels **A1 to C1**.

---

## 🎯 Key Deck Features

1. **Organized by Verb Frequency**:
   - Cards are sorted from the **most frequent German verbs to less frequent ones** based on corpus frequency lists (DeReKo, DWDS, Goethe-Institut).
   - High-frequency verbs (e.g., *kommen*, *gehen*, *denken*, *halten*, *sprechen*, *warten*) appear first so you gain maximum conversational leverage early.
   - Cards with the same root verb appear sequentially so you can contrast their different prepositions and meanings back-to-back.

2. **Preposition Covered (Cloze Recall)**:
   - **Front Side**: Shows the German verb, the specific English translation (disambiguating the meaning), and an authentic example sentence with the preposition covered:
     ```
     [ ? ]
     ```
   - Tests active recall: you must remember **both the preposition and its required grammatical case** (Akkusativ, Dativ, or Genitiv).

3. **Multiple Cards for Verbs with Multiple Prepositions**:
   - Verbs that take different prepositions for different meanings have dedicated cards for each combination.
   - *Examples*:
     - `sich freuen auf + Akk.` (*to look forward to [future]*) vs. `sich freuen über + Akk.` (*to be pleased about [present/past]*)
     - `bestehen aus + Dat.` (*to consist of*) vs. `bestehen auf + Dat.` (*to insist on*) vs. `bestehen in + Dat.` (*to lie/consist in*)
     - `denken an + Akk.` (*to think of / remember*) vs. `denken über + Akk.` (*to have an opinion about*)
     - `leiden an + Dat.` (*to suffer from an illness*) vs. `leiden unter + Dat.` (*to suffer under conditions/stress*)
     - `handeln von + Dat.` (*to be about a story/plot*) vs. `sich handeln um + Akk.` (*to be a matter of*) vs. `handeln mit + Dat.` (*to trade in*)

4. **Contrast Box on Card Back**:
   - Whenever a verb has multiple preposition combinations, the back side automatically displays a cross-reference box listing all the other prepositions and meanings for that verb.

5. **Color-Coded Grammatical Cases**:
   - 🔴 **Akkusativ (+ Akk.)**: Soft rose/red badge
   - 🔵 **Dativ (+ Dat.)**: Royal blue badge
   - 🟡 **Genitiv (+ Gen.)**: Amber/gold badge
   - 🟢 **Nominativ (+ Nom.)**: Emerald green badge

6. **Pronominal Adverbs (Da- / Wo- Compounds)**:
   - Every card includes the interrogative and demonstrative compounds (e.g., *Worauf? • Darauf / Auf wen?*), which are heavily tested in B1/B2/C1 exams.

7. **Modern Dark & Light Mode Styling**:
   - High-contrast, clean typography, responsive on mobile (AnkiMobile, AnkiDroid) and desktop.

---

## 🗂️ Deck Structure & Preview

### Front Card
```
+-------------------------------------------------------------+
| #031           A1              GERMAN VERBS & PREPOSITIONS  |
+-------------------------------------------------------------+
|                                                             |
|                          warten                             |
|                       to wait for                           |
|                                                             |
|  Example Sentence:                                          |
|  "Wir warten schon seit einer halben Stunde [ ... ] den     |
|   verspäteten Zug."                                         |
|  (We have been waiting for the delayed train for half an    |
|   hour.)                                                    |
|                                                             |
|          What is the PREPOSITION and CASE?                  |
+-------------------------------------------------------------+
```

### Back Card
```
+-------------------------------------------------------------+
| #031           A1              GERMAN VERBS & PREPOSITIONS  |
+-------------------------------------------------------------+
|                                                             |
|                          warten                             |
|                 [ auf ]   [ + Akk. ]                        |
|                       to wait for                           |
|                                                             |
|  Full Sentence:                                             |
|  "Wir warten schon seit einer halben Stunde auf den         |
|   verspäteten Zug."                                         |
|  We have been waiting for the delayed train for half an     |
|  hour.                                                      |
|                                                             |
|  ❓ Da- / Wo- Form:                                         |
|     Worauf? • Darauf / Auf wen?                             |
|                                                             |
|  ⚠️ Different prepositions with warten:                     |
|     • warten mit + Dat.: to hold off on / to delay doing    |
|                                                             |
|  💡 Usage Tip:                                              |
|     Preposition 'auf' always takes Akkusativ here.          |
|     Never use 'für'!                                        |
+-------------------------------------------------------------+
```

---

## 🚀 How to Import into Anki

### Option 1: Direct 1-Click Import (`.apkg`) — Recommended

1. Open **Anki** on your computer (Mac / Windows / Linux) or mobile device (iOS / Android).
2. Double-click the file:
   [German_Verbs_with_Prepositions.apkg](file:///Users/YuhouZhou/projects/german_verb_prep/German_Verbs_with_Prepositions.apkg)
   *(Or in Anki: Click `File` -> `Import...` -> Select `German_Verbs_with_Prepositions.apkg`)*.
3. The deck will be imported as **`German::Most Frequent Verbs with Prepositions`**.
4. **Study Order**:
   - By default, Anki introduces new cards in the order they were added. Since cards are added in order of verb frequency (Rank `001` through `218`), you will automatically learn the highest-frequency verbs first!
   - In Anki Deck Options, verify: **New card gather order: Deck** (or **Order added**).

### Option 2: Spreadsheet / TSV Import (`.tsv` / `.csv`)

If you want to view the raw data in Excel / Google Sheets or customize card fields:
- Tab-Separated File: [german_verbs_with_prepositions.tsv](file:///Users/YuhouZhou/projects/german_verb_prep/german_verbs_with_prepositions.tsv)
- Comma-Separated File: [german_verbs_with_prepositions.csv](file:///Users/YuhouZhou/projects/german_verb_prep/german_verbs_with_prepositions.csv)
- Raw JSON: [german_verbs_with_prepositions.json](file:///Users/YuhouZhou/projects/german_verb_prep/german_verbs_with_prepositions.json)

---

## 🛠️ Modifying & Rebuilding the Deck

The deck is fully automated. If you want to add new verbs, adjust example sentences, or modify the card templates:

1. **Edit Verb Data**:
   Open [verbs_data.py](file:///Users/YuhouZhou/projects/german_verb_prep/verbs_data.py) and add or update entries in `RAW_VERB_DATA`.

2. **Re-generate Deck & Export Files**:
   Run the build script from the project root:
   ```bash
   python3 build_deck.py
   ```
   This will automatically recalculate cross-references, apply styling, update all export files (`.apkg`, `.tsv`, `.csv`, `.json`), and output the updated package.

---

## 📊 Summary of Included Verb Categories

| CEFR Level | Card Count | Key Examples |
|---|---|---|
| **A1** | 22 | *warten auf, denken an, sprechen mit, freuen auf/über, einladen zu, danken für, antworten auf* |
| **A2** | 64 | *abhängen von, ankommen auf, sich ärgern über, sich interessieren für, sich kümmern um, suchen nach* |
| **B1** | 86 | *bestehen aus/auf, zweifeln an, leiden an/unter, sich verlassen auf, beitragen zu, überzeugen von* |
| **B2** | 42 | *anknüpfen an, sich auseinandersetzen mit, beharren auf, beruhen auf, verstoßen gegen, zurückschrecken vor* |
| **C1** | 4 | *wetteifern um, feilschen um* |
| **Total** | **218** | Full spectrum of standard Goethe / telc exam verb-preposition requirements |
