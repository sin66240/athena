from athena.service.selfplay_storage_service import (
    SelfPlayStorageService
)

from athena.selfplay.history import MatchHistory



def test_storage_service_save(tmp_path):

    db = tmp_path / "service.db"


    service = SelfPlayStorageService(
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

        elo_b_after=984

    )


    service.save_match(
        match
    )


    assert service.count_matches() == 1
