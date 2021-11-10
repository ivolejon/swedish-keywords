# -*- coding: utf-8 -*-
from operator import itemgetter
from core import Extractor
import textwrap
from summa import summarizer
import nouns
import verbs
import entities

def run(org_text):
    extractor = Extractor()
    chunks_word_count = 250
    text = summarizer.summarize(org_text, language='swedish', words=500)
    chunks = textwrap.wrap(text, chunks_word_count)

    if(len(text) == 0):
        text = org_text
        chunks = [text]

    n = nouns.get(text, chunks, extractor)
    v = verbs.get(text, chunks, extractor)
    e = entities.get(text)

    res = n + v

    words = sorted(res, key=itemgetter('score'), reverse=True)
    res = dict(words=words, entities=e)

    return res
