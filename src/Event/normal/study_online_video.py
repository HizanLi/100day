from src.Event.normal.study import study
from src.Event.eventExpections.exceptions import *

# Normal 普通事件 0
# Special 特殊事件 1
# Limit  限定事件 2

#study for random grade subject
class watchVideo(study):
    def study_random(self, mainPlayer):
        if mainPlayer.wallet < 50:
            raise notEnoughMoney
        mainPlayer.wallet -= 50
        result = mainPlayer.update_mark_random(3, 1.5)
        result = self.trans_sub(result)
        info = "你今天做跟着网上的教程解做了一整天的难题，你感觉你对"
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
