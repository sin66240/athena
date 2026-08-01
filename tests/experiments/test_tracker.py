from athena.experiments.tracker import ExperimentTracker
from athena.experiments.experiment import Experiment



def test_tracker_save_and_latest():

    tracker = ExperimentTracker()


    exp = Experiment(
        name="run1",
        model_version="v1",
        feature_version="v1",
        dataset_version="v1"
    )


    tracker.save(
        exp
    )


    assert len(
        tracker.list()
    ) == 1


    assert tracker.latest() == exp
