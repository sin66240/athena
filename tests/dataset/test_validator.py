from athena.dataset.validator import DatasetValidator


def test_dataset_validator():

    validator = DatasetValidator()

    assert validator.validate(
        [1,2,3]
    )
