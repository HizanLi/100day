import random
from decimal import *
from src.Character.Character import character
import numpy


class mainPlayer(character):
    def __init__(self, name, gender, difficulty,sub_type):
        super().__init__(name, gender, difficulty,sub_type)
        self.initialize_character_type("main")
        self.initialize_mark(101, 109, 104, 66, 66, 66, 66, 66, 66)
        self.initialize_status(1000, 0)
        self.initialize_attribute(10, 10, 10, 10, 10, 10, 10)
        self.traits.generate(difficulty)
        self.update_attribute()
        # 成长系数
        # self.intelligence_coefficient = Decimal(0.05)
        # self.luck_coefficient = Decimal(0.10)
        # self.strength_coefficient = Decimal(0.05)
        # self.dexterity_coefficient = Decimal(0.05)
        # self.constitution_coefficient = Decimal(0.05)
        # self.charm_coefficient = Decimal(0.05)
        # self.willpower_coefficient = Decimal(0.10)
        self.intelligence_coefficient = (0.05)
        self.luck_coefficient = (0.10)
        self.strength_coefficient = (0.05)
        self.dexterity_coefficient = (0.05)
        self.constitution_coefficient = (0.05)
        self.charm_coefficient = (0.05)
        self.willpower_coefficient = (0.10)

    def update_mark(self, num_subject, change_rate, sub_type):
        subjects_art = ['chinese', 'math', 'english', 'political', 'history', 'geography']
        subjects_science = ['chinese', 'math', 'english', 'physics', 'chemistry', 'biology']
        result_subject = []

        if sub_type == "art":
            count = 0
            while count < num_subject:
                temp = subjects_art[random.randint(0, 5)]
                if temp not in result_subject:
                    result_subject.append(temp)
                    count+=1
        else:
            count = 0
            while count < num_subject:
                temp = subjects_science[random.randint(0, 5)]
                if temp not in result_subject:
                    result_subject.append(temp)
                    count+=1

        # for subject in result_subject:
        #     getcontext().prec = 6
        #     change = change_rate + Decimal(change_rate/2)*self.intelligence *self.intelligence_coefficient + Decimal(change_rate/4)*self.luck * self.luck_coefficient + Decimal(change_rate/4)*self.willpower * self.willpower_coefficient
        #     exec("self." + subject + "+=" + change)
        for subject in result_subject:
            getcontext().prec = 6
            change = change_rate + float(change_rate/2)*self.intelligence *self.intelligence_coefficient + float(change_rate/4)*self.luck * self.luck_coefficient + float(change_rate/4)*self.willpower * self.willpower_coefficient
            exec ("self." + subject + "+=" + str(change))