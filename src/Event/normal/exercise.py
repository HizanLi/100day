from src.Event.mainEvent import mainEvent
from src.Event.eventExpections.exceptions import *


class exercise(mainEvent):
    def __init__(self):
        self.event_type = 0


class practice(exercise):
    def __init__(self):
        super().__init__()

    def practice(self, mainPlayer):
        mainPlayer.pressure -= 2
        mainPlayer.strength += 0.1
        mainPlayer.constitution += 0.1
        mainPlayer.dexterity += 0.1
        info = "你拿你爸爸的健身卡去健身房锻炼了一整天，你的压力小幅度减少了，力量，体质，和敏捷小幅度提升"
        return info


class tutor(exercise):
    def __init__(self):
        super().__init__()

    def tutor(self, mainPlayer):
        if mainPlayer.wallet < 200:
            raise notEnoughMoney
        mainPlayer.wallet -= 200

        if mainPlayer.pressure >= 5:
            mainPlayer.pressure -= 5
        else:
            mainPlayer.pressure = 0
        mainPlayer.strength += 0.2
        mainPlayer.constitution += 0.2
        mainPlayer.dexterity += 0.2

        info = "你和你爸爸的健身教练一起锻炼了一整天，你的压力中幅度减少了，力量，体质，和敏捷中幅度提升"
        return info


class extraClass(exercise):
    def __init__(self):
        super().__init__()

    def extraClass(self, mainPlayer):
        if mainPlayer.wallet < 500:
            raise notEnoughMoney
        mainPlayer.wallet -= 500

        if mainPlayer.pressure >= 10:
            mainPlayer.pressure -= 10
        else:
            mainPlayer.pressure = 0

        mainPlayer.strength += 0.5
        mainPlayer.constitution += 0.5
        mainPlayer.dexterity += 0.5

        info = "你找了国家级运动员给你陪练，你的压力大幅度减少了，力量，体质，和敏捷大幅度提升"
        return info

#解锁条件 - 好感达到 60
class exercise_with_her(exercise):
    def __init__(self):
        super().__init__()

    def exercise_with_her(self, mainPlayer):
        if mainPlayer.pressure >= 10:
            mainPlayer.pressure -= 10
        else:
            mainPlayer.pressure = 0
        mainPlayer.strength += 0.1
        mainPlayer.constitution += 0.1
        mainPlayer.dexterity += 0.1

        info = "你和你的青梅竹马一起锻炼了一整天，你的压力大幅度减少了，力量，体质，和敏捷小幅度提升"
        return info
