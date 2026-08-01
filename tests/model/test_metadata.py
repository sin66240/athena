from athena.model.metadata import ModelMetadata


def test_model_metadata():

    metadata = ModelMetadata(
        name="athena_model_v1",
        feature_version="v1",
        dataset_version="v1",
        score=0.95
    )


    assert metadata.name == "athena_model_v1"

    assert metadata.feature_version == "v1"

    assert metadata.dataset_version == "v1"

    assert metadata.score == 0.95



def test_metadata_to_dict():

    metadata = ModelMetadata(
        name="athena_model_v1",
        feature_version="v1",
        dataset_version="v1",
        score=0.95
    )


    data = metadata.to_dict()


    assert data["name"] == "athena_model_v1"

    assert data["score"] == 0.95
