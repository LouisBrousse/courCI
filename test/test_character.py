import pytest
from src.character import Character

def test_default_hp():
    c = Character("Alice")
    assert c.hp == 10