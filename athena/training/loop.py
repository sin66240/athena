class TrainingLoop:
    """
    Controls self-play and training cycle.
    """


    def __init__(
        self,
        selfplay,
        trainer,
        dataset
    ):

        self.selfplay = selfplay
        self.trainer = trainer
        self.dataset = dataset



    def run_cycle(
        self,
        episodes=1
    ):

        games = self.selfplay.run(
            episodes
        )


        for game in games:

            self.dataset.add(
                state=game,
                action=None,
                reward=0
            )


        result = self.trainer.train(
            self.dataset
        )


        return result