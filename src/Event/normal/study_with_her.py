from src.Event.normal.study import study


# Normal 普通事件 0
# Special 特殊事件 1
# Limit  限定事件 2

#study for lowest subject
class study_with_her(study):

    def study_select(self, mainPlayer):
        result = mainPlayer.update_mark_select(1, 4)
        result = self.trans_sub(result)
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
