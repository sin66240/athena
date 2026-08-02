from athena.selfplay.history import SelfPlayHistory


def test_create_history():

    history = SelfPlayHistory()

    assert history.count() == 0



def test_add_match_history():

    history = SelfPlayHistory()


    history.add_match(

        model_a="model_v1",

        model_b="model_v2",

        winner="model_v1",

        score_a=1.0,

        score_b=0.0,

        elo_a_before=1200,

        elo_b_before=1200,

        elo_a_after=1216,

        elo_b_after=1184

    )


    assert history.count() == 1



def test_get_all_history():

    history = SelfPlayHistory()


    history.add_match(

        model_a="alpha",

        model_b="beta",

        winner="alpha",

        score_a=1,

        score_b=0,

        elo_a_before=1000,

        elo_b_before=1000,

        elo_a_after=1015,

        elo_b_after=985

    )


    records = history.get_all()


    assert len(records) == 1

    assert records[0]["winner"] == "alpha"



def test_latest_history():

    history = SelfPlayHistory()


    history.add_match(

        model_a="a",

        model_b="b",

        winner="a",

        score_a=1,

        score_b=0,

        elo_a_before=1000,

        elo_b_before=1000,

        elo_a_after=1010,

        elo_b_after=990

    )


    latest = history.latest()


    assert latest.model_a == "a"



def test_clear_history():

    history = SelfPlayHistory()


    history.add_match(

        model_a="a",

        model_b="b",

        winner="a",

        score_a=1,

        score_b=0,

        elo_a_before=1000,

        elo_b_before=1000,

        elo_a_after=1010,

        elo_b_after=990

    )


    history.clear()


    assert history.count() == 0
