import random


class Dice:
    def __init__(self, ):
        pass

    def even(self):
        return random.randrange(2, 7, 2)

    def odd(self):
        return random.randint(1,6)



