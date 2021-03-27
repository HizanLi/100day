import random

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

    def update_mark(self,num_subject, change_rate, sub_type):
        subjects_art = ['chinese','math','english','political','history','geography']
        subjects_science = ['chinese','math','english','physics','chemistry','biology']
        result_subject = []


        if sub_type is "art":
            count = 0
            while count < num_subject:
                temp = subjects_art[random.randint(0, 5)]
                if temp not in result_subject:
                    result_subject.append(temp)
        else:
            count = 0
            while count < num_subject:
                temp = subjects_science[random.randint(0, 5)]
                if temp not in result_subject:
                    result_subject.append(temp)

