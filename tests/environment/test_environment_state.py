from athena.environment.poker_env import PokerEnvironment
from athena.agents.random_agent import RandomAgent
from athena.agents.rule_agent import RuleAgent
from athena.state.game_state import GameState


def test_environment_uses_game_state():

    players = [
        RandomAgent("A"),
        RuleAgent("B"),
    ]

    env = PokerEnvironment(players)

    env.reset()

    assert isinstance(
        env.state,
        GameState
    )


def test_state_has_players():

    players = [
        RandomAgent("A"),
        RuleAgent("B"),
    ]

    env = PokerEnvironment(players)

    env.reset()

    assert len(env.state.players) == 2