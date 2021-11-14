# -*- coding: utf-8 -*-
from lemmatizer import lemitize


def get(text, extractor):
    doc = extractor.get_words_and_entities(text)
    ents = []
    for ent in doc.ents:
        if(len(ent.text) > 1 and ent.label_ not in ['TME', 'MSR']):
            new_ent = dict(text=lemitize(ent.text, ent.label_),
                           type=ent.label_, score=1)
            if new_ent not in ents:
                ents.append(dict(new_ent))
    return ents
