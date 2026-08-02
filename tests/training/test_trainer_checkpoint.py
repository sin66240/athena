from athena.training.trainer import Trainer
from athena.training.checkpoint import Checkpoint


def test_trainer_updates_checkpoint():

    checkpoint = Checkpoint()

    trainer = Trainer(
        checkpoint=checkpoint
    )


    trainer.train_step(
        score=0.80
    )


    assert checkpoint.best_score == 0.80

