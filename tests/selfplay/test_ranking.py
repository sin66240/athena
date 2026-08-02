from athena.selfplay.ranking import RankingEngine



def test_ranking_engine():

    ranking = RankingEngine()


    ranking.record_win(
        "Alpha",
        "Beta"
    )

    ranking.record_win(
        "Alpha",
        "Beta"
    )


    ranking.record_win(
        "Beta",
        "Gamma"
    )


    champion = ranking.champion()


    assert champion.name == "Alpha"
    assert champion.wins == 2
