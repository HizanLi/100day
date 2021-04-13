from src.Event.mainEvent import mainEvent

#Normal 普通事件 0
#Special 特殊事件 1
#Limit  限定事件 2

class buyBook(mainEvent):
    event_type = 2
    #use iter method to return story
    def get_event_info(self, date, character):
        pass

    def __iter__(self):
        script = ["今天是阳光明媚的一天",
                  "你乘坐地铁2号线去了附近的书城",
                  "",]
        for line in script:
            yield line.split(",")