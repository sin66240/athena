from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class MatchPair:
    agent_a: str
    agent_b: str


class LeagueScheduler:
    """
    Selects balanced selfplay matches
    based on ranking / Elo proximity.
    """

    def __init__(self):
        self.agents = []

    def add_agent(
        self,
        name: str,
        rating: float = 1000
    ):
        self.agents.append(
            {
                "name": name,
                "rating": rating
            }
        )

    def remove_agent(
        self,
        name: str
    ):
        self.agents = [
            agent
            for agent in self.agents
            if agent["name"] != name
        ]

    def get_sorted_agents(self):
        return sorted(
            self.agents,
            key=lambda x: x["rating"],
            reverse=True
        )

    def create_pairs(
        self
    ) -> List[MatchPair]:

        ranked = self.get_sorted_agents()

        pairs = []

        for i in range(
            0,
            len(ranked) - 1,
            2
        ):
            pairs.append(
                MatchPair(
                    agent_a=ranked[i]["name"],
                    agent_b=ranked[i + 1]["name"]
                )
            )

        return pairs

    def find_closest_opponent(
        self,
        name: str
    ):

        target = None

        for agent in self.agents:
            if agent["name"] == name:
                target = agent
                break

        if target is None:
            return None


        opponents = [
            agent
            for agent in self.agents
            if agent["name"] != name
        ]

        if not opponents:
            return None


        opponents.sort(
            key=lambda x:
            abs(
                x["rating"]
                -
                target["rating"]
            )
        )

        return opponents[0]["name"]
