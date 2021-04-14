from src.Event.mainEvent import mainEvent


# Normal 普通事件 0
# Special 特殊事件 1
# Limit  限定事件 2

class buyBook(mainEvent):
    event_type = 2

    # use iter method to return story
    def get_event_info(self, date, character):
        pass

    def __iter__(self):
        script = ["今天是开学第一天",
                  "老师发了一个购书清单",
                  "你需要把上面清单上的的书买齐",
                  "你乘坐地铁2号线去了附近的书城",
                  "刚一进门，你就看到你的青梅竹马站在收银台前",
                  "看起来很困惑的样子",
                  ["去问问发生了什么"],
                  "主角：怎么了？",
                  "竹马：太好了！是你！",
                  "竹马：我的钱包好像忘到学校里了",
                  "竹马：能不能帮我先付一下",
                  "竹马：我明天把钱还你？",
                  ["没问题"],
                  "竹马：谢啦！",
                  "竹马：周末你有空的话，请你喝奶茶！", ]
        for line in script:
            yield line.split(",")
