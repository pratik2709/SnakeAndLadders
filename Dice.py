from FairDice import FairDice
from UnfairDice import UnFairDice


class Dice:
    def __init__(self, fair):
        self.fair = fair
        self.caller = None
        self.setCaller()

    def setCaller(self):
        if self.fair == 1:
            self.caller = FairDice()
        else:
            self.caller = UnFairDice()

    def generateDieRoll(self):
        return self.caller.generateRandomNumber()



