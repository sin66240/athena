class FeatureStore:
    """
    Store generated features.
    """


    def __init__(
        self
    ):

        self.storage = []



    def save(
        self,
        features
    ):

        self.storage.append(
            features
        )

        return features



    def all(
        self
    ):

        return self.storage
