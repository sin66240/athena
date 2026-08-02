from athena.selfplay.arena import (
    SelfPlayArena
)



def test_run_match():

    arena = SelfPlayArena()


    result = arena.run_match(
        "agent_a",
        "agent_b"
    )


    assert result.matches == 1
    assert result.winner == "agent_a"



def test_run_tournament():

    arena = SelfPlayArena()


    result = arena.run_tournament(
        [
            "agent_a",
            "agent_b",
            "agent_c"
        ]
    )


    assert result.matches == 3
    assert result.winner == "agent_a"



def test_latest_result():

    arena = SelfPlayArena()


    arena.run_match(
        "a",
        "b"
    )


    assert arena.latest_result().winner == "a"
