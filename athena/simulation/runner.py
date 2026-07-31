from dataclasses import dataclass

from athena.simulation.history import (
    GameHistory,
    HistoryLogger,
)


@dataclass
class SimulationState:
    """
    Minimal state passed to agents.
    """

    hand_strength: float



class SimulationRunner:
    """
    Runs poker agent simulations.
    """

    def __init__(self, agents):
        self.agents = agents
        self.history = HistoryLogger()


    def run_game(self):

        actions = []

        state = SimulationState(
            hand_strength=0.5
        )

        for agent in self.agents:

            action = agent.decide_action(state)

            actions.append(action)


        result = GameHistory(
            hands_played=1,
            winner=self.agents[0].name,
            actions=actions,
        )

        self.history.add_game(result)

        return result