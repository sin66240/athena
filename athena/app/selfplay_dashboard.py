from athena.service.selfplay_service import SelfPlayService


class SelfPlayDashboard:

    def __init__(
        self,
        service=None
    ):

        self.service = service or SelfPlayService()


    def overview(self):

        data = self.service.get_dashboard_data()

        return {
            "title": "ATHENA SelfPlay Dashboard",
            "matches": data["total_matches"],
            "champion": data["champion"],
            "generations": data["generations"],
            "win_rate": data["win_rate"]
        }


    def champion_status(self):

        return {
            "champion": self.service.get_champion()
        }


    def match_count(self):

        return self.service.get_total_matches()
