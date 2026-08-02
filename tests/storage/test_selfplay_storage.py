from athena.storage.selfplay_storage import SelfPlayStorage
from athena.selfplay.history import MatchHistory



def test_storage_save_and_count(tmp_path):

    db = tmp_path / "selfplay.db"


    storage = SelfPlayStorage(
        str(db)
    )


    match = MatchHistory(

        model_a="agent_a",

        model_b="agent_b",

        winner="agent_a",

        score_a=1,

        score_b=0,

        elo_a_before=1000,

        elo_b_before=1000,

        elo_a_after=1016,

        elo_b_after=984,

        timestamp="now"

    )


    storage.save_match(match)


    assert storage.count() == 1



def test_storage_clear(tmp_path):

    db = tmp_path / "selfplay.db"


    storage = SelfPlayStorage(
        str(db)
    )


    storage.clear()


    assert storage.count() == 0
