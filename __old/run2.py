# -*- coding: utf-8 -*-

from operator import itemgetter
from core import Extractor
from sv_lemmatizer import lemmatizer
from sv_lemmatizer.rules.sv import rules as sv_rules
from transformers import AutoModel, AutoTokenizer
import textwrap
from collections import Counter
from summa import summarizer
lem = lemmatizer.Lemmatizer(sv_rules)


def lemitize(word, type_of_word):
    if(type_of_word == 'LOC'):
        return lem.lemmatize("PROPN", word)[-1]
    elif(type_of_word == 'PRS'):
        return word
    else:
        return lem.lemmatize("NOUN", word)[-1]


text = """
De senaste 20 åren har mer än 420 miljoner vilda djur och växter fångats in i 226 länder, för att exporteras. Handeln sker till största del i länder med stora ekonomiska skillnader, konstaterar forskare i en ny studie.

Vilda grodor som fångas in i Madagaskar säljs sedan i USA och vild fisk som fångas i Thailand hamnar inte sällan i Hong Kong. Det är två exempel på att vilda djur i de allra flesta fall fångas in i låginkomstländer och säljs illegalt till länder med hög levnadsstandard. Det konstaterar forskare vid bland annat University of Hong Kong och National University of Singapore i den nya studien.

Forskarna har utgått från data över vildfångade djur från Cites, konventionen om handel med hotade arter, och jämfört med socioekonomiska faktorer i de länder där handeln med vilda djur är som störst. Indonesien, Jamaica och Honduras exporterade flest vilda djur mellan 1998 och 2018. De allra flesta djuren hamnade i USA, följt av Frankrike och Italien.

Den internationella handeln med djur och växter är en av de största farorna för hotade arter. Ett problem enligt forskarna är att det finns mycket få ekonomiska incitament för att begränsa den illegala handeln i de internationella avtal som har tecknats. De föreslår därför att de länder där flest djur fångas in får ekonomisk hjälp under förutsättning att de lyckas minska handeln.

– Vi menar att pengarna borde komma från höginkomstländer. Dels för att de har ett ansvar genom FN:s globala mål, dels för att de spelar en oproportionerligt stor roll i den globala djurhandeln, säger Jia Huan Liew, som har lett studien, till BBC News.

Mycket tyder på att den illegala handeln med vilda djur och växter har minskat under pandemin, bland annat på grund av Kinas förbud mot konsumtion av vilda djur.

– Nu har vi en chans att dra nytta av människors medvetenhet kring riskerna med den här handeln och därmed undvika att allt åtgår till det vanliga efter pandemin, säger Jia Huan Liew.


  """

entities = []
extractor = Extractor()
chunks_word_count = 250
text = summarizer.summarize(text, language='swedish', words=500)
chunks = textwrap.wrap(text, chunks_word_count)

for chunk in chunks:
    keywords = extractor.generate(chunk, top_k=3)
    for token in keywords:
        if(" " not in token):
            entities.append(token)

doc = extractor.get_words_and_entities(text.lower())
for token in doc:
    if(token.tag_ == 'NOUN' and (token.dep_ == 'nmod' or token.dep_ == 'nsubj')):
        entities.append(token.text)

low_noun_words = []
high_noun_words = []
final_noun_words = []
final_enteties_words = []
all_words = dict(Counter(entities))


for key, value in all_words.items():
    if(value > 1):
        high_noun_words.append(dict(text=key, score=value))
    else:
        low_noun_words.append(dict(text=key, score=value))


for hw in high_noun_words:
    hw_score = hw['score']/10
    for lw in low_noun_words:
        if(extractor.similarity(hw['text'], lw['text']) > 0.85):
            hw_score = hw_score + 0.125
            final_noun_words.append(
                dict(text=lw['text'], type='NOUN', score=hw['score']/10*0.85))
    final_noun_words.append(
        dict(text=hw['text'], type='NOUN', score=hw_score))

for ent in doc.ents:
    if(len(ent.text) > 1 and ent.label_ not in ['TME', 'MSR']):
        new_ent = dict(text=ent.text,
                       type=ent.label_, score=1)
        final_enteties_words.append(new_ent)


final_noun_words = sorted(
    final_noun_words, key=itemgetter('score'), reverse=True)

# If the noun also is in the noun remove that noun.
for noun in final_noun_words[:]:
    for entity in final_enteties_words:
        if entity['text'] == noun['text']:
            final_noun_words.remvove(noun)

print(final_noun_words)
print('--------------')
print(final_enteties_words)
