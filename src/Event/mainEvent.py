from src.Character.player.mainPlayer import mainPlayer

#Normal 普通事件 0
#Special 特殊事件 1
#Limit  限定事件 2

class mainEvent: #事件

    def get_event_info(self, date, character, info):
        return date.strftime("%B") + " " + date.strftime("%d") + ", " + date.strftime("%Y") + ' ' + date.strftime(
            "%A") + character.name


