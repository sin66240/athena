from athena.features.poker_features import PokerFeatureExtractor


class PokerModel:
    """
    Simple poker model interface.
    """

    def __init__(self):

        self.extractor = PokerFeatureExtractor()
        self.is_trained = False

    def train(self, features, labels):

        self.is_trained = True

    def predict(self, state):

        if not self.is_trained:
            raise RuntimeError(
                "Model has not been trained."
            )

        features = self.extractor.extract(
            state
        )

        if features["street"] == 0:
            return "call"

        if features["pot"] > 100:
            return "raise"

        return "fold"