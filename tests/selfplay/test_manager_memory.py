from athena.selfplay.manager import SelfPlayManager
from athena.experience.replay_buffer import ReplayBuffer


class DummyRunner:

    def run_game(self):

        return {
            "agent_a": "Athena",
            "agent_b": "Bot",
            "winner": "Athena"
        }



def test_manager_saves_experience():

    buffer = ReplayBuffer()


    manager = SelfPlayManager(
        DummyRunner(),
        replay_buffer=buffer
    )


    manager.run(
        episodes=1
    )


    assert buffer.count() == 1
