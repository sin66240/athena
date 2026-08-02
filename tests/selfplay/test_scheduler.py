from athena.selfplay.scheduler import LeagueScheduler


def test_create_scheduler():

    scheduler = LeagueScheduler()

    assert scheduler.agents == []


def test_add_agent():

    scheduler = LeagueScheduler()

    scheduler.add_agent(
        "model_a",
        1500
    )

    assert len(
        scheduler.agents
    ) == 1



def test_remove_agent():

    scheduler = LeagueScheduler()

    scheduler.add_agent(
        "model_a"
    )

    scheduler.remove_agent(
        "model_a"
    )

    assert scheduler.agents == []



def test_create_pairs():

    scheduler = LeagueScheduler()

    scheduler.add_agent(
        "A",
        1500
    )

    scheduler.add_agent(
        "B",
        1400
    )

    scheduler.add_agent(
        "C",
        1300
    )

    scheduler.add_agent(
        "D",
        1200
    )


    pairs = scheduler.create_pairs()


    assert len(
        pairs
    ) == 2


def test_find_closest():

    scheduler = LeagueScheduler()


    scheduler.add_agent(
        "A",
        1500
    )

    scheduler.add_agent(
        "B",
        1490
    )

    scheduler.add_agent(
        "C",
        1200
    )


    opponent = scheduler.find_closest_opponent(
        "A"
    )


    assert opponent == "B"
