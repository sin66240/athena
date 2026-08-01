from athena.features.extractor import FeatureExtractor


class MockState:

    pot = 100

    players = [
        1,
        2
    ]

    street = "flop"



def test_feature_extractor():

    extractor = FeatureExtractor()

    result = extractor.extract(
        MockState()
    )

    assert result["pot"] == 100
    assert result["player_count"] == 2
