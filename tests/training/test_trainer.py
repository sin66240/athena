from athena.training.trainer import Trainer
from athena.memory.replay_buffer import ReplayBuffer
from athena.agents.random_agent import RandomAgent


class MockEnvironment:

    def reset(self):
        return "state"


    def step(self):

        return {
            "reward": 1
        }



def test_trainer_episode():

    agent = RandomAgent(
        "Bot"
    )

    env = MockEnvironment()

    memory = ReplayBuffer()


    trainer = Trainer(
        agent,
        env,
        memory
    )


    reward = trainer.run_episode()


    assert reward == 1
    assert len(memory) == 1