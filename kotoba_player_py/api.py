import spacy

from .constants import POS_tags
from .exceptions import InputFormatError

def get_last_open_class_word(sent: spacy.tokens.span.Span) -> str:
    sent = reversed(sent)
    for token in sent:
        if token.pos_ in POS_tags.OPEN_CLASS_WORDS:
            return token.text

class KotobaPlayer:
    def __init__(self) -> None:
        self.nlp = spacy.load("ja_ginza")

    def parrot(self, text:str) -> str:
        if not text:
            raise InputFormatError
        doc = self.nlp(text)
        if isinstance(doc[-1], spacy.tokens.token.Token):
            parrot_word = get_last_open_class_word(doc)
        else:
            parrot_word = get_last_open_class_word(doc[-1])

        return f"{parrot_word}! {parrot_word}!"

    def masquerade(self, text:str, mask_token:str, mask_char_by_char:bool=False) -> str:
        if not text:
            raise InputFormatError
        pass