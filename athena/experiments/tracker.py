class Tracker:
    """
    Tracks experiment results.
    """


    def __init__(
        self
    ):

        self.experiments = []



    def log(
        self,
        experiment_result
    ):

        self.experiments.append(
            experiment_result
        )



    def save(
        self,
        experiment
    ):

        self.experiments.append(
            experiment
        )



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



    def best(
        self,
        metric
    ):

        if not self.experiments:

            return None


        return max(
            self.experiments,
            key=lambda x: x.metrics.get(
                metric,
                float("-inf")
            )
        )



class ExperimentTracker(Tracker):
    """
    Backward compatible tracker.
    """

    pass
