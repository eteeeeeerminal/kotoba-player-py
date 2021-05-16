from kotoba_player_py.exceptions import InputFormatError
import pytest

from kotoba_player_py import (
    __version__, KotobaPlayer, InputFormatError
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