class TrainingSession:
    """
    Connects training process with experiment tracking.
    """


    def __init__(
        self,
        trainer,
        tracker
    ):

        self.trainer = trainer
        self.tracker = tracker



    def run(
        self,
        dataset,
        experiment
    ):

        result = self.trainer.train(
            dataset
        )


        self.tracker.save(
            experiment
        )


        return result
