from src.Character.npc.zhuma import zhuma
from src.Character.player.mainPlayer import mainPlayer
from src.Event.normal.study import *
from src.Event.mainEvent import mainPlayer
import datetime
import copy
import random
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from functools import partial

from src.Event.normal import *
from ui import mainWindoe


class game(object):
    def __init__(self):
        self.monthly_money = 1000  # 每月零花钱
        self.event_log = []  # 事件记录
        self.date = datetime.datetime(2015, 8, 31)  # 游戏开始日期 （开学第一天）
        self.initilize_npc()

    def initialize_player(self, name, gender, difficulty, sub_type):
        self.player = mainPlayer(name, gender, difficulty, sub_type)

    def oneDayPass(self):
        copy_date = copy.copy(self.date)
        # update wallet 更新钱包
        self.date += datetime.timedelta(days=1)
        if copy_date.month != self.date.month:
            self.player.wallet += self.monthly_money

    def monthly_test(self):
        first_test = datetime.datetime(2015, 9, 30)  # 解锁家教
        second_test = datetime.datetime(2015, 10, 30)
        third_test = datetime.datetime(2015, 11, 30)
        fourth_test = datetime.datetime(2015, 12, 31)
        fifth_test = datetime.datetime(2016, 1, 29)  # 解锁补习班
        sixth_test = datetime.datetime(2016, 2, 26)
        seventh_test = datetime.datetime(2016, 3, 31)
        eighth_test = datetime.datetime(2016, 4, 29)
        ninth_test = datetime.datetime(2016, 5, 31)

    def initilize_npc(self):
        self.zhuma = zhuma("青梅竹马", "gender", "normal", "art")  # 你的青梅竹马

    def final_test(self):
        final_test = datetime.datetime(2016, 6, 7)

    def event_interpreter(self):
        # date.strftime("%B") + " " + date.strftime("%d") + ", " + date.strftime("%Y") + ' ' + date.strftime("%A")
        pass

    def start(self):
        pass


def main():
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = mainWindoe.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    #get info from mainWindow
    name = ui.name.text()
    gender = ui.gender.currentText()
    if ui.subject_type.currentText() == "文综":
        subject_type = "art"
    else:
        subject_type = "science"
    #start initialize game
    ge = game()
    ge.initialize_player(name,gender,"normal",subject_type)
    show_attributes(ui,ge)
    print(ge.player.get_character_status())
    ui.refresh.clicked.connect(partial(re_generate, ui, ge))

    sys.exit(app.exec_())


def re_generate(ui, ge):
    name = ui.name.text()
    gender = ui.gender.currentText()
    if ui.subject_type.currentText() == "文综":
        subject_type = "art"
    else:
        subject_type = "science"
    ge.initialize_player(name, gender, "normal", subject_type)
    print(ge.player.get_character_status())

    show_attributes(ui, ge)


def show_attributes(ui, ge):
    ui.luck.setText(str(ge.player.luck))
    ui.Charm.setText(str(ge.player.charm))
    ui.dexterity.setText(str(ge.player.dexterity))
    ui.constitution.setText(str(ge.player.constitution))
    ui.intelligence.setText(str(ge.player.intelligence))
    ui.strength.setText(str(ge.player.strength))


if __name__ == '__main__':
    main()
