from athena.selfplay.match import Match
from athena.selfplay.history import SelfPlayHistory


class SelfPlayRunnerService:


    def __init__(self):

        self.history = SelfPlayHistory()



    def run_match(self, agent_a, agent_b):

        match = Match(
            agent_a,
            agent_b
        )


        result = match.play()


        self.history.add_match_history(
            result
        )


        return result



    def run_series(self, agents, rounds=1):

        results = []


        for _ in range(rounds):

            for i in range(len(agents)-1):

                result = self.run_match(
                    agents[i],
                    agents[i+1]
                )

                results.append(result)


        return results
