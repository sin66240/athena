from athena.experiments.metrics import Metrics



def test_metrics_creation():

    metrics = Metrics(
        reward=100,
        accuracy=0.85,
        loss=0.25
    )


    assert metrics.reward == 100

    assert metrics.accuracy == 0.85

    assert metrics.loss == 0.25



def test_metrics_to_dict():

    metrics = Metrics(
        reward=100,
        accuracy=0.85,
        loss=0.25
    )


    data = metrics.to_dict()


    assert data["reward"] == 100

    assert data["accuracy"] == 0.85

    assert data["loss"] == 0.25
