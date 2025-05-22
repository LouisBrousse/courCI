import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from src.character import Character

def test_character_starts_with_10_hp():
    hero = Character("Hero")
    assert hero.hp == 10
