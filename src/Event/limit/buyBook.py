from src.Event.mainEvent import mainEvent

#Normal 普通事件 0
#Special 特殊事件 1
#Limit  限定事件 2

class buyBook(mainEvent):
    event_type = 2
    #use iter method to return story
    def get_event_info(self, date, character, info):
        super(buyBook, self).get_event_info(date,character,info)