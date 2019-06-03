import pytest
from spellchecker import SpellCheck, erase_triple_dupes


def test_find_likely_words():
    spell = SpellCheck(['apple'], "appel")
    assert ['apple'] == spell.find_likely_words()


def test_find_optional_words():
    spell = SpellCheck(['air', 'all', 'lay'], "arl")
    assert ['air', 'all', 'lay'] == spell.find_optional_words()


def test_erase_triple_dupes():
    assert erase_triple_dupes('happpy') == 'happy'
