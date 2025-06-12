from src.character import Character


def test_character_starts_with_10_hp():
    hero = Character("Hero")
    assert hero.hp == 10

def test_character_is_alive_initially():
    hero = Character("Hero")
    assert hero.is_alive

def test_attack_reduces_target_hp_by_one():
    attacker = Character("A")
    target = Character("B")
    attacker.attack(target)
    assert target.hp == 9

# def test_character_dies_at_zero_hp():
#     hero = Character("Hero")
#     for _ in range(10):
#         Character("Orc").attack(hero)
#     assert hero.hp == 0
#     assert not hero.is_alive

# def test_hp_cannot_go_below_zero():
#     victim = Character("Victim")
#     for _ in range(15):
#         Character("Assassin").attack(victim)
#     assert victim.hp == 0