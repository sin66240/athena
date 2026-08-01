from athena.evaluation.promotion_service import PromotionService
from athena.evaluation.promotion_policy import PromotionPolicy
from athena.evaluation.model_comparator import ModelComparator
from athena.evaluation.model_manager import ModelManager



class MockEvaluator:

    def evaluate(
        self,
        model
    ):

        return model.score



class MockModel:

    def __init__(
        self,
        score
    ):

        self.score = score



def test_promote_challenger():

    manager = ModelManager(
        champion=MockModel(0.70)
    )


    service = PromotionService(
        MockEvaluator(),
        ModelComparator(),
        PromotionPolicy(
            minimum_gain=0.05
        ),
        manager
    )


    result = service.evaluate_and_promote(
        MockModel(0.90)
    )


    assert result["promoted"] is True
    assert manager.champion.score == 0.90



def test_reject_challenger():

    manager = ModelManager(
        champion=MockModel(0.80)
    )


    service = PromotionService(
        MockEvaluator(),
        ModelComparator(),
        PromotionPolicy(
            minimum_gain=0.05
        ),
        manager
    )


    result = service.evaluate_and_promote(
        MockModel(0.82)
    )


    assert result["promoted"] is False