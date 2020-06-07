import pandas as pd


class SnakesAndLaddersVisualBoard:
    def __init__(self, dataStore):
        self.dataStore = dataStore
        self.m = 10
        self.n = 10
        self.mat = [[0 for _ in range(0, self.m)] for _ in range(0, self.n)]
        self.zigzagLevelOrder()

    def zigzagLevelOrder(self):
        # goto last m
        count = 1
        lastx = self.n - 1
        lasty = 0
        increment = True
        while lastx >= 0:
            self.mat[lastx][lasty] = count
            self.dataStore.positionTable[count]['boardPosition'] = (lastx,lasty)
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
        lastx, lasty = self.dataStore.positionTable[position]['boardPosition']
        temp = self.mat[lastx][lasty]
        self.mat[lastx][lasty] = "*P*"
        self.showBoard()
        self.mat[lastx][lasty] = temp
        print("********************")

    def showBoard(self):
        print((pd.DataFrame(self.mat)))