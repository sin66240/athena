class Experiment:
    """
    Represents a training experiment run.
    """


    def __init__(
        self,
        name,
        model_version,
        feature_version,
        dataset_version
    ):

        self.name = name

        self.model_version = model_version

        self.feature_version = feature_version

        self.dataset_version = dataset_version



    def to_dict(
        self
    ):

        return {
            "name": self.name,
            "model_version": self.model_version,
            "feature_version": self.feature_version,
            "dataset_version": self.dataset_version
        }
