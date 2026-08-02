from athena.selfplay.match import Match


def test_match_creation():

    match = Match(
        "champion",
        "challenger",
        10
    )

    result = match.run()

    assert result["agent_a"] == "champion"
    assert result["episodes"] == 10

