from dataclasses import dataclass


@dataclass
class EvolutionResult:
    winner: str
    champion: str
    promoted: bool


class EvolutionEngine:

    def __init__(self, elo_system):
        self.elo_system = elo_system


    def evaluate(
        self,
        champion,
        challenger,
        winner
    ):

        if winner == challenger:
            return EvolutionResult(
                winner=challenger,
                champion=challenger,
                promoted=True
            )

        return EvolutionResult(
            winner=winner,
            champion=champion,
            promoted=False
        )
