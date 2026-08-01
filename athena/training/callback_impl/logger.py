from athena.training.callbacks import TrainingCallback


class LoggerCallback(TrainingCallback):
    """
    Simple training logger callback.
    """


    def __init__(self):

        self.logs = []


    def on_train_start(
        self,
        trainer
    ):

        self.logs.append(
            "Training started"
        )


    def on_episode_end(
        self,
        trainer,
        episode,
        reward
    ):

        self.logs.append(
            f"Episode {episode}: reward={reward}"
        )


    def on_best_model(
        self,
        trainer,
        reward
    ):

        self.logs.append(
            f"Best model reward={reward}"
        )


    def on_train_end(
        self,
        trainer
    ):

        self.logs.append(
            "Training finished"
        )