from athena.selfplay.elo import EloRating



def test_elo_update():

    elo = EloRating()


    elo.update(
        "Alpha",
        "Beta"
    )


    assert elo.ratings["Alpha"] > 1000
    assert elo.ratings["Beta"] < 1000



def test_elo_champion():

    elo = EloRating()


    elo.update(
        "Alpha",
        "Beta"
    )

    elo.update(
        "Alpha",
        "Gamma"
    )


    champion = elo.champion()


    assert champion[0] == "Alpha"
