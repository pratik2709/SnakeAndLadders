from src.Dice import Dice
from src.Player import Player
from src.SnakeAndLadderBoard import SnakesAndLadderBoard


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
        print("TURN NUMBER:" + str(self.turns))
        print("INITIAL PLAYER POSITION:" + str(self.player.playerPosition))
        self.player.movePlayer(self.dice.generateDieRoll())
        if self.gameOver():
            return self.handleGameOver()
        else:
            return self.handleNormalGame()

    def handleNormalGame(self):
        if self.snakeAndLadderBoard.checkSquareContainsSnake(self.player.playerPosition):
            print("ALERT!! SNAKE FOUND ON:" + str(self.player.playerPosition))
            print(
                "MOVING TO:"
                + str(self.snakeAndLadderBoard.getFallbackPostion(self.player.playerPosition)))
            self.player.setPlayerPosition(
                self.snakeAndLadderBoard.getFallbackPostion(self.player.playerPosition))
            self.handleVisualBoard()
        else:
            print("MOVING TO:" + str(self.player.playerPosition))
            self.handleVisualBoard()
        return True

    def handleGameOver(self):
        print("MOVING TO:" + str(self.player.playerPosition))
        print("GAME OVER")
        self.handleVisualBoard()
        return False

    def handleVisualBoard(self):
        self.snakeAndLadderBoard.visual.showPlayerPositionOnBoard(self.player.playerPosition)