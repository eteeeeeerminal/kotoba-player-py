from kotoba_player_py.exceptions import InputFormatError
import pytest

from kotoba_player_py import (
    __version__, KotobaPlayer, InputFormatError
)
from kotoba_player_py.api import (
    mask_noun_word
)

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def player():
    return KotobaPlayer()

def test_parrot(player: KotobaPlayer):
    with pytest.raises(InputFormatError):
        player.parrot("")
    with pytest.raises(InputFormatError):
        player.parrot(None)
    assert player.parrot("お宝はいただくぜ") == "いただく! いただく!"
    assert player.parrot("キトさんは、とっても可愛いです。") == "可愛い! 可愛い!"

def test_mask_noun_word(player: KotobaPlayer):
    tokens = player.nlp("東京")
    assert mask_noun_word(tokens[0], "hogehoge") == "hogehoge"
    tokens = player.nlp("美しい")
    assert mask_noun_word(tokens[0], "hogehoge") == "美しい"
    tokens = player.nlp("東京")
    assert mask_noun_word(tokens[0], "x", True) == "xx"

def test_masquerade(player: KotobaPlayer):
    with pytest.raises(InputFormatError):
        player.masquerade("", "")
    with pytest.raises(InputFormatError):
        player.masquerade(None, None)

    assert player.masquerade("東京タワーは綺麗です。", "hoge") == "hogehogeは綺麗です。"
    assert player.masquerade("東京タワーは綺麗です。", "x", True) == "xxxxxは綺麗です。"
    assert player.masquerade("東京タワーは綺麗です。私の家はあっちです。", "x", True) == "xxxxxは綺麗です。私のxはあっちです。"
    assert player.masquerade("美しすぎる。", "hoge") == "美しすぎる。"