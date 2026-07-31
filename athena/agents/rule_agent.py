from athena.agents.base import BaseAgent


class RuleAgent(BaseAgent):
    """
    Simple rule-based poker agent.
    """

    def decide_action(self, state):

        strength = state.hand_strength

        if strength >= 0.75:
            return "BET"

        if strength >= 0.40:
            return "CALL"

        return "FOLD"