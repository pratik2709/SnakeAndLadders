from abc import abstractmethod


class Command(object):
    """
    The Command interface declares a method for executing a command.
    """
    def execute(self) -> None:
        pass