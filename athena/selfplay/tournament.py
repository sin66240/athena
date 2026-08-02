from dataclasses import dataclass
from typing import List

from athena.selfplay.match import Match
from athena.selfplay.result import MatchResult


@dataclass
class TournamentResult:
    rankings: dict


class Tournament:

    def __init__(self, agents):
        self.agents = agents
        self.results: List[MatchResult] = []


    def run(self):

        for i in range(len(self.agents)):

            for j in range(i + 1, len(self.agents)):

                match = Match(
                    self.agents[i],
                    self.agents[j]
                )

                result = match.play()

                self.results.append(result)


        return self.rank()


    def rank(self):

        scores = {}

        for result in self.results:

            winner = result.winner

            if winner not in scores:
                scores[winner] = 0

            scores[winner] += 1


        return TournamentResult(
            rankings=scores
        )
