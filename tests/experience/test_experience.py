from athena.experience.experience import Experience


def test_create_experience():

    exp = Experience(
        state="state",
        action="raise",
        reward=1.0,
        next_state="next",
        done=True
    )


    assert exp.action == "raise"
    assert exp.reward == 1.0
