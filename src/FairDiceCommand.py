import random

from src.Command import Command


class FairDiceCommand(Command):
    # excute fairdice on somehting ?
    #  like a stereo or a player instead of returning! ??? :D
    # correction fair and unfiar are just commands operating on dice object
    # should dice notify player?

    def __init__(self, payload):
        self.payload = payload

    def execute(self):
        self.payload.odd()

