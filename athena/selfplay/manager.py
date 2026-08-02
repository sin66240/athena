from athena.selfplay.history import SelfPlayHistory
from athena.selfplay.analytics import SelfPlayAnalytics
from athena.experience.experience_builder import ExperienceBuilder


class SelfPlayManager:
    """
    Controls multiple self-play episodes.
    """


    def __init__(
        self,
        runner,
        storage_service=None,
        replay_buffer=None
    ):

        self.runner = runner

        self.history = SelfPlayHistory()

        self.analytics = SelfPlayAnalytics()

        self.storage_service = storage_service

        self.replay_buffer = replay_buffer

        self.experience_builder = ExperienceBuilder()



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


            # บันทึกประสบการณ์เข้า Replay Buffer
            if self.replay_buffer:

                experience = self.experience_builder.build(
                    result
                )

                self.replay_buffer.add(
                    experience
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