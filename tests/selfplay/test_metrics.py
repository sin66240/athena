from athena.selfplay.metrics import SelfPlayMetrics


def test_total_matches():

    metrics = SelfPlayMetrics()

    metrics.add_match(
        {
            "winner": "model_a"
        }
    )

    assert metrics.total_matches() == 1



def test_best_agent():

    metrics = SelfPlayMetrics()

    metrics.add_match(
        {
            "winner": "model_a"
        }
    )

    metrics.add_match(
        {
            "winner": "model_a"
        }
    )

    metrics.add_match(
        {
            "winner": "model_b"
        }
    )


    assert metrics.best_agent() == "model_a"



def test_summary():

    metrics = SelfPlayMetrics()

    metrics.add_generation(
        {
            "id": 1
        }
    )


    result = metrics.summary()


    assert result["matches"] == 0
    assert result["generations"] == 1
