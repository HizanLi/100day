from src.Event.mainEvent import mainEvent


class study(mainEvent):
    event_type = 0
    def study(self, mainPlayer):
        mainPlayer.update_mark(3, 1, mainPlayer.sub_type)
