class ModelMetadata:
    """
    Store model artifact metadata.
    """


    def __init__(
        self,
        name,
        feature_version,
        dataset_version,
        score
    ):

        self.name = name

        self.feature_version = feature_version

        self.dataset_version = dataset_version

        self.score = score



    def to_dict(
        self
    ):

        return {
            "name": self.name,
            "feature_version": self.feature_version,
            "dataset_version": self.dataset_version,
            "score": self.score
        }
