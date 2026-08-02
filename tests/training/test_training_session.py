from athena.training.session import TrainingSession


class MockTrainer:

    def train(self, dataset):

        return "trained"



class MockTracker:

    def __init__(self):

        self.saved = None


    def save(self, experiment):

        self.saved = experiment



def test_training_session_tracks_experiment():

    tracker = MockTracker()

    session = TrainingSession(
        trainer=MockTrainer(),
        tracker=tracker
    )


    exp = {
        "name":"run001"
    }


    result = session.run(
        dataset=[1,2,3],
        experiment=exp
    )


    assert result == "trained"

    assert tracker.saved == exp
