from src.SnakeAndLaddersVisualBoard import SnakesAndLaddersVisualBoard


class SnakesAndLadderBoard:
    def __init__(self):
        self.positionTable = dict()
        self.intializePositionTable()
        self.visual = SnakesAndLaddersVisualBoard(self)


    def intializePositionTable(self):
        for i in range(1,101):
            self.positionTable[i] = {
                "fallback": None,
                "boardPosition": None
            }

    def addSnake(self, current_position, slip_position):
        self.positionTable[current_position]['fallback'] = slip_position

    def checkSquareContainsSnake(self, current_position):
        if self.positionTable[current_position]['fallback'] is not None:
            return True
        return False

    def getFallbackPostion(self, current_position):
        return self.positionTable[current_position]['fallback']

