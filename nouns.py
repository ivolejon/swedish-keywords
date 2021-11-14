# -*- coding: utf-8 -*-
from collections import Counter
from lemmatizer import lemitize
from operator import itemgetter


def get(text, chunks, extractor):
    low_noun_words = []
    high_noun_words = []
    final_noun_words = []

    entities = []
    for chunk in chunks:
        keywords = extractor.generate(chunk, top_k=3, word_class="NOUN")
        for token in keywords:
            if(" " not in token):
                entities.append(lemitize(token, 'NOUN'))

    doc = extractor.get_words_and_entities(text.lower())
    for token in doc:
        if(token.tag_ == 'NOUN' and (token.dep_ == 'nmod' or token.dep_ == 'nsubj')):
            entities.append(lemitize(token.text, 'NOUN'))

    all_entities = dict(Counter(entities))

    for key, value in all_entities.items():
        if(value > 1):
            high_noun_words.append(dict(text=key, score=value))
        else:
            low_noun_words.append(dict(text=key, score=value))

    for hw in high_noun_words:
        hw_score = hw['score']
        for lw in low_noun_words:
            if(extractor.similarity(hw['text'], lw['text']) > 0.85):
                hw_score = hw_score + 1
                final_noun_words.append(
                    dict(text=lw['text'], type='NOUN', score=hw['score']*0.85))
        final_noun_words.append(
            dict(text=hw['text'], type='NOUN', score=hw_score))

    final_noun_words = sorted(
        final_noun_words, key=itemgetter('score'), reverse=True)

    return final_noun_words
