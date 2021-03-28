import numpy


class mainTraits(object):  # 人物特性

    # 运气
    luck_positive = ["顺水顺风,luck,+1", "万事如意,luck,+2", "吉人天相,luck,+3"]
    luck_negative = ["祸不单行,luck,-1", "背禄逐马,luck,-2", "丧门灾星,luck,-3"]

    # 魅力
    charm_positive = ["一表非凡,charm,+1", "气宇轩昂,charm,+2", "玉树临风,charm,+3"]
    charm_negative = ["獐头鼠目,charm,-1", "不堪入目,charm,-2", "百拙千丑,charm,-3"]

    # 力量
    strength_positive = ["孔武有力,strength,+1", "力大无穷,strength,+2", "摇山振岳,strength,+3"]
    strength_negative = ["文弱无力,strength,-1", "无力缚鸡,strength,-2", "力若蚍蜉,strength,-3"]

    # 敏捷
    dexterity_positive = ["耳聪目明,dexterity,+1", "剖决如流,dexterity,+2", "诡变无踪,dexterity,+3"]
    dexterity_negative = ["蛮手蛮脚,dexterity,-1", "手拙口夯,dexterity,-2", "钝似泥偶,dexterity,-3"]

    # 意志力
    willpower_positive = ["刚毅隐忍,willpower,+1", "百折不挠,willpower,+2", "始终如一,willpower,+3"]
    willpower_negative = ["心猿意马,willpower,-1", "柔懦寡断,willpower,-2", "桃花七煞,willpower,-3"]

    # 体质
    constitution_positive = ["身强体健,constitution,+1", "龙神马壮,constitution,+2", "天人骨血,constitution,+3"]
    constitution_negative = ["身如薄柳,constitution,-1", "弱不禁风,constitution,-2", "羸弱早夭,constitution,-3"]

    # 智力
    intelligence_positive = ["才思敏捷,intelligence,+1", "灵心慧性,intelligence,+2", "智绝无双,intelligence,+3"]
    intelligence_negative = ["傻头傻脑,intelligence,-1", "呆若木鸡,intelligence,-2", "蠢笨如猪,intelligence,-3"]

    attributes_positive = ['luck','charm','strength','dexterity','willpower','constitution','intelligence']
    attributes_positive_possibility = [0.1, 0.10, 0.16, 0.16, 0.16, 0.16, 0.16]
    attribute_positive_possibility=[0.8,0.15,0.05]

    attributes_negative = ['luck','charm','strength','dexterity','willpower','constitution','intelligence']
    attributes_negative_possibility = [0.1, 0.10, 0.16, 0.16, 0.16, 0.16, 0.16]
    attribute_negative_possibility=[0.8,0.15,0.05]



    def generate(self,difficulty):
        print("generate is called")
        #generate positive
        count = 0
        if difficulty == 'hard':
            time = 2
        elif difficulty == 'easy':
            time = 4
        else:
            time = 3
        print("generate_positive is called, and count is " + str(time))
        positive_result = []
        attributes_result=[]
        while count < time:
            temp = numpy.random.choice(self.attributes_positive, p=self.attributes_positive_possibility)
            if temp not in positive_result:
                positive_result.append(temp)
                count += 1

        for attribute in positive_result:
            temp = numpy.random.choice(eval("self."+attribute+"_positive"),p=self.attribute_positive_possibility)
            attributes_result.append(temp)
        #generate negative
        count = 0
        if difficulty == 'hard':
            time = 2
        elif difficulty == 'easy':
            time = 0
        else:
            time = 1
        print("generate_negative is called, and count is " + str(time))
        negative_result = []
        while count < time:
            temp = numpy.random.choice(self.attributes_negative, p=self.attributes_negative_possibility)
            if temp not in positive_result and temp not in negative_result:
                negative_result.append(temp)
                count += 1

        for attribute in negative_result:
            temp = numpy.random.choice(eval("self."+attribute+"_negative"),p=self.attribute_negative_possibility)
            attributes_result.append(temp)

        return attributes_result