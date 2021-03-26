from src.Character.Character import character
import numpy


class mainPlayer(character):
    def __init__(self, name, gender, difficulty):
        super().__init__(name, gender, difficulty)
        self.initialize_character_type("main")
        self.initialize_mark(101, 109, 104, 66, 66, 66, 66, 66, 66)
        self.initialize_status(1000,0)
        self.initialize_attribute(10, 10, 10, 10, 10, 10, 10)
        self.traits.generate(difficulty)
        self.update_attribute()

    def update_mark(self,num_subject,change_rate):
        subjects = ['chinese','math','english','political','history','geography']

