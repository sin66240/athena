from athena.selfplay.runner import SelfPlayRunner
from athena.agents.random_agent import RandomAgent
from athena.dataset.training_dataset import TrainingDataset


class MockEnvironment:

    def reset(self):
        return {
            "pot": 100
        }


    def step(self):

        return {
            "reward": 1
        }



def test_selfplay_generates_data():

    env = MockEnvironment()

    agent1 = RandomAgent(
        "A"
    )

    agent2 = RandomAgent(
        "B"
    )


    dataset = TrainingDataset()


    runner = SelfPlayRunner(
        env,
        agent1,
        agent2,
        dataset
    )


    result = runner.run_game()


    assert "actions" in result

    assert len(dataset) == 2