from athena.environment.actions import Action


def test_action_values():

    assert Action.FOLD.value == "fold"
    assert Action.CHECK.value == "check"
    assert Action.CALL.value == "call"
    assert Action.RAISE.value == "raise"
    