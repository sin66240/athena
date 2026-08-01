from athena.features.poker_features import PokerFeatureExtractor


class FeatureExtractor:
    """
    Extract features from domain objects.
    """


    def __init__(
        self,
        extractor=None
    ):

        self.extractor = extractor or PokerFeatureExtractor()



    def extract(
        self,
        state
    ):

        return self.extractor.extract(
            state
        )
