from athena.training.history import TrainingHistory



def test_history_store_metrics():

    history = TrainingHistory()


    history.add(
        epoch=1,
        metrics={
            "loss":0.1,
            "accuracy":0.9
        }
    )


    assert len(
        history.records
    ) == 1


    assert history.latest()["epoch"] == 1
