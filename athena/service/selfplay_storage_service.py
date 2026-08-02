from athena.storage.selfplay_storage import SelfPlayStorage
from athena.selfplay.history import MatchHistory


class SelfPlayStorageService:

    def __init__(self, db_path):

        self.storage = SelfPlayStorage(
            db_path
        )


    def save_match(
        self,
        match: MatchHistory
    ):

        return self.storage.save(
            match
        )


    def count_matches(self):

        return self.storage.count()


    def get_matches(self):

        return self.storage.get_all()
