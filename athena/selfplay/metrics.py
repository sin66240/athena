class SelfPlayMetrics:

    def __init__(self):
        self.matches = []
        self.generations = []


    def add_match(self, match):
        self.matches.append(match)


    def add_generation(self, generation):
        self.generations.append(generation)


    def total_matches(self):
        return len(self.matches)


    def wins(self):

        result = {}

        for match in self.matches:

            winner = match.get("winner")

            if winner:
                result[winner] = result.get(winner, 0) + 1

        return result


    def win_rate(self):

        total = self.total_matches()

        if total == 0:
            return {}

        return {
            agent: wins / total
            for agent, wins in self.wins().items()
        }


    def best_agent(self):

        wins = self.wins()

        if not wins:
            return None

        return max(
            wins,
            key=wins.get
        )


    def generation_count(self):

        return len(self.generations)


    def summary(self):

        return {
            "matches": self.total_matches(),
            "best_agent": self.best_agent(),
            "win_rate": self.win_rate(),
            "generations": self.generation_count()
        }
