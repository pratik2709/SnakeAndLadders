import random

from Dice import Dice
from Player import Player


class SnakesAndLadders:
    def __init__(self):
        self.positionTable = dict()
        self.intializePositionTable()
        self.addSnake(14, 7)
        self.player = Player()
        self.turns = 0
        self.dice = None

    def intializePositionTable(self):
        for i in range(1,101):
            self.positionTable[i] = {
                "fallback": None,
                "boardPosition": None
            }

    def addSnake(self, current_position, slip_position):
        self.positionTable[current_position]['fallback'] = slip_position

    def checkSquareContainsSnake(self):
        if self.positionTable[self.player.playerPosition]['fallback'] is not None:
            return True
        return False

    def handleCaseWhenSquareContainsSnake(self):
        self.player.playerPosition = self.positionTable[self.player.playerPosition]['fallback']

    def gameOver(self):
        if not self.player.checkIfInBounds() or self.turns > 10:
            return True
        return False

    def playGame(self, fairness):
        self.dice = Dice(fairness)
        self.turns += 1
        print("INITIAL PLAYER POSITION:" + str(self.player.playerPosition))
        self.player.movePlayer(self.dice.generateDieRoll())
        if self.gameOver():
            print("GAME OVER")
            return False
        else:
            if self.checkSquareContainsSnake():
                print("SNAKE FOUND ON:" + str(self.player.playerPosition))
                print("MOVING TO:" + str(self.positionTable[self.player.playerPosition]['fallback']))
                self.handleCaseWhenSquareContainsSnake()
            else:
                print("MOVING TO:" + str(self.player.playerPosition))
            return True


