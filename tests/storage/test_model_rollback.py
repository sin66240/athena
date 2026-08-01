from athena.storage.model_registry import ModelRegistry


class MockModel:

    def __init__(
        self,
        name
    ):
        self.name = name



def test_register_versions():

    registry = ModelRegistry()


    v1 = MockModel(
        "model_v1"
    )

    v2 = MockModel(
        "model_v2"
    )


    registry.register(
        v1,
        reward=0.80
    )


    registry.register(
        v2,
        reward=0.90
    )


    assert registry.latest()["reward"] == 0.90



def test_rollback_version():

    registry = ModelRegistry()


    model1 = MockModel(
        "model_v1"
    )

    model2 = MockModel(
        "model_v2"
    )


    registry.register(
        model1,
        reward=0.80
    )


    registry.register(
        model2,
        reward=0.90
    )


    registry.rollback(
        1
    )


    current = registry.latest()


    assert current["model"].name == "model_v1"
