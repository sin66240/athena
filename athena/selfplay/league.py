from itertools import combinations


class League:

    def __init__(self):
        self.agents = []


    def add_agent(self, agent):
        self.agents.append(agent)


    def remove_agent(self, agent):
        if agent in self.agents:
            self.agents.remove(agent)


    def create_match_pairs(self):
        return list(
            combinations(
                self.agents,
                2
            )
        )


    def size(self):
        return len(self.agents)
