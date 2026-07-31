from athena.state.game_state import GameState


class DummyPlayer:

    def __init__(self, name):
        self.name = name



def test_add_player():

    state = GameState()

    player = DummyPlayer("A")

    state.add_player(player)

    assert len(state.players) == 1



def test_hand_storage():

    state = GameState()

    cards = ["A", "K"]

    state.set_hand(
        "A",
        cards
    )

    assert state.get_hand("A") == cards



def test_advance_street():

    state = GameState()

    state.advance_street()

    assert state.street == "flop"