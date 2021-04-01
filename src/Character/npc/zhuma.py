from src.Character.Character import character
from src.Character.trait.mainTraits import mainTraits


class zhuma(character):
    def __init__(self, name, gender, difficulty, sub_type):
        super().__init__(name, gender,difficulty,sub_type)
        self.initialize_character_type("zhuma")
        self.initialize_mark(140, 145, 150, 91, 94, 92, 60, 59, 51)
        self.initialize_status(1000, 0)
        self.initialize_attribute(10, 10, 10, 10, 10, 10, 10)
        self.update_attribute('npc','zhuma')
        self.relationship = "friend"
        self.impression_level = 20

