from functools import partial
import spacy

from .constants import POS_tags
from .exceptions import InputFormatError

def get_last_open_class_word(sent: spacy.tokens.span.Span) -> str:
    sent = reversed(sent)
    for token in sent:
        if token.pos_ in POS_tags.OPEN_CLASS_WORDS:
            return token.text

def mask_noun_word(
    word: spacy.tokens.token.Token,
    mask_token:str, mask_char_by_char:bool=False
    ) -> str:
    if word.pos_ in ["NOUN", "PROPN"]:
        if mask_char_by_char:
            return mask_token*len(word.text)
        else:
            return mask_token
    else:
        return word.text

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
        """名詞を伏せる
        """
        if not text:
            raise InputFormatError

        mask_word = partial(
            mask_noun_word,
            mask_token=mask_token, mask_char_by_char=mask_char_by_char
        )
        doc = self.nlp(text)
        if isinstance(doc[-1], spacy.tokens.token.Token):
            return "".join(map(mask_word, doc))
        else:
            return "".join((
                "".join(map(mask_word, sent))
                for sent in doc
            ))