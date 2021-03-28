from src.Event.normal.study import study
from src.Event.eventExpections.exceptions import *

# Normal 普通事件 0
# Special 特殊事件 1
# Limit  限定事件 2

#study for lowest grade subject
class tutor(study):
    def study_select(self, mainPlayer, num_subject, change_rate):
        if mainPlayer.wallet < 200:
            raise notEnoughMoney
        mainPlayer.wallet -= 200
        super(tutor, self).study_select(mainPlayer,1,5)
