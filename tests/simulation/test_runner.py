from athena.agents.random_agent import RandomAgent
from athena.agents.rule_agent import RuleAgent
from athena.simulation.runner import SimulationRunner



def test_runner_create():

    agents = [
        RandomAgent("Random"),
        RuleAgent("Rule"),
    ]

    runner = SimulationRunner(agents)

    assert len(runner.agents) == 2



def test_runner_game():

    agents = [
        RandomAgent("Random"),
        RuleAgent("Rule"),
    ]

    runner = SimulationRunner(agents)

    result = runner.run_game()

    assert result.hands_played == 1
    assert len(result.actions) == 2