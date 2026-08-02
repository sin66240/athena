from athena.selfplay.evolution_runner import EvolutionRunner


def test_run_generation():

    runner = EvolutionRunner()

    result = runner.run_generation(1)

    assert result["generation"] == 1
    assert result["status"] == "completed"


def test_history():

    runner = EvolutionRunner()

    runner.run_generation(1)
    runner.run_generation(2)

    assert len(runner.get_history()) == 2
