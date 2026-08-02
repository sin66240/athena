class TrainingPipelineOrchestrator:
    """
    Coordinate the full training pipeline.

    Generation
        ↓
    Training
        ↓
    Promotion
    """

    def __init__(
        self,
        generation,
        trainer,
        promotion
    ):

        self.generation = generation
        self.trainer = trainer
        self.promotion = promotion


    def run(self):

        generation_result = self.generation.run()

        candidate_model = self.trainer.run()

        promotion_result = self.promotion.evaluate_and_promote(
            candidate_model
        )

        return {

            **generation_result,

            **promotion_result

        }
