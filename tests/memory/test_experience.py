from athena.memory.experience import Experience


def test_experience_creation():

    exp = Experience(
        state="state",
        action="call",
        reward=10,
        next_state="next"
    )

    assert exp.state == "state"
    assert exp.action == "call"
    assert exp.reward == 10
    assert exp.next_state == "next"