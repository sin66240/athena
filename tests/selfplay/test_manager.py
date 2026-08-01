from athena.selfplay.manager import SelfPlayManager


class MockRunner:

    def __init__(self):

        self.count = 0


    def run_game(self):

        self.count += 1

        return {
            "game": self.count
        }



def test_selfplay_manager_runs_multiple_games():

    runner = MockRunner()


    manager = SelfPlayManager(
        runner
    )


    results = manager.run(
        episodes=5
    )


    assert len(results) == 5

    assert results[0]["game"] == 1

    assert results[-1]["game"] == 5