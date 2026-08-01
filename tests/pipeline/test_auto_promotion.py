from athena.evaluation.promotion_service import PromotionService
from athena.evaluation.promotion_policy import PromotionPolicy
from athena.evaluation.model_comparator import ModelComparator
from athena.evaluation.model_manager import ModelManager



class MockModel:

    def __init__(
        self,
        score
    ):
        self.score = score



class MockEvaluator:

    def evaluate(
        self,
        model
    ):
        return model.score



def test_pipeline_promotes_better_model():

    manager = ModelManager(
        champion=MockModel(0.70)
    )


    service = PromotionService(
        evaluator=MockEvaluator(),
        comparator=ModelComparator(),
        policy=PromotionPolicy(
            minimum_gain=0.05
        ),
        manager=manager
    )


    challenger = MockModel(
        0.90
    )


    result = service.evaluate_and_promote(
        challenger
    )


    assert result["promoted"] is True
    assert manager.champion.score == 0.90



def test_pipeline_rejects_weaker_model():

    manager = ModelManager(
        champion=MockModel(0.90)
    )


    service = PromotionService(
        evaluator=MockEvaluator(),
        comparator=ModelComparator(),
        policy=PromotionPolicy(
            minimum_gain=0.05
        ),
        manager=manager
    )


    challenger = MockModel(
        0.91
    )


    result = service.evaluate_and_promote(
        challenger
    )


    assert result["promoted"] is False
    assert manager.champion.score == 0.90