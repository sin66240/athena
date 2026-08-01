from athena.training.trainer import Trainer
from athena.training.callbacks import TrainingCallback



class MockCallback(TrainingCallback):

    def __init__(self):

        self.events = []


    def on_train_start(
        self,
        trainer
    ):

        self.events.append(
            "start"
        )


    def on_episode_end(
        self,
        trainer,
        episode,
        reward
    ):

        self.events.append(
            "episode"
        )


    def on_best_model(
        self,
        trainer,
        reward
    ):

        self.events.append(
            "best"
        )


    def on_train_end(
        self,
        trainer
    ):

        self.events.append(
            "end"
        )



class DummyTrainer(Trainer):

    def run_episode(self):

        return 10



def test_trainer_callback_events():

    callback = MockCallback()


    trainer = DummyTrainer(
        callbacks=[
            callback
        ]
    )


    trainer.train(3)


    assert callback.events[0] == "start"

    assert "episode" in callback.events

    assert "best" in callback.events

    assert callback.events[-1] == "end"