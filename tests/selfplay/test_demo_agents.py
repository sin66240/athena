from athena.selfplay.demo_agents import create_demo_agents


def test_create_demo_agents():

    agents = create_demo_agents(4)

    assert len(agents) == 4
    assert agents[0].name == "agent_1"
