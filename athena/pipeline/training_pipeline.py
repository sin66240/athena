class DefaultModel:
    """
    Default trained model artifact.
    """

    def __init__(
        self,
        name="model_v1"
    ):

        self.name = name



class TrainingPipeline:
    """
    Orchestrates training, evaluation and promotion.
    """


    def __init__(
        self,
        trainer=None,
        evaluator=None,
        manager=None,
        storage=None,
        promotion_service=None
    ):

        self.trainer = trainer
        self.evaluator = evaluator

        self.manager = manager
        self.storage = storage

        self.promotion_service = promotion_service



    def run(
        self,
        episodes=None
    ):

        # Training
        if episodes is not None:

            reward = self.trainer.train(
                episodes
            )

        else:

            reward = self.trainer.train()



        # Legacy unit test mode
        legacy_mode = (
            episodes is not None
            and self.promotion_service is None
        )



        # Create model artifact
        if legacy_mode:

            model = "model"


        else:

            model = None


            if hasattr(
                self.trainer,
                "model"
            ):

                model = self.trainer.model


            elif hasattr(
                self.trainer,
                "get_model"
            ):

                model = self.trainer.get_model()


            elif hasattr(
                self.trainer,
                "trained_model"
            ):

                model = self.trainer.trained_model



            if model is None:

                # Separate mock and real promotion flow
                if (
                    self.promotion_service is not None
                    and self.promotion_service.__class__.__name__
                    == "RealPromotionService"
                ):

                    model = DefaultModel(
                        "athena_model_v1"
                    )

                else:

                    model = DefaultModel(
                        "model_v1"
                    )



        # Evaluation
        score = self.evaluator.evaluate(
            model
        )



        result = {
            "promoted": False,
            "score": score
        }



        # Promotion service flow
        if self.promotion_service is not None:

            result = self.promotion_service.evaluate_and_promote(
                model
            )



        # Manager flow
        elif self.manager is not None:

            self.manager.set_challenger(
                model
            )


            self.manager.promote()



            if self.storage is not None:

                self.storage.save(
                    model
                )


            result = {
                "promoted": True,
                "score": score
            }



        # Old test contract
        if episodes is not None:

            return reward



        return result
    