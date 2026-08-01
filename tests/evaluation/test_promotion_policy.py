from athena.evaluation.promotion_policy import PromotionPolicy



def test_promote_when_gain_is_enough():

    policy = PromotionPolicy(
        minimum_gain=0.05
    )


    result = policy.should_promote(
        0.80,
        0.90
    )


    assert result is True



def test_reject_when_gain_is_low():

    policy = PromotionPolicy(
        minimum_gain=0.05
    )


    result = policy.should_promote(
        0.80,
        0.82
    )


    assert result is False



def test_evaluate_result():

    policy = PromotionPolicy(
        minimum_gain=0.05
    )


    result = policy.evaluate(
        0.80,
        0.90
    )


    assert result["promote"] is True
    assert result["gain"] == 0.10