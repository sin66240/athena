class PokerFeatureExtractor:
    """
    Converts poker state into numerical features.
    """

    def extract(self, state):

        features = {}

        features["pot"] = state.pot

        features["player_count"] = len(
            state.players
        )

        features["street"] = self.encode_street(
            state.street
        )

        return features


    def encode_street(self, street):

        mapping = {
            "preflop": 0,
            "flop": 1,
            "turn": 2,
            "river": 3
        }

        return mapping.get(
            street,
            -1
        )