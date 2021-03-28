from src.Event.normal.study import study


# Normal 普通事件 0
# Special 特殊事件 1
# Limit  限定事件 2

#study for subject
class practice(study):
    def study_random(self, mainPlayer, num_subject, change_rate):
        super(practice, self).study_random(mainPlayer,3,1)
