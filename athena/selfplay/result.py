from dataclasses import dataclass


@dataclass
class MatchResult:
    winner: str
    loser: str
    score_winner: float
    score_loser: float
