class TrainingCallback:
    """
    Base callback interface for training events.
    """


    def on_train_start(
        self,
        trainer
    ):
        pass



    def on_episode_end(
        self,
        trainer,
        episode,
        reward
    ):
        pass



    def on_best_model(
        self,
        trainer,
        reward
    ):
        pass



    def on_train_end(
        self,
        trainer
    ):
        pass