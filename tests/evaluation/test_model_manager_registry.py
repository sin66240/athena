from athena.evaluation.model_manager import ModelManager
from athena.storage.model_registry import ModelRegistry



class MockModel:
    pass



def test_register_challenger_model():

    registry = ModelRegistry()

    manager = ModelManager(
        registry=registry
    )


    model = MockModel()


    manager.set_challenger(
        model
    )


    record = manager.register_challenger(
        reward=10
    )


    assert record["model"] is model

    assert record["reward"] == 10



def test_promote_updates_registry():

    registry = ModelRegistry()

    manager = ModelManager(
        registry=registry
    )


    model = MockModel()


    manager.set_challenger(
        model
    )


    manager.register_challenger(
        reward=20
    )


    champion = manager.promote()


    assert champion is model

    assert manager.has_champion()



def test_registry_has_champion():

    registry = ModelRegistry()

    manager = ModelManager(
        registry=registry
    )


    model = MockModel()


    manager.set_challenger(
        model
    )


    manager.register_challenger(
        reward=50
    )


    manager.promote()


    champion = registry.champion()


    assert champion["reward"] == 50