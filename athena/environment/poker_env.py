from athena.core.deck import Deck
from athena.core.hand import HandEvaluator


class PokerEnvironment:
    """
    Basic poker environment.
    Handles game state and rewards.
    """

    def __init__(self, players):
        self.players = players
        self.deck = None
        self.hands = {}
        self.winner = None
        self.reward = {}

    def reset(self):
        self.deck = Deck.create_standard()
        self.deck.shuffle()

        self.hands = {}

        for player in self.players:
            self.hands[player.name] = [
                self.deck.draw(),
                self.deck.draw(),
                self.deck.draw(),
                self.deck.draw(),
                self.deck.draw(),
            ]

        self.winner = None
        self.reward = {}

        return self.get_state()

    def get_state(self):
        return {
            "hands": self.hands,
            "players": [
                player.name
                for player in self.players
            ]
        }

    def evaluate(self):
        best_player = None
        best_score = -1

        for player in self.players:
            cards = self.hands[player.name]

            result = HandEvaluator.evaluate(cards)

            if result.score > best_score:
                best_score = result.score
                best_player = player

        self.winner = best_player

        for player in self.players:
            self.reward[player.name] = (
                1 if player == self.winner else -1
            )

        return self.winner

    def step(self):
        winner = self.evaluate()

        return {
            "winner": winner.name,
            "reward": self.reward
        }