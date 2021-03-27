from src.Character.trait.mainTraits import mainTraits


class character(object):

    def __init__(self, name, gender,difficulty):
        self.name = name
        self.gender=gender
        self.difficulty=difficulty

        self.event_log = []
        self.trait_log = []

        self.traits = mainTraits()


    def initialize_character_type(self,type):
        self.character_type=type

    def initialize_attribute(self,luck,strength,intelligence,dexterity,constitution,charm,willpower):
        self.luck = luck  # 运气
        self.strength = strength  # 力量
        self.intelligence = intelligence  # 智力
        self.dexterity = dexterity  # 敏捷
        self.constitution = constitution  # 体质
        self.charm = charm  # 魅力
        self.willpower = willpower  # 意志力

    def initialize_status(self,wallet,pressure):
        self.wallet = wallet  # 钱包
        self.pressure = pressure  # 压力

    def initialize_mark(self,chinese,math,english,political,history,geography,physics,chemistry,biology):
        self.chinese = chinese  # 语文
        self.math = math  # 数学
        self.english = english # 外语
        self.political = political # 政治
        self.history = history # 历史
        self.geography = geography # 地理
        self.physics = physics #物理
        self.chemistry = chemistry #化学
        self.biology = biology #生物

    def update_attribute(self):
        for change in self.traits.attributes_positive_result:
            self.trait_log.append(change)
            change = change.split(',')
            exec("self." + change[1] + "=" + "self." + change[1] + change[2])
        for change in self.traits.attributes_negative_result:
            self.trait_log.append(change)
            change = change.split(',')
            exec("self." + change[1] + "=" + "self." + change[1] + change[2])

    def get_character_status(self):
        return "姓名: " + self.name  \
               + "\n\n人物属性: " \
               + "\n运气: " + str(self.luck) \
               + "\n魅力: " + str(self.charm) \
               + "\n力量: " + str(self.strength) \
               + "\n敏捷: " + str(self.dexterity) \
               + "\n意志力: " + str(self.willpower) \
               + "\n体质: " + str(self.constitution) \
               + "\n智力: " + str(self.intelligence) \
               + "\n\n人物状态: " \
               + "\n压力值: " + str(self.pressure) \
               + "\n钱包余额: " + str(self.wallet) \
               + "\n\n各科成绩：" \
               + "\n语文: %.2f" % round(self.chinese, 2)\
               + "\n数学: %.2f" % round(self.math, 2) \
               + "\n英语: %.2f" % round(self.english, 2) \
               +" \n政治: %.2f" % round(self.political, 2) \
               +" \n历史: %.2f" % round(self.history, 2) \
               +" \n地理: %.2f" % round(self.geography, 2)\
               +" \n物理: %.2f" % round(self.physics, 2)\
               +" \n化学: %.2f" % round(self.chemistry, 2) \
               + "\n生物: %.2f" % round(self.biology, 2)\
               + "\n文综: %.2f" % round(self.geography + self.political + self.history, 2) \
               + "\n理综: %.2f" % round(self.physics + self.chemistry + self.biology, 2)

