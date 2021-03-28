from src.Character.player.mainPlayer import mainPlayer
from src.Event.normal.study import study
from src.Event.mainEvent import mainPlayer
import datetime
import copy
import random


# 第一层按钮
# Study 1 学习
# Excerise 2 锻炼
# relax 3 休息
# invite 4 邀约

# 第二层按钮
# 学习 +成绩 +压力
# Study 1-1 做习题
# Study 1-2 看网课
# Study 1-3 请家教
# Study 1-4 补习班

# 锻炼 -压力 -体力 -金钱？ +体制/敏捷/力量
# Excerise 2 举铁
# Excerise 2 长跑
# Excerise 2 铁人三项
# Excerise 2 专业训练

# 休息 -压力 -金钱 +体力
# relax 3 玩手机
# relax 3 去网吧
# relax 3 逛超市
# relax 3 玩电脑

# 邀约 +好感 -金钱
# invite 4 图书馆
# invite 4 大商场
# invite 4 电影院
# invite 4 游乐园

class game(object):
    def __init__(self):
        self.monthly_money = 1000  # 每月零花钱
        self.event_log = []  # 事件记录
        self.date = datetime.datetime(2015, 8, 31)  # 游戏开始日期 （开学第一天）

    def initialize_player(self, name, gender, difficulty, sub_type):
        self.player = mainPlayer(name, gender, difficulty, sub_type)

    def oneDayPass(self):
        copy_date = copy.copy(self.date)
        # update wallet 更新钱包
        self.date += datetime.timedelta(days=1)
        if copy_date.month != self.date.month:
            self.player.wallet += self.monthly_money

    def monthly_test(self):
        first_test = datetime.datetime(2015, 9, 30)
        second_test = datetime.datetime(2015, 10, 30)
        third_test = datetime.datetime(2015, 11, 30)
        fourth_test = datetime.datetime(2015, 12, 31)
        fifth_test = datetime.datetime(2016, 1, 29)
        sixth_test = datetime.datetime(2016, 2, 26)
        seventh_test = datetime.datetime(2016, 3, 31)
        eighth_test = datetime.datetime(2016, 4, 29)
        ninth_test = datetime.datetime(2016, 5, 31)

    def final_test(self):
        final_test = datetime.datetime(2016, 6, 7)

    def event_interpreter(self):
        pass

    def start(self):
        pass


def main():
    ge = game()
    ge.initialize_player("Leon", "male", "normal", 'art')
    print(ge.player.get_character_status())

    # for i in range(0, 30):
    #     ge.player.update_mark(3, 1, "science")
    # print(ge.player.get_character_status())

    event_test = study()

    event_test.study(ge.player)
    print(ge.player.get_character_status())


if __name__ == '__main__':
    main()
