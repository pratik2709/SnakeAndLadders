import random


class SnakesAndLadders:
    def __init__(self):
        self.positionTable = dict()
        self.intializePositionTable()
        self.addSnake(14, 7)
        self.playerPosition = 0
        self.turns = 0

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

    def movePlayer(self, fairness):
        if fairness == 1:
            random_number = self.generateRandomNumber()
        else:
            random_number = self.generateEvenRandomNumber()
        print("DIE ROLLED IS:" + str(random_number))
        self.playerPosition += random_number

    def checkIfInBounds(self):
        if self.playerPosition > 100:
            return False
        return True

    def checkSquareContainsSnake(self):
        if self.positionTable[self.playerPosition]['fallback'] is not None:
            return True
        return False

    def handleCaseWhenSquareContainsSnake(self):
        self.playerPosition = self.positionTable[self.playerPosition]['fallback']

    def gameOver(self):
        if not self.checkIfInBounds() or self.turns > 10:
            return True
        return False

    def playGame(self, fairness):
        self.turns += 1
        print("INITIAL PLAYER POSITION:" + str(self.playerPosition))
        self.movePlayer(fairness)
        if self.gameOver():
            print("GAME OVER")
            return False
        else:
            if self.checkSquareContainsSnake():
                print("SNAKE FOUND ON:" + str(self.playerPosition))
                print("MOVING TO:" + str(self.positionTable[self.playerPosition]['fallback']))
                self.handleCaseWhenSquareContainsSnake()
            else:
                print("MOVING TO:" + str(self.playerPosition))
            return True


