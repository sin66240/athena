import os
import pickle

from athena.training.callbacks import TrainingCallback



class CheckpointCallback(TrainingCallback):
    """
    Save best model checkpoint.
    """


    def __init__(
        self,
        path="checkpoint.pkl"
    ):

        self.path = path
        self.saved = False



    def on_best_model(
        self,
        trainer,
        reward
    ):

        if trainer.agent is None:
            return


        with open(
            self.path,
            "wb"
        ) as f:

            pickle.dump(
                trainer.agent,
                f
            )


        self.saved = True