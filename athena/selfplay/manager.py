class SelfPlayManager:
    """
    Controls multiple self-play episodes.
    """

    def __init__(
        self,
        runner
    ):

        self.runner = runner


    def run(
        self,
        episodes=1
    ):

        results = []


        for _ in range(episodes):

            result = self.runner.run_game()

            results.append(
                result
            )


        return results