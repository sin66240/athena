from athena.training.trainer import Trainer
from athena.training.result import TrainingResult


class MockModel:

    def fit(self, data):
        return {
            "loss": 0.1,
            "accuracy": 0.9
        }



def test_trainer_returns_result():

    trainer = Trainer(
        model=MockModel()
    )


    result = trainer.train(
        dataset=[
            1,
            2,
            3
        ]
    )


    assert isinstance(
        result,
        TrainingResult
    )


    assert result.metrics["accuracy"] == 0.9
