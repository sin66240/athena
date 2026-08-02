from dataclasses import dataclass


@dataclass
class SessionResult:
    champion: str
    challenger: str
    winner: str
    promoted: bool



class SelfPlaySession:

    def __init__(
        self,
        champion,
        challenger,
        rounds=1
    ):
        self.champion = champion
        self.challenger = challenger
        self.rounds = rounds


    def start(self):

        wins = 0

        for _ in range(self.rounds):

            # placeholder match logic
            winner = self.champion

            if winner == self.challenger:
                wins += 1


        promoted = wins > self.rounds / 2

        return SessionResult(
            champion=self.champion,
            challenger=self.challenger,
            winner=self.champion,
            promoted=promoted
        )
