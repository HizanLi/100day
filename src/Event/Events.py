from src.Character.player.mainPlayer import mainPlayer


class events: #事件
    intelligence_coefficient = 0.05
    luck_coefficient = 0.05
    strength_coefficient = 0.05
    dexterity_coefficient = 0.05
    constitution_coefficient = 0.05
    charm_coefficient = 0.05
    willpower_coefficient = 0.05

    def study(self,mainPlayer):
        mainPlayer.knowledge += 1 + (mainPlayer.intelligence-10)*self.intelligence_coefficient + (mainPlayer.luck-10)*self.luck_coefficient
        mainPlayer.experience += 0.5 + (mainPlayer.intelligence-10)*self.intelligence_coefficient + (mainPlayer.luck-10)*self.luck_coefficient

        mainPlayer.pressure += 1 - (mainPlayer.willpower-10)*self.willpower_coefficient - (mainPlayer.luck-10)*self.luck_coefficient

    def reading(self,mainPlayer):
        mainPlayer.knowledge += 0.5 + (mainPlayer.intelligence-10)*self.intelligence_coefficient + (mainPlayer.luck-10)*self.luck_coefficient
        mainPlayer.experience += 1 + (mainPlayer.intelligence-10)*self.intelligence_coefficient + (mainPlayer.luck-10)*self.luck_coefficient

        mainPlayer.pressure -= 1 - (mainPlayer.willpower-10)*self.willpower_coefficient - (mainPlayer.luck-10)*self.luck_coefficient

