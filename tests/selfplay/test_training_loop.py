from athena.selfplay.training_loop import SelfPlayTrainingLoop


def test_training_loop_runs():

    loop = SelfPlayTrainingLoop(
        "model_a",
        "model_b",
        matches=10
    )

    results = loop.run()

    assert len(results) == 10
    assert results[0]["winner"] == "model_a"
