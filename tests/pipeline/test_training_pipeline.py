from athena.pipeline.training_pipeline import TrainingPipeline



class MockTrainer:

    def __init__(self):

        self.agent = "model"


    def train(
        self,
        episodes
    ):

        return episodes



class MockEvaluator:

    def evaluate(
        self,
        model
    ):

        return 1.0



class MockManager:

    def __init__(self):

        self.challenger = None
        self.champion = None


    def set_challenger(
        self,
        model
    ):

        self.challenger = model


    def promote(
        self
    ):

        self.champion = self.challenger



class MockStorage:

    def __init__(self):

        self.saved = None


    def save(
        self,
        model
    ):

        self.saved = model



def test_training_pipeline():


    trainer = MockTrainer()

    evaluator = MockEvaluator()

    manager = MockManager()

    storage = MockStorage()


    pipeline = TrainingPipeline(
        trainer,
        evaluator,
        manager,
        storage
    )


    reward = pipeline.run(
        10
    )


    assert reward == 10

    assert manager.champion == "model"

    assert storage.saved == "model"