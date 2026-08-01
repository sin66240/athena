from athena.training.trainer import Trainer


class DummyTrainer(Trainer):

    def __init__(self):

        super().__init__()

        self.calls = 0


    def run_episode(self):

        self.calls += 1

        return self.calls


def test_training_history():

    trainer = DummyTrainer()

    trainer.train(3)

    assert trainer.history == [1, 2, 3]


def test_average_reward():

    trainer = DummyTrainer()

    trainer.train(3)

    assert trainer.average_reward() == 2.0