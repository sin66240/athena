class SelfPlayAnalytics:

    def __init__(self):
        self.matches = []


    def add_match(self, match):
        self.matches.append(match)


    def total_matches(self):
        return len(self.matches)


    def wins_by_agent(self):

        result = {}

        for match in self.matches:

            winner = match.get("winner")

            if winner:
                result[winner] = result.get(winner,0) + 1

        return result


    def win_rate(self):

        total = self.total_matches()

        if total == 0:
            return {}

        wins = self.wins_by_agent()

        return {
            agent: value / total
            for agent,value in wins.items()
        }


    def champion(self):

        wins = self.wins_by_agent()

        if not wins:
            return None

        return max(
            wins,
            key=wins.get
        )


    def report(self):

        return {
            "matches": self.total_matches(),
            "wins": self.wins_by_agent(),
            "champion": self.champion()
        }

