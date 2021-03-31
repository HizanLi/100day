from src.Event.normal.study import study
from src.Event.eventExpections.exceptions import *

# Normal 普通事件 0
# Special 特殊事件 1
# Limit  限定事件 2

#study for lowest grade subject
class tutor(study):
    def study_select(self, mainPlayer):
        if mainPlayer.wallet < 200:
            raise notEnoughMoney
        mainPlayer.wallet -= 200
        result = mainPlayer.update_mark_select(1,5)
        result = self.trans_sub(result)
        info = "你今天做了找了私教给你补了一整天的课，你感觉你对"
        count = 0
        for sub in result:

            info += sub
            if count == len(result)-2:
                info += "，和"
            elif count != len(result)-1:
                info += "，"

            count+=1
        info += '的理解中幅度提升了。'
        return info
