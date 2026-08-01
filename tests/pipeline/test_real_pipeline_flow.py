from athena.pipeline.training_pipeline import TrainingPipeline
from athena.storage.model_storage import ModelStorage
from athena.storage.model_registry import ModelRegistry
from athena.evaluation.model_manager import ModelManager


class RealModel:

    def __init__(self):

        self.name = "athena_model_v1"



class RealTrainer:

    def train(self):

        return RealModel()



class RealEvaluator:

    def evaluate(
        self,
        model
    ):

        return {
            "score": 0.90
        }



class RealPromotionService:

    def __init__(
        self,
        manager
    ):

        self.manager = manager


    def evaluate_and_promote(
        self,
        model
    ):

        self.manager.set_challenger(
            model
        )

        promoted = self.manager.promote()

        return {
            "promoted": True,
            "model": promoted
        }



def test_real_pipeline_flow():

    storage = ModelStorage()

    registry = ModelRegistry()


    manager = ModelManager(
        storage=storage,
        registry=registry
    )


    pipeline = TrainingPipeline(
        trainer=RealTrainer(),
        evaluator=RealEvaluator(),
        promotion_service=RealPromotionService(
            manager
        )
    )


    result = pipeline.run()


    assert result["promoted"] is True

    assert manager.has_champion()

    assert manager.champion.name == "athena_model_v1"
