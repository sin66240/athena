from athena.environment.poker_env import PokerEnvironment
from athena.agents.random_agent import RandomAgent
from athena.agents.rule_agent import RuleAgent


def test_environment_reset():

    players = [
        RandomAgent("A"),
        RuleAgent("B"),
    ]

    env = PokerEnvironment(players)

    state = env.reset()

    assert "hands" in state
    assert len(state["hands"]) == 2


def test_environment_step():

    players = [
        RandomAgent("A"),
        RuleAgent("B"),
    ]

    env = PokerEnvironment(players)

    env.reset()

    result = env.step()

    assert "winner" in result
    assert "reward" in result