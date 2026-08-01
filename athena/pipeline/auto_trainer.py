class AutoTrainer:
    """
    Automatic model improvement pipeline.
    """


    def __init__(
        self,
        trainer,
        evaluator,
        manager
    ):

        self.trainer = trainer
        self.evaluator = evaluator
        self.manager = manager



    def run(
        self,
        challenger
    ):

        self.manager.set_challenger(
            challenger
        )


        result = self.evaluator.evaluate(
            self.manager.champion,
            challenger
        )


        if result["challenger_winrate"] > 0.5:

            self.manager.promote()

            return {
                "status": "promoted",
                "result": result
            }


        return {
            "status": "rejected",
            "result": result
        }