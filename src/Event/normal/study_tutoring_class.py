from src.Event.normal.study import study
from src.Event.eventExpections.exceptions import *


# Normal 普通事件 0
# Special 特殊事件 1
# Limit  限定事件 2

# study for lowest grade subject
class extraClass(study):
    def study_select(self, mainPlayer):
        if mainPlayer.wallet < 500:
            raise notEnoughMoney
        mainPlayer.wallet -= 500
        result = mainPlayer.update_mark_select(mainPlayer, 1, 10)
        result = self.trans_sub(result)
        info = "你今天去上了一整天的加强补习班，你感觉你对"
        count = 0
        for sub in result:

            info += sub
            if count == len(result)-2:
                info += "，和"
            elif count != len(result)-1:
                info += "，"

            count+=1
        info += '的理解大幅度提升了。'
        return info