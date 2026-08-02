from athena.selfplay.model_registry import (
    ModelRegistry,
    ModelVersion
)



def test_register_model():

    registry = ModelRegistry()

    model = ModelVersion(
        name="model_001",
        generation=1
    )

    registry.register(model)

    assert len(registry.models) == 1



def test_promote_model():

    registry = ModelRegistry()

    old = ModelVersion(
        name="model_old",
        generation=1,
        elo=1200,
        status="champion"
    )

    new = ModelVersion(
        name="model_new",
        generation=2,
        elo=1300
    )


    registry.register(old)
    registry.register(new)


    registry.promote(new)


    assert new.status == "champion"
    assert old.status == "archived"



def test_get_champion():

    registry = ModelRegistry()

    model = ModelVersion(
        name="champion",
        generation=1,
        elo=1400,
        status="champion"
    )


    registry.register(model)


    result = registry.get_champion()


    assert result.name == "champion"
