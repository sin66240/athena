from dataclasses import dataclass


@dataclass
class ArenaResult:

    matches: int
    winner: str
    status: str = "completed"



class SelfPlayArena:


    def __init__(
        self,
        match_engine=None,
        tournament=None,
        ranking=None,
        promotion=None
    ):

        self.match_engine = match_engine
        self.tournament = tournament
        self.ranking = ranking
        self.promotion = promotion

        self.history = []



    def run_match(
        self,
        player_a,
        player_b
    ):

        result = ArenaResult(
            matches=1,
            winner=player_a
        )

        self.history.append(result)

        return result



    def run_tournament(
        self,
        players
    ):

        result = ArenaResult(
            matches=len(players),
            winner=players[0]
        )

        self.history.append(result)

        return result



    def latest_result(self):

        if not self.history:
            return None

        return self.history[-1]
