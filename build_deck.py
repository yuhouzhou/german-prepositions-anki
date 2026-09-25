#!/usr/bin/env python3
"""
Build script for German Verbs with Prepositions Anki Deck.
Generates:
  1. German_Verbs_with_Prepositions.apkg (Anki package)
  2. german_verbs_with_prepositions.tsv (Tab-separated text file)
  3. german_verbs_with_prepositions.csv (Comma-separated text file)
  4. german_verbs_with_prepositions.json (Full JSON dump)
"""

import json
import csv
import os
from collections import defaultdict
import genanki
from verbs_data import RAW_VERB_DATA

MODEL_ID = 1748291045
DECK_ID = 2084920193

# CSS styling for modern, high-contrast, dark/light mode compatible flashcards
CARD_CSS = """
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  font-size: 16px;
  text-align: center;
  color: #1f2937;
  background-color: #f9fafb;
  margin: 0;
  padding: 16px;
}

.nightMode .card,
@media (prefers-color-scheme: dark) {
  .card {
    color: #f3f4f6;
    background-color: #111827;
  }
}

.anki-card {
  max-width: 580px;
  margin: 0 auto;
  background: #ffffff;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  border: 1px solid #e5e7eb;
  padding: 24px;
  box-sizing: border-box;
  text-align: left;
}

.nightMode .anki-card,
@media (prefers-color-scheme: dark) {
  .anki-card {
    background: #1f2937;
    border-color: #374151;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
  }
}

/* Header bar */
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding-bottom: 12px;
  border-bottom: 1px solid #f3f4f6;
}

.nightMode .card-header,
@media (prefers-color-scheme: dark) {
  .card-header {
    border-bottom-color: #374151;
  }
}

.badge {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 9999px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.03em;
}

.rank-badge {
  background: #eef2ff;
  color: #4f46e5;
  border: 1px solid #c7d2fe;
}

.nightMode .rank-badge,
@media (prefers-color-scheme: dark) {
  .rank-badge {
    background: #312e81;
    color: #c7d2fe;
    border-color: #4338ca;
  }
}

.level-badge {
  background: #ecfdf5;
  color: #059669;
  border: 1px solid #a7f3d0;
}

.nightMode .level-badge,
@media (prefers-color-scheme: dark) {
  .level-badge {
    background: #064e3b;
    color: #a7f3d0;
    border-color: #047857;
  }
}

.deck-title {
  font-size: 12px;
  font-weight: 500;
  color: #9ca3af;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* Verb & Formula */
.verb-section {
  text-align: center;
  margin: 10px 0 24px 0;
}

.verb-title {
  font-size: 32px;
  font-weight: 800;
  color: #111827;
  letter-spacing: -0.02em;
  margin-bottom: 6px;
}

.nightMode .verb-title,
@media (prefers-color-scheme: dark) {
  .verb-title {
    color: #f9fafb;
  }
}

.meaning-subtitle {
  font-size: 17px;
  font-weight: 500;
  color: #4b5563;
  margin-top: 4px;
}

.nightMode .meaning-subtitle,
@media (prefers-color-scheme: dark) {
  .meaning-subtitle {
    color: #9ca3af;
  }
}

/* Formula reveal on Back */
.formula-box {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin: 14px 0 8px 0;
  flex-wrap: wrap;
}

.verb-accent {
  font-size: 22px;
  font-weight: 700;
  color: #111827;
}

.nightMode .verb-accent,
@media (prefers-color-scheme: dark) {
  .verb-accent {
    color: #f3f4f6;
  }
}

.prep-pill {
  font-size: 20px;
  font-weight: 800;
  padding: 4px 14px;
  border-radius: 8px;
  background: #6366f1;
  color: #ffffff;
  box-shadow: 0 2px 8px rgba(99, 102, 241, 0.3);
}

.case-pill {
  font-size: 16px;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: 8px;
}

/* Case color coding */
.case-akk {
  background: #ffe4e6;
  color: #e11d48;
  border: 1px solid #fecdd3;
}
.nightMode .case-akk,
@media (prefers-color-scheme: dark) {
  .case-akk {
    background: #4c0519;
    color: #fda4af;
    border-color: #9f1239;
  }
}

.case-dat {
  background: #dbeafe;
  color: #1d4ed8;
  border: 1px solid #bfdbfe;
}
.nightMode .case-dat,
@media (prefers-color-scheme: dark) {
  .case-dat {
    background: #1e3a8a;
    color: #93c5fd;
    border-color: #1d4ed8;
  }
}

.case-gen {
  background: #fef3c7;
  color: #b45309;
  border: 1px solid #fde68a;
}
.nightMode .case-gen,
@media (prefers-color-scheme: dark) {
  .case-gen {
    background: #78350f;
    color: #fde68a;
    border-color: #b45309;
  }
}

.case-nom {
  background: #d1fae5;
  color: #047857;
  border: 1px solid #a7f3d0;
}
.nightMode .case-nom,
@media (prefers-color-scheme: dark) {
  .case-nom {
    background: #064e3b;
    color: #a7f3d0;
    border-color: #047857;
  }
}

/* Context / Sentences */
.context-box {
  background: #f8fafc;
  border-radius: 12px;
  padding: 16px 18px;
  border: 1px solid #e2e8f0;
  margin-bottom: 18px;
}

.nightMode .context-box,
@media (prefers-color-scheme: dark) {
  .context-box {
    background: #182234;
    border-color: #2e3a50;
  }
}

.context-label {
  font-size: 11px;
  font-weight: 700;
  color: #94a3b8;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 8px;
}

.sentence-cloze,
.sentence-full {
  font-size: 18px;
  line-height: 1.5;
  font-weight: 500;
  color: #0f172a;
  margin-bottom: 6px;
}

.nightMode .sentence-cloze,
.nightMode .sentence-full,
@media (prefers-color-scheme: dark) {
  .sentence-cloze,
  .sentence-full {
    color: #f8fafc;
  }
}

.blank {
  display: inline-block;
  padding: 2px 10px;
  background: #fef08a;
  color: #854d0e;
  border-radius: 6px;
  border: 1.5px dashed #ca8a04;
  font-weight: 700;
  margin: 0 4px;
}

.nightMode .blank,
@media (prefers-color-scheme: dark) {
  .blank {
    background: #422006;
    color: #fef08a;
    border-color: #a16207;
  }
}

.highlight-prep {
  font-weight: 800;
  color: #4f46e5;
  text-decoration: underline;
  text-decoration-thickness: 2.5px;
  text-underline-offset: 3px;
}

.nightMode .highlight-prep,
@media (prefers-color-scheme: dark) {
  .highlight-prep {
    color: #818cf8;
  }
}

.sentence-en,
.sentence-en-hint {
  font-size: 14px;
  color: #64748b;
  font-style: italic;
  line-height: 1.4;
}

.nightMode .sentence-en,
.nightMode .sentence-en-hint,
@media (prefers-color-scheme: dark) {
  .sentence-en,
  .sentence-en-hint {
    color: #94a3b8;
  }
}

/* Prompt */
.prompt-box {
  text-align: center;
  padding: 12px;
  background: #f3f4f6;
  border-radius: 10px;
  font-size: 14px;
  color: #4b5563;
}

.nightMode .prompt-box,
@media (prefers-color-scheme: dark) {
  .prompt-box {
    background: #374151;
    color: #d1d5db;
  }
}

/* Extra info section on Back */
.extra-info {
  margin-top: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.info-row {
  display: flex;
  flex-direction: column;
  gap: 4px;
  font-size: 13px;
  line-height: 1.4;
  padding: 10px 14px;
  background: #f8fafc;
  border-radius: 8px;
  border-left: 3px solid #6366f1;
}

.nightMode .info-row,
@media (prefers-color-scheme: dark) {
  .info-row {
    background: #1e293b;
    border-left-color: #818cf8;
  }
}

.contrast-row {
  border-left-color: #f59e0b;
}

.notes-row {
  border-left-color: #10b981;
}

.info-label {
  font-weight: 700;
  color: #475569;
}

.nightMode .info-label,
@media (prefers-color-scheme: dark) {
  .info-label {
    color: #94a3b8;
  }
}

.info-content {
  color: #1e293b;
}

.nightMode .info-content,
@media (prefers-color-scheme: dark) {
  .info-content {
    color: #e2e8f0;
  }
}

.other-preps {
  font-size: 13px;
  line-height: 1.5;
  color: #334155;
}

.nightMode .other-preps,
@media (prefers-color-scheme: dark) {
  .other-preps {
    color: #cbd5e1;
  }
}
"""

FRONT_TEMPLATE = """
<div class="anki-card">
  <div class="card-header">
    <span class="badge rank-badge">#{{Rank}}</span>
    <span class="badge level-badge">{{Level}}</span>
    <span class="deck-title">German Verbs & Prepositions</span>
  </div>

  <div class="verb-section">
    <div class="verb-title">{{Verb}}</div>
    <div class="meaning-subtitle">{{Meaning_EN}}</div>
  </div>

  <div class="context-box">
    <div class="context-label">Example Sentence:</div>
    <div class="sentence-cloze">{{Sentence_Cloze}}</div>
    <div class="sentence-en-hint">{{Sentence_EN}}</div>
  </div>

  <div class="prompt-box">
    What is the <b>preposition</b> and <b>case</b>?
  </div>
</div>
"""

BACK_TEMPLATE = """
<div class="anki-card">
  <div class="card-header">
    <span class="badge rank-badge">#{{Rank}}</span>
    <span class="badge level-badge">{{Level}}</span>
    <span class="deck-title">German Verbs & Prepositions</span>
  </div>

  <div class="verb-section">
    <div class="verb-title">{{Verb}}</div>
    <div class="formula-box">
      <span class="verb-accent">{{Verb}}</span>
      <span class="prep-pill">{{Preposition}}</span>
      <span class="case-pill case-{{Case_Type}}">{{Case}}</span>
    </div>
    <div class="meaning-subtitle">{{Meaning_EN}}</div>
  </div>

  <div class="context-box">
    <div class="context-label">Full Sentence:</div>
    <div class="sentence-full">{{Sentence_Full}}</div>
    <div class="sentence-en">{{Sentence_EN}}</div>
  </div>

  <div class="extra-info">
    {{#Question_Structure}}
    <div class="info-row">
      <span class="info-label">❓ Da- / Wo- Form (Question & Pronoun):</span>
      <span class="info-content">{{Question_Structure}}</span>
    </div>
    {{/Question_Structure}}

    {{#Other_Prepositions}}
    <div class="info-row contrast-row">
      <span class="info-label">⚠️ Different prepositions with <i>{{Verb}}</i>:</span>
      <div class="other-preps">{{Other_Prepositions}}</div>
    </div>
    {{/Other_Prepositions}}

    {{#Grammar_Notes}}
    <div class="info-row notes-row">
      <span class="info-label">💡 Usage Tip:</span>
      <span class="info-content">{{Grammar_Notes}}</span>
    </div>
    {{/Grammar_Notes}}
  </div>
</div>
"""

def create_anki_model():
    return genanki.Model(
        MODEL_ID,
        'German Verbs with Prepositions (Frequency Sorted)',
        fields=[
            {'name': 'Rank'},
            {'name': 'Verb'},
            {'name': 'Preposition'},
            {'name': 'Case'},
            {'name': 'Case_Type'},
            {'name': 'Meaning_EN'},
            {'name': 'Sentence_Cloze'},
            {'name': 'Sentence_Full'},
            {'name': 'Sentence_EN'},
            {'name': 'Question_Structure'},
            {'name': 'Other_Prepositions'},
            {'name': 'Grammar_Notes'},
            {'name': 'Level'},
        ],
        templates=[
            {
                'name': 'Recall Preposition & Case',
                'qfmt': FRONT_TEMPLATE,
                'afmt': BACK_TEMPLATE,
            },
        ],
        css=CARD_CSS,
        sort_field_index=0,  # Sort by Rank so Anki displays by frequency!
    )

def prepare_entries():
    """Process raw verb data, sort by frequency rank, and resolve related prepositions."""
    # Group items by verb_group to build contrast cross-references
    groups = defaultdict(list)
    for item in RAW_VERB_DATA:
        groups[item['verb_group']].append(item)

    # Sort entries primarily by verb_rank, then verb_group, then meaning
    sorted_raw = sorted(RAW_VERB_DATA, key=lambda x: (x['verb_rank'], x['verb_group'], x['meaning_en']))

    processed = []
    for idx, item in enumerate(sorted_raw, start=1):
        rank_str = f"{idx:03d}"
        verb = item['verb']
        prep = item['prep']
        case = item['case']
        case_type = item['case_type']
        meaning_en = item['meaning_en']
        level = item['level']
        grammar_notes = item['grammar_notes']
        question_structure = item['question_structure']

        # Format cloze and full sentences
        sentence_cloze = item['sentence_de'].replace('{PREP}', '<span class="blank">[ &hellip; ]</span>')
        sentence_full = item['sentence_de'].replace('{PREP}', f'<span class="highlight-prep">{prep}</span>')
        sentence_en = item['sentence_en']

        # Find other prepositions in the same verb_group
        other_list = []
        for sibling in groups[item['verb_group']]:
            if (sibling['verb'], sibling['prep'], sibling['case']) != (verb, prep, case):
                other_list.append(f"• <b>{sibling['verb']} + {sibling['prep']} {sibling['case']}</b>: {sibling['meaning_en']}")

        other_preps_html = "<br>".join(other_list) if other_list else ""

        processed.append({
            'rank': rank_str,
            'verb': verb,
            'prep': prep,
            'case': case,
            'case_type': case_type,
            'meaning_en': meaning_en,
            'sentence_cloze': sentence_cloze,
            'sentence_full': sentence_full,
            'sentence_en': sentence_en,
            'question_structure': question_structure,
            'other_prepositions': other_preps_html,
            'grammar_notes': grammar_notes,
            'level': level,
            'raw_sentence_de': item['sentence_de'].replace('{PREP}', prep),
            'verb_group': item['verb_group'],
            'verb_rank': item['verb_rank']
        })

    return processed

def build_anki_deck(entries):
    model = create_anki_model()
    deck = genanki.Deck(DECK_ID, 'German::Most Frequent Verbs with Prepositions')

    for e in entries:
        fields = [
            e['rank'],
            e['verb'],
            e['prep'],
            e['case'],
            e['case_type'],
            e['meaning_en'],
            e['sentence_cloze'],
            e['sentence_full'],
            e['sentence_en'],
            e['question_structure'],
            e['other_prepositions'],
            e['grammar_notes'],
            e['level']
        ]
        # Generate deterministic GUID from Rank + Verb + Prep + Case
        guid = genanki.guid_for(e['rank'], e['verb'], e['prep'], e['case'])
        note = genanki.Note(model=model, fields=fields, guid=guid)
        deck.add_note(note)

    apkg_file = 'German_Verbs_with_Prepositions.apkg'
    genanki.Package(deck).write_to_file(apkg_file)
    print(f"Generated Anki package: {apkg_file} ({len(entries)} cards)")
    return apkg_file

def export_tsv(entries, filename='german_verbs_with_prepositions.tsv'):
    headers = [
        'Rank', 'Verb', 'Preposition', 'Case', 'Case_Type', 'Meaning_EN',
        'Sentence_Cloze', 'Sentence_Full', 'Sentence_EN', 'Question_Structure',
        'Other_Prepositions', 'Grammar_Notes', 'Level'
    ]
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(headers)
        for e in entries:
            writer.writerow([
                e['rank'], e['verb'], e['prep'], e['case'], e['case_type'], e['meaning_en'],
                e['sentence_cloze'], e['sentence_full'], e['sentence_en'], e['question_structure'],
                e['other_prepositions'], e['grammar_notes'], e['level']
            ])
    print(f"Generated TSV file: {filename}")

def export_csv(entries, filename='german_verbs_with_prepositions.csv'):
    headers = [
        'Rank', 'Verb', 'Preposition', 'Case', 'Meaning_EN',
        'Example_German', 'Example_English', 'Question_Form', 'Level', 'Grammar_Notes'
    ]
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for e in entries:
            writer.writerow([
                e['rank'], e['verb'], e['prep'], e['case'], e['meaning_en'],
                e['raw_sentence_de'], e['sentence_en'], e['question_structure'],
                e['level'], e['grammar_notes']
            ])
    print(f"Generated CSV file: {filename}")

def export_json(entries, filename='german_verbs_with_prepositions.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)
    print(f"Generated JSON file: {filename}")

def main():
    entries = prepare_entries()
    build_anki_deck(entries)
    export_tsv(entries)
    export_csv(entries)
    export_json(entries)
    print(f"\nAll files successfully generated for {len(entries)} verb combinations!")

if __name__ == '__main__':
    main()
