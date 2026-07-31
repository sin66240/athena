from athena.agents.random_agent import RandomAgent


def test_random_agent_name():

    agent = RandomAgent("Alice")

    assert agent.name == "Alice"



def test_random_agent_action():

    agent = RandomAgent("Bot")

    action = agent.decide_action(None)

    assert action in agent.ACTIONS



def test_agent_observe():

    agent = RandomAgent("Bot")

    agent.observe(
        {
            "reward": 10
        }
    )

    assert len(agent.history) == 1