from athena.config.hyperparameters import HyperParameters



def test_hyperparameters_creation():

    params = HyperParameters(
        learning_rate=0.001,
        batch_size=64,
        epochs=100
    )


    assert params.learning_rate == 0.001

    assert params.batch_size == 64

    assert params.epochs == 100



def test_hyperparameters_to_dict():

    params = HyperParameters(
        learning_rate=0.001,
        batch_size=64,
        epochs=100
    )


    data = params.to_dict()


    assert data["learning_rate"] == 0.001

    assert data["batch_size"] == 64

    assert data["epochs"] == 100
