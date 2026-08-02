from athena.selfplay.result import MatchResult


def test_match_result():

    result = MatchResult(
        winner="agent_a",
        loser="agent_b",
        score_winner=1.0,
        score_loser=0.0
    )

    assert result.winner == "agent_a"
    assert result.loser == "agent_b"
    assert result.score_winner == 1.0

