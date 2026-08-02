from athena.experiments.tracker import Tracker
from athena.experiments.result import ExperimentResult


def test_tracker_best_reward():

    tracker = Tracker()


    tracker.log(
        ExperimentResult(
            experiment_name="run001",
            status="completed",
            metrics={
                "reward":100
            }
        )
    )


    tracker.log(
        ExperimentResult(
            experiment_name="run002",
            status="completed",
            metrics={
                "reward":200
            }
        )
    )


    best = tracker.best(
        "reward"
    )


    assert best.experiment_name == "run002"
