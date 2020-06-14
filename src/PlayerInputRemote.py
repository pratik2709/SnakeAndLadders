from src.NoCommand import NoCommand


class PlayerInputRemote(object):
    def __init__(self):
        self.commands = []
        self.noCommand = NoCommand()
        self.intializePlayerInputRemote()

    def intializePlayerInputRemote(self):
        # putting 4 slots in the player remote: Fair, unfair, quit and nocommand
        for i in range(1,5):
            self.commands.append(self.noCommand)