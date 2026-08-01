from athena.pipeline.training_pipeline import TrainingPipeline


class MockModel:

    def __init__(self):

        self.name = "model_v1"



class MockTrainer:

    def __init__(self):

        self.saved = False


    def train(self):

        return MockModel()



class MockStorage:

    def __init__(self):

        self.model = None


    def save(
        self,
        model
    ):

        self.model = model



class MockEvaluator:

    def evaluate(
        self,
        model
    ):

        return 0.95



class MockPromotion:

    def __init__(
        self,
        storage
    ):

        self.storage = storage
        self.registered = False


    def evaluate_and_promote(
        self,
        model
    ):

        self.storage.save(
            model
        )

        self.registered = True

        return {
            "promoted": True,
            "score": 0.95
        }



def test_pipeline_artifact_flow():

    storage = MockStorage()

    trainer = MockTrainer()

    evaluator = MockEvaluator()

    promotion = MockPromotion(
        storage
    )


    pipeline = TrainingPipeline(
        trainer=trainer,
        evaluator=evaluator,
        promotion_service=promotion
    )


    result = pipeline.run()


    assert result["promoted"] is True

    assert result["score"] == 0.95

    assert storage.model is not None

    assert storage.model.name == "model_v1"

    assert promotion.registered is True
