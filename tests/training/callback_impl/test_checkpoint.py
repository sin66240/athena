import os

from athena.training.callback_impl.checkpoint import CheckpointCallback



class MockAgent:

    pass



class MockTrainer:

    def __init__(self):

        self.agent = MockAgent()



def test_checkpoint_save(tmp_path):

    path = tmp_path / "model.pkl"


    callback = CheckpointCallback(
        str(path)
    )


    trainer = MockTrainer()


    callback.on_best_model(
        trainer,
        100
    )


    assert callback.saved is True

    assert os.path.exists(path)