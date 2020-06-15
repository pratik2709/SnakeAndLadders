from src.FairDice import FairDice
from src.Player import Player
from src.PlayerInputRemote import PlayerInputRemote
from src.SnakeAndLaddersMain import SnakesAndLadders
from src.UnfairDice import UnFairDice


class Game:
    def playSnakesAndLadders(self):
        playerInputRemote = PlayerInputRemote()
        player = Player()
        snakeAndLadders = SnakesAndLadders(player)
        fairDice = FairDice(player)
        unFairDice = UnFairDice(player)
        playerInputRemote.setCommand(1,fairDice)
        playerInputRemote.setCommand(2,unFairDice)

        print("STARTING GAME...")
        # command pattern ?
        while True:
            playerInput = input(" Press 1 to roll normal die \n Press 2 to roll crooked die\n "
                                "Press q to quit::")
            print(" ")
            playerInputRemote.buttonPushed(int(playerInput))
            print(player.playerPosition)
            snakeAndLadders.playGame()

