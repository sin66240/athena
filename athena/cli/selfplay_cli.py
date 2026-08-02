from athena.app.selfplay_dashboard import SelfPlayDashboard


class SelfPlayCLI:

    def __init__(self):
        self.dashboard = SelfPlayDashboard()


    def status(self):

        return self.dashboard.overview()


    def champion(self):

        return self.dashboard.champion_status()


    def matches(self):

        return {
            "matches": self.dashboard.match_count()
        }
