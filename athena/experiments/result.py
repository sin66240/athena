class ExperimentResult:
    """
    Represents the outcome of an experiment run.
    """


    def __init__(
        self,
        experiment_name,
        status,
        metrics=None
    ):

        self.experiment_name = experiment_name

        self.status = status

        self.metrics = metrics or {}



    def to_dict(
        self
    ):

        return {
            "experiment_name": self.experiment_name,
            "status": self.status,
            "metrics": self.metrics
        }
