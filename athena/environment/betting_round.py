from athena.environment.actions import Action


class BettingRound:
    """
    Handles a single poker betting round.
    """

    def __init__(self, players, starting_chips=1000):

        self.players = players

        self.chips = {
            player.name: starting_chips
            for player in players
        }

        self.bets = {
            player.name: 0
            for player in players
        }

        self.pot = 0
        self.folded = set()


    def apply_action(self, player, action, amount=0):

        name = player.name


        if name in self.folded:
            return


        if action == Action.FOLD:

            self.folded.add(name)


        elif action == Action.CALL:

            call_amount = amount

            self.chips[name] -= call_amount
            self.bets[name] += call_amount
            self.pot += call_amount


        elif action == Action.RAISE:

            self.chips[name] -= amount
            self.bets[name] += amount
            self.pot += amount


        elif action == Action.CHECK:

            pass


    def active_players(self):

        return [
            player
            for player in self.players
            if player.name not in self.folded
        ]