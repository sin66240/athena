from athena.core.deck import Deck
from athena.core.hand import HandEvaluator
from athena.state.game_state import GameState


class PokerEnvironment:
    """
    Basic poker environment.
    Handles game state and rewards.
    """

    def __init__(self, players):

        self.players = players
        self.deck = None
        self.state = None


    def reset(self):

        self.deck = Deck.create_standard()
        self.deck.shuffle()

        hands = {}

        for player in self.players:

            hands[player.name] = [
                self.deck.draw(),
                self.deck.draw(),
                self.deck.draw(),
                self.deck.draw(),
                self.deck.draw(),
            ]


        self.state = GameState(
            players=self.players,
            hands=hands,
            pot=0,
            street="preflop"
        )


        return {
    "hands": self.state.hands,
    "players": [
        player.name
        for player in self.players
    ]
}
  


    def evaluate(self):

        best_player = None
        best_score = -1


        for player in self.players:

            cards = self.state.hands[player.name]

            result = HandEvaluator.evaluate(cards)


            if result.score > best_score:

                best_score = result.score
                best_player = player



        self.state.winner = best_player


        self.state.rewards = {}

        for player in self.players:

            self.state.rewards[player.name] = (
                1 if player == best_player else -1
            )


        return best_player



    def step(self):

        winner = self.evaluate()


        return {
            "winner": winner.name,
            "reward": self.state.rewards
        }