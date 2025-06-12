from character import Character

def test_character_starts_with_10_hp():
    hero = Character("Hero")
    assert hero.hp == 10