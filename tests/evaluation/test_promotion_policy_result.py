from athena.evaluation.promotion_policy import PromotionPolicy



def test_policy_with_match_result():

    policy = PromotionPolicy(
        minimum_gain=0.1
    )


    result = {

        "games": 100,

        "champion_wins": 40,

        "challenger_wins": 60

    }


    decision = policy.evaluate_match_result(
        result
    )


    assert decision["promote"] is True
