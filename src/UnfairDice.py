import random

from src.Command import Command


class UnFairDice(Command):
    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.movePlayer(random.randrange(2, 7, 2))
