from athena.training.trainer import Trainer
from athena.training.history import TrainingHistory


class MockModel:

    def fit(self, dataset):

        return {
            "loss": 0.1,
            "accuracy": 0.95
        }



def test_trainer_records_history():

    history = TrainingHistory()


    trainer = Trainer(
        model=MockModel(),
        history=history
    )


    trainer.train(
        dataset=[1,2,3]
    )


    assert len(
        history.records
    ) == 1


    assert history.latest()["metrics"]["accuracy"] == 0.95
