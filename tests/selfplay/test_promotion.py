from athena.selfplay.promotion import PromotionPolicy


def test_promote_when_winrate_high():

    policy = PromotionPolicy(
        threshold=0.55
    )

    result = policy.evaluate(
        wins=6,
        games=10
    )

    assert result.promoted is True
    assert result.win_rate == 0.6



def test_reject_when_winrate_low():

    policy = PromotionPolicy(
        threshold=0.55
    )

    result = policy.evaluate(
        wins=4,
        games=10
    )

    assert result.promoted is False
