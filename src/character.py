class Character:
    def __init__(self, name: str, hp: int = 10):
        self.name = name
        self.hp = hp
#     
#     @property
#     def is_alive(self) -> bool:
#         return self.hp > 0
    
#     def attack(self, other: "Character") -> None:
#         if not self.is_alive:
#             raise RuntimeError(f"{self.name} est mort : ne peut pas attaquer")
#         if not other.is_alive:
#             return
#         other.hp = max(0, other.hp - 1)
