import random


class UnFairDice:
    def __init__(self):
        pass

    def generateRandomNumber(self):
        return random.randrange(2, 7, 2)