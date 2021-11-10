# -*- coding: utf-8 -*-
import torch
from sklearn.feature_extraction.text import CountVectorizer
from stop_words import get_stop_words


# stop_words = text.ENGLISH_STOP_WORDS

def squash(value):
    if not torch.is_tensor(value):
        raise ValueError(f"unexpected `value` of type {value.__class__}")
    if value.ndim == 2:
        return value
    return value.mean(dim=1)


def get_all_candidates(in_text, n_gram_range):
    stop_words = get_stop_words('swedish')
    count = CountVectorizer(ngram_range=n_gram_range,
                            stop_words=stop_words).fit([in_text])
    all_candidates = count.get_feature_names()
    return all_candidates
