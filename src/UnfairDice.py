import random

from src.Command import Command


class UnFairDice(Command):
    def __init__(self):
        pass

    def execute(self):
        return random.randrange(2, 7, 2)