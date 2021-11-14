# -*- coding: utf-8 -*-
from collections import Counter
from lemmatizer import lemitize
from operator import itemgetter


def get(text, chunks, extractor):
    low_verb_words = []
    high_verb_words = []
    final_verb_words = []

    entities = []
    for chunk in chunks:
        keywords = extractor.generate(chunk, top_k=3, word_class="VERB")
        for token in keywords:
            if(" " not in token):
                entities.append(lemitize(token, 'VERB'))

    doc = extractor.get_words_and_entities(text.lower())
    for token in doc:
        if(token.tag_ == 'VERB' and (token.dep_ == 'ROOT' or token.dep_ == 'acl:relcl' or token.dep_ == 'conj' or token.dep_ == 'acl' or token.dep_ == 'xcomp')):
            entities.append(lemitize(token.text, 'VERB'))

    all_entities = dict(Counter(entities))

    for key, value in all_entities.items():
        if(value > 1):
            high_verb_words.append(dict(text=key, score=value))
        else:
            low_verb_words.append(dict(text=key, score=value))

    for hw in high_verb_words:
        hw_score = hw['score']
        for lw in low_verb_words:
            if(extractor.similarity(hw['text'], lw['text']) > 0.85):
                hw_score = hw_score + 1
                final_verb_words.append(
                    dict(text=lw['text'], type='VERB', score=hw['score']*0.85))
        final_verb_words.append(
            dict(text=hw['text'], type='VERB', score=hw_score))

    final_verb_words = sorted(
        final_verb_words, key=itemgetter('score'), reverse=True)

    return final_verb_words
