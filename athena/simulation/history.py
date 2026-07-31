from dataclasses import dataclass
from typing import List


@dataclass
class GameHistory:
    """
    Store result from one simulation game.
    """

    hands_played: int
    winner: str
    actions: List[str]


class HistoryLogger:
    """
    Collect simulation history.
    """

    def __init__(self):
        self.games = []


    def add_game(self, history: GameHistory):
        self.games.append(history)


    def count(self):
        return len(self.games)