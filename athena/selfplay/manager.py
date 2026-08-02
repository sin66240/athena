from athena.selfplay.history import SelfPlayHistory
from athena.selfplay.analytics import SelfPlayAnalytics


class SelfPlayManager:
    """
    Controls multiple self-play episodes.
    """

    def __init__(
        self,
        runner,
        storage_service=None
    ):

        self.runner = runner

        self.history = SelfPlayHistory()

        self.analytics = SelfPlayAnalytics()

        self.storage_service = storage_service



    def run(
        self,
        episodes=1
    ):

        results = []


        for _ in range(episodes):

            result = self.runner.run_game()


            results.append(
                result
            )


            # บันทึกประวัติการแข่งขัน
            self.history.add_match_history(
                result
            )


            # วิเคราะห์สถิติ
            self.analytics.add_match(
                result
            )


            # บันทึก database ถ้ามี storage service
            if self.storage_service:

                match = self.history.latest()

                self.storage_service.save_match(
                    match
                )


        return results



    def report(self):

        return self.analytics.report()



    def count(self):

        return self.history.count()