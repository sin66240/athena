from athena.selfplay.trainer_manager import (
    TrainerManager
)


from athena.selfplay.model_registry import (
    ModelRegistry
)



def test_create_training_job():

    registry = ModelRegistry()

    manager = TrainerManager(
        registry
    )


    job = manager.create_job(
        "model_v1",
        1
    )


    assert job.model_name == "model_v1"
    assert job.status == "created"



def test_training_flow():

    registry = ModelRegistry()

    manager = TrainerManager(
        registry
    )


    job = manager.create_job(
        "model_v2",
        2
    )


    manager.start_training(job)


    assert job.status == "training"



    manager.complete_training(job)


    assert job.status == "completed"



def test_latest_job():

    manager = TrainerManager(
        ModelRegistry()
    )


    manager.create_job(
        "a",
        1
    )

    result = manager.latest_job()


    assert result.model_name == "a"
