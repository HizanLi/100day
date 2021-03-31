from src.Character.player.mainPlayer import mainPlayer

#Normal 普通事件 0
#Special 特殊事件 1
#Limit  限定事件 2

class mainEvent(object): #事件

    def trans_sub(self,result_en):
        result_cn = []
        for sub in result_en:
            if sub == 'chinese':
                result_cn.append('语文')
            elif sub == 'math':
                result_cn.append('数学')
            elif sub == 'english':
                result_cn.append('英语')
            elif sub == 'political':
                result_cn.append('政治')
            elif sub == 'history':
                result_cn.append('历史')
            elif sub == 'geography':
                result_cn.append('地理')
            elif sub == 'physics':
                result_cn.append('物理')
            elif sub == 'chemistry':
                result_cn.append('化学')
            elif sub == 'biology':
                result_cn.append('生物')
        return result_cn