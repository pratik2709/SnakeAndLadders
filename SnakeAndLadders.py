import random


class SnakesAndLadders:
    def __init__(self):
        self.positionTable = dict()
        self.intializePositionTable()
        self.addSnake(14, 7)
        self.playerPosition = 0

    def intializePositionTable(self):
        for i in range(1,101):
            self.positionTable[i] = {
                "fallback": None,
                "boardPosition": None
            }

    def addSnake(self, current_position, slip_position):
        self.positionTable[current_position]['fallback'] = slip_position

    def generateRandomNumber(self):
        return random.randint(1,6)

    def generateEvenRandomNumber(self):
        return random.randrange(2,7,2)

    def movePlayer(self):
        random_number = self.generateRandomNumber()
        self.playerPosition += random_number

    def checkIfInBounds(self):
        if self.playerPosition > 100:
            return False
        return True

    def handleCaseWhenSquareContainsSnake(self):
        self.playerPosition = self.positionTable[self.playerPosition]['fallback']
