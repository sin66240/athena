class SelfPlayTrainingLoop:

    def __init__(
        self,
        champion,
        challenger,
        matches=100
    ):
        self.champion = champion
        self.challenger = challenger
        self.matches = matches


    def run(self):

        results = []

        for _ in range(self.matches):

            result = {
                "champion": self.champion,
                "challenger": self.challenger,
                "winner": self.champion
            }

            results.append(result)

        return results
