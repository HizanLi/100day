from src.Character.Character import character
from src.Character.trait.mainTraits import mainTraits


class mainNpc(character):
    def __init__(self, name, gender, difficulty):
        super().__init__(name, gender,difficulty)
        self.initialize_character_type("main")

