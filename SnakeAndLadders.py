class SnakesAndLadders:
    def __init__(self):
        self.positionTable = dict()
        self.intializePositionTable()

    def intializePositionTable(self):
        for i in range(1,101):
            self.positionTable[i] = {
                "fallback": None,
                "boardPosition": None
            }