from athena.dataset.splitter import DatasetSplitter


def test_split_dataset():

    splitter = DatasetSplitter()

    data = [
        1,2,3,4,5
    ]

    train, test = splitter.split(
        data,
        test_size=0.2
    )

    assert len(train) > 0
    assert len(test) > 0
