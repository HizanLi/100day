from src.Event.mainEvent import mainEvent
from src.Event.eventExpections.exceptions import *


class study(mainEvent):
    def __init__(self):
        self.event_type = 0


class practice(study):
    def __init__(self):
        super().__init__()

    def practice(self, mainPlayer):
        result = mainPlayer.update_mark_random(3, 1)
        result = self.trans_sub(result)
        mainPlayer.pressure += 5
        info = "你今天做了一整天的练习题，你感觉你对"
        count = 0
        for sub in result:

            info += sub
            if count == len(result) - 2:
                info += "，和"
            elif count != len(result) - 1:
                info += "，"

            count += 1
        info += '的理解小幅度提升了。'
        return info


class tutor(study):
    def __init__(self):
        super().__init__()

    def tutor(self, mainPlayer):
        if mainPlayer.wallet < 200:
            raise notEnoughMoney
        mainPlayer.wallet -= 200
        result = mainPlayer.update_mark_select(1, 5)
        result = self.trans_sub(result)
        mainPlayer.pressure += 10
        info = "你今天做了找了私教给你补了一整天的课，你感觉你对"
        count = 0
        for sub in result:

            info += sub
            if count == len(result) - 2:
                info += "，和"
            elif count != len(result) - 1:
                info += "，"

            count += 1
        info += '的理解中幅度提升了。'
        return info


class extraClass(study):
    def __init__(self):
        super().__init__()

    def extraClass(self, mainPlayer):
        if mainPlayer.wallet < 500:
            raise notEnoughMoney
        mainPlayer.wallet -= 500
        result = mainPlayer.update_mark_select(1, 10)
        result = self.trans_sub(result)
        mainPlayer.pressure += 20
        info = "你今天去上了一整天的加强补习班，你感觉你对"
        count = 0
        for sub in result:

            info += sub
            if count == len(result) - 2:
                info += "，和"
            elif count != len(result) - 1:
                info += "，"

            count += 1
        info += '的理解大幅度提升了。'
        return info


class study_with_her(study):
    def __init__(self):
        super().__init__()

    def study_with_her(self, mainPlayer):
        result = mainPlayer.update_mark_select(1, 4)
        result = self.trans_sub(result)
        mainPlayer.pressure -= 5
        info = "你的青梅竹马今天给你补了一整天的课，你感觉你对"
        count = 0
        for sub in result:

            info += sub
            if count == len(result) - 2:
                info += "，和"
            elif count != len(result) - 1:
                info += "，"

            count += 1
        info += '的理解中幅度提升了。'
        return info
