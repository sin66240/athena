from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """
    Base interface for all poker agents.
    """

    def __init__(self, name: str):
        self.name = name
        self.history = []

    @abstractmethod
    def decide_action(self, state):
        """
        Decide next poker action.
        """
        pass

    def observe(self, result):
        """
        Store game result.
        """
        self.history.append(result)

    def learn(self):
        """
        Learning hook for trainable agents.
        """
        pass