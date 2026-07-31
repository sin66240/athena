from athena.features.poker_features import PokerFeatureExtractor


class MockState:

    pot = 100

    players = [
        "A",
        "B"
    ]

    street = "flop"



def test_feature_extraction():

    extractor = PokerFeatureExtractor()

    result = extractor.extract(
        MockState()
    )


    assert result["pot"] == 100

    assert result["player_count"] == 2

    assert result["street"] == 1