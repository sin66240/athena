from athena.agents.rule_agent import RuleAgent


class MockState:

    def __init__(self, strength):
        self.hand_strength = strength



def test_rule_agent_name():

    agent = RuleAgent("RuleBot")

    assert agent.name == "RuleBot"



def test_rule_agent_strong_hand():

    agent = RuleAgent("Bot")

    state = MockState(0.9)

    assert agent.decide_action(state) == "BET"



def test_rule_agent_medium_hand():

    agent = RuleAgent("Bot")

    state = MockState(0.5)

    assert agent.decide_action(state) == "CALL"



def test_rule_agent_weak_hand():

    agent = RuleAgent("Bot")

    state = MockState(0.2)

    assert agent.decide_action(state) == "FOLD"