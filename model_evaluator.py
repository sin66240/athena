class ModelEvaluator:
    """
    Evaluate champion vs challenger.
    """

    def __init__(
        self,
        games=100,
        game_runner=None
    ):

        self.games = games
        self.game_runner = game_runner



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

            elif result == "challenger":

                challenger_wins += 1



        return {

            "games": self.games,

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

        if self.game_runner:

            return self.game_runner(
                champion,
                challenger
            )


        # fallback
        return "champion"
