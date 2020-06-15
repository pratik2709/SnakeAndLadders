from src.FairDice import FairDice
from src.PlayerInputRemote import PlayerInputRemote
from src.SnakeAndLaddersMain import SnakesAndLadders
from src.UnfairDice import UnFairDice


class Game:
    def playSnakesAndLadders(self):
        snakeAndLadders = SnakesAndLadders()
        playerInputRemote = PlayerInputRemote()
        playerInputRemote.setCommand(1,FairDice())
        playerInputRemote.setCommand(2,UnFairDice())
        print("STARTING GAME...")
        # command pattern ?
        while True:
            playerInput = input(" Press 1 to roll normal die \n Press 2 to roll crooked die\n "
                                "Press q to quit::")
            print(" ")
            snakeAndLadders.playGame(playerInputRemote.buttonPushed(int(playerInput)))
            # if playerInput == "1":
            #     if not snakeAndLadders.playGame(1):
            #         break
            # elif playerInput == "2":
            #     if not snakeAndLadders.playGame(2):
            #         break
            # elif playerInput == "q":
            #     break

