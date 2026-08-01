class TrainingPipeline:
    """
    Connect training, evaluation and model management.
    """


    def __init__(
        self,
        trainer=None,
        evaluator=None,
        model_manager=None,
        storage=None
    ):

        self.trainer = trainer
        self.evaluator = evaluator
        self.model_manager = model_manager
        self.storage = storage



    def run(
        self,
        episodes
    ):

        reward = self.trainer.train(
            episodes
        )


        model = self.trainer.agent


        if self.evaluator is not None:

            self.evaluator.evaluate(
                model
            )


        if self.model_manager is not None:

            self.model_manager.set_challenger(
                model
            )

            self.model_manager.promote()



        if self.storage is not None:

            self.storage.save(
                model
            )


        return reward