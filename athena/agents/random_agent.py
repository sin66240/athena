import random

from athena.agents.base import BaseAgent


class RandomAgent(BaseAgent):
    """
    Agent that selects actions randomly.
    Used for simulation testing.
    """

    ACTIONS = [
        "FOLD",
        "CHECK",
        "CALL",
        "BET",
    ]

    def decide_action(self, state):
        return random.choice(self.ACTIONS)