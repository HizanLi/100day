import random
from decimal import *
from src.Character.Character import character
import numpy


class mainPlayer(character):

    def __init__(self, name, gender, difficulty, sub_type):
        super().__init__(name, gender, difficulty, sub_type)
        self.initialize_character_type("player")
        self.initialize_mark(101, 109, 104, 66, 66, 66, 66, 66, 66)
        self.initialize_status(1000, 0)
        self.initialize_attribute(10, 10, 10, 10, 10, 10, 10)
        self.update_attribute("player", "player")

        self.intelligence_coefficient = (0.05)
        self.luck_coefficient = (0.10)
        self.strength_coefficient = (0.05)
        self.dexterity_coefficient = (0.05)
        self.constitution_coefficient = (0.05)
        self.charm_coefficient = 0.05
        self.willpower_coefficient = 0.10

    def update_mark_random(self, num_subject, change_rate):
        subjects_art = ['chinese', 'math', 'english', 'political', 'history', 'geography']
        subjects_science = ['chinese', 'math', 'english', 'physics', 'chemistry', 'biology']
        result_subject = []

        if self.sub_type == "art":
            count = 0
            while count < num_subject:
                temp = subjects_art[random.randint(0, 5)]
                if temp not in result_subject:
                    result_subject.append(temp)
                    count += 1
        else:
            count = 0
            while count < num_subject:
                temp = subjects_science[random.randint(0, 5)]
                if temp not in result_subject:
                    result_subject.append(temp)
                    count += 1
        for subject in result_subject:
            change = change_rate + float(change_rate / 2) * self.intelligence * self.intelligence_coefficient + float(
                change_rate / 4) * self.luck * self.luck_coefficient + float(
                change_rate / 4) * self.willpower * self.willpower_coefficient
            exec("self." + subject + "+=" + str(change))
        return result_subject

    def update_mark_select(self, num_subject, change_rate):
        count = 0
        subs = []
        while count < num_subject:
            sub = self.get_lowest()
            exec("self." + sub + "+=" + str(change_rate))
            count += 1
            subs.append(sub)
        return subs

    def get_lowest(self):
        if self.sub_type == "art":
            subjects = ['chinese', 'math', 'english', 'political', 'history', 'geography']
        else:
            subjects = ['chinese', 'math', 'english', 'physics', 'chemistry', 'biology']
        marks = []

        for sub in subjects:
            marks.append(eval("self."+sub))
        lowest = min(marks)

        for sub in subjects:
            sub_mark = eval("self."+sub)
            if sub_mark == lowest:
                return sub
