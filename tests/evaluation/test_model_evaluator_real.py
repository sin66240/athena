from athena.evaluation.model_evaluator import ModelEvaluator



def fake_game(
    champion,
    challenger
):

    return "champion"



def test_evaluator_with_runner():


    evaluator = ModelEvaluator(
        games=10,
        game_runner=fake_game
    )


    result = evaluator.evaluate(
        "model_a",
        "model_b"
    )


    assert result["champion_wins"] == 10
    assert result["challenger_wins"] == 0
