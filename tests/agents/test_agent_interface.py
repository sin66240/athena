from athena.agents.random_agent import RandomAgent
from athena.agents.rule_agent import RuleAgent
from athena.decision.interface import DecisionInterface


def test_agents_use_interface():

    agents = [
        RandomAgent("Random"),
        RuleAgent("Rule"),
    ]


    for agent in agents:

        assert isinstance(
            agent,
            DecisionInterface
        )


def test_agents_can_decide():

    agent = RandomAgent("Test")

    action = agent.decide(None)

    assert action in [
        "fold",
        "call",
        "raise"
    ]