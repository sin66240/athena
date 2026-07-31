from athena.decision.interface import DecisionInterface


class DummyDecision(DecisionInterface):

    def decide(self, state):
        return "fold"


def test_decision_interface():

    agent = DummyDecision("Test")

    assert agent.name == "Test"

    assert agent.decide(None) == "fold"