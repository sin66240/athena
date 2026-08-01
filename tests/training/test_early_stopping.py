from athena.training.trainer import Trainer


class DummyTrainer(Trainer):

    def __init__(self):

        super().__init__()

        self.rewards = [
            10,
            12,
            12,
            12,
            12
        ]

        self.index = 0


    def run_episode(self):

        reward = self.rewards[self.index]

        self.index += 1

        return reward



def test_early_stopping_trigger():

    trainer = DummyTrainer()

    trainer.train(
        episodes=10,
        patience=2
    )

    assert trainer.stopped_early is True



def test_stop_reason():

    trainer = DummyTrainer()

    trainer.train(
        episodes=10,
        patience=2
    )

    assert trainer.stop_reason == "No improvement"



def test_no_early_stop():

    trainer = DummyTrainer()

    trainer.rewards = [
        1,
        2,
        3,
        4,
        5
    ]

    trainer.train(
        episodes=5,
        patience=2
    )

    assert trainer.stopped_early is False