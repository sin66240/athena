from dataclasses import dataclass


@dataclass
class AgentScore:

    name: str
    wins: int = 0
    losses: int = 0
    draws: int = 0


    @property
    def games(self):

        return self.wins + self.losses + self.draws


    @property
    def win_rate(self):

        if self.games == 0:
            return 0.0

        return self.wins / self.games



class RankingEngine:


    def __init__(self):

        self.agents = {}



    def add_agent(self, name):

        if name not in self.agents:

            self.agents[name] = AgentScore(
                name=name
            )



    def record_win(self, winner, loser):

        self.add_agent(winner)
        self.add_agent(loser)

        self.agents[winner].wins += 1
        self.agents[loser].losses += 1



    def record_draw(self, agent1, agent2):

        self.add_agent(agent1)
        self.add_agent(agent2)

        self.agents[agent1].draws += 1
        self.agents[agent2].draws += 1



    def leaderboard(self):

        return sorted(
            self.agents.values(),
            key=lambda x: (
                x.win_rate,
                x.wins
            ),
            reverse=True
        )



    def champion(self):

        board = self.leaderboard()

        if not board:
            return None

        return board[0]
