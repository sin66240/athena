from athena.evaluation.promotion_service import PromotionService
from athena.evaluation.promotion_policy import PromotionPolicy
from athena.evaluation.model_comparator import ModelComparator
from athena.evaluation.model_manager import ModelManager


class MockModel:

    def __init__(
        self,
        name,
        score
    ):
        self.name = name
        self.score = score



class MockEvaluator:

    def evaluate(
        self,
        model
    ):
        return model.score



def test_full_training_promotion_cycle():

    # Current champion
    champion = MockModel(
        "champion_v1",
        0.70
    )


    manager = ModelManager(
        champion=champion
    )


    service = PromotionService(
        evaluator=MockEvaluator(),
        comparator=ModelComparator(),
        policy=PromotionPolicy(
            minimum_gain=0.05
        ),
        manager=manager
    )


    # New trained model
    challenger = MockModel(
        "challenger_v2",
        0.85
    )


    result = service.evaluate_and_promote(
        challenger
    )


    assert result["promoted"] is True

    assert (
        manager.champion.name
        ==
        "challenger_v2"
    )



def test_full_cycle_reject_bad_training():

    champion = MockModel(
        "champion_v1",
        0.90
    )


    manager = ModelManager(
        champion=champion
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
        "bad_model",
        0.91
    )


    result = service.evaluate_and_promote(
        challenger
    )


    assert result["promoted"] is False

    assert (
        manager.champion.name
        ==
        "champion_v1"
    )