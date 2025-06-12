from src.character import Character


def test_character_starts_with_10_hp():
    heros = Character("Hero")
    assert heros.hp == 10