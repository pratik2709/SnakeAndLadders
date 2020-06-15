import random

from src.Command import Command


class FairDice(Command):
    # excute fairdice on somehting ? like a stereo or a player instead of returning! ??? :D
    def __init__(self):
        pass

    def execute(self):
        return random.randint(1,6)