class ModelEvaluator:
    """
    Compare two models.
    """


    def __init__(
        self,
        games=100
    ):

        self.games = games



    def evaluate(
        self,
        champion,
        challenger
    ):

        champion_wins = 0
        challenger_wins = 0


        for _ in range(self.games):

            result = self.play_game(
                champion,
                challenger
            )


            if result == "champion":
                champion_wins += 1

            else:
                challenger_wins += 1



        return {
            "champion_wins": champion_wins,
            "challenger_wins": challenger_wins,
            "challenger_winrate":
                challenger_wins / self.games
        }



    def play_game(
        self,
        champion,
        challenger
    ):

        # placeholder
        # later connect PokerEnvironment

        return "challenger"