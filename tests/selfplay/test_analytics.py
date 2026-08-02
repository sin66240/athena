from athena.selfplay.analytics import SelfPlayAnalytics


def test_add_match():

    a = SelfPlayAnalytics()

    a.add_match(
        {
            "winner":"model_v1"
        }
    )

    assert a.total_matches() == 1



def test_winner_count():

    a = SelfPlayAnalytics()

    a.add_match({"winner":"A"})
    a.add_match({"winner":"A"})
    a.add_match({"winner":"B"})


    result = a.wins_by_agent()

    assert result["A"] == 2
    assert result["B"] == 1



def test_champion():

    a = SelfPlayAnalytics()

    a.add_match({"winner":"A"})
    a.add_match({"winner":"A"})
    a.add_match({"winner":"B"})


    assert a.champion() == "A"
