class Player:
    def __init__(self):
        self.playerPosition = 0

    def movePlayer(self, number):
        print("DIE ROLLED IS:" + str(number))
        self.playerPosition += number

    def checkIfInBounds(self):
        if self.playerPosition > 100:
            return False
        return True

    def setPlayerPosition(self, position):
        self.playerPosition = position