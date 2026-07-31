from athena.environment.betting_round import BettingRound
from athena.environment.actions import Action


class DummyPlayer:

    def __init__(self, name):
        self.name = name



def test_call_adds_pot():

    players = [
        DummyPlayer("A"),
        DummyPlayer("B"),
    ]

    round = BettingRound(players)

    round.apply_action(
        players[0],
        Action.CALL,
        50
    )

    assert round.pot == 50
    assert round.chips["A"] == 950



def test_fold_removes_player():

    players = [
        DummyPlayer("A"),
        DummyPlayer("B"),
    ]

    round = BettingRound(players)

    round.apply_action(
        players[0],
        Action.FOLD
    )

    assert len(round.active_players()) == 1