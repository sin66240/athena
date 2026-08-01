from athena.training.trainer import Trainer


class DummyTrainer(Trainer):

    def __init__(self):

        super().__init__()

        self.calls = 0


    def run_episode(self):

        self.calls += 1

        return 10


def test_train_multiple_episodes():

    trainer = DummyTrainer()

    reward = trainer.train(5)

    assert trainer.calls == 5

    assert reward == 50


def test_train_zero_episode():

    trainer = DummyTrainer()

    reward = trainer.train(0)

    assert trainer.calls == 0

    assert reward == 0