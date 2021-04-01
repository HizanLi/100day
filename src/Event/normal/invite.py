from src.Event.mainEvent import mainEvent
from src.Event.eventExpections.exceptions import *


class invite(mainEvent):
    def __init__(self):
        self.event_type = 0

#解锁条件 - 好感达到 20
class park(invite): #图书馆
    def __init__(self):
        super().__init__()

    def park(self, mainPlayer,zhuma):
        mainPlayer.pressure -= 2
        info = "你和你的青梅竹马今天附近的公园转了一天。"

        return info

#解锁条件 - 好感达到 30
class library(invite): #图书馆
    def __init__(self):
        super().__init__()

    def library(self, mainPlayer,zhuma):
        result = mainPlayer.update_mark_random(4, 1)
        result = self.trans_sub(result)
        mainPlayer.pressure -= 5
        info = "你和你的青梅竹马今天去图书馆看了一天的书。从书中，你学习了"
        count = 0
        for sub in result:

            info += sub
            if count == len(result) - 2:
                info += "，和"
            elif count != len(result) - 1:
                info += "，"

            count += 1
        return info

#解锁条件 - 好感达到 40
class shopping_center(invite): #大商场
    def __init__(self):
        super().__init__()

    def shopping_center(self, mainPlayer,zhuma):
        if mainPlayer.wallet < 200:
            raise notEnoughMoney
        mainPlayer.wallet -= 200

        if mainPlayer.pressure >= 5:
            mainPlayer.pressure -= 5
        else:
            mainPlayer.pressure = 0
        mainPlayer.strength += 0.2
        mainPlayer.constitution += 0.2
        mainPlayer.dexterity += 0.2

        info = "你和你爸爸的健身教练一起锻炼了一整天，你的压力中幅度减少了，力量，体质，和敏捷中幅度提升"
        return info

#解锁条件 - 好感达到 50
class theater(invite): #电影院
    def __init__(self):
        super().__init__()

    def theater(self, mainPlayer,zhuma):
        if mainPlayer.wallet < 100:
            raise notEnoughMoney
        mainPlayer.wallet -= 100

        if mainPlayer.pressure >= 10:
            mainPlayer.pressure -= 10
        else:
            mainPlayer.pressure = 0

        mainPlayer.strength += 0.5
        mainPlayer.constitution += 0.5
        mainPlayer.dexterity += 0.5

        info = "你找了国家级运动员给你陪练，你的压力大幅度减少了，力量，体质，和敏捷大幅度提升"
        return info

#解锁条件 - 好感达到 60
class amusement_park(invite): #游乐园
    def __init__(self):
        super().__init__()

    def amusement_park(self, mainPlayer,zhuma):
        if mainPlayer.wallet < 500:
            raise notEnoughMoney
        mainPlayer.wallet -= 500
        if mainPlayer.pressure >= 20:
            mainPlayer.pressure -= 20
        else:
            mainPlayer.pressure = 0

        info = "你和你的青梅竹马去游旅游玩了一整天，你的压力大幅度减少了"
        return info
