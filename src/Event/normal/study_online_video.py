from src.Event.normal.study import study
from src.Event.eventExpections.exceptions import *

# Normal 普通事件 0
# Special 特殊事件 1
# Limit  限定事件 2

#study for random grade subject
class watchVideo(study):
    def study_random(self, mainPlayer, num_subject, change_rate):
        if mainPlayer.wallet < 50:
            raise notEnoughMoney
        mainPlayer.wallet -= 50
        super(watchVideo, self).study_random(mainPlayer,3,1.5)
