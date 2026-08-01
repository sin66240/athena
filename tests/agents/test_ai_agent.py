from athena.agents.ai_agent import AIAgent


class MockState:

    pot = 150

    players = [
        "A",
        "B"
    ]

    street = "turn"


def test_ai_agent_decide():

    agent = AIAgent("AI")

    action = agent.decide(
        MockState()
    )

    assert action == "raise"


def test_ai_agent_decide_action():

    agent = AIAgent("AI")

    action = agent.decide_action(
        MockState()
    )

    assert action == "RAISE"