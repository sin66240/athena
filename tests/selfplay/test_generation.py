from athena.selfplay.generation import SelfPlayGeneration


def test_generation_run():

    generation = SelfPlayGeneration()

    result = generation.run(4)

    assert "agents" in result
    assert "matches" in result
