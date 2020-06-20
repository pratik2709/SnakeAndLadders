import random

from src.Command import Command


class UnFairDiceCommand(Command):
    def __init__(self, payload):
        self.payload = payload

    def execute(self):
        self.payload.even()
