# -*- coding: utf-8 -*-
from operator import itemgetter
from core import Extractor
import textwrap
from summa import summarizer
import nouns
import verbs
import entities

def normalize_score(score, _max_):
    _min_ = 0
    _max_ = _max_ + 1
    return (score - _min_) / (_max_-_min_)


def run(org_text, section):
    extractor = Extractor()
    chunks_word_count = 250
    text = summarizer.summarize(org_text, language='swedish', words=500)
    chunks = textwrap.wrap(text, chunks_word_count)

    if(len(text) == 0):
        text = org_text
        chunks = [text]

    n = v = e = words = []

    if section == 'all' or section == 'nouns':
        print('Get nouns')
        n = nouns.get(text, chunks, extractor)
    if section == 'all' or section == 'verbs':
        print('Get verbs')
        v = verbs.get(text, chunks, extractor)
    if section == 'all' or section == 'enteties':
        print('Get enteties')
        print(org_text)
        e = entities.get(org_text, extractor)

    res = n + v

    if section != 'enteties':
        words = sorted(res, key=itemgetter('score'), reverse=True)
        highest_score = words[0]['score']
        for word in words:
            word['score'] = normalize_score(word['score'], highest_score)

    res = dict(words=words, entities=e)

    return res
