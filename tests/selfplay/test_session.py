from athena.selfplay.session import SelfPlaySession


def test_session_start():

    session = SelfPlaySession(
        "model_v1",
        "model_v2",
        rounds=10
    )

    result = session.start()

    assert result.champion == "model_v1"
    assert result.winner == "model_v1"
    assert result.promoted is False
