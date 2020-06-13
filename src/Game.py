from src.SnakeAndLaddersMain import SnakesAndLadders


class Game:
    def playSnakesAndLadders(self):
        snakeAndLadders = SnakesAndLadders()
        print("STARTING GAME...")
        # command pattern ?
        while True:
            playerInput = input(" Press 1 to roll normal die \n Press 2 to roll crooked die\n "
                                "Press q to quit::")
            print(" ")
            if playerInput == "1":
                if not snakeAndLadders.playGame(1):
                    break
            elif playerInput == "2":
                if not snakeAndLadders.playGame(2):
                    break
            elif playerInput == "q":
                break

class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self) -> None:
        pass
