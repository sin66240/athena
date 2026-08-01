from athena.experiments.result import ExperimentResult


def test_experiment_result_creation():

    result = ExperimentResult(
        experiment_name="run001",
        status="completed"
    )


    assert result.experiment_name == "run001"

    assert result.status == "completed"



def test_experiment_result_with_metrics():

    result = ExperimentResult(
        experiment_name="run001",
        status="completed",
        metrics={
            "reward":100
        }
    )


    data = result.to_dict()


    assert data["metrics"]["reward"] == 100
