from athena.selfplay.pipeline import SelfPlayPipeline



def test_pipeline_promotes():

    pipeline = SelfPlayPipeline()

    result = pipeline.run(
        wins=7,
        games=10
    )

    assert result.promoted is True
    assert result.wins == 7



def test_pipeline_rejects():

    pipeline = SelfPlayPipeline()

    result = pipeline.run(
        wins=3,
        games=10
    )

    assert result.promoted is False
