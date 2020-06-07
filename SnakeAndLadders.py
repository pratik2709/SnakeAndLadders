from Dice import Dice
from Player import Player
from SnakeAndLadderBoard import SnakesAndLadderBoard


class SnakesAndLadders:
    def __init__(self):
        self.snakeAndLadderBoard = SnakesAndLadderBoard()
        self.snakeAndLadderBoard.addSnake(14, 7)
        self.player = Player()
        self.turns = 0
        self.dice = Dice()

    def gameOver(self):
        if not self.player.checkIfInBounds() or self.turns > 10:
            return True
        return False

    def playGame(self, fairness=1):
        self.dice = Dice(fairness)
        self.turns += 1
        print("INITIAL PLAYER POSITION:" + str(self.player.playerPosition))
        self.player.movePlayer(self.dice.generateDieRoll())
        if self.gameOver():
            print("GAME OVER")
            return False
        else:
            if self.snakeAndLadderBoard.checkSquareContainsSnake(self.player.playerPosition):
                print("SNAKE FOUND ON:" + str(self.player.playerPosition))
                print(
                    "MOVING TO:"
                    + str(self.snakeAndLadderBoard.getFallbackPostion(self.player.playerPosition)))
                self.player.setPlayerPosition(
                    self.snakeAndLadderBoard.getFallbackPostion(self.player.playerPosition))
            else:
                print("MOVING TO:" + str(self.player.playerPosition))
            return True
