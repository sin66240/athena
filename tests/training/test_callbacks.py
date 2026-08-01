from athena.training.callbacks import TrainingCallback



class MockTrainer:
    pass



def test_callback_interface():

    callback = TrainingCallback()

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