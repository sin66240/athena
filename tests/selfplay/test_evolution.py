from athena.selfplay.evolution import EvolutionEngine


def test_challenger_promoted():

    engine = EvolutionEngine(None)

    result = engine.evaluate(
        champion="A",
        challenger="B",
        winner="B"
    )

    assert result.promoted is True
    assert result.champion == "B"



def test_champion_keeps_position():

    engine = EvolutionEngine(None)

    result = engine.evaluate(
        champion="A",
        challenger="B",
        winner="A"
    )

    assert result.promoted is False
    assert result.champion == "A"
