import random

from src.Command import Command


class FairDice(Command):
    # excute fairdice on somehting ?
    #  like a stereo or a player instead of returning! ??? :D
    # correction fair and unfiar are just commands operating on dice object
    # should dice notify player?

    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.movePlayer(random.randint(1,6))
