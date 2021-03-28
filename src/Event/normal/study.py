from src.Event.mainEvent import mainEvent


class study(mainEvent):
    event_type = 0

    def study_random(self, mainPlayer, num_subject, change_rate):
        mainPlayer.update_mark_random(num_subject, change_rate, mainPlayer.sub_type)

    def study_select(self, mainPlayer, num_subject, change_rate):
        mainPlayer.update_mark_select(num_subject, change_rate)