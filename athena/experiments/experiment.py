class Experiment:
    """
    Represents a training experiment run.
    """


    def __init__(
        self,
        name,
        model_version,
        feature_version,
        dataset_version,
        hyperparameters=None
    ):

        self.name = name

        self.model_version = model_version

        self.feature_version = feature_version

        self.dataset_version = dataset_version

        self.hyperparameters = hyperparameters



    def to_dict(
        self
    ):

        data = {
            "name": self.name,
            "model_version": self.model_version,
            "feature_version": self.feature_version,
            "dataset_version": self.dataset_version
        }


        if self.hyperparameters is not None:

            data["hyperparameters"] = (
                self.hyperparameters.to_dict()
            )

        else:

            data["hyperparameters"] = None


        return data
