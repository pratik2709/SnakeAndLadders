class SnakesAndLadders:
    def __init__(self):
        self.positionTable = dict()
        self.intializePositionTable()
        self.addSnake(14, 7)

    def intializePositionTable(self):
        for i in range(1,101):
            self.positionTable[i] = {
                "fallback": None,
                "boardPosition": None
            }

    def addSnake(self, current_position, slip_position):
        self.positionTable[current_position]['fallback'] = slip_position