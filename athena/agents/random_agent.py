import random

from athena.decision.interface import DecisionInterface


class RandomAgent(DecisionInterface):

    ACTIONS = [
        "fold",
        "call",
        "raise",
    ]


    def __init__(self, name):

        self.name = name
        self.history = []


    def decide(self, state):

        return self.decide_action(state)


    def decide_action(self, state):

        return random.choice(
            self.ACTIONS
        )


    def observe(self, data):

        self.history.append(data)