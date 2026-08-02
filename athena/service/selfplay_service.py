from athena.selfplay.metrics import SelfPlayMetrics


class SelfPlayService:

    def __init__(
        self,
        metrics=None
    ):

        self.metrics = metrics or SelfPlayMetrics()


    def record_match(
        self,
        winner,
        loser
    ):

        self.metrics.add_match(
            {
                "winner": winner,
                "loser": loser
            }
        )


    def record_generation(
        self,
        generation
    ):

        self.metrics.add_generation(
            {
                "id": generation
            }
        )


    def get_dashboard_data(self):

        summary = self.metrics.summary()

        return {
            "total_matches": summary["matches"],
            "champion": summary["best_agent"],
            "win_rate": summary["win_rate"],
            "generations": summary["generations"]
        }


    def get_champion(self):

        return self.metrics.best_agent()


    def get_total_matches(self):

        return self.metrics.total_matches()
