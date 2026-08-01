from athena.training.trainer import Trainer
from athena.dataset.training_dataset import TrainingDataset


def test_trainer_accepts_dataset():

    dataset = TrainingDataset()

    trainer = Trainer(dataset)

    assert trainer.dataset is dataset


def test_trainer_uses_dataset():

    dataset = TrainingDataset()

    dataset.add(
        state={"pot": 100},
        action="raise",
        reward=1.0,
    )

    trainer = Trainer(dataset)

    assert len(trainer.dataset) == 1