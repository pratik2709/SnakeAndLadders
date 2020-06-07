import pandas as pd


class SnakesAndLadderBoard:
    def __init__(self):
        self.positionTable = dict()
        self.intializePositionTable()
        self.m = 10
        self.n = 10
        self.mat = [[0 for _ in range(0, self.m)] for _ in range(0, self.n)]
        self.zigzagLevelOrder()

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

    def zigzagLevelOrder(self):
        # goto last m
        count = 1
        lastx = self.n - 1
        lasty = 0
        increment = True
        while lastx >= 0:
            self.mat[lastx][lasty] = count
            self.positionTable[count]['boardPosition'] = (lastx,lasty)
            count += 1
            if increment:
                lasty += 1
            else:
                lasty -= 1
            if lasty > self.m-1 or lasty < 0:
                lastx -= 1
                if increment:
                    lasty = self.m - 1
                    increment = False
                else:
                    lasty = 0
                    increment = True

    def showPlayerPositionOnBoard(self, position):
        lastx, lasty = self.positionTable[position]['boardPosition']
        temp = self.mat[lastx][lasty]
        self.mat[lastx][lasty] = "*P*"
        self.showBoard()
        self.mat[lastx][lasty] = temp
        print("********************")

    def showBoard(self):
        print((pd.DataFrame(self.mat)))