from athena.experiments.experiment import Experiment
from athena.config.hyperparameters import HyperParameters



def test_experiment_with_hyperparameters():

    params = HyperParameters(
        learning_rate=0.001,
        batch_size=64,
        epochs=100
    )


    exp = Experiment(
        name="run001",
        model_version="v1",
        feature_version="v1",
        dataset_version="v1",
        hyperparameters=params
    )


    assert exp.hyperparameters == params



def test_experiment_dict_contains_parameters():

    params = HyperParameters(
        learning_rate=0.001,
        batch_size=64,
        epochs=100
    )


    exp = Experiment(
        name="run001",
        model_version="v1",
        feature_version="v1",
        dataset_version="v1",
        hyperparameters=params
    )


    data = exp.to_dict()


    assert data["hyperparameters"]["learning_rate"] == 0.001

    assert data["hyperparameters"]["batch_size"] == 64
