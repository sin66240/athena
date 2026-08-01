from athena.evaluation.model_evaluator import ModelEvaluator



class MockModel:

    pass



def test_model_evaluation():


    evaluator = ModelEvaluator(
        games=10
    )


    result = evaluator.evaluate(
        MockModel(),
        MockModel()
    )


    assert result["challenger_wins"] == 10

    assert result["challenger_winrate"] == 1.0