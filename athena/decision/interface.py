from abc import ABC, abstractmethod


class DecisionInterface(ABC):
    """
    Base interface for all poker decision makers.
    """

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def decide(self, state):
        """
        Return poker action based on current state.
        """
        pass