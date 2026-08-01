from athena.dataset.training_dataset import TrainingDataset


def test_add_sample():

    dataset = TrainingDataset()

    dataset.add(
        state={"pot": 100},
        action="raise",
        reward=1.0,
    )

    assert len(dataset) == 1


def test_clear_dataset():

    dataset = TrainingDataset()

    dataset.add(
        state={},
        action="call",
        reward=0,
    )

    dataset.clear()

    assert len(dataset) == 0