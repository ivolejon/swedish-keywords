import spacy
import subprocess
from string import punctuation


def extract_keywords(nlp, sequence, special_tags: list = None):
    """ Takes a Spacy core language model,
    string sequence of text and optional
    list of special tags as arguments.

    If any of the words in the string are 
    in the list of special tags they are immediately 
    added to the result.  

    Arguments:
        sequence {str} -- string sequence to have keywords extracted from

    Keyword Arguments:
        tags {list} --  list of tags to be automatically added (default: {None})

    Returns:
        {list} -- list of the unique keywords extracted from a string
    """
    result = []

    # custom list of part of speech tags we are interested in
    # we are interested in proper nouns, nouns, and adjectives
    # edit this list of POS tags according to your needs.
    pos_tag = ['PROPN', 'NOUN']

    # create a spacy doc object by calling the nlp object on the input sequence
    doc = nlp(sequence.lower())

    # if special tags are given and exist in the input sequence
    # add them to results by default
    if special_tags:
        tags = [tag.lower() for tag in special_tags]
        for token in doc:
            if token.text in tags:
                result.append(token.text)

    for chunk in doc.noun_chunks:
        final_chunk = ""
        for token in chunk:
            if (token.pos_ in pos_tag):
                final_chunk = final_chunk + token.text + " "
        if final_chunk:
            result.append(final_chunk.strip())

    for token in doc:
        if (token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        if (token.pos_ in pos_tag):
            result.append(token.text)
    return list(set(result))


if __name__ == "__main__":
    """
    install the langauge model using the subprocess package
    useful when hosting the service in the cloud as it prevents against
    us forgetting to do this via the CLI
    """

    # load the small english language model,
    nlp = spacy.load("models/sv_pipeline-0.0.0/sv_pipeline/sv_pipeline-0.0.0")

    print("Loaded language vocabulary")
    print(extract_keywords(nlp, """Indien överraskade i början av veckan med ett löfte om klimatneutralitet till 2070, vilket kan leda till att flera länder ökar sina ambitioner. Det säger forskare på plats vid klimatmötet COP26 i Glasgow till Extrakt. I början av veckan meddelade Indiens premiärminister Narendra Modi på klimattoppmötet i Glasgow att landet ska nå nettonollutsläpp 2070, vilket överraskande Mikael Karlsson, docent i miljövetenskap vid Uppsala Universitet, som är på plats i Glasgow. – De har tidigare sagt att de ska leverera ett klimatåtagande när de rika länderna har samlat ihop de 100 miljarder dollar i klimatfinansiering som utlovades i Köpenhamn 2009. Men det har ännu inte uppnåtts, säger han. Han tycker att Indiens agerande sätter press på övriga länder. – Indiens plan är på ett sätt mer ambitiös än de rika ländernas. Stefan Löfven kommenterade att 2070 är för sent, men då är även det svenska målet 2045 för sent satt, givet att de svenska utsläppen per person ligger långt över de indiska. Den bollen har Sverige inte tagit. Indiens åtagande kan leda till att länder skruvar upp sina nationella planer, då kan det bli en bra effekt både på mötet och i verkligheten, säger Mikael Karlsson. """))
