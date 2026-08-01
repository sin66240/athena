from athena.pipeline.auto_trainer import AutoTrainer



class MockManager:

    def __init__(self):

        self.champion = "old"

        self.challenger = None



    def set_challenger(
        self,
        model
    ):

        self.challenger = model



    def promote(
        self
    ):

        self.champion = self.challenger

        self.challenger = None



class MockEvaluator:


    def evaluate(
        self,
        champion,
        challenger
    ):

        return {
            "challenger_winrate": 0.8
        }



def test_auto_training_promote():

    pipeline = AutoTrainer(
        None,
        MockEvaluator(),
        MockManager()
    )


    result = pipeline.run(
        "new_model"
    )


    assert result["status"] == "promoted"