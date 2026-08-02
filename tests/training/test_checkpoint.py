from athena.training.checkpoint import Checkpoint


def test_checkpoint_saves_best_model():

    checkpoint = Checkpoint()


    model_a = {
        "accuracy":0.80
    }


    model_b = {
        "accuracy":0.95
    }


    checkpoint.save_if_best(
        model_a,
        score=model_a["accuracy"]
    )


    checkpoint.save_if_best(
        model_b,
        score=model_b["accuracy"]
    )


    assert checkpoint.best_score == 0.95

    assert checkpoint.best_model == model_b
