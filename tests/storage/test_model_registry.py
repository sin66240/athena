from athena.storage.model_registry import ModelRegistry



class MockModel:
    pass



def test_register_model():

    registry = ModelRegistry()

    model = MockModel()


    record = registry.register(
        model,
        reward=10
    )


    assert record["version"] == 1

    assert record["model"] is model



def test_latest_model():

    registry = ModelRegistry()


    registry.register(
        MockModel(),
        reward=5
    )


    latest = registry.latest()


    assert latest["version"] == 1



def test_promote_champion():

    registry = ModelRegistry()


    registry.register(
        MockModel(),
        reward=20
    )


    champion = registry.promote(
        1
    )


    assert champion["status"] == "champion"



def test_best_champion():

    registry = ModelRegistry()


    registry.register(
        MockModel(),
        reward=10,
        status="champion"
    )


    registry.register(
        MockModel(),
        reward=30,
        status="champion"
    )


    champion = registry.champion()


    assert champion["reward"] == 30