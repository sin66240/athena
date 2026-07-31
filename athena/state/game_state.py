from dataclasses import dataclass, field


@dataclass
class GameState:
    """
    Central state object passed to poker agents.
    """

    players: list = field(default_factory=list)

    hands: dict = field(default_factory=dict)

    pot: int = 0

    current_player: str | None = None

    street: str = "preflop"

    betting_round: object | None = None


    def add_player(self, player):

        self.players.append(player)


    def set_hand(self, player_name, cards):

        self.hands[player_name] = cards


    def get_hand(self, player_name):

        return self.hands.get(player_name, [])


    def advance_street(self):

        streets = [
            "preflop",
            "flop",
            "turn",
            "river",
            "showdown",
        ]

        index = streets.index(self.street)

        if index < len(streets) - 1:
            self.street = streets[index + 1]