"""
Curated database of the most frequent German verbs and their prepositions.
Organized by verb frequency rank (1 = highest frequency in German corpora).

Every entry includes:
- verb_group: Root lemma for grouping alternate prepositions
- verb: Form of the verb (including reflexivity or prefix)
- prep: The required preposition
- case: "+ Akk.", "+ Dat.", "+ Gen.", "+ Nom."
- case_type: "akk", "dat", "gen", "nom" (for CSS badge styling)
- meaning_en: Meaning of this specific verb + preposition combination
- sentence_de: German sentence with {PREP} placeholder
- sentence_en: English translation of sentence
- question_structure: Da-/Wo- compound for things and prepositional question for people
- level: CEFR level (A1, A2, B1, B2)
- grammar_notes: Practical usage advice, nuances, contrasts
- verb_rank: Corpus frequency rank of the base verb
"""

RAW_VERB_DATA = [
    # ==========================================
    # RANK 1: kommen / ankommen
    # ==========================================
    {
        "verb_group": "kommen",
        "verb": "ankommen",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to depend on / to be a matter of",
        "sentence_de": "Es kommt {PREP} das Wetter an, ob wir grillen.",
        "sentence_en": "It depends on the weather whether we have a barbecue.",
        "question_structure": "Worauf? • Darauf",
        "level": "A2",
        "grammar_notes": "Impersonal expression 'es kommt an auf...'. Synonymous with 'abhängen von'.",
        "verb_rank": 1,
    },
    {
        "verb_group": "kommen",
        "verb": "kommen",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to think of / to hit upon (an idea or solution)",
        "sentence_de": "Wie bist du denn {PREP} diese geniale Idee gekommen?",
        "sentence_en": "How did you come up with this brilliant idea?",
        "question_structure": "Worauf? • Darauf",
        "level": "B1",
        "grammar_notes": "Idiomatic for suddenly getting an idea or remembering something.",
        "verb_rank": 1,
    },
    {
        "verb_group": "kommen",
        "verb": "kommen",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to arrive at (a conclusion) / to come to",
        "sentence_de": "Nach langer Diskussion kamen wir {PREP} einem Entschluss.",
        "sentence_en": "After a long discussion we came to a decision.",
        "question_structure": "Wozu? • Dazu",
        "level": "B1",
        "grammar_notes": "Often used with abstract nouns: zum Schluss kommen, zur Ruhe kommen.",
        "verb_rank": 1,
    },

    # ==========================================
    # RANK 2: gehen
    # ==========================================
    {
        "verb_group": "gehen",
        "verb": "gehen",
        "prep": "um",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to be about / to concern",
        "sentence_de": "In diesem Film geht es {PREP} eine mutige Detektivin.",
        "sentence_en": "This movie is about a courageous detective.",
        "question_structure": "Worum? • Darum",
        "level": "A2",
        "grammar_notes": "Impersonal phrase: 'Es geht um + Akk.' Crucial for summarizing texts or plots.",
        "verb_rank": 2,
    },
    {
        "verb_group": "gehen",
        "verb": "ausgehen",
        "prep": "von",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to assume / to start from (a premise)",
        "sentence_de": "Wir gehen {PREP} einem erfolgreichen Abschluss aus.",
        "sentence_en": "We assume a successful conclusion.",
        "question_structure": "Wovon? • Davon",
        "level": "B1",
        "grammar_notes": "Very common in academic and formal German for stating assumptions.",
        "verb_rank": 2,
    },

    # ==========================================
    # RANK 3: stehen
    # ==========================================
    {
        "verb_group": "stehen",
        "verb": "stehen",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to have an opinion on / to stand by",
        "sentence_de": "Wie stehst du {PREP} dem neuen Vorschlag?",
        "sentence_en": "What is your stance on the new proposal?",
        "question_structure": "Wozu? • Dazu / Zu wem?",
        "level": "B1",
        "grammar_notes": "Expresses someone's attitude or commitment toward a topic or person.",
        "verb_rank": 3,
    },
    {
        "verb_group": "stehen",
        "verb": "entstehen",
        "prep": "aus",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to arise from / to develop out of",
        "sentence_de": "Aus einem kleinen Missverständnis entstand {PREP} der Streit.",
        "sentence_en": "From a small misunderstanding arose the dispute.",
        "question_structure": "Woraus? • Daraus",
        "level": "B2",
        "grammar_notes": "Indicates the source or root cause of a development.",
        "verb_rank": 3,
    },

    # ==========================================
    # RANK 4: sehen
    # ==========================================
    {
        "verb_group": "sehen",
        "verb": "ansehen",
        "prep": "als",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to regard as / to consider as",
        "sentence_de": "Er sieht sie {PREP} seine beste Ratgeberin an.",
        "sentence_en": "He regards her as his best advisor.",
        "question_structure": "Als was? • Als solche(n)",
        "level": "B1",
        "grammar_notes": "'Als' takes the same case as the object ('sie' = Akk -> 'seine beste Ratgeberin' = Akk).",
        "verb_rank": 4,
    },
    {
        "verb_group": "sehen",
        "verb": "absehen",
        "prep": "von",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to refrain from / to disregard",
        "sentence_de": "Die Polizei sah diesmal {PREP} einer Geldstrafe ab.",
        "sentence_en": "The police refrained from a fine this time.",
        "question_structure": "Wovon? • Davon",
        "level": "B2",
        "grammar_notes": "Often used in the fixed idiom 'abgesehen von + Dat' (apart from / aside from).",
        "verb_rank": 4,
    },

    # ==========================================
    # RANK 5: lassen
    # ==========================================
    {
        "verb_group": "lassen",
        "verb": "sich einlassen",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to get involved in / to agree to (a venture or risk)",
        "sentence_de": "Er wollte sich nicht {PREP} dieses riskante Geschäft einlassen.",
        "sentence_en": "He did not want to get involved in this risky business.",
        "question_structure": "Worauf? • Darauf",
        "level": "B2",
        "grammar_notes": "Reflexive verb (sich einlassen). Implies willingness to engage in something uncertain.",
        "verb_rank": 5,
    },

    # ==========================================
    # RANK 6: denken
    # ==========================================
    {
        "verb_group": "denken",
        "verb": "denken",
        "prep": "an",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to think of / to remember",
        "sentence_de": "Ich muss jeden Tag {PREP} dich denken.",
        "sentence_en": "I have to think of you every single day.",
        "question_structure": "Woran? • Daran / An wen?",
        "level": "A1",
        "grammar_notes": "Refers to having someone/something in mind, or remembering to do something.",
        "verb_rank": 6,
    },
    {
        "verb_group": "denken",
        "verb": "denken",
        "prep": "über",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to have an opinion about / to reflect on",
        "sentence_de": "Was denkst du eigentlich {PREP} seinen Vorschlag?",
        "sentence_en": "What do you actually think about his proposal?",
        "question_structure": "Worüber? • Darüber",
        "level": "A2",
        "grammar_notes": "Expresses an opinion or judgment (synonymous with 'meinen zu').",
        "verb_rank": 6,
    },
    {
        "verb_group": "denken",
        "verb": "nachdenken",
        "prep": "über",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to ponder / to reflect on in depth",
        "sentence_de": "Ich muss in Ruhe {PREP} dieses Angebot nachdenken.",
        "sentence_en": "I need to reflect on this offer in peace.",
        "question_structure": "Worüber? • Darüber",
        "level": "A2",
        "grammar_notes": "Separable verb: implies deeper, continuous contemplation than 'denken an'.",
        "verb_rank": 6,
    },

    # ==========================================
    # RANK 7: nehmen
    # ==========================================
    {
        "verb_group": "nehmen",
        "verb": "teilnehmen",
        "prep": "an",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to participate in / to take part in",
        "sentence_de": "Viele Studenten nehmen {PREP} dem Sprachkurs teil.",
        "sentence_en": "Many students take part in the language course.",
        "question_structure": "Woran? • Daran / An wem?",
        "level": "A2",
        "grammar_notes": "Separable verb (teil|nehmen). Always takes 'an + Dativ'.",
        "verb_rank": 7,
    },
    {
        "verb_group": "nehmen",
        "verb": "zunehmen",
        "prep": "an",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to increase in / to gain in",
        "sentence_de": "Der Sturm nimmt stetig {PREP} Stärke zu.",
        "sentence_en": "The storm is steadily increasing in strength.",
        "question_structure": "Woran? • Daran",
        "level": "B2",
        "grammar_notes": "Used with abstract qualities: an Bedeutung zunehmen (gain importance).",
        "verb_rank": 7,
    },
    {
        "verb_group": "nehmen",
        "verb": "abnehmen",
        "prep": "an",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to decrease in / to lose (quality/measure)",
        "sentence_de": "Die Begeisterung nimmt leider {PREP} Intensität ab.",
        "sentence_en": "The enthusiasm is unfortunately decreasing in intensity.",
        "question_structure": "Woran? • Daran",
        "level": "B2",
        "grammar_notes": "Opposite of 'zunehmen an'. Takes Dativ.",
        "verb_rank": 7,
    },

    # ==========================================
    # RANK 8: glauben
    # ==========================================
    {
        "verb_group": "glauben",
        "verb": "glauben",
        "prep": "an",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to believe in",
        "sentence_de": "Sie glaubt fest {PREP} das Gute im Menschen.",
        "sentence_en": "She firmly believes in the good in people.",
        "question_structure": "Woran? • Daran / An wen?",
        "level": "A2",
        "grammar_notes": "Note: 'jemandem (Dat) glauben' means to believe someone's words; 'an + Akk glauben' means to have faith in.",
        "verb_rank": 8,
    },

    # ==========================================
    # RANK 9: halten
    # ==========================================
    {
        "verb_group": "halten",
        "verb": "halten",
        "prep": "von",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to think of / to have an opinion of",
        "sentence_de": "Was hältst du {PREP} meinem neuen Haarschnitt?",
        "sentence_en": "What do you think of my new haircut?",
        "question_structure": "Wovon? • Davon / Von wem?",
        "level": "A2",
        "grammar_notes": "Standard conversational formula: 'Was hältst du von...?'",
        "verb_rank": 9,
    },
    {
        "verb_group": "halten",
        "verb": "halten",
        "prep": "für",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to consider to be / to deem to be",
        "sentence_de": "Ich halte diesen Plan {PREP} eine ausgezeichnete Idee.",
        "sentence_en": "I consider this plan an excellent idea.",
        "question_structure": "Wofür? • Dafür / Für wen?",
        "level": "B1",
        "grammar_notes": "Takes Akkusativ for both the direct object and the prepositional phrase.",
        "verb_rank": 9,
    },
    {
        "verb_group": "halten",
        "verb": "sich halten",
        "prep": "an",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to abide by / to adhere to (rules, agreements)",
        "sentence_de": "Alle Autofahrer müssen sich {PREP} das Tempolimit halten.",
        "sentence_en": "All drivers must adhere to the speed limit.",
        "question_structure": "Woran? • Daran / An wen?",
        "level": "B1",
        "grammar_notes": "Reflexive verb (sich halten). Meaning: sticking strictly to a guideline.",
        "verb_rank": 9,
    },

    # ==========================================
    # RANK 10: bringen
    # ==========================================
    {
        "verb_group": "bringen",
        "verb": "bringen",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to lead someone to / to prompt someone to",
        "sentence_de": "Was hat dich {PREP} dieser schweren Entscheidung gebracht?",
        "sentence_en": "What prompted you to make this difficult decision?",
        "question_structure": "Wozu? • Dazu",
        "level": "B1",
        "grammar_notes": "Often used with a direct object: jemanden zu etwas bringen.",
        "verb_rank": 10,
    },
    {
        "verb_group": "bringen",
        "verb": "bringen",
        "prep": "um",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to deprive of / to rob someone of",
        "sentence_de": "Der ständige Lärm bringt mich {PREP} den Schlaf.",
        "sentence_en": "The constant noise robs me of my sleep.",
        "question_structure": "Worum? • Darum",
        "level": "B2",
        "grammar_notes": "Idiom: 'jemanden um den Verstand / Schlaf bringen'.",
        "verb_rank": 10,
    },

    # ==========================================
    # RANK 11: führen
    # ==========================================
    {
        "verb_group": "führen",
        "verb": "führen",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to lead to / to result in",
        "sentence_de": "Harte Arbeit führt oft {PREP} großem Erfolg.",
        "sentence_en": "Hard work often leads to great success.",
        "question_structure": "Wozu? • Dazu",
        "level": "A2",
        "grammar_notes": "Cause-and-effect relationship. Very high frequency in writing.",
        "verb_rank": 11,
    },

    # ==========================================
    # RANK 12: sprechen
    # ==========================================
    {
        "verb_group": "sprechen",
        "verb": "sprechen",
        "prep": "über",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to talk about (a topic/subject)",
        "sentence_de": "Wir müssen dringend {PREP} unsere Zukunft sprechen.",
        "sentence_en": "We urgently need to talk about our future.",
        "question_structure": "Worüber? • Darüber / Über wen?",
        "level": "A1",
        "grammar_notes": "Focuses on the content of the conversation.",
        "verb_rank": 12,
    },
    {
        "verb_group": "sprechen",
        "verb": "sprechen",
        "prep": "von",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to speak of / to mention / to tell of",
        "sentence_de": "Mein Großvater spricht oft {PREP} seinen alten Freunden.",
        "sentence_en": "My grandfather often speaks of his old friends.",
        "question_structure": "Wovon? • Davon / Von wem?",
        "level": "A2",
        "grammar_notes": "Focuses on referring to or recalling someone or an experience.",
        "verb_rank": 12,
    },
    {
        "verb_group": "sprechen",
        "verb": "sprechen",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to speak with / to converse with",
        "sentence_de": "Hast du schon {PREP} deiner Lehrerin gesprochen?",
        "sentence_en": "Have you already spoken with your teacher?",
        "question_structure": "Mit wem?",
        "level": "A1",
        "grammar_notes": "Always takes 'mit + Dativ' for the conversational partner.",
        "verb_rank": 12,
    },
    {
        "verb_group": "sprechen",
        "verb": "absprechen",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to coordinate with / to agree on with",
        "sentence_de": "Ich spreche den Urlaubsplan {PREP} meinen Kollegen ab.",
        "sentence_en": "I coordinate the vacation schedule with my colleagues.",
        "question_structure": "Mit wem?",
        "level": "B1",
        "grammar_notes": "Separable verb (ab|sprechen). To mutually arrange or agree.",
        "verb_rank": 12,
    },

    # ==========================================
    # RANK 13: zeigen
    # ==========================================
    {
        "verb_group": "zeigen",
        "verb": "zeigen",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to point at / to",
        "sentence_de": "Das kleine Kind zeigte {PREP} den bunten Schmetterling.",
        "sentence_en": "The little child pointed at the colorful butterfly.",
        "question_structure": "Worauf? • Darauf / Auf wen?",
        "level": "A2",
        "grammar_notes": "Physical pointing gesture with finger or indicator.",
        "verb_rank": 13,
    },

    # ==========================================
    # RANK 14: leben
    # ==========================================
    {
        "verb_group": "leben",
        "verb": "leben",
        "prep": "von",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to live on / to subsist on",
        "sentence_de": "Er kann kaum {PREP} seinem geringen Einkommen leben.",
        "sentence_en": "He can barely live on his meager income.",
        "question_structure": "Wovon? • Davon",
        "level": "A2",
        "grammar_notes": "Financial subsistence or sustenance.",
        "verb_rank": 14,
    },
    {
        "verb_group": "leben",
        "verb": "leben",
        "prep": "für",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to live for (a passion, purpose)",
        "sentence_de": "Sie lebt ganz {PREP} ihre Musik und ihre Kunst.",
        "sentence_en": "She lives entirely for her music and her art.",
        "question_structure": "Wofür? • Dafür / Für wen?",
        "level": "B1",
        "grammar_notes": "Expresses true life dedication or passion.",
        "verb_rank": 14,
    },

    # ==========================================
    # RANK 15: fahren
    # ==========================================
    {
        "verb_group": "fahren",
        "verb": "fahren",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to travel by / to ride with (means of transport)",
        "sentence_de": "Morgens fahre ich am liebsten {PREP} der U-Bahn.",
        "sentence_en": "In the morning I prefer traveling by subway.",
        "question_structure": "Womit? • Damit / Mit wem?",
        "level": "A1",
        "grammar_notes": "All vehicles in German take 'mit + Dativ' (mit dem Bus, mit dem Zug).",
        "verb_rank": 15,
    },

    # ==========================================
    # RANK 16: fragen
    # ==========================================
    {
        "verb_group": "fragen",
        "verb": "fragen",
        "prep": "nach",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to ask about / to inquire after",
        "sentence_de": "Ein Tourist fragte mich {PREP} dem kürzesten Weg zum Bahnhof.",
        "sentence_en": "A tourist asked me for the shortest way to the station.",
        "question_structure": "Wonach? • Danach / Nach wem?",
        "level": "A1",
        "grammar_notes": "Standard formula: jemanden (Akk) nach etwas (Dat) fragen.",
        "verb_rank": 16,
    },
    {
        "verb_group": "fragen",
        "verb": "fragen",
        "prep": "um",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to ask for (advice / help)",
        "sentence_de": "Sie fragte ihren Mentor {PREP} Rat in dieser Angelegenheit.",
        "sentence_en": "She asked her mentor for advice in this matter.",
        "question_structure": "Worum? • Darum",
        "level": "B1",
        "grammar_notes": "Most commonly in the fixed idiom 'um Rat fragen'.",
        "verb_rank": 16,
    },

    # ==========================================
    # RANK 17: gelten
    # ==========================================
    {
        "verb_group": "gelten",
        "verb": "gelten",
        "prep": "als",
        "case": "+ Nom.",
        "case_type": "nom",
        "meaning_en": "to be considered as / to count as",
        "sentence_de": "Er gilt weltweit {PREP} führender Experte für KI.",
        "sentence_en": "He is considered worldwide as a leading expert in AI.",
        "question_structure": "Als was? • Als wer?",
        "level": "B1",
        "grammar_notes": "'Als' takes Nominative when referring to the grammatical subject.",
        "verb_rank": 17,
    },
    {
        "verb_group": "gelten",
        "verb": "gelten",
        "prep": "für",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to apply to / to be valid for",
        "sentence_de": "Diese Sonderregelung gilt nur {PREP} neue Kunden.",
        "sentence_en": "This special regulation applies only to new customers.",
        "question_structure": "Wofür? • Dafür / Für wen?",
        "level": "B1",
        "grammar_notes": "Denotes the scope of validity of rules, laws, tickets.",
        "verb_rank": 17,
    },

    # ==========================================
    # RANK 18: stellen
    # ==========================================
    {
        "verb_group": "stellen",
        "verb": "sich einstellen",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to adapt to / to prepare oneself for",
        "sentence_de": "Wir müssen uns {PREP} plötzliche Veränderungen einstellen.",
        "sentence_en": "We must adapt to sudden changes.",
        "question_structure": "Worauf? • Darauf",
        "level": "B1",
        "grammar_notes": "Reflexive verb (sich einstellen auf). Mentally getting ready for something.",
        "verb_rank": 18,
    },

    # ==========================================
    # RANK 19: spielen
    # ==========================================
    {
        "verb_group": "spielen",
        "verb": "spielen",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to play with",
        "sentence_de": "Die Katze spielt begeistert {PREP} dem Wollknäuel.",
        "sentence_en": "The cat enthusiastically plays with the ball of yarn.",
        "question_structure": "Womit? • Damit / Mit wem?",
        "level": "A1",
        "grammar_notes": "Literal or figurative ('mit dem Feuer spielen' = to play with fire).",
        "verb_rank": 19,
    },
    {
        "verb_group": "spielen",
        "verb": "spielen",
        "prep": "um",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to play for (money, stakes, championship)",
        "sentence_de": "Die beiden Teams spielen {PREP} den Meistertitel.",
        "sentence_en": "Both teams are playing for the championship title.",
        "question_structure": "Worum? • Darum",
        "level": "B1",
        "grammar_notes": "Specifies the prize or stake at risk in a game.",
        "verb_rank": 19,
    },

    # ==========================================
    # RANK 20: arbeiten
    # ==========================================
    {
        "verb_group": "arbeiten",
        "verb": "arbeiten",
        "prep": "an",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to work on (a project, task, book)",
        "sentence_de": "Die Wissenschaftler arbeiten {PREP} einem neuen Impfstoff.",
        "sentence_en": "The scientists are working on a new vaccine.",
        "question_structure": "Woran? • Daran",
        "level": "A2",
        "grammar_notes": "Always Dativ when indicating the task or project being worked upon.",
        "verb_rank": 20,
    },
    {
        "verb_group": "arbeiten",
        "verb": "arbeiten",
        "prep": "bei",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to work at / for (an employer or company)",
        "sentence_de": "Mein Bruder arbeitet schon seit fünf Jahren {PREP} BMW.",
        "sentence_en": "My brother has been working at BMW for five years.",
        "question_structure": "Bei wem?",
        "level": "A1",
        "grammar_notes": "Used for the company/institution that employs someone.",
        "verb_rank": 20,
    },
    {
        "verb_group": "arbeiten",
        "verb": "arbeiten",
        "prep": "für",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to work for (a client, employer, or cause)",
        "sentence_de": "Sie arbeitet als freie Journalistin {PREP} verschiedene Zeitungen.",
        "sentence_en": "She works as a freelance journalist for various newspapers.",
        "question_structure": "Wofür? • Dafür / Für wen?",
        "level": "A2",
        "grammar_notes": "Emphasizes the beneficiary or contracting party.",
        "verb_rank": 20,
    },

    # ==========================================
    # RANK 21: folgen
    # ==========================================
    {
        "verb_group": "folgen",
        "verb": "folgen",
        "prep": "aus",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to follow from / to result from",
        "sentence_de": "Aus dieser Analyse folgt {PREP} den Daten eine klare Warnung.",
        "sentence_en": "From this analysis, a clear warning follows from the data.",
        "question_structure": "Woraus? • Daraus",
        "level": "B2",
        "grammar_notes": "Logical consequence: 'Daraus folgt, dass...'",
        "verb_rank": 21,
    },

    # ==========================================
    # RANK 22: lernen
    # ==========================================
    {
        "verb_group": "lernen",
        "verb": "lernen",
        "prep": "aus",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to learn from (a mistake, experience)",
        "sentence_de": "Kluge Menschen lernen {PREP} ihren eigenen Fehlern.",
        "sentence_en": "Smart people learn from their own mistakes.",
        "question_structure": "Woraus? • Daraus",
        "level": "A2",
        "grammar_notes": "Indicates the source of wisdom or lesson.",
        "verb_rank": 22,
    },

    # ==========================================
    # RANK 23: verstehen
    # ==========================================
    {
        "verb_group": "verstehen",
        "verb": "sich verstehen",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to get along with (someone)",
        "sentence_de": "Ich verstehe mich hervorragend {PREP} meinem neuen Mitbewohner.",
        "sentence_en": "I get along great with my new roommate.",
        "question_structure": "Mit wem?",
        "level": "A2",
        "grammar_notes": "Reflexive verb (sich gut/schlecht verstehen mit).",
        "verb_rank": 23,
    },
    {
        "verb_group": "verstehen",
        "verb": "verstehen",
        "prep": "unter",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to understand by (a concept or definition)",
        "sentence_de": "Was verstehen Sie genau {PREP} dem Begriff Nachhaltigkeit?",
        "sentence_en": "What exactly do you understand by the concept of sustainability?",
        "question_structure": "Worunter? • Darunter",
        "level": "B1",
        "grammar_notes": "Used when asking for definitions or subjective interpretations.",
        "verb_rank": 23,
    },

    # ==========================================
    # RANK 24: setzen
    # ==========================================
    {
        "verb_group": "setzen",
        "verb": "sich auseinandersetzen",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to deal with / to grapple with / to examine",
        "sentence_de": "Der Philosoph setzt sich tiefgehend {PREP} ethischen Fragen auseinander.",
        "sentence_en": "The philosopher grapples profoundly with ethical questions.",
        "question_structure": "Womit? • Damit / Mit wem?",
        "level": "B2",
        "grammar_notes": "Crucial academic verb for critical engagement with a subject.",
        "verb_rank": 24,
    },
    {
        "verb_group": "setzen",
        "verb": "sich einsetzen",
        "prep": "für",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to advocate for / to champion / to stand up for",
        "sentence_de": "Die Organisation setzt sich entschlossen {PREP} den Tierschutz ein.",
        "sentence_en": "The organization resolutely advocates for animal welfare.",
        "question_structure": "Wofür? • Dafür / Für wen?",
        "level": "B1",
        "grammar_notes": "Reflexive verb (sich einsetzen für). Dedicating active effort to a cause.",
        "verb_rank": 24,
    },

    # ==========================================
    # RANK 25: beginnen
    # ==========================================
    {
        "verb_group": "beginnen",
        "verb": "beginnen",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to begin with / to start with",
        "sentence_de": "Wir beginnen die Besprechung {PREP} einer kurzen Vorstellungsrunde.",
        "sentence_en": "We start the meeting with a short round of introductions.",
        "question_structure": "Womit? • Damit",
        "level": "A1",
        "grammar_notes": "Synonymous with 'anfangen mit + Dat'.",
        "verb_rank": 25,
    },

    # ==========================================
    # RANK 26: erzählen
    # ==========================================
    {
        "verb_group": "erzählen",
        "verb": "erzählen",
        "prep": "von",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to tell about / to narrate (events or experiences)",
        "sentence_de": "Oma erzählte uns stundenlang {PREP} ihrer Jugend auf dem Land.",
        "sentence_en": "Grandma told us for hours about her youth in the countryside.",
        "question_structure": "Wovon? • Davon / Von wem?",
        "level": "A1",
        "grammar_notes": "General recounting of memories or stories.",
        "verb_rank": 26,
    },
    {
        "verb_group": "erzählen",
        "verb": "erzählen",
        "prep": "über",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to tell / report about (factual topic or detailed info)",
        "sentence_de": "Der Reiseleiter erzählte viel Interessantes {PREP} die alte Burg.",
        "sentence_en": "The tour guide told many interesting things about the old castle.",
        "question_structure": "Worüber? • Darüber / Über wen?",
        "level": "A2",
        "grammar_notes": "'über + Akk' focuses on specific facts/details of a subject.",
        "verb_rank": 26,
    },

    # ==========================================
    # RANK 27: schreiben
    # ==========================================
    {
        "verb_group": "schreiben",
        "verb": "schreiben",
        "prep": "an",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to write to (a recipient)",
        "sentence_de": "Sie schreibt eine lange Nachricht {PREP} ihre beste Freundin.",
        "sentence_en": "She is writing a long message to her best friend.",
        "question_structure": "An wen?",
        "level": "A1",
        "grammar_notes": "Recipient takes Akkusativ: 'an + Akk' (alternatively just Dativ without prep).",
        "verb_rank": 27,
    },
    {
        "verb_group": "schreiben",
        "verb": "schreiben",
        "prep": "an",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to work on writing (a book, dissertation, article)",
        "sentence_de": "Der bekannte Schriftsteller schreibt schon seit Jahren {PREP} einem neuen Roman.",
        "sentence_en": "The famous author has been working on writing a new novel for years.",
        "question_structure": "Woran? • Daran",
        "level": "B1",
        "grammar_notes": "Note the contrast: 'an + Dat' means being in the process of composing a work!",
        "verb_rank": 27,
    },
    {
        "verb_group": "schreiben",
        "verb": "schreiben",
        "prep": "über",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to write about (a topic)",
        "sentence_de": "Er schreibt seine Masterarbeit {PREP} erneuerbare Energien.",
        "sentence_en": "He is writing his master's thesis about renewable energy.",
        "question_structure": "Worüber? • Darüber",
        "level": "A2",
        "grammar_notes": "Denotes the theme or topic of the written piece.",
        "verb_rank": 27,
    },

    # ==========================================
    # RANK 28: handeln
    # ==========================================
    {
        "verb_group": "handeln",
        "verb": "handeln",
        "prep": "von",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to be about (plot, theme of a story/book/movie)",
        "sentence_de": "Das Lied handelt {PREP} einer bittersüßen Liebe im Sommer.",
        "sentence_en": "The song is about a bittersweet love in summer.",
        "question_structure": "Wovon? • Davon",
        "level": "A2",
        "grammar_notes": "Active verb: 'Das Buch handelt von...'. Do not confuse with 'es handelt sich um'!",
        "verb_rank": 28,
    },
    {
        "verb_group": "handeln",
        "verb": "sich handeln",
        "prep": "um",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to be a matter of / to concern (essential nature)",
        "sentence_de": "Bei dieser Angelegenheit handelt es sich {PREP} ein ernstes Problem.",
        "sentence_en": "In this matter, it is a serious problem.",
        "question_structure": "Worum? • Darum",
        "level": "B1",
        "grammar_notes": "Impersonal reflexive: always 'es handelt sich um + Akk'. Used for formal definitions.",
        "verb_rank": 28,
    },
    {
        "verb_group": "handeln",
        "verb": "handeln",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to trade in / to deal with (goods, commodities)",
        "sentence_de": "Der Händler handelt {PREP} edlen Weinen und Antiquitäten.",
        "sentence_en": "The merchant trades in fine wines and antiques.",
        "question_structure": "Womit? • Damit / Mit wem?",
        "level": "B1",
        "grammar_notes": "Commerce and business transactions.",
        "verb_rank": 28,
    },

    # ==========================================
    # RANK 29: gehören
    # ==========================================
    {
        "verb_group": "gehören",
        "verb": "gehören",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to belong to / to be part of (a group, set, or category)",
        "sentence_de": "Kaffee gehört für viele {PREP} einem perfekten Morgen.",
        "sentence_en": "For many, coffee belongs to a perfect morning.",
        "question_structure": "Wozu? • Dazu / Zu wem?",
        "level": "A2",
        "grammar_notes": "Membership or integral part. Note: simple ownership is 'etwas gehört jemandem (Dat)' without prep.",
        "verb_rank": 29,
    },

    # ==========================================
    # RANK 30: bitten
    # ==========================================
    {
        "verb_group": "bitten",
        "verb": "bitten",
        "prep": "um",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to ask for / to request",
        "sentence_de": "Darf ich Sie {PREP} einen kurzen Augenblick Geduld bitten?",
        "sentence_en": "May I ask you for a brief moment of patience?",
        "question_structure": "Worum? • Darum",
        "level": "A2",
        "grammar_notes": "Formula: jemanden (Akk) um etwas (Akk) bitten. Crucial polite request phrasing.",
        "verb_rank": 30,
    },

    # ==========================================
    # RANK 31: warten
    # ==========================================
    {
        "verb_group": "warten",
        "verb": "warten",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to wait for",
        "sentence_de": "Wir warten schon seit einer halben Stunde {PREP} den verspäteten Zug.",
        "sentence_en": "We have been waiting for the delayed train for half an hour.",
        "question_structure": "Worauf? • Darauf / Auf wen?",
        "level": "A1",
        "grammar_notes": "Preposition 'auf' always takes Akkusativ here. Never use 'für'!",
        "verb_rank": 31,
    },
    {
        "verb_group": "warten",
        "verb": "warten",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to hold off on / to delay doing something",
        "sentence_de": "Wir sollten {PREP} dem Kauf noch warten, bis die Preise sinken.",
        "sentence_en": "We should hold off on the purchase until prices drop.",
        "question_structure": "Womit? • Damit",
        "level": "B1",
        "grammar_notes": "Indicates postponing an action: 'mit der Entscheidung warten'.",
        "verb_rank": 31,
    },

    # ==========================================
    # RANK 32: bestehen
    # ==========================================
    {
        "verb_group": "bestehen",
        "verb": "bestehen",
        "prep": "aus",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to consist of / to be made of",
        "sentence_de": "Das Team besteht {PREP} fünf erfahrenen Entwicklern.",
        "sentence_en": "The team consists of five experienced developers.",
        "question_structure": "Woraus? • Daraus",
        "level": "A2",
        "grammar_notes": "Physical components or group members.",
        "verb_rank": 32,
    },
    {
        "verb_group": "bestehen",
        "verb": "bestehen",
        "prep": "auf",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to insist on",
        "sentence_de": "Der Gast bestand unnachgiebig {PREP} seinem Recht auf Rückerstattung.",
        "sentence_en": "The guest unyieldingly insisted on his right to a refund.",
        "question_structure": "Worauf? • Darauf",
        "level": "B1",
        "grammar_notes": "In modern German, 'bestehen auf' predominantly takes Dativ.",
        "verb_rank": 32,
    },
    {
        "verb_group": "bestehen",
        "verb": "bestehen",
        "prep": "in",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to consist in / to lie in (the essence of)",
        "sentence_de": "Die Schwierigkeit besteht {PREP} der genauen Umsetzung des Plans.",
        "sentence_en": "The difficulty lies in the exact implementation of the plan.",
        "question_structure": "Worin? • Darin",
        "level": "B2",
        "grammar_notes": "Defines the core essence or nature of an abstract issue.",
        "verb_rank": 32,
    },

    # ==========================================
    # RANK 33: suchen
    # ==========================================
    {
        "verb_group": "suchen",
        "verb": "suchen",
        "prep": "nach",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to search for / to look for",
        "sentence_de": "Die Forscher suchen intensiv {PREP} einer Heilung für die Krankheit.",
        "sentence_en": "The researchers are searching intensively for a cure for the disease.",
        "question_structure": "Wonach? • Danach / Nach wem?",
        "level": "A2",
        "grammar_notes": "Note: 'etwas suchen' (direct object Akk) is common for objects; 'suchen nach + Dat' emphasizes ongoing quest/effort.",
        "verb_rank": 33,
    },

    # ==========================================
    # RANK 34: hoffen
    # ==========================================
    {
        "verb_group": "hoffen",
        "verb": "hoffen",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to hope for",
        "sentence_de": "Die Landwirte hoffen dringend {PREP} ergiebigen Regen.",
        "sentence_en": "The farmers are urgently hoping for plentiful rain.",
        "question_structure": "Worauf? • Darauf",
        "level": "A2",
        "grammar_notes": "Always takes 'auf + Akkusativ'. Never 'für'!",
        "verb_rank": 34,
    },

    # ==========================================
    # RANK 35: achten
    # ==========================================
    {
        "verb_group": "achten",
        "verb": "achten",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to pay attention to / to watch out for",
        "sentence_de": "Beim Überqueren der Straße musst du {PREP} den Verkehr achten.",
        "sentence_en": "When crossing the street you have to pay attention to the traffic.",
        "question_structure": "Worauf? • Darauf / Auf wen?",
        "level": "A2",
        "grammar_notes": "Active attentiveness or care (e.g. auf die Ernährung achten).",
        "verb_rank": 35,
    },

    # ==========================================
    # RANK 36: antworten
    # ==========================================
    {
        "verb_group": "antworten",
        "verb": "antworten",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to reply to / to answer (a question or message)",
        "sentence_de": "Er hat noch immer nicht {PREP} meine dringende Frage geantwortet.",
        "sentence_en": "He still hasn't answered my urgent question.",
        "question_structure": "Worauf? • Darauf",
        "level": "A1",
        "grammar_notes": "jemandem (Dat) auf etwas (Akk) antworten. Contrast: 'etwas beantworten' takes direct Akk object.",
        "verb_rank": 36,
    },

    # ==========================================
    # RANK 37: danken
    # ==========================================
    {
        "verb_group": "danken",
        "verb": "danken",
        "prep": "für",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to thank for",
        "sentence_de": "Ich danke dir von ganzem Herzen {PREP} deine großzügige Unterstützung.",
        "sentence_en": "I thank you with all my heart for your generous support.",
        "question_structure": "Wofür? • Dafür",
        "level": "A1",
        "grammar_notes": "Formula: jemandem (Dat) für etwas (Akk) danken.",
        "verb_rank": 37,
    },

    # ==========================================
    # RANK 38: rechnen
    # ==========================================
    {
        "verb_group": "rechnen",
        "verb": "rechnen",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to count on / to expect / to anticipate",
        "sentence_de": "Im Winter muss man jederzeit {PREP} glatten Straßen rechnen.",
        "sentence_en": "In winter one must expect slippery roads at any time.",
        "question_structure": "Womit? • Damit / Mit wem?",
        "level": "B1",
        "grammar_notes": "Anticipating a condition, event, or problem.",
        "verb_rank": 38,
    },

    # ==========================================
    # RANK 39: fehlen
    # ==========================================
    {
        "verb_group": "fehlen",
        "verb": "fehlen",
        "prep": "an",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to lack / to be deficient in",
        "sentence_de": "In dem Projekt fehlt es vor allem {PREP} qualifizierten Mitarbeitern.",
        "sentence_en": "In the project, there is primarily a lack of qualified employees.",
        "question_structure": "Woran? • Daran",
        "level": "B1",
        "grammar_notes": "Often used impersonally: 'Es fehlt an + Dat'.",
        "verb_rank": 39,
    },

    # ==========================================
    # RANK 40: passen
    # ==========================================
    {
        "verb_group": "passen",
        "verb": "passen",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to match / to suit / to go well with",
        "sentence_de": "Dieser dunkle Gürtel passt perfekt {PREP} deinen neuen Schuhen.",
        "sentence_en": "This dark belt goes perfectly with your new shoes.",
        "question_structure": "Wozu? • Dazu / Zu wem?",
        "level": "A2",
        "grammar_notes": "Compatibility in style, character, or harmony.",
        "verb_rank": 40,
    },
    {
        "verb_group": "passen",
        "verb": "passen",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to fit onto / to fit (physically)",
        "sentence_de": "Der Deckel passt genau {PREP} diese kleine Dose.",
        "sentence_en": "The lid fits exactly onto this small tin.",
        "question_structure": "Worauf? • Darauf",
        "level": "B1",
        "grammar_notes": "Physical fit or attachment onto a surface/opening.",
        "verb_rank": 40,
    },

    # ==========================================
    # RANK 41: vertrauen
    # ==========================================
    {
        "verb_group": "vertrauen",
        "verb": "vertrauen",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to trust in / to rely on",
        "sentence_de": "Sie vertraut voll und ganz {PREP} ihre eigene Intuition.",
        "sentence_en": "She trusts completely in her own intuition.",
        "question_structure": "Worauf? • Darauf / Auf wen?",
        "level": "B1",
        "grammar_notes": "Can take simple Dativ (jemandem vertrauen) or 'auf + Akk' for strong reliance/faith.",
        "verb_rank": 41,
    },

    # ==========================================
    # RANK 42: leiden
    # ==========================================
    {
        "verb_group": "leiden",
        "verb": "leiden",
        "prep": "an",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to suffer from (a specific medical illness or disease)",
        "sentence_de": "Der Patient leidet seit seiner Kindheit {PREP} schwerem Asthma.",
        "sentence_en": "The patient has suffered from severe asthma since childhood.",
        "question_structure": "Woran? • Daran",
        "level": "B1",
        "grammar_notes": "CRUCIAL CONTRAST: 'leiden an + Dat' is reserved for diagnostic illnesses/diseases.",
        "verb_rank": 42,
    },
    {
        "verb_group": "leiden",
        "verb": "leiden",
        "prep": "unter",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to suffer under (difficult circumstances, stress, noise, loneliness)",
        "sentence_de": "Viele Großstädter leiden {PREP} dem ständigen Lärm und der Hektik.",
        "sentence_en": "Many city dwellers suffer under the constant noise and hectic pace.",
        "question_structure": "Worunter? • Darunter",
        "level": "B1",
        "grammar_notes": "CRUCIAL CONTRAST: 'leiden unter + Dat' is used for environmental or situational conditions.",
        "verb_rank": 42,
    },

    # ==========================================
    # RANK 43: zweifeln
    # ==========================================
    {
        "verb_group": "zweifeln",
        "verb": "zweifeln",
        "prep": "an",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to doubt / to have doubts about",
        "sentence_de": "Niemand im Kollegium zweifelt {PREP} seiner außergewöhnlichen Kompetenz.",
        "sentence_en": "No one on the faculty doubts his extraordinary competence.",
        "question_structure": "Woran? • Daran / An wem?",
        "level": "B1",
        "grammar_notes": "Always takes 'an + Dativ'.",
        "verb_rank": 43,
    },

    # ==========================================
    # RANK 44: sich freuen
    # ==========================================
    {
        "verb_group": "sich freuen",
        "verb": "sich freuen",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to look forward to (a FUTURE event)",
        "sentence_de": "Wir freuen uns schon riesig {PREP} den bevorstehenden Urlaub.",
        "sentence_en": "We are already looking forward very much to the upcoming vacation.",
        "question_structure": "Worauf? • Darauf / Auf wen?",
        "level": "A1",
        "grammar_notes": "FUTURE TIME ONLY: anticipation of something yet to happen. Always Akkusativ.",
        "verb_rank": 44,
    },
    {
        "verb_group": "sich freuen",
        "verb": "sich freuen",
        "prep": "über",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to be pleased / happy about (a PRESENT or PAST event/gift)",
        "sentence_de": "Ich habe mich sehr {PREP} deinen liebevollen Brief gefreut.",
        "sentence_en": "I was very pleased about your loving letter.",
        "question_structure": "Worüber? • Darüber / Über wen?",
        "level": "A1",
        "grammar_notes": "PRESENT/PAST ONLY: reaction to something that has occurred or already arrived.",
        "verb_rank": 44,
    },

    # ==========================================
    # RANK 45: sich interessieren
    # ==========================================
    {
        "verb_group": "sich interessieren",
        "verb": "sich interessieren",
        "prep": "für",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to be interested in",
        "sentence_de": "Interessierst du dich eigentlich {PREP} klassische Architektur?",
        "sentence_en": "Are you actually interested in classical architecture?",
        "question_structure": "Wofür? • Dafür / Für wen?",
        "level": "A1",
        "grammar_notes": "Reflexive verb with Akk. object (sich) and 'für + Akk'.",
        "verb_rank": 45,
    },

    # ==========================================
    # RANK 46: sich erinnern
    # ==========================================
    {
        "verb_group": "sich erinnern",
        "verb": "sich erinnern",
        "prep": "an",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to remember / to recall",
        "sentence_de": "Erinnert ihr euch noch {PREP} unseren ersten gemeinsamen Schultag?",
        "sentence_en": "Do you still remember our first school day together?",
        "question_structure": "Woran? • Daran / An wen?",
        "level": "A2",
        "grammar_notes": "Reflexive: 'sich erinnern an + Akk'. Active form 'jemanden an etwas erinnern' = to remind someone of something.",
        "verb_rank": 46,
    },

    # ==========================================
    # RANK 47: sich kümmern
    # ==========================================
    {
        "verb_group": "sich kümmern",
        "verb": "sich kümmern",
        "prep": "um",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to take care of / to look after / to attend to",
        "sentence_de": "Wer kümmert sich während deiner Abwesenheit {PREP} die Haustiere?",
        "sentence_en": "Who will take care of the pets during your absence?",
        "question_structure": "Worum? • Darum / Um wen?",
        "level": "A2",
        "grammar_notes": "Taking responsibility for someone or dealing with a task.",
        "verb_rank": 47,
    },

    # ==========================================
    # RANK 48: sich ärgern
    # ==========================================
    {
        "verb_group": "sich ärgern",
        "verb": "sich ärgern",
        "prep": "über",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to be annoyed / irritated / angry about",
        "sentence_de": "Sie ärgert sich maßlos {PREP} den unzuverlässigen Handwerker.",
        "sentence_en": "She is exceedingly annoyed about the unreliable craftsman.",
        "question_structure": "Worüber? • Darüber / Über wen?",
        "level": "A2",
        "grammar_notes": "Reflexive emotional state. Always 'über + Akkusativ'.",
        "verb_rank": 48,
    },

    # ==========================================
    # RANK 49: sich beschäftigen
    # ==========================================
    {
        "verb_group": "sich beschäftigen",
        "verb": "sich beschäftigen",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to occupy oneself with / to be busy with",
        "sentence_de": "In ihrer Freizeit beschäftigt sie sich gern {PREP} Malerei.",
        "sentence_en": "In her free time she likes to occupy herself with painting.",
        "question_structure": "Womit? • Damit / Mit wem?",
        "level": "A2",
        "grammar_notes": "Dedicated activity or hobby. Always takes 'mit + Dativ'.",
        "verb_rank": 49,
    },

    # ==========================================
    # RANK 50: sich bewerben
    # ==========================================
    {
        "verb_group": "sich bewerben",
        "verb": "sich bewerben",
        "prep": "um",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to apply for (a job, position, scholarship)",
        "sentence_de": "Er bewirbt sich {PREP} ein Stipendium an einer angesehenen Universität.",
        "sentence_en": "He is applying for a scholarship at a prestigious university.",
        "question_structure": "Worum? • Darum",
        "level": "A2",
        "grammar_notes": "The target role or prize takes 'um + Akkusativ'.",
        "verb_rank": 50,
    },
    {
        "verb_group": "sich bewerben",
        "verb": "sich bewerben",
        "prep": "bei",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to apply to / at (a company, institution)",
        "sentence_de": "Sie hat sich {PREP} einer internationalen Bank beworben.",
        "sentence_en": "She applied at an international bank.",
        "question_structure": "Bei wem?",
        "level": "A2",
        "grammar_notes": "The target organization/company takes 'bei + Dativ'.",
        "verb_rank": 50,
    },

    # ==========================================
    # RANK 51: sich gewöhnen
    # ==========================================
    {
        "verb_group": "sich gewöhnen",
        "verb": "sich gewöhnen",
        "prep": "an",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to get used to / to accustom oneself to",
        "sentence_de": "Ich kann mich einfach nicht {PREP} den frühen Wecker gewöhnen.",
        "sentence_en": "I simply cannot get used to the early alarm clock.",
        "question_structure": "Woran? • Daran / An wen?",
        "level": "A2",
        "grammar_notes": "Always takes 'an + Akkusativ'.",
        "verb_rank": 51,
    },

    # ==========================================
    # RANK 52: sich konzentrieren
    # ==========================================
    {
        "verb_group": "sich konzentrieren",
        "verb": "sich konzentrieren",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to concentrate on / to focus on",
        "sentence_de": "Bitte konzentrieren Sie sich voll {PREP} die bevorstehende Prüfung!",
        "sentence_en": "Please concentrate fully on the upcoming exam!",
        "question_structure": "Worauf? • Darauf / Auf wen?",
        "level": "A2",
        "grammar_notes": "Direction of mental focus: takes Akkusativ.",
        "verb_rank": 52,
    },

    # ==========================================
    # RANK 53: sich verlassen
    # ==========================================
    {
        "verb_group": "sich verlassen",
        "verb": "sich verlassen",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to rely on / to depend on",
        "sentence_de": "Auf meine engsten Freunde kann ich mich immer {PREP} blind verlassen.",
        "sentence_en": "I can always blindly rely on my closest friends.",
        "question_structure": "Worauf? • Darauf / Auf wen?",
        "level": "B1",
        "grammar_notes": "Reflexive verb (sich verlassen auf). Trusting someone's dependability.",
        "verb_rank": 53,
    },

    # ==========================================
    # RANK 54: sich beziehen
    # ==========================================
    {
        "verb_group": "sich beziehen",
        "verb": "sich beziehen",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to refer to / to relate to",
        "sentence_de": "Mein Schreiben bezieht sich {PREP} Ihr Inserat vom 15. Mai.",
        "sentence_en": "My letter refers to your advertisement from May 15th.",
        "question_structure": "Worauf? • Darauf",
        "level": "B1",
        "grammar_notes": "Essential in formal correspondence ('Bezug nehmend auf...').",
        "verb_rank": 54,
    },

    # ==========================================
    # RANK 55: sich vorbereiten
    # ==========================================
    {
        "verb_group": "sich vorbereiten",
        "verb": "sich vorbereiten",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to prepare for",
        "sentence_de": "Die Sportler bereiten sich monatelang {PREP} den Marathon vor.",
        "sentence_en": "The athletes prepare for months for the marathon.",
        "question_structure": "Worauf? • Darauf",
        "level": "A2",
        "grammar_notes": "Separable reflexive verb (sich vor|bereiten).",
        "verb_rank": 55,
    },

    # ==========================================
    # RANK 56: sich verlieben
    # ==========================================
    {
        "verb_group": "sich verlieben",
        "verb": "sich verlieben",
        "prep": "in",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to fall in love with",
        "sentence_de": "Er hat sich unsterblich {PREP} seine Arbeitskollegin verliebt.",
        "sentence_en": "He fell hopelessly in love with his coworker.",
        "question_structure": "In wen? / Worin?",
        "level": "A2",
        "grammar_notes": "Note: takes 'in + Akkusativ' (never 'mit'!).",
        "verb_rank": 56,
    },

    # ==========================================
    # RANK 57: sich verabreden
    # ==========================================
    {
        "verb_group": "sich verabreden",
        "verb": "sich verabreden",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to arrange to meet with / to make a date with",
        "sentence_de": "Ich habe mich für heute Abend {PREP} Markus verabredet.",
        "sentence_en": "I arranged to meet with Markus for this evening.",
        "question_structure": "Mit wem?",
        "level": "A2",
        "grammar_notes": "Social meeting appointment.",
        "verb_rank": 57,
    },

    # ==========================================
    # RANK 58: abhängen
    # ==========================================
    {
        "verb_group": "abhängen",
        "verb": "abhängen",
        "prep": "von",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to depend on",
        "sentence_de": "Der Erfolg eines Unternehmens hängt stark {PREP} seinen Mitarbeitern ab.",
        "sentence_en": "The success of a business depends heavily on its employees.",
        "question_structure": "Wovon? • Davon / Von wem?",
        "level": "A2",
        "grammar_notes": "Separable verb: 'ab|hängen von + Dat'.",
        "verb_rank": 58,
    },

    # ==========================================
    # RANK 59: aufhören
    # ==========================================
    {
        "verb_group": "aufhören",
        "verb": "aufhören",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to stop / to cease doing something",
        "sentence_de": "Wann hörst du endlich {PREP} dem ständigen Jammern auf?",
        "sentence_en": "When will you finally stop the constant whining?",
        "question_structure": "Womit? • Damit",
        "level": "A1",
        "grammar_notes": "Separable verb: 'auf|hören mit + Dat'.",
        "verb_rank": 59,
    },

    # ==========================================
    # RANK 60: aufpassen
    # ==========================================
    {
        "verb_group": "aufpassen",
        "verb": "aufpassen",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to watch out for / to look after",
        "sentence_de": "Könntest du kurz {PREP} mein Gepäck aufpassen?",
        "sentence_en": "Could you watch my luggage for a moment?",
        "question_structure": "Worauf? • Darauf / Auf wen?",
        "level": "A2",
        "grammar_notes": "Separable verb: 'auf|passen auf + Akk'. Guarding or minding someone/something.",
        "verb_rank": 60,
    },

    # ==========================================
    # RANK 61: ausgeben
    # ==========================================
    {
        "verb_group": "ausgeben",
        "verb": "ausgeben",
        "prep": "für",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to spend (money) on",
        "sentence_de": "Er gibt viel zu viel Geld {PREP} teure Kleidung aus.",
        "sentence_en": "He spends far too much money on expensive clothes.",
        "question_structure": "Wofür? • Dafür",
        "level": "A2",
        "grammar_notes": "Separable verb: Geld ausgeben für + Akk.",
        "verb_rank": 61,
    },

    # ==========================================
    # RANK 62: beitragen
    # ==========================================
    {
        "verb_group": "beitragen",
        "verb": "beitragen",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to contribute to",
        "sentence_de": "Jeder einzelne Bürger kann {PREP} einer sauberen Umwelt beitragen.",
        "sentence_en": "Every single citizen can contribute to a clean environment.",
        "question_structure": "Wozu? • Dazu",
        "level": "B1",
        "grammar_notes": "Irregular separable verb (trägt bei; trug bei; beigetragen).",
        "verb_rank": 62,
    },

    # ==========================================
    # RANK 63: berichten
    # ==========================================
    {
        "verb_group": "berichten",
        "verb": "berichten",
        "prep": "über",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to report on (a comprehensive subject or event)",
        "sentence_de": "Die Zeitungen berichten ausführlich {PREP} die neue Gesetzesreform.",
        "sentence_en": "The newspapers report extensively on the new legal reform.",
        "question_structure": "Worüber? • Darüber / Über wen?",
        "level": "A2",
        "grammar_notes": "Journalistic or detailed factual reporting.",
        "verb_rank": 63,
    },
    {
        "verb_group": "berichten",
        "verb": "berichten",
        "prep": "von",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to report / tell of (an incident or experience)",
        "sentence_de": "Der Augenzeuge berichtete {PREP} einem lauten Knall.",
        "sentence_en": "The eyewitness reported of a loud bang.",
        "question_structure": "Wovon? • Davon",
        "level": "B1",
        "grammar_notes": "Focuses on personal observation or occurrence.",
        "verb_rank": 63,
    },

    # ==========================================
    # RANK 64: einladen
    # ==========================================
    {
        "verb_group": "einladen",
        "verb": "einladen",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to invite to (an event or party)",
        "sentence_de": "Wir möchten dich herzlich {PREP} unserer Geburtstagsfeier einladen.",
        "sentence_en": "We would like to warmly invite you to our birthday party.",
        "question_structure": "Wozu? • Dazu",
        "level": "A1",
        "grammar_notes": "Formula: jemanden (Akk) zu etwas (Dat) einladen.",
        "verb_rank": 64,
    },

    # ==========================================
    # RANK 65: sich entscheiden
    # ==========================================
    {
        "verb_group": "sich entscheiden",
        "verb": "sich entscheiden",
        "prep": "für",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to decide in favor of / to choose",
        "sentence_de": "Nach langer Überlegung entschied sie sich {PREP} das Medizinstudium.",
        "sentence_en": "After long consideration she decided in favor of medical school.",
        "question_structure": "Wofür? • Dafür / Für wen?",
        "level": "A2",
        "grammar_notes": "Selecting an option among alternatives.",
        "verb_rank": 65,
    },
    {
        "verb_group": "sich entscheiden",
        "verb": "sich entscheiden",
        "prep": "gegen",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to decide against",
        "sentence_de": "Er hat sich bewusst {PREP} den teuren Umzug entschieden.",
        "sentence_en": "He deliberately decided against the expensive relocation.",
        "question_structure": "Wogegen? • Dagegen",
        "level": "A2",
        "grammar_notes": "Rejecting an option.",
        "verb_rank": 65,
    },

    # ==========================================
    # RANK 66: sich entschuldigen
    # ==========================================
    {
        "verb_group": "sich entschuldigen",
        "verb": "sich entschuldigen",
        "prep": "bei",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to apologize to (a person)",
        "sentence_de": "Er sollte sich aufrichtig {PREP} seiner Nachbarin entschuldigen.",
        "sentence_en": "He should sincerely apologize to his neighbor.",
        "question_structure": "Bei wem?",
        "level": "A1",
        "grammar_notes": "The recipient of the apology takes 'bei + Dativ'.",
        "verb_rank": 66,
    },
    {
        "verb_group": "sich entschuldigen",
        "verb": "sich entschuldigen",
        "prep": "für",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to apologize for (a mistake or action)",
        "sentence_de": "Ich entschuldige mich vielmals {PREP} das Missgeschick.",
        "sentence_en": "I apologize very much for the mishap.",
        "question_structure": "Wofür? • Dafür",
        "level": "A1",
        "grammar_notes": "The reason for the apology takes 'für + Akkusativ'.",
        "verb_rank": 66,
    },

    # ==========================================
    # RANK 67: sich erholen
    # ==========================================
    {
        "verb_group": "sich erholen",
        "verb": "sich erholen",
        "prep": "von",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to recover from (illness, stress, strain)",
        "sentence_de": "Sie muss sich erst {PREP} den Strapazen der langen Reise erholen.",
        "sentence_en": "She first needs to recover from the hardships of the long journey.",
        "question_structure": "Wovon? • Davon",
        "level": "A2",
        "grammar_notes": "Restoration of health or energy.",
        "verb_rank": 67,
    },

    # ==========================================
    # RANK 68: erkennen
    # ==========================================
    {
        "verb_group": "erkennen",
        "verb": "erkennen",
        "prep": "an",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to recognize by (a characteristic feature)",
        "sentence_de": "Ich habe sie sofort {PREP} ihrem herzlichen Lachen erkannt.",
        "sentence_en": "I recognized her immediately by her hearty laugh.",
        "question_structure": "Woran? • Daran",
        "level": "B1",
        "grammar_notes": "Formula: jemanden an etwas (Dat) erkennen.",
        "verb_rank": 68,
    },

    # ==========================================
    # RANK 69: sich erkundigen
    # ==========================================
    {
        "verb_group": "sich erkundigen",
        "verb": "sich erkundigen",
        "prep": "nach",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to inquire about (information, conditions)",
        "sentence_de": "Er erkundigte sich am Schalter {PREP} den Abfahrtszeiten.",
        "sentence_en": "He inquired at the counter about departure times.",
        "question_structure": "Wonach? • Danach",
        "level": "B1",
        "grammar_notes": "More formal synonym for 'fragen nach + Dat'.",
        "verb_rank": 69,
    },
    {
        "verb_group": "sich erkundigen",
        "verb": "sich erkundigen",
        "prep": "bei",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to inquire with / at (a person or institution)",
        "sentence_de": "Sie erkundigte sich {PREP} der Behörde nach den notwendigen Unterlagen.",
        "sentence_en": "She inquired at the agency about the required documents.",
        "question_structure": "Bei wem?",
        "level": "B1",
        "grammar_notes": "The source/authority being asked takes 'bei + Dativ'.",
        "verb_rank": 69,
    },

    # ==========================================
    # RANK 70: erschrecken
    # ==========================================
    {
        "verb_group": "erschrecken",
        "verb": "erschrecken",
        "prep": "über",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to be shocked / startled by (news, realization)",
        "sentence_de": "Die Bürger erschraken {PREP} den drastischen Preisanstieg.",
        "sentence_en": "The citizens were shocked by the drastic price increase.",
        "question_structure": "Worüber? • Darüber",
        "level": "B1",
        "grammar_notes": "Emotional shock upon discovering a fact or news item.",
        "verb_rank": 70,
    },
    {
        "verb_group": "erschrecken",
        "verb": "erschrecken",
        "prep": "vor",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to be frightened of (a sudden noise, animal, entity)",
        "sentence_de": "Das Baby erschrak furchtbar {PREP} dem lauten Donner.",
        "sentence_en": "The baby was terribly frightened by the loud thunder.",
        "question_structure": "Wovor? • Davor / Vor wem?",
        "level": "B1",
        "grammar_notes": "Direct sensory startle response to a danger or sudden noise.",
        "verb_rank": 70,
    },

    # ==========================================
    # RANK 71: sich fürchten
    # ==========================================
    {
        "verb_group": "sich fürchten",
        "verb": "sich fürchten",
        "prep": "vor",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to be afraid of / to dread",
        "sentence_de": "Manche Menschen fürchten sich {PREP} engen Räumen.",
        "sentence_en": "Some people are afraid of confined spaces.",
        "question_structure": "Wovor? • Davor / Vor wem?",
        "level": "B1",
        "grammar_notes": "Always 'vor + Dativ'. Synonymous with 'Angst haben vor + Dat'.",
        "verb_rank": 71,
    },

    # ==========================================
    # RANK 72: gratulieren
    # ==========================================
    {
        "verb_group": "gratulieren",
        "verb": "gratulieren",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to congratulate on",
        "sentence_de": "Wir gratulieren dir ganz herzlich {PREP} deiner bestandenen Prüfung!",
        "sentence_en": "We warmly congratulate you on your passed exam!",
        "question_structure": "Wozu? • Dazu",
        "level": "A2",
        "grammar_notes": "Formula: jemandem (Dat) zu etwas (Dat) gratulieren.",
        "verb_rank": 72,
    },

    # ==========================================
    # RANK 73: klagen
    # ==========================================
    {
        "verb_group": "klagen",
        "verb": "klagen",
        "prep": "über",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to complain about / to lament",
        "sentence_de": "Die Patienten klagen {PREP} anhaltende Übelkeit.",
        "sentence_en": "The patients complain of persistent nausea.",
        "question_structure": "Worüber? • Darüber",
        "level": "B1",
        "grammar_notes": "Medical complaints or general grievances.",
        "verb_rank": 73,
    },
    {
        "verb_group": "klagen",
        "verb": "klagen",
        "prep": "gegen",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to file a lawsuit against / to sue",
        "sentence_de": "Der Anwohner klagt {PREP} den Bau der neuen Autobahn.",
        "sentence_en": "The resident is suing against the construction of the new highway.",
        "question_structure": "Wogegen? • Dagegen / Gegen wen?",
        "level": "B2",
        "grammar_notes": "Legal context: bringing action before a court.",
        "verb_rank": 73,
    },

    # ==========================================
    # RANK 74: protestieren
    # ==========================================
    {
        "verb_group": "protestieren",
        "verb": "protestieren",
        "prep": "gegen",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to protest against",
        "sentence_de": "Tausende Bürger protestieren friedlich {PREP} die Steuererhöhung.",
        "sentence_en": "Thousands of citizens are peacefully protesting against the tax increase.",
        "question_structure": "Wogegen? • Dagegen",
        "level": "B1",
        "grammar_notes": "Always takes 'gegen + Akkusativ'.",
        "verb_rank": 74,
    },

    # ==========================================
    # RANK 75: reagieren
    # ==========================================
    {
        "verb_group": "reagieren",
        "verb": "reagieren",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to react to",
        "sentence_de": "Wie hat die Schulleitung {PREP} die Beschwerde reagiert?",
        "sentence_en": "How did the school administration react to the complaint?",
        "question_structure": "Worauf? • Darauf / Auf wen?",
        "level": "A2",
        "grammar_notes": "Always takes 'auf + Akkusativ'.",
        "verb_rank": 75,
    },

    # ==========================================
    # RANK 76: riechen
    # ==========================================
    {
        "verb_group": "riechen",
        "verb": "riechen",
        "prep": "nach",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to smell like / of",
        "sentence_de": "Im ganzen Haus riecht es köstlich {PREP} frisch gebackenem Brot.",
        "sentence_en": "The whole house smells delicious like freshly baked bread.",
        "question_structure": "Wonach? • Danach",
        "level": "A2",
        "grammar_notes": "Sensory impression of aroma.",
        "verb_rank": 76,
    },

    # ==========================================
    # RANK 77: schmecken
    # ==========================================
    {
        "verb_group": "schmecken",
        "verb": "schmecken",
        "prep": "nach",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to taste like / of",
        "sentence_de": "Das Dessert schmeckt wunderbar {PREP} frischer Vanille.",
        "sentence_en": "The dessert tastes wonderful like fresh vanilla.",
        "question_structure": "Wonach? • Danach",
        "level": "A2",
        "grammar_notes": "Sensory impression of taste.",
        "verb_rank": 77,
    },

    # ==========================================
    # RANK 78: schützen
    # ==========================================
    {
        "verb_group": "schützen",
        "verb": "schützen",
        "prep": "vor",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to protect from / to shield against",
        "sentence_de": "Sonnencreme schützt die empfindliche Haut {PREP} gefährlichen Sonnenbränden.",
        "sentence_en": "Sunscreen protects sensitive skin from dangerous sunburns.",
        "question_structure": "Wovor? • Davor",
        "level": "A2",
        "grammar_notes": "Defense against an environmental threat or hazard.",
        "verb_rank": 78,
    },
    {
        "verb_group": "schützen",
        "verb": "schützen",
        "prep": "gegen",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to protect against (disease, attack)",
        "sentence_de": "Die Impfung schützt zuverlässig {PREP} eine schwere Infektion.",
        "sentence_en": "The vaccination reliably protects against severe infection.",
        "question_structure": "Wogegen? • Dagegen",
        "level": "B1",
        "grammar_notes": "Often used interchangeably with 'vor + Dat', especially in medical contexts.",
        "verb_rank": 78,
    },

    # ==========================================
    # RANK 79: sorgen
    # ==========================================
    {
        "verb_group": "sorgen",
        "verb": "sorgen",
        "prep": "für",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to provide for / to ensure / to take care of",
        "sentence_de": "Gute Musik sorgt {PREP} eine ausgelassene Stimmung.",
        "sentence_en": "Good music provides for a lively atmosphere.",
        "question_structure": "Wofür? • Dafür",
        "level": "A2",
        "grammar_notes": "Creating a condition or caring for dependents ('für die Kinder sorgen').",
        "verb_rank": 79,
    },
    {
        "verb_group": "sorgen",
        "verb": "sich sorgen",
        "prep": "um",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to worry about",
        "sentence_de": "Die Großmutter sorgt sich sehr {PREP} das Wohl ihrer Enkel.",
        "sentence_en": "The grandmother worries greatly about the well-being of her grandchildren.",
        "question_structure": "Worum? • Darum / Um wen?",
        "level": "B1",
        "grammar_notes": "Reflexive: 'sich sorgen um + Akk'. Synonymous with 'sich Sorgen machen um'.",
        "verb_rank": 79,
    },

    # ==========================================
    # RANK 80: sterben
    # ==========================================
    {
        "verb_group": "sterben",
        "verb": "sterben",
        "prep": "an",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to die of (a cause or illness)",
        "sentence_de": "Viele Patienten starben früher {PREP} einer einfachen Wundinfektion.",
        "sentence_en": "Many patients formerly died of a simple wound infection.",
        "question_structure": "Woran? • Daran",
        "level": "B1",
        "grammar_notes": "Cause of death takes 'an + Dativ'.",
        "verb_rank": 80,
    },

    # ==========================================
    # RANK 81: träumen
    # ==========================================
    {
        "verb_group": "träumen",
        "verb": "träumen",
        "prep": "von",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to dream of / about",
        "sentence_de": "Seit ihrer Kindheit träumt sie {PREP} einem eigenen Haus am Meer.",
        "sentence_en": "Since childhood she has been dreaming of her own house by the sea.",
        "question_structure": "Wovon? • Davon / Von wem?",
        "level": "A1",
        "grammar_notes": "Both nocturnal dreams and long-term aspirational wishes.",
        "verb_rank": 81,
    },

    # ==========================================
    # RANK 82: überzeugen
    # ==========================================
    {
        "verb_group": "überzeugen",
        "verb": "überzeugen",
        "prep": "von",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to convince of / to persuade of",
        "sentence_de": "Seine schlüssigen Argumente überzeugten uns {PREP} der Richtigkeit des Plans.",
        "sentence_en": "His coherent arguments convinced us of the correctness of the plan.",
        "question_structure": "Wovon? • Davon / Von wem?",
        "level": "B1",
        "grammar_notes": "Formula: jemanden (Akk) von etwas (Dat) überzeugen.",
        "verb_rank": 82,
    },

    # ==========================================
    # RANK 83: sich unterhalten
    # ==========================================
    {
        "verb_group": "sich unterhalten",
        "verb": "sich unterhalten",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to converse with / to chat with (someone)",
        "sentence_de": "Ich habe mich auf dem Empfang lange {PREP} dem Botschafter unterhalten.",
        "sentence_en": "At the reception, I chatted for a long time with the ambassador.",
        "question_structure": "Mit wem?",
        "level": "A2",
        "grammar_notes": "Partner in conversation: 'mit + Dativ'.",
        "verb_rank": 83,
    },
    {
        "verb_group": "sich unterhalten",
        "verb": "sich unterhalten",
        "prep": "über",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to converse about / to discuss (a topic)",
        "sentence_de": "Wir haben uns stundenlang {PREP} alte Erinnerungen unterhalten.",
        "sentence_en": "We chatted for hours about old memories.",
        "question_structure": "Worüber? • Darüber / Über wen?",
        "level": "A2",
        "grammar_notes": "Topic of conversation: 'über + Akkusativ'.",
        "verb_rank": 83,
    },

    # ==========================================
    # RANK 84: verbinden
    # ==========================================
    {
        "verb_group": "verbinden",
        "verb": "verbinden",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to connect with / to associate with",
        "sentence_de": "Mit diesem melancholischen Lied verbinde ich {PREP} meinen schönsten Sommer.",
        "sentence_en": "I associate this melancholic song with my most beautiful summer.",
        "question_structure": "Womit? • Damit / Mit wem?",
        "level": "B1",
        "grammar_notes": "Mental association or physical connection.",
        "verb_rank": 84,
    },

    # ==========================================
    # RANK 85: vergleichen
    # ==========================================
    {
        "verb_group": "vergleichen",
        "verb": "vergleichen",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to compare with",
        "sentence_de": "Man kann die Situation heute kaum {PREP} den Zuständen vor fünfzig Jahren vergleichen.",
        "sentence_en": "One can hardly compare the situation today with conditions fifty years ago.",
        "question_structure": "Womit? • Damit / Mit wem?",
        "level": "B1",
        "grammar_notes": "Drawing comparisons.",
        "verb_rank": 85,
    },

    # ==========================================
    # RANK 86: verzichten
    # ==========================================
    {
        "verb_group": "verzichten",
        "verb": "verzichten",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to do without / to forgo / to renounce",
        "sentence_de": "Er verzichtet während der Fastenzeit komplett {PREP} raffinierten Zucker.",
        "sentence_en": "During Lent, he completely gives up refined sugar.",
        "question_structure": "Worauf? • Darauf",
        "level": "B1",
        "grammar_notes": "Voluntarily giving up a privilege, habit, or item. Always 'auf + Akk'.",
        "verb_rank": 86,
    },

    # ==========================================
    # RANK 87: warnen
    # ==========================================
    {
        "verb_group": "warnen",
        "verb": "warnen",
        "prep": "vor",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to warn against / to alert to",
        "sentence_de": "Experten warnen eindringlich {PREP} den Folgen des Klimawandels.",
        "sentence_en": "Experts urgently warn against the consequences of climate change.",
        "question_structure": "Wovor? • Davor / Vor wem?",
        "level": "B1",
        "grammar_notes": "Formula: jemanden vor etwas (Dat) warnen.",
        "verb_rank": 87,
    },

    # ==========================================
    # RANK 88: sich wundern
    # ==========================================
    {
        "verb_group": "sich wundern",
        "verb": "sich wundern",
        "prep": "über",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to be surprised at / to wonder at",
        "sentence_de": "Ich wundere mich immer wieder {PREP} seine unglaubliche Energie.",
        "sentence_en": "I am repeatedly amazed at his incredible energy.",
        "question_structure": "Worüber? • Darüber / Über wen?",
        "level": "A2",
        "grammar_notes": "Surprise or bewilderment. Always 'über + Akkusativ'.",
        "verb_rank": 88,
    },

    # ==========================================
    # RANK 89: zusammenhängen
    # ==========================================
    {
        "verb_group": "zusammenhängen",
        "verb": "zusammenhängen",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to be connected with / to correlate with",
        "sentence_de": "Häufige Kopfschmerzen hängen oft eng {PREP} zu wenig Schlaf zusammen.",
        "sentence_en": "Frequent headaches are often closely linked to too little sleep.",
        "question_structure": "Womit? • Damit",
        "level": "B1",
        "grammar_notes": "Separable verb: 'zusammen|hängen mit + Dat'.",
        "verb_rank": 89,
    },

    # ==========================================
    # RANK 90: zwingen
    # ==========================================
    {
        "verb_group": "zwingen",
        "verb": "zwingen",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to force to / to compel to",
        "sentence_de": "Die schwere Verletzung zwang den Athleten {PREP} einem vorzeitigen Karriereende.",
        "sentence_en": "The severe injury forced the athlete to an early retirement.",
        "question_structure": "Wozu? • Dazu",
        "level": "B1",
        "grammar_notes": "Formula: jemanden zu etwas (Dat) zwingen.",
        "verb_rank": 90,
    },

    # ==========================================
    # RANK 91: anfangen
    # ==========================================
    {
        "verb_group": "anfangen",
        "verb": "anfangen",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to start with / to begin with",
        "sentence_de": "Wann fängst du endlich {PREP} der Vorbereitung auf das Examen an?",
        "sentence_en": "When will you finally start preparing for the exam?",
        "question_structure": "Womit? • Damit",
        "level": "A1",
        "grammar_notes": "Separable verb (fängt an; fing an; angefangen). Takes Dativ.",
        "verb_rank": 91,
    },

    # ==========================================
    # RANK 92: eingehen
    # ==========================================
    {
        "verb_group": "eingehen",
        "verb": "eingehen",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to address / to respond to / to agree to",
        "sentence_de": "Der Referent ging freundlich {PREP} alle Fragen des Publikums ein.",
        "sentence_en": "The speaker kindly addressed all questions from the audience.",
        "question_structure": "Worauf? • Darauf",
        "level": "B1",
        "grammar_notes": "Separable verb (auf etwas eingehen). Thorough response or consideration.",
        "verb_rank": 92,
    },

    # ==========================================
    # RANK 93: hinweisen
    # ==========================================
    {
        "verb_group": "hinweisen",
        "verb": "hinweisen",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to point out / to draw attention to",
        "sentence_de": "Das Schild weist die Autofahrer {PREP} die akute Rutschgefahr hin.",
        "sentence_en": "The sign alerts drivers to the acute danger of skidding.",
        "question_structure": "Worauf? • Darauf / Auf wen?",
        "level": "B1",
        "grammar_notes": "Separable verb (hin|weisen). Takes 'auf + Akkusativ'.",
        "verb_rank": 93,
    },

    # ==========================================
    # RANK 94: hören
    # ==========================================
    {
        "verb_group": "hören",
        "verb": "hören",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to listen to / to obey (advice, a person)",
        "sentence_de": "Der sture Junge will einfach nicht {PREP} den Rat seiner Eltern hören.",
        "sentence_en": "The stubborn boy simply does not want to listen to his parents' advice.",
        "question_structure": "Worauf? • Darauf / Auf wen?",
        "level": "A2",
        "grammar_notes": "Heeding instructions or following advice.",
        "verb_rank": 94,
    },
    {
        "verb_group": "hören",
        "verb": "hören",
        "prep": "von",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to hear from / about (someone/something)",
        "sentence_de": "Hast du in letzter Zeit etwas Neues {PREP} deinem Schulfreund gehört?",
        "sentence_en": "Have you heard anything new from your school friend lately?",
        "question_structure": "Wovon? • Davon / Von wem?",
        "level": "A1",
        "grammar_notes": "Receiving news or updates.",
        "verb_rank": 94,
    },

    # ==========================================
    # RANK 95: kämpfen
    # ==========================================
    {
        "verb_group": "kämpfen",
        "verb": "kämpfen",
        "prep": "für",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to fight for (a cause, justice, freedom)",
        "sentence_de": "Aktivisten kämpfen unermüdlich {PREP} eine gerechtere Welt.",
        "sentence_en": "Activists fight tirelessly for a more just world.",
        "question_structure": "Wofür? • Dafür / Für wen?",
        "level": "A2",
        "grammar_notes": "Fighting in support of a goal.",
        "verb_rank": 95,
    },
    {
        "verb_group": "kämpfen",
        "verb": "kämpfen",
        "prep": "gegen",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to fight against (an enemy, injustice, disease)",
        "sentence_de": "Die Ärzte kämpfen mit allen Mitteln {PREP} die heimtückische Krankheit.",
        "sentence_en": "Doctors are fighting by all means against the insidious disease.",
        "question_structure": "Wogegen? • Dagegen / Gegen wen?",
        "level": "A2",
        "grammar_notes": "Opposing or battling a threat.",
        "verb_rank": 95,
    },
    {
        "verb_group": "kämpfen",
        "verb": "kämpfen",
        "prep": "um",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to fight over / for (survival, a trophy, custody)",
        "sentence_de": "Die beiden Finalisten kämpfen verbissen {PREP} den begehrten Pokal.",
        "sentence_en": "Both finalists are fighting fiercely for the coveted trophy.",
        "question_structure": "Worum? • Darum",
        "level": "B1",
        "grammar_notes": "Contesting or struggling to obtain/retain an object or state.",
        "verb_rank": 95,
    },

    # ==========================================
    # RANK 96: klarkommen
    # ==========================================
    {
        "verb_group": "klarkommen",
        "verb": "klarkommen",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to cope with / to manage / to get along with",
        "sentence_de": "Kommst du im Alltag gut {PREP} deinem neuen Vorgesetzten klar?",
        "sentence_en": "Do you get along well with your new supervisor in daily life?",
        "question_structure": "Womit? • Damit / Mit wem?",
        "level": "A2",
        "grammar_notes": "Separable colloquial idiom: 'klar|kommen mit + Dat'.",
        "verb_rank": 96,
    },

    # ==========================================
    # RANK 97: mangeln
    # ==========================================
    {
        "verb_group": "mangeln",
        "verb": "mangeln",
        "prep": "an",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to lack / to be wanting in",
        "sentence_de": "Dem jungen Start-up mangelt es vor allem {PREP} ausreichendem Kapital.",
        "sentence_en": "The young start-up primarily lacks sufficient capital.",
        "question_structure": "Woran? • Daran",
        "level": "B1",
        "grammar_notes": "Impersonal: 'Es mangelt an + Dat'. Similar to 'fehlen an'.",
        "verb_rank": 97,
    },

    # ==========================================
    # RANK 98: profitieren
    # ==========================================
    {
        "verb_group": "profitieren",
        "verb": "profitieren",
        "prep": "von",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to profit from / to benefit from",
        "sentence_de": "Beide Unternehmen profitieren enorm {PREP} der neuen Partnerschaft.",
        "sentence_en": "Both companies benefit enormously from the new partnership.",
        "question_structure": "Wovon? • Davon / Von wem?",
        "level": "B1",
        "grammar_notes": "Gaining an advantage from a situation.",
        "verb_rank": 98,
    },

    # ==========================================
    # RANK 99: sich rächen
    # ==========================================
    {
        "verb_group": "sich rächen",
        "verb": "sich rächen",
        "prep": "an",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to take revenge on (a person)",
        "sentence_de": "Er schwor, sich eines Tages {PREP} seinem Verräter zu rächen.",
        "sentence_en": "He swore to take revenge on his betrayer one day.",
        "question_structure": "An wem?",
        "level": "B2",
        "grammar_notes": "The target of revenge takes 'an + Dativ'.",
        "verb_rank": 99,
    },
    {
        "verb_group": "sich rächen",
        "verb": "sich rächen",
        "prep": "für",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to take revenge for (an offense or wrong)",
        "sentence_de": "Sie wollte sich {PREP} die schwere Demütigung rächen.",
        "sentence_en": "She wanted to avenge the severe humiliation.",
        "question_structure": "Wofür? • Dafür",
        "level": "B2",
        "grammar_notes": "The reason or grievance takes 'für + Akkusativ'.",
        "verb_rank": 99,
    },

    # ==========================================
    # RANK 100: raten
    # ==========================================
    {
        "verb_group": "raten",
        "verb": "raten",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to advise to / to recommend",
        "sentence_de": "Der Arzt riet ihm dringend {PREP} einer sofortigen Kur.",
        "sentence_en": "The doctor urgently advised him to take an immediate spa cure.",
        "question_structure": "Wozu? • Dazu",
        "level": "B1",
        "grammar_notes": "Formula: jemandem (Dat) zu etwas (Dat) raten.",
        "verb_rank": 100,
    },

    # ==========================================
    # RANK 101: richten
    # ==========================================
    {
        "verb_group": "richten",
        "verb": "richten",
        "prep": "an",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to address to / to direct toward (an audience)",
        "sentence_de": "Die Worte der Kanzlerin richteten sich {PREP} das gesamte Volk.",
        "sentence_en": "The Chancellor's words were addressed to the entire nation.",
        "question_structure": "An wen?",
        "level": "B1",
        "grammar_notes": "The target audience takes 'an + Akkusativ'.",
        "verb_rank": 101,
    },
    {
        "verb_group": "richten",
        "verb": "sich richten",
        "prep": "nach",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to conform to / to be guided by / to depend on",
        "sentence_de": "Der genaue Preis richtet sich {PREP} der gewünschten Ausstattung.",
        "sentence_en": "The exact price depends on the desired equipment.",
        "question_structure": "Wonach? • Danach",
        "level": "B1",
        "grammar_notes": "Conforming or tailoring to criteria.",
        "verb_rank": 101,
    },

    # ==========================================
    # RANK 102: schimpfen
    # ==========================================
    {
        "verb_group": "schimpfen",
        "verb": "schimpfen",
        "prep": "über",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to rant about / to grumble about",
        "sentence_de": "Die Pendler schimpfen täglich {PREP} die unpünktlichen Züge.",
        "sentence_en": "Commuters rant daily about the unpunctual trains.",
        "question_structure": "Worüber? • Darüber / Über wen?",
        "level": "A2",
        "grammar_notes": "Venting frustration about a situation.",
        "verb_rank": 102,
    },
    {
        "verb_group": "schimpfen",
        "verb": "schimpfen",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to scold / to tell off (a person)",
        "sentence_de": "Die Mutter schimpfte {PREP} ihrem unartigen Sohn.",
        "sentence_en": "The mother scolded her naughty son.",
        "question_structure": "Mit wem?",
        "level": "A2",
        "grammar_notes": "Direct reprimand to a person.",
        "verb_rank": 102,
    },

    # ==========================================
    # RANK 103: schließen
    # ==========================================
    {
        "verb_group": "schließen",
        "verb": "schließen",
        "prep": "aus",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to deduce from / to conclude from",
        "sentence_de": "Aus diesen Befunden schließt der Ermittler {PREP} den genauen Tathergang.",
        "sentence_en": "From these findings, the investigator deduces the exact sequence of events.",
        "question_structure": "Woraus? • Daraus",
        "level": "B1",
        "grammar_notes": "Logical deduction based on evidence.",
        "verb_rank": 103,
    },

    # ==========================================
    # RANK 104: sich sehnen
    # ==========================================
    {
        "verb_group": "sich sehnen",
        "verb": "sich sehnen",
        "prep": "nach",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to long for / to yearn for",
        "sentence_de": "Im kalten und dunklen Winter sehnt er sich {PREP} Wärme und Licht.",
        "sentence_en": "In the cold and dark winter, he yearns for warmth and light.",
        "question_structure": "Wonach? • Danach / Nach wem?",
        "level": "B1",
        "grammar_notes": "Deep emotional longing. Always 'nach + Dativ'.",
        "verb_rank": 104,
    },

    # ==========================================
    # RANK 105: siegen
    # ==========================================
    {
        "verb_group": "siegen",
        "verb": "siegen",
        "prep": "über",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to triumph over / to defeat",
        "sentence_de": "Am Ende siegte die Gerechtigkeit {PREP} die Willkür.",
        "sentence_en": "In the end, justice triumphed over arbitrariness.",
        "question_structure": "Worüber? • Darüber / Über wen?",
        "level": "B2",
        "grammar_notes": "Victory over an adversary or difficulty.",
        "verb_rank": 105,
    },

    # ==========================================
    # RANK 106: stimmen
    # ==========================================
    {
        "verb_group": "stimmen",
        "verb": "stimmen",
        "prep": "für",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to vote in favor of",
        "sentence_de": "Die Abgeordneten stimmten mit großer Mehrheit {PREP} den Gesetzentwurf.",
        "sentence_en": "The deputies voted by a large majority in favor of the bill.",
        "question_structure": "Wofür? • Dafür / Für wen?",
        "level": "B1",
        "grammar_notes": "Democratic ballot/vote in favor.",
        "verb_rank": 106,
    },
    {
        "verb_group": "stimmen",
        "verb": "stimmen",
        "prep": "gegen",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to vote against",
        "sentence_de": "Nur zwei Parteimitglieder stimmten {PREP} den Beschluss.",
        "sentence_en": "Only two party members voted against the resolution.",
        "question_structure": "Wogegen? • Dagegen / Gegen wen?",
        "level": "B1",
        "grammar_notes": "Democratic ballot/vote against.",
        "verb_rank": 106,
    },

    # ==========================================
    # RANK 107: streiten
    # ==========================================
    {
        "verb_group": "streiten",
        "verb": "streiten",
        "prep": "über",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to argue / quarrel about (a topic)",
        "sentence_de": "Die Politiker streiten leidenschaftlich {PREP} die richtige Steuerreform.",
        "sentence_en": "The politicians are passionately arguing about the right tax reform.",
        "question_structure": "Worüber? • Darüber",
        "level": "A2",
        "grammar_notes": "Topic of the dispute takes 'über + Akkusativ'.",
        "verb_rank": 107,
    },
    {
        "verb_group": "streiten",
        "verb": "streiten",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to argue with (a person)",
        "sentence_de": "Ich habe keine Lust, mich ständig {PREP} dir zu streiten.",
        "sentence_en": "I have no desire to constantly argue with you.",
        "question_structure": "Mit wem?",
        "level": "A2",
        "grammar_notes": "Opponent in the dispute takes 'mit + Dativ'.",
        "verb_rank": 107,
    },
    {
        "verb_group": "streiten",
        "verb": "streiten",
        "prep": "um",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to dispute over / to contest (property, possession)",
        "sentence_de": "Die zerstrittenen Geschwister streiten {PREP} das Erbe der Eltern.",
        "sentence_en": "The estranged siblings are quarreling over the parents' inheritance.",
        "question_structure": "Worum? • Darum",
        "level": "B1",
        "grammar_notes": "Contesting ownership or control of an asset.",
        "verb_rank": 107,
    },

    # ==========================================
    # RANK 108: taugen
    # ==========================================
    {
        "verb_group": "taugen",
        "verb": "taugen",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to be fit for / to be good for",
        "sentence_de": "Dieses alte, stumpfe Messer taugt nicht mehr {PREP} Schneiden von Fleisch.",
        "sentence_en": "This old, blunt knife is no longer good for cutting meat.",
        "question_structure": "Wozu? • Dazu",
        "level": "B2",
        "grammar_notes": "Suitability or utility: 'taugen zu + Dat'.",
        "verb_rank": 108,
    },

    # ==========================================
    # RANK 109: überreden
    # ==========================================
    {
        "verb_group": "überreden",
        "verb": "überreden",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to persuade into / to talk someone into",
        "sentence_de": "Sie überredete ihren Freund {PREP} einem gemeinsamen Tanzkurs.",
        "sentence_en": "She talked her boyfriend into taking a dance course together.",
        "question_structure": "Wozu? • Dazu",
        "level": "B1",
        "grammar_notes": "Formula: jemanden (Akk) zu etwas (Dat) überreden.",
        "verb_rank": 109,
    },

    # ==========================================
    # RANK 110: urteilen
    # ==========================================
    {
        "verb_group": "urteilen",
        "verb": "urteilen",
        "prep": "über",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to pass judgment on / to judge",
        "sentence_de": "Niemand sollte vorschnell {PREP} andere Menschen urteilen.",
        "sentence_en": "Nobody should judge other people hastily.",
        "question_structure": "Worüber? • Darüber / Über wen?",
        "level": "B2",
        "grammar_notes": "Making an evaluation or moral assessment.",
        "verb_rank": 110,
    },
    {
        "verb_group": "urteilen",
        "verb": "urteilen",
        "prep": "nach",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to judge according to / by",
        "sentence_de": "Man darf Personen niemals nur {PREP} ihrem äußeren Anschein beurteilen.",
        "sentence_en": "One must never judge persons solely by their outward appearance.",
        "question_structure": "Wonach? • Danach",
        "level": "B2",
        "grammar_notes": "The criteria or basis of judgment takes 'nach + Dativ'.",
        "verb_rank": 110,
    },

    # ==========================================
    # RANK 111: verführen
    # ==========================================
    {
        "verb_group": "verführen",
        "verb": "verführen",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to entice / seduce into",
        "sentence_de": "Die ständigen Sonderangebote verführten ihn {PREP} unnötigen Ausgaben.",
        "sentence_en": "The constant special offers seduced him into unnecessary spending.",
        "question_structure": "Wozu? • Dazu",
        "level": "B2",
        "grammar_notes": "Tempting someone to do something unwise or illicit.",
        "verb_rank": 111,
    },

    # ==========================================
    # RANK 112: verhandeln
    # ==========================================
    {
        "verb_group": "verhandeln",
        "verb": "verhandeln",
        "prep": "über",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to negotiate about (wages, conditions)",
        "sentence_de": "Die Gewerkschaft verhandelt derzeit {PREP} eine spürbare Lohnerhöhung.",
        "sentence_en": "The union is currently negotiating for a noticeable pay raise.",
        "question_structure": "Worüber? • Darüber",
        "level": "B1",
        "grammar_notes": "Negotiation topic takes 'über + Akkusativ'.",
        "verb_rank": 112,
    },
    {
        "verb_group": "verhandeln",
        "verb": "verhandeln",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to negotiate with (a party, representative)",
        "sentence_de": "Die Firmenleitung verhandelt direkt {PREP} dem Betriebsrat.",
        "sentence_en": "Management is negotiating directly with the works council.",
        "question_structure": "Mit wem?",
        "level": "B1",
        "grammar_notes": "Negotiation partner takes 'mit + Dativ'.",
        "verb_rank": 112,
    },

    # ==========================================
    # RANK 113: verlangen
    # ==========================================
    {
        "verb_group": "verlangen",
        "verb": "verlangen",
        "prep": "nach",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to crave / to call for / to yearn for",
        "sentence_de": "Nach stundenlanger Wanderung in der Hitze verlangte sein Körper {PREP} kaltem Wasser.",
        "sentence_en": "After hours of hiking in the heat, his body craved cold water.",
        "question_structure": "Wonach? • Danach / Nach wem?",
        "level": "B2",
        "grammar_notes": "Strong physical or psychological craving. Always 'nach + Dativ'.",
        "verb_rank": 113,
    },

    # ==========================================
    # RANK 114: verstoßen
    # ==========================================
    {
        "verb_group": "verstoßen",
        "verb": "verstoßen",
        "prep": "gegen",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to violate / to offend against (laws, regulations)",
        "sentence_de": "Dieses illegale Verhalten verstößt eindeutig {PREP} geltendes Recht.",
        "sentence_en": "This illegal behavior clearly violates applicable law.",
        "question_structure": "Wogegen? • Dagegen",
        "level": "B2",
        "grammar_notes": "Breaching rules or ethical codes. Always 'gegen + Akkusativ'.",
        "verb_rank": 114,
    },

    # ==========================================
    # RANK 115: sich vertiefen
    # ==========================================
    {
        "verb_group": "sich vertiefen",
        "verb": "sich vertiefen",
        "prep": "in",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to immerse oneself in / to become engrossed in",
        "sentence_de": "Sie vertiefte sich völlig {PREP} das fesselnde Geschichtsbuch.",
        "sentence_en": "She immersed herself completely in the captivating history book.",
        "question_structure": "Worin? • Darin",
        "level": "B2",
        "grammar_notes": "Total absorption in study or reading. Takes 'in + Akkusativ'.",
        "verb_rank": 115,
    },

    # ==========================================
    # RANK 116: wählen
    # ==========================================
    {
        "verb_group": "wählen",
        "verb": "wählen",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to elect as / to choose as",
        "sentence_de": "Die Mitglieder wählten sie einstimmig {PREP} neuen Vorsitzenden.",
        "sentence_en": "The members unanimously elected her as the new chairperson.",
        "question_structure": "Wozu? • Dazu / Zu wem?",
        "level": "B1",
        "grammar_notes": "Formula: jemanden (Akk) zu etwas (Dat) wählen.",
        "verb_rank": 116,
    },

    # ==========================================
    # RANK 117: sich wenden
    # ==========================================
    {
        "verb_group": "sich wenden",
        "verb": "sich wenden",
        "prep": "an",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to turn to / to consult / to contact",
        "sentence_de": "Bei rechtlichen Fragen sollten Sie sich sofort {PREP} einen Fachanwalt wenden.",
        "sentence_en": "For legal questions you should immediately turn to a specialist lawyer.",
        "question_structure": "An wen?",
        "level": "B1",
        "grammar_notes": "Seeking assistance or counsel from someone.",
        "verb_rank": 117,
    },
    {
        "verb_group": "sich wenden",
        "verb": "sich wenden",
        "prep": "gegen",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to turn against / to oppose",
        "sentence_de": "Die öffentliche Kritik wendet sich nun scharf {PREP} die Entscheidungsträger.",
        "sentence_en": "Public criticism is now turning sharply against the decision-makers.",
        "question_structure": "Wogegen? • Dagegen / Gegen wen?",
        "level": "B2",
        "grammar_notes": "Taking an adversarial stance against someone/something.",
        "verb_rank": 117,
    },

    # ==========================================
    # RANK 118: werben
    # ==========================================
    {
        "verb_group": "werben",
        "verb": "werben",
        "prep": "für",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to advertise / to promote / to campaign for",
        "sentence_de": "Das Unternehmen wirbt intensiv {PREP} seine neue Produktlinie.",
        "sentence_en": "The company advertises intensively for its new product line.",
        "question_structure": "Wofür? • Dafür",
        "level": "B1",
        "grammar_notes": "Commercial promotion or advocating an idea.",
        "verb_rank": 118,
    },
    {
        "verb_group": "werben",
        "verb": "werben",
        "prep": "um",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to court / to solicit / to vie for",
        "sentence_de": "Internationale Universitäten werben eifrig {PREP} talentierte Nachwuchsforscher.",
        "sentence_en": "International universities eagerly vie for talented young researchers.",
        "question_structure": "Worum? • Darum / Um wen?",
        "level": "B2",
        "grammar_notes": "Wooing or courting favor/people.",
        "verb_rank": 118,
    },

    # ==========================================
    # RANK 119: wirken
    # ==========================================
    {
        "verb_group": "wirken",
        "verb": "wirken",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to have an effect on / to make an impression on",
        "sentence_de": "Die sanfte Melodie wirkt überaus beruhigend {PREP} gestresste Gemüter.",
        "sentence_en": "The gentle melody has an exceedingly calming effect on stressed minds.",
        "question_structure": "Worauf? • Darauf / Auf wen?",
        "level": "B1",
        "grammar_notes": "Psychological or physical effect on someone.",
        "verb_rank": 119,
    },

    # ==========================================
    # RANK 120: zählen
    # ==========================================
    {
        "verb_group": "zählen",
        "verb": "zählen",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to count among / to rank among",
        "sentence_de": "Diese Entdeckung zählt zweifellos {PREP} den größten Meilensteinen der Medizin.",
        "sentence_en": "This discovery undoubtedly counts among the greatest milestones in medicine.",
        "question_structure": "Wozu? • Dazu",
        "level": "B1",
        "grammar_notes": "Category membership or prestige ranking.",
        "verb_rank": 120,
    },
    {
        "verb_group": "zählen",
        "verb": "zählen",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to count on / to rely on",
        "sentence_de": "In schwierigen Zeiten kann ich mich immer {PREP} meine treuen Freunde verlassen und auf sie zählen.",
        "sentence_en": "In difficult times I can always count on my loyal friends.",
        "question_structure": "Worauf? • Darauf / Auf wen?",
        "level": "B1",
        "grammar_notes": "Synonymous with 'sich verlassen auf + Akk'.",
        "verb_rank": 120,
    },

    # ==========================================
    # RANK 121: zögern
    # ==========================================
    {
        "verb_group": "zögern",
        "verb": "zögern",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to hesitate with / to delay doing",
        "sentence_de": "Bitte zögern Sie nicht {PREP} Ihrer Rückmeldung!",
        "sentence_en": "Please do not hesitate with your feedback!",
        "question_structure": "Womit? • Damit",
        "level": "B1",
        "grammar_notes": "Polite business correspondence: 'Zögern Sie nicht mit...' or infinitive clause.",
        "verb_rank": 121,
    },

    # ==========================================
    # RANK 122: zurückführen
    # ==========================================
    {
        "verb_group": "zurückführen",
        "verb": "zurückführen",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to attribute to / to trace back to",
        "sentence_de": "Die Experten führen den Kursabsturz {PREP} weltweite Unsicherheiten zurück.",
        "sentence_en": "The experts trace the price crash back to global uncertainties.",
        "question_structure": "Worauf? • Darauf",
        "level": "B2",
        "grammar_notes": "Separable verb: 'etwas (Akk) zurückführen auf + Akk'. Causal attribution.",
        "verb_rank": 122,
    },

    # ==========================================
    # RANK 123: ausmachen
    # ==========================================
    {
        "verb_group": "ausmachen",
        "verb": "ausmachen",
        "prep": "mit",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to agree on / to settle with (a person)",
        "sentence_de": "Ich habe den genauen Liefertermin {PREP} dem Spediteur ausgemacht.",
        "sentence_en": "I settled on the exact delivery date with the freight forwarder.",
        "question_structure": "Mit wem?",
        "level": "B1",
        "grammar_notes": "Mutual agreement or arrangement.",
        "verb_rank": 123,
    },

    # ==========================================
    # RANK 124: bürgen
    # ==========================================
    {
        "verb_group": "bürgen",
        "verb": "bürgen",
        "prep": "für",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to vouch for / to guarantee",
        "sentence_de": "Der wohlhabende Onkel bürgt {PREP} den Bankkredit seines Neffen.",
        "sentence_en": "The wealthy uncle vouches for his nephew's bank loan.",
        "question_structure": "Wofür? • Dafür / Für wen?",
        "level": "B2",
        "grammar_notes": "Legal or personal guarantee.",
        "verb_rank": 124,
    },

    # ==========================================
    # RANK 125: dienen
    # ==========================================
    {
        "verb_group": "dienen",
        "verb": "dienen",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to serve for / to be used for (purpose)",
        "sentence_de": "Dieses spezielle Werkzeug dient {PREP} schnellen Öffnen von Dosen.",
        "sentence_en": "This special tool serves for opening cans quickly.",
        "question_structure": "Wozu? • Dazu",
        "level": "B1",
        "grammar_notes": "Designated functional purpose.",
        "verb_rank": 125,
    },
    {
        "verb_group": "dienen",
        "verb": "dienen",
        "prep": "als",
        "case": "+ Nom.",
        "case_type": "nom",
        "meaning_en": "to serve as (a role or substitute)",
        "sentence_de": "Das bequeme Sofa dient nachts {PREP} gemütliches Gästebett.",
        "sentence_en": "The comfortable couch serves as a cozy guest bed at night.",
        "question_structure": "Als was?",
        "level": "B1",
        "grammar_notes": "'Als' takes Nominative agreeing with the subject.",
        "verb_rank": 125,
    },

    # ==========================================
    # RANK 126: sich eignen
    # ==========================================
    {
        "verb_group": "sich eignen",
        "verb": "sich eignen",
        "prep": "für",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to be suitable for (a target audience or role)",
        "sentence_de": "Dieses spannende Buch eignet sich hervorragend {PREP} Sprachanfänger.",
        "sentence_en": "This exciting book is wonderfully suitable for language beginners.",
        "question_structure": "Wofür? • Dafür / Für wen?",
        "level": "B1",
        "grammar_notes": "Target audience suitability.",
        "verb_rank": 126,
    },
    {
        "verb_group": "sich eignen",
        "verb": "sich eignen",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to be suitable for (an action or function)",
        "sentence_de": "Das robuste Holz eignet sich bestens {PREP} Bau von Gartenmöbeln.",
        "sentence_en": "The sturdy wood is best suited for building garden furniture.",
        "question_structure": "Wozu? • Dazu",
        "level": "B1",
        "grammar_notes": "Task or utility suitability (often nominalized verbs: zum Kochen, zum Bau).",
        "verb_rank": 126,
    },

    # ==========================================
    # RANK 127: sich ekeln
    # ==========================================
    {
        "verb_group": "sich ekeln",
        "verb": "sich ekeln",
        "prep": "vor",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to be disgusted by / repulsed by",
        "sentence_de": "Er ekelt sich furchtbar {PREP} kriechenden Würmern.",
        "sentence_en": "He is terribly disgusted by crawling worms.",
        "question_structure": "Wovor? • Davor",
        "level": "B2",
        "grammar_notes": "Always 'vor + Dativ'.",
        "verb_rank": 127,
    },

    # ==========================================
    # RANK 128: feilschen
    # ==========================================
    {
        "verb_group": "feilschen",
        "verb": "feilschen",
        "prep": "um",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to haggle / bargain over",
        "sentence_de": "Auf dem bunten Trödelmarkt feilscht man gern {PREP} jeden einzelnen Euro.",
        "sentence_en": "At the colorful flea market, people gladly haggle over every single euro.",
        "question_structure": "Worum? • Darum",
        "level": "B2",
        "grammar_notes": "Price negotiation. Takes 'um + Akkusativ'.",
        "verb_rank": 128,
    },

    # ==========================================
    # RANK 129: fliehen
    # ==========================================
    {
        "verb_group": "fliehen",
        "verb": "fliehen",
        "prep": "vor",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to flee from / to escape from",
        "sentence_de": "Tausende Menschen flohen {PREP} den verheerenden Flammen des Waldbrands.",
        "sentence_en": "Thousands of people fled from the devastating flames of the wildfire.",
        "question_structure": "Wovor? • Davor / Vor wem?",
        "level": "B1",
        "grammar_notes": "Escape from danger: 'vor + Dativ'.",
        "verb_rank": 129,
    },

    # ==========================================
    # RANK 130: geraten
    # ==========================================
    {
        "verb_group": "geraten",
        "verb": "geraten",
        "prep": "in",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to get into / to fall into (trouble, panic, danger)",
        "sentence_de": "Das Unternehmen geriet durch Fehlinvestitionen {PREP} große finanzielle Not.",
        "sentence_en": "The company got into great financial distress through bad investments.",
        "question_structure": "Worin? • Darin",
        "level": "B2",
        "grammar_notes": "Unintentionally entering a difficult state (in Panik geraten, in Wut geraten). Takes Akkusativ.",
        "verb_rank": 130,
    },

    # ==========================================
    # RANK 131: hindern
    # ==========================================
    {
        "verb_group": "hindern",
        "verb": "hindern",
        "prep": "an",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to prevent from / to hinder from",
        "sentence_de": "Starker Nebel hinderte die Piloten {PREP} einem sicheren Landeanflug.",
        "sentence_en": "Heavy fog prevented the pilots from a safe landing approach.",
        "question_structure": "Woran? • Daran",
        "level": "B1",
        "grammar_notes": "Formula: jemanden (Akk) an etwas (Dat) hindern.",
        "verb_rank": 131,
    },

    # ==========================================
    # RANK 132: sich schämen
    # ==========================================
    {
        "verb_group": "sich schämen",
        "verb": "sich schämen",
        "prep": "für",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to be ashamed of (an action or behavior)",
        "sentence_de": "Er schämte sich zutiefst {PREP} seine ungehobelten Worte.",
        "sentence_en": "He was deeply ashamed of his rude words.",
        "question_structure": "Wofür? • Dafür",
        "level": "B1",
        "grammar_notes": "Reason for shame takes 'für + Akkusativ'.",
        "verb_rank": 132,
    },
    {
        "verb_group": "sich schämen",
        "verb": "sich schämen",
        "prep": "vor",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to be ashamed in front of (a person)",
        "sentence_de": "Das Mädchen schämte sich {PREP} den fremden Gästen und versteckte sich.",
        "sentence_en": "The girl was ashamed in front of the unfamiliar guests and hid.",
        "question_structure": "Vor wem?",
        "level": "B1",
        "grammar_notes": "Person in whose presence one feels ashamed takes 'vor + Dativ'.",
        "verb_rank": 132,
    },

    # ==========================================
    # RANK 133: beruhen
    # ==========================================
    {
        "verb_group": "beruhen",
        "verb": "beruhen",
        "prep": "auf",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to be based on / to rest upon (facts, principles)",
        "sentence_de": "Die wissenschaftliche These beruht {PREP} verlässlichen Experimenten.",
        "sentence_en": "The scientific thesis is based on reliable experiments.",
        "question_structure": "Worauf? • Darauf",
        "level": "B2",
        "grammar_notes": "Takes Dativ (unlike 'hoffen auf' or 'warten auf'!). Formal and academic.",
        "verb_rank": 133,
    },

    # ==========================================
    # RANK 134: basieren
    # ==========================================
    {
        "verb_group": "basieren",
        "verb": "basieren",
        "prep": "auf",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to be based on",
        "sentence_de": "Der erfolgreiche Film basiert {PREP} einer wahren Begebenheit.",
        "sentence_en": "The successful movie is based on a true story.",
        "question_structure": "Worauf? • Darauf",
        "level": "B1",
        "grammar_notes": "Takes Dativ ('auf + Dat'). Very common in journalism and academia.",
        "verb_rank": 134,
    },

    # ==========================================
    # RANK 135: anknüpfen
    # ==========================================
    {
        "verb_group": "anknüpfen",
        "verb": "anknüpfen",
        "prep": "an",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to tie in with / to build upon (earlier progress/ideas)",
        "sentence_de": "Wir möchten heute direkt {PREP} die Diskussion der letzten Woche anknüpfen.",
        "sentence_en": "Today we would like to tie directly into last week's discussion.",
        "question_structure": "Woran? • Daran",
        "level": "B2",
        "grammar_notes": "Separable verb: an|knüpfen an + Akk.",
        "verb_rank": 135,
    },

    # ==========================================
    # RANK 136: abstimmen
    # ==========================================
    {
        "verb_group": "abstimmen",
        "verb": "abstimmen",
        "prep": "über",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to vote on (a motion or proposal)",
        "sentence_de": "Die Vereinsmitglieder stimmen heute {PREP} den neuen Mitgliedsbeitrag ab.",
        "sentence_en": "The club members are voting today on the new membership fee.",
        "question_structure": "Worüber? • Darüber",
        "level": "B1",
        "grammar_notes": "Voting procedure.",
        "verb_rank": 136,
    },
    {
        "verb_group": "abstimmen",
        "verb": "abstimmen",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to coordinate / tune / tailor to",
        "sentence_de": "Das Vier-Gänge-Menü ist exakt {PREP} die erlesenen Weine abgestimmt.",
        "sentence_en": "The four-course menu is precisely matched to the exquisite wines.",
        "question_structure": "Worauf? • Darauf",
        "level": "B2",
        "grammar_notes": "Harmonizing or tailoring one element to another.",
        "verb_rank": 136,
    },

    # ==========================================
    # RANK 137: anregen
    # ==========================================
    {
        "verb_group": "anregen",
        "verb": "anregen",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to stimulate / prompt / inspire to",
        "sentence_de": "Das nachdenkliche Theaterstück regte die Zuschauer {PREP} langen Diskussionen an.",
        "sentence_en": "The thoughtful play stimulated the audience to long discussions.",
        "question_structure": "Wozu? • Dazu",
        "level": "B2",
        "grammar_notes": "Incentivizing thought or action (anregen zum Nachdenken).",
        "verb_rank": 137,
    },

    # ==========================================
    # RANK 138: auffordern
    # ==========================================
    {
        "verb_group": "auffordern",
        "verb": "auffordern",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to call upon / urge / request someone to",
        "sentence_de": "Die Flugbegleiterin forderte die Passagiere {PREP} Anschnallen auf.",
        "sentence_en": "The flight attendant called upon passengers to fasten their seatbelts.",
        "question_structure": "Wozu? • Dazu",
        "level": "B1",
        "grammar_notes": "Formula: jemanden (Akk) zu etwas (Dat) auffordern.",
        "verb_rank": 138,
    },

    # ==========================================
    # RANK 139: beharren
    # ==========================================
    {
        "verb_group": "beharren",
        "verb": "beharren",
        "prep": "auf",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to persist in / to stubbornly insist on",
        "sentence_de": "Er beharrte stur {PREP} seiner einmal gefassten Meinung.",
        "sentence_en": "He stubbornly persisted in his once-formed opinion.",
        "question_structure": "Worauf? • Darauf",
        "level": "B2",
        "grammar_notes": "Takes Dativ ('auf + Dat'). Connotes obstinacy or unwavering persistence.",
        "verb_rank": 139,
    },

    # ==========================================
    # RANK 140: beneiden
    # ==========================================
    {
        "verb_group": "beneiden",
        "verb": "beneiden",
        "prep": "um",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to envy for",
        "sentence_de": "Viele seiner Kollegen beneiden ihn {PREP} seine beneidenswerte Gelassenheit.",
        "sentence_en": "Many of his colleagues envy him for his enviable serenity.",
        "question_structure": "Worum? • Darum / Um wen?",
        "level": "B2",
        "grammar_notes": "Formula: jemanden (Akk) um etwas (Akk) beneiden.",
        "verb_rank": 140,
    },

    # ==========================================
    # RANK 141: drängen
    # ==========================================
    {
        "verb_group": "drängen",
        "verb": "drängen",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to press for / to urge (a quick decision or action)",
        "sentence_de": "Die Kunden drängen ungeduldig {PREP} eine rasche Behebung der Störung.",
        "sentence_en": "The customers are impatiently pressing for a prompt resolution to the outage.",
        "question_structure": "Worauf? • Darauf",
        "level": "B2",
        "grammar_notes": "Urgency and pressure. Takes 'auf + Akkusativ'.",
        "verb_rank": 141,
    },

    # ==========================================
    # RANK 142: wetteifern
    # ==========================================
    {
        "verb_group": "wetteifern",
        "verb": "wetteifern",
        "prep": "um",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to compete for / to vie for",
        "sentence_de": "Die begabten Athleten wetteifern ehrgeizig {PREP} den ersten Platz.",
        "sentence_en": "The talented athletes ambitiously vie for first place.",
        "question_structure": "Worum? • Darum",
        "level": "C1",
        "grammar_notes": "Elevated vocabulary for fierce competition over an accolade.",
        "verb_rank": 142,
    },

    # ==========================================
    # RANK 143: zulassen
    # ==========================================
    {
        "verb_group": "zulassen",
        "verb": "zulassen",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to admit to / to qualify for (an exam or study program)",
        "sentence_de": "Nach Prüfung der Unterlagen wurde sie {PREP} den Staatsprüfungen zugelassen.",
        "sentence_en": "After reviewing the documents, she was admitted to the state examinations.",
        "question_structure": "Wozu? • Dazu",
        "level": "B2",
        "grammar_notes": "Official admission or licensing.",
        "verb_rank": 143,
    },

    # ==========================================
    # RANK 144: zurückschrecken
    # ==========================================
    {
        "verb_group": "zurückschrecken",
        "verb": "zurückschrecken",
        "prep": "vor",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to shrink back from / to recoil from (a danger or obstacle)",
        "sentence_de": "Ein entschlossener Bergsteiger schreckt nicht {PREP} großen Gefahren zurück.",
        "sentence_en": "A determined mountaineer does not shrink back from great dangers.",
        "question_structure": "Wovor? • Davor",
        "level": "B2",
        "grammar_notes": "Hesitating or shrinking from daunting tasks.",
        "verb_rank": 144,
    },

    # ==========================================
    # RANK 145: abhalten
    # ==========================================
    {
        "verb_group": "abhalten",
        "verb": "abhalten",
        "prep": "von",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to keep from / to deter from",
        "sentence_de": "Nichts auf der Welt konnte ihn {PREP} seinen ehrgeizigen Plänen abhalten.",
        "sentence_en": "Nothing in the world could deter him from his ambitious plans.",
        "question_structure": "Wovon? • Davon",
        "level": "B2",
        "grammar_notes": "Formula: jemanden (Akk) von etwas (Dat) abhalten.",
        "verb_rank": 145,
    },

    # ==========================================
    # RANK 146: aufrufen
    # ==========================================
    {
        "verb_group": "aufrufen",
        "verb": "aufrufen",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to call for / to appeal for (action, donations)",
        "sentence_de": "Der Bürgermeister rief die Bürger {PREP} gegenseitiger Solidarität auf.",
        "sentence_en": "The mayor appealed to citizens for mutual solidarity.",
        "question_structure": "Wozu? • Dazu",
        "level": "B1",
        "grammar_notes": "Public appeal or mobilization.",
        "verb_rank": 146,
    },

    # ==========================================
    # RANK 147: sich berufen
    # ==========================================
    {
        "verb_group": "sich berufen",
        "verb": "sich berufen",
        "prep": "auf",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to invoke / to appeal to / to cite (a law, right, statement)",
        "sentence_de": "Der Angeklagte berief sich vor Gericht {PREP} sein Recht zu schweigen.",
        "sentence_en": "The defendant invoked his right to remain silent in court.",
        "question_structure": "Worauf? • Darauf",
        "level": "B2",
        "grammar_notes": "Legal or formal citation of authority or rights. Takes Akkusativ.",
        "verb_rank": 147,
    },

    # ==========================================
    # RANK 148: sich einmischen
    # ==========================================
    {
        "verb_group": "sich einmischen",
        "verb": "sich einmischen",
        "prep": "in",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to interfere in / to meddle in",
        "sentence_de": "Bitte mische dich nicht ungefragt {PREP} meine privaten Angelegenheiten ein!",
        "sentence_en": "Please do not meddle unasked in my private affairs!",
        "question_structure": "Worin? • Darin",
        "level": "B1",
        "grammar_notes": "Separable reflexive verb: sich ein|mischen in + Akk.",
        "verb_rank": 148,
    },

    # ==========================================
    # RANK 149: greifen
    # ==========================================
    {
        "verb_group": "greifen",
        "verb": "greifen",
        "prep": "nach",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to reach for / to grasp at",
        "sentence_de": "Das Kleinkind griff neugierig {PREP} der glänzenden Tasse.",
        "sentence_en": "The toddler curiously reached for the shiny mug.",
        "question_structure": "Wonach? • Danach",
        "level": "B1",
        "grammar_notes": "Physical reach towards an object.",
        "verb_rank": 149,
    },
    {
        "verb_group": "greifen",
        "verb": "greifen",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to resort to / to reach for (measures, remedies)",
        "sentence_de": "In seiner Verzweiflung griff er {PREP} unkonventionellen Mitteln.",
        "sentence_en": "In his desperation, he resorted to unconventional means.",
        "question_structure": "Wozu? • Dazu",
        "level": "B2",
        "grammar_notes": "Choosing a remedy or extreme measure.",
        "verb_rank": 149,
    },

    # ==========================================
    # RANK 150: haften
    # ==========================================
    {
        "verb_group": "haften",
        "verb": "haften",
        "prep": "für",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to be liable for / to be responsible for",
        "sentence_de": "Eltern haften bekanntlich {PREP} die Schäden ihrer minderjährigen Kinder.",
        "sentence_en": "Parents are famously liable for the damages of their minor children.",
        "question_structure": "Wofür? • Dafür",
        "level": "B1",
        "grammar_notes": "Classic legal warning phrase in Germany ('Eltern haften für ihre Kinder').",
        "verb_rank": 150,
    },

    # ==========================================
    # RANK 151: neigen
    # ==========================================
    {
        "verb_group": "neigen",
        "verb": "neigen",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to tend to / to have an inclination toward",
        "sentence_de": "Unter starkem Stress neigt er leider {PREP} voreiligen Kurzschlusshandlungen.",
        "sentence_en": "Under severe stress he unfortunately tends toward hasty rash actions.",
        "question_structure": "Wozu? • Dazu",
        "level": "B2",
        "grammar_notes": "Disposition or behavioral tendency.",
        "verb_rank": 151,
    },

    # ==========================================
    # RANK 152: schwärmen
    # ==========================================
    {
        "verb_group": "schwärmen",
        "verb": "schwärmen",
        "prep": "von",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to rave about / to swoon over",
        "sentence_de": "Sie schwärmt unaufhörlich {PREP} den kulinarischen Genüssen in Rom.",
        "sentence_en": "She raves incessantly about the culinary delights in Rome.",
        "question_structure": "Wovon? • Davon",
        "level": "B1",
        "grammar_notes": "Enthusiastic praise or recounting.",
        "verb_rank": 152,
    },
    {
        "verb_group": "schwärmen",
        "verb": "schwärmen",
        "prep": "für",
        "case": "+ Akk.",
        "case_type": "akk",
        "meaning_en": "to have a crush on / to be fond of / to adore",
        "sentence_de": "Als Teenager schwärmte sie heimlich {PREP} einen berühmten Popstar.",
        "sentence_en": "As a teenager, she secretly had a crush on a famous pop star.",
        "question_structure": "Für wen? / Wofür?",
        "level": "B1",
        "grammar_notes": "Romantic infatuation or fandom.",
        "verb_rank": 152,
    },

    # ==========================================
    # RANK 153: übergehen
    # ==========================================
    {
        "verb_group": "übergehen",
        "verb": "übergehen",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to pass on to / to transition to (the next agenda item)",
        "sentence_de": "Lassen Sie uns nun {PREP} dem nächsten Tagesordnungspunkt übergehen.",
        "sentence_en": "Let us now transition to the next agenda item.",
        "question_structure": "Wozu? • Dazu",
        "level": "B2",
        "grammar_notes": "Separable verb: 'über|gehen zu + Dat' in meetings and presentations.",
        "verb_rank": 153,
    },

    # ==========================================
    # RANK 154: verleiten
    # ==========================================
    {
        "verb_group": "verleiten",
        "verb": "verleiten",
        "prep": "zu",
        "case": "+ Dat.",
        "case_type": "dat",
        "meaning_en": "to entice / mislead / induce into",
        "sentence_de": "Schlechte Vorbilder verleiteten den Jungen {PREP} gefährlichen Mutproben.",
        "sentence_en": "Bad role models enticed the boy into dangerous tests of courage.",
        "question_structure": "Wozu? • Dazu",
        "level": "B2",
        "grammar_notes": "Formula: jemanden (Akk) zu etwas (Dat) verleiten.",
        "verb_rank": 154,
    },
]
