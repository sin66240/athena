from athena.training.callback_impl.logger import LoggerCallback



class MockTrainer:
    pass



def test_logger_callback():

    callback = LoggerCallback()

    trainer = MockTrainer()


    callback.on_train_start(
        trainer
    )


    callback.on_episode_end(
        trainer,
        1,
        10
    )


    callback.on_best_model(
        trainer,
        10
    )


    callback.on_train_end(
        trainer
    )


    assert len(callback.logs) == 4

    assert callback.logs[0] == "Training started"

    assert "Episode 1" in callback.logs[1]

    assert "Best model" in callback.logs[2]

    assert callback.logs[3] == "Training finished"