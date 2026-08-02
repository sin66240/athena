from athena.selfplay.tournament import Tournament


class DummyAgent:

    def __init__(self,name):
        self.name=name


def test_tournament_create():

    agents=[
        DummyAgent("A"),
        DummyAgent("B")
    ]

    tournament=Tournament(agents)

    assert len(tournament.agents)==2
