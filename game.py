from src.Character.player.mainPlayer import mainPlayer
from src.Event.Events import events
import datetime

class game(object):

    def __init__(self):
        event_log = []


    def initialize_player(self, name, gender, difficulty):
        self.player = mainPlayer(name, gender, difficulty)

    # initialize_


def main():
    day = datetime.datetime(2015,8,31)
    for i in range(5):
        day += datetime.timedelta(days=1)
        print(day)




if __name__ == '__main__':
    main()
