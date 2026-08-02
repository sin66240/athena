from athena.pipeline.training_pipeline_orchestrator import (
    TrainingPipelineOrchestrator
)


class DummyGeneration:

    def run(self):
        return {
            "matches": 20
        }


class DummyTraining:

    def run(self):
        return "candidate_model"


class DummyPromotion:

    def evaluate_and_promote(
        self,
        model
    ):
        return {
            "promoted": True
        }


def test_orchestrator_run():

    orchestrator = TrainingPipelineOrchestrator(

        generation=DummyGeneration(),

        trainer=DummyTraining(),

        promotion=DummyPromotion()

    )

    result = orchestrator.run()

    assert result["matches"] == 20
    assert result["promoted"] is True
