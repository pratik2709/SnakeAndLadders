from src.Player import Player
from src.SnakeAndLadderBoard import SnakesAndLadderBoard


class SnakesAndLadders:
    def __init__(self, player):
        self.snakeAndLadderBoard = SnakesAndLadderBoard()
        self.snakeAndLadderBoard.addSnake(14, 7)
        self.snakeAndLadderBoard.addSnake(18, 1)
        self.snakeAndLadderBoard.addSnake(6, 1)
        self.snakeAndLadderBoard.addSnake(4, 1)
        self.snakeAndLadderBoard.addSnake(2, 1)
        self.turns = 0
        self.player = player

    def gameOver(self):
        if not self.player.checkIfInBounds() or self.turns > 10:
            return True
        return False

    def playGame(self):
        self.turns += 1
        print("TURN NUMBER:" + str(self.turns))
        print("INITIAL PLAYER POSITION:" + str(self.player.playerPosition))
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
        print("GAME OVER")
        self.handleVisualBoard()
        return False

    def handleVisualBoard(self):
        self.snakeAndLadderBoard.visual.showPlayerPositionOnBoard(self.player.playerPosition)