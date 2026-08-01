from athena.storage.model_storage import ModelStorage



class MockModel:

    def __init__(self):

        self.name = "Athena"



def test_save_model(tmp_path):

    path = tmp_path / "model.pkl"


    storage = ModelStorage(
        path
    )


    model = MockModel()


    result = storage.save(
        model
    )


    assert result is True



def test_load_model(tmp_path):

    path = tmp_path / "model.pkl"


    storage = ModelStorage(
        path
    )


    model = MockModel()


    storage.save(
        model
    )


    loaded = storage.load()


    assert loaded.name == "Athena"