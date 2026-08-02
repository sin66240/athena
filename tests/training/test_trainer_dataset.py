from athena.training.trainer import Trainer
from athena.dataset.training_dataset import TrainingDataset



def test_trainer_with_dataset():

    dataset = TrainingDataset()


    dataset.add(
        state={"hand":"AA"},
        action="raise",
        reward=10
    )


    trainer = Trainer(
        dataset=dataset
    )


    result = trainer.train()


    assert result is not None
