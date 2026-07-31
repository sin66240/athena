from athena.decision.interface import DecisionInterface


class RuleAgent(DecisionInterface):

    def __init__(self, name):
        self.name = name
        self.history = []


    def decide(self, state):

        return self.decide_action(state)


    def decide_action(self, state):

        strength = state.hand_strength


        if strength >= 0.8:
            return "BET"


        elif strength >= 0.4:
            return "CALL"


        else:
            return "FOLD"


    def observe(self, data):

        self.history.append(data)