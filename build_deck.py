#!/usr/bin/env python3
"""
Build script for German Prepositions Master Anki Suite:
  1. Verbs with Prepositions (218 cards)
  2. Adjectives with Prepositions (102 cards)
  3. Nouns with Prepositions (68 cards)
  4. Noun-Verb Idioms / Nomen-Verb-Verbindungen (51 cards)

Total: 439 Cards
Generates:
  - German_Prepositions_Master_Deck.apkg (4-subdeck Master Package)
  - Individual & combined TSV, CSV, and JSON exports.
"""

import json
import csv
import os
import re
from collections import defaultdict
import genanki

from verbs_data import RAW_VERB_DATA
from adjectives_data import RAW_ADJECTIVE_DATA
from nouns_data import RAW_NOUN_DATA
from idioms_data import RAW_IDIOM_DATA

MODEL_ID = 1748291045
MASTER_DECK_ID = 2084920190
VERBS_DECK_ID = 2084920191
ADJECTIVES_DECK_ID = 2084920192
NOUNS_DECK_ID = 2084920193
IDIOMS_DECK_ID = 2084920194

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

.header-badges {
  display: flex;
  gap: 6px;
  align-items: center;
  flex-wrap: wrap;
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

.category-badge {
  background: #fdf2f8;
  color: #db2777;
  border: 1px solid #fbcfe8;
}

.nightMode .category-badge,
@media (prefers-color-scheme: dark) {
  .category-badge {
    background: #831843;
    color: #fbcfe8;
    border-color: #9d174d;
  }
}

.deck-title {
  font-size: 12px;
  font-weight: 500;
  color: #9ca3af;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* Word & Formula */
.word-section {
  text-align: center;
  margin: 10px 0 24px 0;
}

.word-title {
  font-size: 30px;
  font-weight: 800;
  color: #111827;
  letter-spacing: -0.02em;
  margin-bottom: 6px;
}

.nightMode .word-title,
@media (prefers-color-scheme: dark) {
  .word-title {
    color: #f9fafb;
  }
}

.synonym-line {
  font-size: 14px;
  font-weight: 600;
  color: #059669;
  margin-bottom: 4px;
}

.nightMode .synonym-line,
@media (prefers-color-scheme: dark) {
  .synonym-line {
    color: #34d399;
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

.word-accent {
  font-size: 22px;
  font-weight: 700;
  color: #111827;
}

.nightMode .word-accent,
@media (prefers-color-scheme: dark) {
  .word-accent {
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
    <div class="header-badges">
      <span class="badge rank-badge">#{{Rank}}</span>
      <span class="badge level-badge">{{Level}}</span>
      <span class="badge category-badge">{{Category}}</span>
    </div>
    <span class="deck-title">German Prepositions</span>
  </div>

  <div class="word-section">
    <div class="word-title">{{Word}}</div>
    {{#Synonym}}
    <div class="synonym-line">= {{Synonym}}</div>
    {{/Synonym}}
    <div class="meaning-subtitle">{{Meaning_EN}}</div>
  </div>

  <div class="context-box">
    <div class="context-label">Example Sentence:</div>
    <div class="sentence-cloze">{{Sentence_Cloze}}</div>
    <div class="sentence-en-hint">{{Sentence_EN}}</div>
  </div>

  <div class="prompt-box">
    {{Prompt_Text}}
  </div>
</div>
"""

BACK_TEMPLATE = """
<div class="anki-card">
  <div class="card-header">
    <div class="header-badges">
      <span class="badge rank-badge">#{{Rank}}</span>
      <span class="badge level-badge">{{Level}}</span>
      <span class="badge category-badge">{{Category}}</span>
    </div>
    <span class="deck-title">German Prepositions</span>
  </div>

  <div class="word-section">
    <div class="word-title">{{Word}}</div>
    {{#Synonym}}
    <div class="synonym-line">= {{Synonym}}</div>
    {{/Synonym}}
    <div class="formula-box">
      <span class="word-accent">{{Word}}</span>
      <span class="prep-pill">{{Preposition}}</span>
      {{#Case}}
      <span class="case-pill case-{{Case_Type}}">{{Case}}</span>
      {{/Case}}
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
      <span class="info-label">⚠️ Different prepositions with <i>{{Word}}</i>:</span>
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
        'German Preposition Suite (Hierarchical & Frequency Sorted)',
        fields=[
            {'name': 'Rank'},
            {'name': 'Category'},
            {'name': 'Word'},
            {'name': 'Synonym'},
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
            {'name': 'Prompt_Text'},
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
        sort_field_index=0,  # Sort by Rank field
    )

def prepare_verb_entries():
    groups = defaultdict(list)
    for item in RAW_VERB_DATA:
        groups[item['verb_group']].append(item)

    sorted_raw = sorted(RAW_VERB_DATA, key=lambda x: (x['verb_rank'], x['verb_group'], x['meaning_en']))

    processed = []
    for idx, item in enumerate(sorted_raw, start=1):
        rank_str = f"V-{idx:03d}"
        verb = item['verb']
        prep = item['prep']
        case = item['case']
        case_type = item['case_type']
        meaning_en = item['meaning_en']
        level = item['level']
        grammar_notes = item['grammar_notes']
        question_structure = item['question_structure']

        sentence_cloze = item['sentence_de'].replace('{PREP}', '<span class="blank">[ &hellip; ]</span>')
        sentence_full = item['sentence_de'].replace('{PREP}', f'<span class="highlight-prep">{prep}</span>')
        sentence_en = item['sentence_en']

        other_list = []
        for sibling in groups[item['verb_group']]:
            if (sibling['verb'], sibling['prep'], sibling['case']) != (verb, prep, case):
                other_list.append(f"• <b>{sibling['verb']} + {sibling['prep']} {sibling['case']}</b>: {sibling['meaning_en']}")

        other_preps_html = "<br>".join(other_list) if other_list else ""
        tags = [
            f"level::{level}",
            "category::verb",
            f"prep::{prep.lower()}",
            f"case::{case_type}"
        ]

        processed.append({
            'rank': rank_str,
            'category': 'Verb',
            'word': verb,
            'synonym': '',
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
            'prompt_text': 'What is the <b>preposition</b> and <b>case</b>?',
            'level': level,
            'tags': tags,
            'raw_sentence_de': item['sentence_de'].replace('{PREP}', prep),
            'group': item['verb_group'],
            'freq_rank': item['verb_rank']
        })

    return processed

def prepare_adjective_entries():
    groups = defaultdict(list)
    for item in RAW_ADJECTIVE_DATA:
        groups[item['adj_group']].append(item)

    sorted_raw = sorted(RAW_ADJECTIVE_DATA, key=lambda x: (x['adj_rank'], x['adj_group'], x['meaning_en']))

    processed = []
    for idx, item in enumerate(sorted_raw, start=1):
        rank_str = f"A-{idx:03d}"
        adjective = item['adjective']
        prep = item['prep']
        case = item['case']
        case_type = item['case_type']
        meaning_en = item['meaning_en']
        level = item['level']
        grammar_notes = item['grammar_notes']
        question_structure = item['question_structure']

        sentence_cloze = item['sentence_de'].replace('{PREP}', '<span class="blank">[ &hellip; ]</span>')
        sentence_full = item['sentence_de'].replace('{PREP}', f'<span class="highlight-prep">{prep}</span>')
        sentence_en = item['sentence_en']

        other_list = []
        for sibling in groups[item['adj_group']]:
            if (sibling['adjective'], sibling['prep'], sibling['case']) != (adjective, prep, case):
                other_list.append(f"• <b>{sibling['adjective']} + {sibling['prep']} {sibling['case']}</b>: {sibling['meaning_en']}")

        other_preps_html = "<br>".join(other_list) if other_list else ""
        tags = [
            f"level::{level}",
            "category::adjective",
            f"prep::{prep.lower()}",
            f"case::{case_type}"
        ]

        processed.append({
            'rank': rank_str,
            'category': 'Adjective',
            'word': adjective,
            'synonym': '',
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
            'prompt_text': 'What is the <b>preposition</b> and <b>case</b>?',
            'level': level,
            'tags': tags,
            'raw_sentence_de': item['sentence_de'].replace('{PREP}', prep),
            'group': item['adj_group'],
            'freq_rank': item['adj_rank']
        })

    return processed

def prepare_noun_entries():
    groups = defaultdict(list)
    for item in RAW_NOUN_DATA:
        groups[item['noun_group']].append(item)

    sorted_raw = sorted(RAW_NOUN_DATA, key=lambda x: (x['noun_rank'], x['noun_group'], x['meaning_en']))

    processed = []
    for idx, item in enumerate(sorted_raw, start=1):
        rank_str = f"N-{idx:03d}"
        noun = item['noun']
        prep = item['prep']
        case = item['case']
        case_type = item['case_type']
        meaning_en = item['meaning_en']
        level = item['level']
        grammar_notes = item['grammar_notes']
        question_structure = item['question_structure']

        sentence_cloze = item['sentence_de'].replace('{PREP}', '<span class="blank">[ &hellip; ]</span>')
        sentence_full = item['sentence_de'].replace('{PREP}', f'<span class="highlight-prep">{prep}</span>')
        sentence_en = item['sentence_en']

        other_list = []
        for sibling in groups[item['noun_group']]:
            if (sibling['noun'], sibling['prep'], sibling['case']) != (noun, prep, case):
                other_list.append(f"• <b>{sibling['noun']} + {sibling['prep']} {sibling['case']}</b>: {sibling['meaning_en']}")

        other_preps_html = "<br>".join(other_list) if other_list else ""
        tags = [
            f"level::{level}",
            "category::noun",
            f"prep::{prep.lower()}",
            f"case::{case_type}"
        ]

        processed.append({
            'rank': rank_str,
            'category': 'Noun',
            'word': noun,
            'synonym': '',
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
            'prompt_text': 'What is the <b>preposition</b> and <b>case</b>?',
            'level': level,
            'tags': tags,
            'raw_sentence_de': item['sentence_de'].replace('{PREP}', prep),
            'group': item['noun_group'],
            'freq_rank': item['noun_rank']
        })

    return processed

def prepare_idiom_entries():
    groups = defaultdict(list)
    for item in RAW_IDIOM_DATA:
        groups[item['idiom_group']].append(item)

    sorted_raw = sorted(RAW_IDIOM_DATA, key=lambda x: (x['idiom_rank'], x['idiom_group'], x['meaning_en']))

    processed = []
    for idx, item in enumerate(sorted_raw, start=1):
        rank_str = f"I-{idx:03d}"
        idiom = item['idiom']
        phrase_cloze = item['phrase_cloze']
        prep = item['prep']
        case = item['case']
        case_type = item['case_type']
        simple_verb = item['simple_verb']
        meaning_en = item['meaning_en']
        level = item['level']
        grammar_notes = item['grammar_notes']

        # Blank out the preposition and noun phrase
        sentence_cloze = item['sentence_de'].replace('{PHRASE}', '<span class="blank">[ &hellip; ]</span>')
        sentence_full = item['sentence_de'].replace('{PHRASE}', f'<span class="highlight-prep">{phrase_cloze}</span>')
        sentence_en = item['sentence_en']

        other_list = []
        for sibling in groups[item['idiom_group']]:
            if sibling['idiom'] != idiom:
                other_list.append(f"• <b>{sibling['idiom']}</b> (= {sibling['simple_verb']}): {sibling['meaning_en']}")

        other_preps_html = "<br>".join(other_list) if other_list else ""
        tags = [
            f"level::{level}",
            "category::idiom",
            f"prep::{prep.lower()}",
            f"case::{case_type}"
        ]

        processed.append({
            'rank': rank_str,
            'category': 'Noun-Verb Idiom',
            'word': idiom,
            'synonym': simple_verb,
            'prep': phrase_cloze,
            'case': case,
            'case_type': case_type,
            'meaning_en': meaning_en,
            'sentence_cloze': sentence_cloze,
            'sentence_full': sentence_full,
            'sentence_en': sentence_en,
            'question_structure': '',
            'other_prepositions': other_preps_html,
            'grammar_notes': grammar_notes,
            'prompt_text': 'What is the <b>prepositional phrase</b>?',
            'level': level,
            'tags': tags,
            'raw_sentence_de': item['sentence_de'].replace('{PHRASE}', phrase_cloze),
            'group': item['idiom_group'],
            'freq_rank': item['idiom_rank']
        })

    return processed

def build_master_anki_deck(verb_entries, adj_entries, noun_entries, idiom_entries):
    model = create_anki_model()

    # 4-subdeck hierarchical structure
    verbs_deck = genanki.Deck(VERBS_DECK_ID, 'German::Prepositions::01 - Verbs with Prepositions')
    adj_deck = genanki.Deck(ADJECTIVES_DECK_ID, 'German::Prepositions::02 - Adjectives with Prepositions')
    nouns_deck = genanki.Deck(NOUNS_DECK_ID, 'German::Prepositions::03 - Nouns with Prepositions')
    idioms_deck = genanki.Deck(IDIOMS_DECK_ID, 'German::Prepositions::04 - Noun-Verb Idioms')

    def add_notes(deck, entries):
        for e in entries:
            fields = [
                e['rank'], e['category'], e['word'], e['synonym'], e['prep'],
                e['case'], e['case_type'], e['meaning_en'], e['sentence_cloze'],
                e['sentence_full'], e['sentence_en'], e['question_structure'],
                e['other_prepositions'], e['grammar_notes'], e['prompt_text'], e['level']
            ]
            guid = genanki.guid_for(e['rank'], e['word'], e['prep'], e['case'])
            note = genanki.Note(model=model, fields=fields, tags=e['tags'], guid=guid)
            deck.add_note(note)

    add_notes(verbs_deck, verb_entries)
    add_notes(adj_deck, adj_entries)
    add_notes(nouns_deck, noun_entries)
    add_notes(idioms_deck, idiom_entries)

    master_package = genanki.Package([verbs_deck, adj_deck, nouns_deck, idioms_deck])
    apkg_file = 'German_Prepositions_Master_Deck.apkg'
    master_package.write_to_file(apkg_file)

    # Legacy verbs-only package kept for convenience
    genanki.Package(verbs_deck).write_to_file('German_Verbs_with_Prepositions.apkg')

    total_count = len(verb_entries) + len(adj_entries) + len(noun_entries) + len(idiom_entries)
    print(f"Generated Master Deck: {apkg_file} ({total_count} cards across 4 subdecks)")
    return apkg_file

def export_all_tsv(verb_entries, adj_entries, noun_entries, idiom_entries):
    headers = [
        'Rank', 'Category', 'Word', 'Synonym', 'Preposition', 'Case', 'Case_Type', 'Meaning_EN',
        'Sentence_Cloze', 'Sentence_Full', 'Sentence_EN', 'Question_Structure',
        'Other_Prepositions', 'Grammar_Notes', 'Prompt_Text', 'Level', 'Tags'
    ]

    def write_tsv(filename, entries):
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerow(headers)
            for e in entries:
                writer.writerow([
                    e['rank'], e['category'], e['word'], e['synonym'], e['prep'],
                    e['case'], e['case_type'], e['meaning_en'], e['sentence_cloze'],
                    e['sentence_full'], e['sentence_en'], e['question_structure'],
                    e['other_prepositions'], e['grammar_notes'], e['prompt_text'], e['level'],
                    " ".join(e['tags'])
                ])
        print(f"Generated TSV: {filename}")

    write_tsv('german_verbs_with_prepositions.tsv', verb_entries)
    write_tsv('german_adjectives_with_prepositions.tsv', adj_entries)
    write_tsv('german_nouns_with_prepositions.tsv', noun_entries)
    write_tsv('german_noun_verb_idioms.tsv', idiom_entries)
    write_tsv('german_all_prepositions_combined.tsv', verb_entries + adj_entries + noun_entries + idiom_entries)

def export_all_csv(verb_entries, adj_entries, noun_entries, idiom_entries):
    headers = [
        'Rank', 'Category', 'Word', 'Synonym', 'Preposition', 'Case', 'Meaning_EN',
        'Example_German', 'Example_English', 'Level', 'Grammar_Notes', 'Tags'
    ]

    def write_csv(filename, entries):
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            for e in entries:
                writer.writerow([
                    e['rank'], e['category'], e['word'], e['synonym'], e['prep'],
                    e['case'], e['meaning_en'], e['raw_sentence_de'], e['sentence_en'],
                    e['level'], e['grammar_notes'], " ".join(e['tags'])
                ])
        print(f"Generated CSV: {filename}")

    write_csv('german_verbs_with_prepositions.csv', verb_entries)
    write_csv('german_adjectives_with_prepositions.csv', adj_entries)
    write_csv('german_nouns_with_prepositions.csv', noun_entries)
    write_csv('german_noun_verb_idioms.csv', idiom_entries)
    write_csv('german_all_prepositions_combined.csv', verb_entries + adj_entries + noun_entries + idiom_entries)

def export_all_json(verb_entries, adj_entries, noun_entries, idiom_entries):
    with open('german_verbs_with_prepositions.json', 'w', encoding='utf-8') as f:
        json.dump(verb_entries, f, indent=2, ensure_ascii=False)
    with open('german_adjectives_with_prepositions.json', 'w', encoding='utf-8') as f:
        json.dump(adj_entries, f, indent=2, ensure_ascii=False)
    with open('german_nouns_with_prepositions.json', 'w', encoding='utf-8') as f:
        json.dump(noun_entries, f, indent=2, ensure_ascii=False)
    with open('german_noun_verb_idioms.json', 'w', encoding='utf-8') as f:
        json.dump(idiom_entries, f, indent=2, ensure_ascii=False)
    with open('german_all_prepositions_combined.json', 'w', encoding='utf-8') as f:
        json.dump(verb_entries + adj_entries + noun_entries + idiom_entries, f, indent=2, ensure_ascii=False)
    print("Generated all JSON files.")

def main():
    verb_entries = prepare_verb_entries()
    adj_entries = prepare_adjective_entries()
    noun_entries = prepare_noun_entries()
    idiom_entries = prepare_idiom_entries()

    build_master_anki_deck(verb_entries, adj_entries, noun_entries, idiom_entries)
    export_all_tsv(verb_entries, adj_entries, noun_entries, idiom_entries)
    export_all_csv(verb_entries, adj_entries, noun_entries, idiom_entries)
    export_all_json(verb_entries, adj_entries, noun_entries, idiom_entries)

    total = len(verb_entries) + len(adj_entries) + len(noun_entries) + len(idiom_entries)
    print(f"\nSuccessfully built entire suite: {len(verb_entries)} verbs + {len(adj_entries)} adjectives + {len(noun_entries)} nouns + {len(idiom_entries)} idioms = {total} cards!")

if __name__ == '__main__':
    main()
