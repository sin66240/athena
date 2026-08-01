from athena.models.poker_model import PokerModel


class MockState:

    pot = 150

    players = [
        "A",
        "B"
    ]

    street = "turn"


def test_model_uses_feature_extractor():

    model = PokerModel()

    model.train([], [])

    action = model.predict(
        MockState()
    )

    assert action == "raise"