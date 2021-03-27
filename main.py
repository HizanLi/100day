from src.Character.player.mainPlayer import mainPlayer
from src.Event.mainEvent import mainPlayer
import datetime
import copy

class game(object):

    def __init__(self):
        self.monthly_money = 1000 #每月零花钱
        self.event_log = [] #事件记录
        self.date = datetime.datetime(2015,8,31) #游戏开始日期 （开学第一天）



    def initialize_player(self, name, gender, difficulty):
        self.player = mainPlayer(name, gender, difficulty)

    def oneDayPass(self):
        copy_date = copy.copy(self.date)
        #update wallet 更新钱包
        self.date += datetime.timedelta(days=1)
        if copy_date.month != self.date.month:
            self.player.wallet += self.monthly_money

    def monthly_test(self):
        first_test = datetime.datetime(2015,9,30)
        second_test = datetime.datetime(2015,10,30)
        third_test = datetime.datetime(2015,11,30)
        fourth_test = datetime.datetime(2015,12,31)
        fifth_test = datetime.datetime(2016,1,29)
        sixth_test = datetime.datetime(2016,2,26)
        seventh_test = datetime.datetime(2016,3,31)
        eighth_test = datetime.datetime(2016,4,29)
        ninth_test = datetime.datetime(2016,5,31)

    def final_test(self):
        final_test = datetime.datetime(2016,6,7)

    def get_event_info(self,date):
        return date.strftime("%B") +" "+ date.strftime("%d") +", "+date.strftime("%Y")+ ' '+ date.strftime("%A")
    # initialize_


def main():
    ge=game()
    ge.initialize_player("Leon","male","normal")
    print(ge.player.get_character_status())
    ge.oneDayPass()
    print(ge.player.get_character_status())

    print(ge.get_event_info(datetime.datetime(2015,9,30)))




if __name__ == '__main__':
    main()
