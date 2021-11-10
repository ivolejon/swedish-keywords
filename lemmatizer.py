
# from sv_lemmatizer import lemmatizer
# from sv_lemmatizer.rules.sv import rules as sv_rules

# lem = lemmatizer.Lemmatizer(sv_rules)

# ivo = lem.lemmatize("PROPN", "Indonesien")
# print(ivo)

from sv_lemmatizer.rules.sv import rules as sv_rules
from sv_lemmatizer import lemmatizer
lem = lemmatizer.Lemmatizer(sv_rules)


def lemitize(word, type_of_word):
    if(type_of_word == 'LOC'):
        return lem.lemmatize("PROPN", word)[-1]
    elif(type_of_word == 'PRS' or type_of_word == 'ORG'):
        return word
    elif(type_of_word == 'VERB'):
        return lem.lemmatize("VERB", word)[-1]
    else:
        return lem.lemmatize("NOUN", word)[-1]
