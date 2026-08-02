class EloRating:


    def __init__(self, k_factor=32):

        self.k_factor = k_factor
        self.ratings = {}



    def add_agent(self, name, rating=1000):

        if name not in self.ratings:

            self.ratings[name] = rating



    def expected_score(self, rating_a, rating_b):

        return 1 / (
            1 + 10 ** (
                (rating_b - rating_a) / 400
            )
        )



    def update(self, winner, loser):

        self.add_agent(winner)
        self.add_agent(loser)


        winner_rating = self.ratings[winner]
        loser_rating = self.ratings[loser]


        expected_winner = self.expected_score(
            winner_rating,
            loser_rating
        )


        expected_loser = self.expected_score(
            loser_rating,
            winner_rating
        )


        self.ratings[winner] += self.k_factor * (
            1 - expected_winner
        )


        self.ratings[loser] += self.k_factor * (
            0 - expected_loser
        )



    def leaderboard(self):

        return sorted(
            self.ratings.items(),
            key=lambda x: x[1],
            reverse=True
        )



    def champion(self):

        board = self.leaderboard()

        if not board:
            return None

        return board[0]
