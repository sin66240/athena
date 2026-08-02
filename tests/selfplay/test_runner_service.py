from athena.selfplay.runner_service import SelfPlayRunnerService


def test_runner_create():

    runner = SelfPlayRunnerService()

    assert runner is not None



def test_run_series_empty():

    runner = SelfPlayRunnerService()

    result = runner.run_series(
        [],
        rounds=1
    )

    assert result == []
