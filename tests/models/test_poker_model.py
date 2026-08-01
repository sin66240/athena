import pytest

from athena.models.poker_model import PokerModel


class MockState:

    pot = 50

    players = [
        "A",
        "B"
    ]

    street = "preflop"


def test_model_train():

    model = PokerModel()

    model.train([], [])

    assert model.is_trained is True


def test_predict_before_training():

    model = PokerModel()

    with pytest.raises(RuntimeError):
        model.predict(MockState())


def test_predict_after_training():

    model = PokerModel()

    model.train([], [])

    action = model.predict(MockState())

    assert action == "call"