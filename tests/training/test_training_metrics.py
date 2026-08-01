from athena.training.trainer import Trainer


class DummyTrainer(Trainer):

    def __init__(self):

        super().__init__()

        self.calls = 0


    def run_episode(self):

        self.calls += 1

        return self.calls


def test_best_reward():

    trainer = DummyTrainer()

    trainer.train(5)

    assert trainer.best_reward == 5


def test_best_episode():

    trainer = DummyTrainer()

    trainer.train(5)

    assert trainer.best_episode == 5


def test_last_reward():

    trainer = DummyTrainer()

    trainer.train(5)

    assert trainer.last_reward == 5


def test_total_episodes():

    trainer = DummyTrainer()

    trainer.train(5)

    assert trainer.total_episodes == 5


def test_reset_history():

    trainer = DummyTrainer()

    trainer.train(5)

    trainer.reset_history()

    assert trainer.history == []

    assert trainer.total_episodes == 0