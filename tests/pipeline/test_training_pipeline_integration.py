from athena.pipeline.training_pipeline import TrainingPipeline


class MockTrainer:

    def __init__(self):
        self.called = False


    def train(self):

        self.called = True

        return "trained_model"



class MockEvaluator:

    def __init__(self):

        self.called = False


    def evaluate(
        self,
        model
    ):

        self.called = True

        return 0.90



class MockPromotion:

    def __init__(self):

        self.called = False


    def evaluate_and_promote(
        self,
        model
    ):

        self.called = True

        return {
            "promoted": True
        }



def test_training_pipeline_full_integration():

    trainer = MockTrainer()

    evaluator = MockEvaluator()

    promotion = MockPromotion()


    pipeline = TrainingPipeline(
        trainer=trainer,
        evaluator=evaluator,
        promotion_service=promotion
    )


    result = pipeline.run()


    assert trainer.called is True

    assert evaluator.called is True

    assert promotion.called is True

    assert result["promoted"] is True
