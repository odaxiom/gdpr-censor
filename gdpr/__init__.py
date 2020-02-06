

def anonymize(text):
    import spacy
    from spacy.pipeline import Tagger
    import en_core_web_sm

    nlp = en_core_web_sm.load()

    doc = nlp(text)

    return " ".join(token.text if token.pos_ != 'PROPN' else token.pos_ for token in doc)
