from athena.training.loop import TrainingLoop



class MockSelfPlay:

    def run(self, episodes):

        return [
            {
                "winner": "AI"
            }
            for _ in range(episodes)
        ]



class MockDataset:

    def __init__(self):

        self.data = []


    def add(
        self,
        state,
        action,
        reward
    ):

        self.data.append(
            {
                "state": state,
                "action": action,
                "reward": reward
            }
        )



class MockTrainer:

    def train(
        self,
        dataset
    ):

        return {
            "trained": True,
            "samples": len(dataset.data)
        }



def test_training_loop_cycle():

    loop = TrainingLoop(
        MockSelfPlay(),
        MockTrainer(),
        MockDataset()
    )


    result = loop.run_cycle(
        episodes=5
    )


    assert result["trained"] is True

    assert result["samples"] == 5