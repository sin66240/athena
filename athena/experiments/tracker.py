class ExperimentTracker:
    """
    Store and retrieve experiments.
    """


    def __init__(
        self
    ):

        self.experiments = []



    def save(
        self,
        experiment
    ):

        self.experiments.append(
            experiment
        )

        return experiment



    def list(
        self
    ):

        return self.experiments



    def latest(
        self
    ):

        if not self.experiments:

            return None


        return self.experiments[-1]
