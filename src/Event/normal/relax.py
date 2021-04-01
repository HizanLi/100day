from src.Event.mainEvent import mainEvent
from src.Event.eventExpections.exceptions import *


class relax(mainEvent):
    def __init__(self):
        self.event_type = 0


class play_phone(relax):
    def __init__(self):
        super().__init__()

    def play_phone(self, mainPlayer):
        if mainPlayer.pressure >= 5:
            mainPlayer.pressure -= 5
        else:
            mainPlayer.pressure = 0
        mainPlayer.constitution -= 0.1
        info = "你玩了一整天的手机，感觉眼睛有点不舒服，但是你的压力中幅下降了"
        return info


class play_computer(relax):
    def __init__(self):
        super().__init__()

    def play_phton(self, mainPlayer):
        if mainPlayer.pressure >= 10:
            mainPlayer.pressure -= 10
        else:
            mainPlayer.pressure = 0
        mainPlayer.constitution -= 0.2
        info = "你玩了一整天的电脑，感觉眼睛有点不舒服，但是你的压力大幅下降了"
        return info


class Internet_cafe(relax):
    def __init__(self):
        super().__init__()

    def play_phton(self, mainPlayer):
        if mainPlayer.wallet < 400:
            raise notEnoughMoney
        mainPlayer.wallet -= 400

        if mainPlayer.pressure >= 20:
            mainPlayer.pressure -= 20
        else:
            mainPlayer.pressure = 0
        mainPlayer.constitution -= 0.5
        info = "你去网吧和朋友玩了一整天的电脑，感觉眼睛有点不舒服，但是你的压力超大幅下降了"
        return info


class relax_with_her(relax):
    def __init__(self):
        super().__init__()

    def relax_with_her(self, mainPlayer):
        if mainPlayer.pressure >= 15:
            mainPlayer.pressure -= 15
        else:
            mainPlayer.pressure = 0

        info = "你的青梅竹马陪着你休息了一整天，你的压力大幅下降了"
        return info
