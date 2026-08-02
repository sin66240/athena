from athena.selfplay.league import League


def test_create_league():

    league = League()

    assert league.agents == []



def test_add_agent():

    league = League()

    league.add_agent(
        "model_v1"
    )

    assert "model_v1" in league.agents



def test_add_multiple_agents():

    league = League()

    league.add_agent("model_v1")
    league.add_agent("model_v2")
    league.add_agent("model_v3")

    assert len(league.agents) == 3



def test_create_match_pairs():

    league = League()

    league.add_agent("model_a")
    league.add_agent("model_b")

    pairs = league.create_match_pairs()

    assert len(pairs) == 1
    assert pairs[0] == (
        "model_a",
        "model_b"
    )



def test_remove_agent():

    league = League()

    league.add_agent("model_a")

    league.remove_agent(
        "model_a"
    )

    assert "model_a" not in league.agents
