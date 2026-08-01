from athena.experiments.experiment import Experiment


def test_experiment_creation():

    exp = Experiment(
        name="test_run",
        model_version="v1",
        feature_version="v1",
        dataset_version="v1"
    )


    assert exp.name == "test_run"

    assert exp.model_version == "v1"

    assert exp.feature_version == "v1"

    assert exp.dataset_version == "v1"



def test_experiment_to_dict():

    exp = Experiment(
        name="test_run",
        model_version="v1",
        feature_version="v1",
        dataset_version="v1"
    )


    data = exp.to_dict()


    assert data["name"] == "test_run"

    assert data["model_version"] == "v1"
